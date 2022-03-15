"""
Material.

Classes to create and manage music materials and lyrics.
"""
import abjad
from itertools import cycle
from .data.guitar_bitones_dict import binotes


class Lyrics:
    """Lyrics."""

    def __init__(self, target):
        """Initializer."""
        self.lyrics = None
        self.target = target
        self.name = target + "_Lyrics"

    def write_lyrics(self, lyrics):
        """Method to write lyrics attribute to a ``muda.Lyrics`` instance."""
        self.lyrics = lyrics


class Material:
    """Material."""

    def __init__(self, name):
        """Initializer."""
        self.name = name
        self.container = abjad.Container()
        self.lyrics = None
        self.container.name = name

    def __call__(self) -> abjad.Container():
        """It returns ``self.container``."""
        return self.container

    def write(self, lilypond_string, name: str):
        """It creates container from lilypond string and append to a
        ``muda.Material()`` instance."""
        self.container.append(abjad.Container(lilypond_string, name=name))

    def alternating_materials(self, annotated_durations: list, makers: dict):
        """Create alternating materials according to a list of named durations."""
        assert isinstance(
            annotated_durations[0], list
        ), "Each duration set must be a list."

        material_names = [dur[0].annotation for dur in annotated_durations]
        material_names = list(dict.fromkeys(material_names))

        for dur in annotated_durations:
            for maker, value in makers.items():
                if maker == dur[0].annotation:
                    if isinstance(value, str):
                        self.container.append(
                            abjad.Container(
                                makers[maker], name=maker, identifier="% " + maker
                            )
                        )
                    else:
                        selection = makers[maker](dur)
                        appendice = abjad.Container(
                            selection, name=maker, identifier="% " + maker
                        )
                        for item in appendice:
                            if isinstance(item, abjad.Tuplet):
                                item.name = "_"
                                item.identifier = "_"
                                # print(item.name)

                        # if isinstance(selection[0], abjad.Tuplet):
                        #     sel = abjad.Selection(selection).components(
                        #         abjad.Container)

                        #     for container in sel:
                        #         print(container)
                        #         container.name = maker
                        #         container.tag = maker
                        #         container.identifier = "% " + maker
                        # self.container.append(selection)
                        # else:
                        self.container.append(appendice)

        # add indices to materials and write comments in lilypond code to identify materials
        for i, name in enumerate(material_names):
            selectable = self.select_material(self.container, name)
            containers = abjad.select.components(selectable, abjad.Container)
            j = 0
            for container in containers:
                if container.name and container.identifier:
                    if name in container.name:
                        container.name = container.name + "_" + str(j)
                        container.identifier = container.identifier + "_" + str(j)
                        if isinstance(container, abjad.Tuplet):
                            string = container.name
                            comment1 = abjad.LilyPondComment(string)
                            abjad.attach(comment1, container[0])
                            comment2 = abjad.LilyPondComment(
                                string, format_slot="after"
                            )
                            abjad.attach(comment2, container[-1])
                        j += 1
                        # print(container.name)

        # # add indices to materials write comments in lilypond code to identify materials
        # for i, name in enumerate(material_names):
        #     j = 0
        #     for container in containers:
        #         if container.name and container.identifier:
        #             if name in container.name:
        #                 container.name = container.name + "_" + str(j)
        #                 container.identifier = container.identifier + \
        #                     "_" + str(j)
        #                 if isinstance(container, abjad.Tuplet):
        #                     string = container.name
        #                     comment1 = abjad.LilyPondComment(string)
        #                     abjad.attach(comment1, container[0])
        #                     comment2 = abjad.LilyPondComment(
        #                         string, format_slot="after")
        #                     abjad.attach(comment2, container[-1])
        #                 j += 1

    def write_pitches(self, pitches):
        """Write pitches to notes in the Material instance."""
        logical_ties = (
            abjad.Selection(self.container).leaves().logical_ties(pitched=True)
        )
        for i, logical_tie in enumerate(logical_ties):
            index = i % len(pitches)
            pitch = pitches[index]
            for note in logical_tie:
                note.written_pitch = pitch

    def write_pitches_by_name(self, annotated_pitches):
        """Write pitches to logical ties in named container."""
        for material_name, pitches in annotated_pitches.items():
            selectable = self.select_material(self.container, material_name)
            selection = abjad.Selection(selectable).leaves().logical_ties(pitched=True)
            for i, logical_tie in enumerate(selection):
                index = i % len(pitches)
                pitch = pitches[index]
                for note in logical_tie:
                    note.written_pitch = pitch

    def write_pitches_by_duration(
        self,
        annotated_pitches: dict,
        annotated_durations: list,
        randomize=0,
    ):
        """write pitches to notes according to annotated durations."""
        assert isinstance(
            annotated_durations[0], list
        ), "each duration set must be a list."

        chords_test = False
        for key, pitches in annotated_pitches.items():
            for item in pitches:
                if isinstance(item, list):
                    chords_test = True

        if chords_test:
            # convert notes to chords
            conversion = abjad.Selection(self.container).leaves(pitched=True)
            for note in conversion:
                chord = abjad.Chord("c'", note.written_duration)
                abjad.mutate.replace(note, chord)

        # select by duration:
        abjad_durations = [sum(dur) for dur in annotated_durations]
        selector = (
            lambda _: abjad.Selection(_)
            .leaves()
            .partition_by_durations(
                abjad_durations,
                cyclic=False,
                fill=abjad.Exact,
                in_seconds=False,
                overhang=True,
            )
        )

        selections = selector(self.container)

        for key in annotated_pitches:
            pitches = cycle(annotated_pitches[key])
            for selection, duration in zip(selections, annotated_durations):
                logical_ties = (
                    abjad.Selection(selection).leaves().logical_ties(pitched=True)
                )
                for a, logical_tie in enumerate(logical_ties):
                    for item in duration:
                        if item.annotation == key:
                            pitch = next(pitches)
                            # print(pitch)
                            for b, chord in enumerate(logical_tie):
                                if isinstance(chord, abjad.Chord):
                                    chord.written_pitches = pitch
                                else:
                                    chord.written_pitch = pitch

    def write_notes_and_chords(self, pitches):

        chords_test = False
        for item in pitches:
            if isinstance(item, list):
                chords_test = True

        if chords_test:
            # convert notes to chords
            conversion = abjad.Selection(self.container).leaves(pitched=True)
            for note in conversion:
                chord = abjad.Chord("c'", note.written_duration)
                abjad.mutate.replace(note, chord)

        logical_ties = (
            abjad.Selection(self.container).leaves().logical_ties(pitched=True)
        )
        for i, logical_tie in enumerate(logical_ties):
            index = i % len(pitches)
            pitch = pitches[index]
            if isinstance(pitch, list):
                for note in logical_tie:
                    note.written_pitches = pitch
            else:
                for note in logical_tie:
                    note.written_pitches = [pitch]

    def annotate_material_names(self, material_name):
        """Add markups to identify materials."""
        copied_container = abjad.mutate.copy(self.container)

        if isinstance(material_name, str):
            material_name = [material_name]

        if material_name is None:
            selectables = [copied_container]
        else:
            selectables = []
            for mat_name in material_name:
                selectable = self.select_material(
                    copied_container, material_name=mat_name
                )
                selectables.append(selectable)

        for i, name in enumerate(material_name):
            selectable = self.select_material(copied_container, name)
            containers = abjad.select.components(selectable, abjad.Container)
            for container in containers:
                if (
                    (not isinstance(container, abjad.Tuplet or abjad.Voice or abjad.BeforeGraceContainer))
                    and (container.name and container.identifier)
                    and (name in container.name)
                ):
                    s = container.name
                    lit = r'\once \override HorizontalBracketText.text = "%s"' % s
                    abjad.attach(abjad.LilyPondLiteral(lit), container[0])

                    abjad.horizontal_bracket(container)
                    for i, leaf in enumerate(abjad.select.leaves(container)):
                        str_ = r"\markup \tiny {\null { \raise #2 {%i}}}" % i
                        abjad.attach(
                            abjad.Markup(str_, direction=abjad.Up),
                            leaf,
                        )

        illustration_score = abjad.Score()
        illustration_staff = abjad.Staff()
        illustration_voice = abjad.Voice()
        illustration_voice.consists_commands.append("Horizontal_bracket_engraver")
        illustration_voice.append(copied_container)
        illustration_staff.append(illustration_voice)
        illustration_score.append(illustration_staff)
        lilypond_file = abjad.LilyPondFile(
            items=[illustration_score],
        )
        import os

        os.chdir(os.path.dirname(__file__))
        abjad.persist.as_ly(lilypond_file, "illustration_score.ly")
        # print(abjad.lilypond(illustration_score))
        os.system("lilypond illustration.ly")
        os.system("open ./illustration.pdf")

    def annotate_indices_on_selection(self, select, material_name: str):
        """Illustrate selection with numbers."""
        if isinstance(material_name, str):
            material_name = [material_name]

        if material_name is None:
            selectables = [self.container]
        else:
            selectables = []
            for mat_name in material_name:
                selectable = self.select_material(
                    self.container, material_name=mat_name
                )
                selectables.append(selectable)

        for selectable in selectables:
            selection = select(selectable)
            for i, leaf in enumerate(selection):
                str_ = r"\markup \tiny {\null { \raise #2 {%i}}}" % i
                abjad.attach(
                    abjad.Markup(str_, direction=abjad.Up),
                    leaf,
                )

    # def see_leaves_number(self, select="leaves", pitched=None):
    #     """Illustrate ``muda.Material.container`` with leaves number."""
    #     if select == "leaves":
    #         selection = abjad.Selection(self.container).leaves(
    #             pitched=pitched, grace=False
    #         )
    #         for i, leaf in enumerate(selection):
    #             str_ = r"\markup \tiny {\null { \raise #2 {%i}}}" % i
    #             abjad.attach(
    #                 abjad.Markup(str_, direction=abjad.Up),
    #                 leaf,
    #             )

    #     elif select == "logical_ties":
    #         selection = (
    #             abjad.Selection(self.container)
    #             .leaves()
    #             .logical_ties(pitched=pitched, grace=False)
    #         )
    #         for i, leaf in enumerate(selection):
    #             str_ = r"\markup \tiny {\null { \raise #2 {%i}}}" % i
    #             abjad.attach(
    #                 abjad.Markup(str_, direction=abjad.Up),
    #                 leaf[0],
    #             )

    # def see_selection(self, select: abjad.Selection, material_name: str or list):
    #     """Illustrate ``muda.Material.container`` with materials leaves number."""
    #     if isinstance(material_name, str):
    #         material_name = [material_name]

    #     if material_name is None:
    #         selectables = [self.container]
    #     else:
    #         selectables = []
    #         for mat_name in material_name:
    #             selectable = self.select_material(
    #                 self.container, material_name=mat_name
    #             )
    #             selectables.append(selectable)

    #     for selectable in selectables:
    #         selection = select(selectable)
    #         if isinstance(selection, abjad.Leaf):
    #             abjad.attach(
    #                 abjad.Markup(
    #                     "\markup" + str(selection.__repr__), direction=abjad.Up
    #                 ),
    #                 selection,
    #             )
    #         else:
    #             for _ in selection:
    #                 abjad.attach(
    #                     abjad.Markup(
    #                         "\markup" + str(selection.__repr__), direction=abjad.Up
    #                     ),
    #                     _,
    #                 )

    def dynamics(self, dynamics: dict, material_name=None):
        """

        :param dynamics: dict (key: str, value: abjad.Selection)
        :param material_name: str
        """
        if material_name is None:
            selectable = self.container
        else:
            selectable = self.select_material(
                self.container, material_name=material_name
            )
        for key, select in dynamics.items():
            selection = select(selectable)
            if abjad.Dynamic.is_dynamic_name(key):
                if isinstance(selection, abjad.Leaf):
                    abjad.attach(abjad.Dynamic(key), selection)
                else:
                    for _ in selection:
                        abjad.attach(abjad.Dynamic(key), _)
            elif isinstance(selection[0], abjad.Selection):
                for sel in selection:
                    abjad.hairpin(key, sel)
            else:
                abjad.hairpin(key, selection)

    def write_indicators(
        self,
        material_name=None,
        dynamics=None,
        articulations=None,
        slur_up=None,
        slur_down=None,
        change_staffs_names=None,
        pitched=True,
    ):
        """Write indicators to leaves."""
        if material_name is not None:
            selection1 = abjad.Selection(self.container).components(abjad.Container)
            for container in selection1:
                if container.name is not None and (
                    (isinstance(material_name, list) or material_name in container.name)
                ):
                    selection2 = abjad.Selection(container).leaves(pitched=pitched)
                    if dynamics:
                        for key in dynamics:
                            if dynamics[key] == "all":
                                for i, leaf in enumerate(selection2[0::2]):
                                    a = i
                                    b = i + 1
                                    abjad.hairpin(key, selection2[a:b])
                            else:
                                for i in dynamics[key]:
                                    if isinstance(i, tuple):
                                        a, b = i
                                        b = b + 1
                                        abjad.hairpin(key, selection2[a:b])
                                    else:
                                        abjad.hairpin(key, selection2[i])

                    # attach slurs
                    if slur_up:
                        for n in slur_up:
                            a, b = n
                            b = b
                            abjad.attach(abjad.StartSlur(), selection2[a])
                            abjad.attach(abjad.StopSlur(), selection2[b])

                    if slur_down:
                        for n in slur_down:
                            a, b = n
                            abjad.attach(
                                abjad.StartSlur(direction=abjad.Down), selection2[a]
                            )
                            abjad.attach(abjad.StopSlur(), selection2[b])

                    if articulations:
                        for key in articulations:
                            for i in articulations[key]:
                                abjad.attach(abjad.Articulation(key), selection2[i])
        else:
            selection = abjad.Selection(self.container).leaves(pitched=pitched)

            if dynamics:
                for key in dynamics:
                    for i in dynamics[key]:
                        if isinstance(i, tuple):
                            a, b = i
                            b = b + 1
                            abjad.hairpin(key, selection[a:b])
                        else:
                            abjad.hairpin(key, selection[i])

            # attach slurs
            if slur_up:
                for n in slur_up:
                    a, b = n
                    b = b
                    abjad.attach(abjad.StartSlur(), selection[a])
                    abjad.attach(abjad.StopSlur(), selection[b])

            if slur_down:
                for n in slur_down:
                    a, b = n
                    abjad.attach(abjad.StartSlur(direction=abjad.Down), selection[a])
                    abjad.attach(abjad.StopSlur(), selection[b])

            if articulations:
                for key in articulations:
                    for i in articulations[key]:
                        abjad.attach(abjad.Articulation(key), selection[i])

    def attach(
        self,
        argument,
        select,
        material_name=None,
    ):
        """Attach ``argument`` to leaves."""
        if isinstance(argument, str or list):
            argument = abjad.LilyPondLiteral(argument)

        if isinstance(material_name, str):
            material_name = [material_name]

        try:
            iter(select)
        except:
            select = [select]

        if material_name is None:
            for sel in select:
                selection = sel(self.container)
                try:
                    iter(selection)
                except:
                    selection = [selection]

                for leaf in selection:
                    abjad.attach(argument, leaf)
                print("attaching", argument, "in general container", selection)

        else:
            for i, name in enumerate(material_name):
                selectable = self.select_material(self.container, name)
                containers = abjad.select.components(selectable, abjad.Container)
                # print(containers)
                for container in containers:
                    if (
                        (not isinstance(container, abjad.Tuplet or abjad.Voice))
                        and (container.name and container.identifier)
                        and (name in container.name)
                    ):
                        # print("each container")
                        # print(container)
                        for sel in select:
                            selection = sel(container)
                            try:
                                iter(selection)
                            except:
                                selection = [selection]

                            for leaf in selection:
                                abjad.attach(argument, leaf)

                            print("attaching", argument, "in", name, selection)

                    
                    





        # for selectable in selectables:
        #     for sel in select:
        #         selection = sel(selectable)
        #         if isinstance(selection, abjad.Rest or abjad.Skip):
        #             pass
        #         elif isinstance(selection, abjad.Note or abjad.Chord):
        #             abjad.override(selection).NoteHead.style = argument
        #         else:
        #             for leaf in selection:
        #                 abjad.override(leaf).NoteHead.style = argument
        #
        # selection = abjad.Selection(self.container[:]).components(abjad.Container)
        # for container in selection:
        #     if container.name is not None and material_name in container.name:
        #         if select is None:
        #             abjad.override(container).NoteHead.style = argument
        #         else:
        #             selection2 = select(container)
        #             if isinstance(selection2, abjad.Leaf):
        #                 abjad.override(selection2).NoteHead.style = argument
        #             else:
        #                 for leaf in selection2:
        #                     abjad.override(leaf).NoteHead.style = argument

    def retrograde(self, material_name):
        """Retrograde components in container."""
        selection = abjad.Selection(self.container[:]).components(abjad.Container)
        for container in selection:
            if container.name is not None and material_name in container.name:
                items = abjad.Selection(container).items
                # print(container.components)
                new_container = abjad.Container(name=container.name)
                for item in reversed(items):
                    for comp in reversed(item.components):
                        if isinstance(comp, abjad.Tuplet):
                            new_tuplet = abjad.Tuplet(
                                multiplier=comp.multiplier, denominator=comp.denominator
                            )
                            for it in reversed(comp.components):
                                new_tuplet.append(it)
                            new_container.append(new_tuplet)
                        elif isinstance(comp, abjad.Container):
                            new_sub_container = abjad.Container()
                            for it in reversed(comp.components):
                                new_sub_container.append(it)
                            new_container.append(new_sub_container)
                        else:
                            new_container.append(comp)
                for i, item in enumerate(container):
                    container.remove(container[i])
                container.append(new_container)

    # def change(self, material_name, selection, change):
    #     """Todo."""
    #     selection1 = abjad.Selection(self.container).components(abjad.Container)
    #     for container in selection1:
    #         if material_name in container.name:
    #             container[selection] = change

    # def delete_material_leaves(self, material_name, leaves):
    #     """Todo."""
    #     selection = abjad.Selection(self.container).components(abjad.Container)
    #     for container in selection:
    #         print(container)
    #         if material_name in container.name:
    #             for _ in leaves:
    #                 del container[_]

    def delete(
        self,
        select,
        material_name=None,
        replace_with_rests=False,
        replace_with_skips=False,
    ):
        """Delete leaves by index.

        Use ``material_name`` to delete a leaf in a
        specific material. Use ``replace_with_rests`` or
        ``replace_with_skips`` to replace leaves by rests or skips.
        """

        if isinstance(material_name, str):
            material_name = [material_name]

        if material_name is None:
            selectables = [self.container]
        else:
            selectables = []
            for mat_name in material_name:
                selectable = self.select_material(
                    self.container, material_name=mat_name
                )
                selectables.append(selectable)

        for i, name in enumerate(material_name):
            selectable = self.select_material(self.container, name)
            containers = abjad.select.components(selectable, abjad.Container)
            # print(containers)
            for container in containers:
                if (
                    (not isinstance(container, abjad.Tuplet or abjad.Voice))
                    and (container.name and container.identifier)
                    and (name in container.name)
                ):
                    # print("each container")
                    # print(container)

                    selection = select(container)
                    

                    try:
                        iter(selection)
                    except:
                        selection = [selection]

                    for leaf in selection:
                        # print(leaf)
                        if replace_with_skips is True:
                            abjad.mutate.replace(
                                leaf,
                                abjad.Skip(leaf.written_duration),
                            )
                        elif replace_with_rests is True:
                            abjad.mutate.replace(
                                leaf,
                                abjad.Rest(leaf.written_duration),
                            )
                        else:
                            del leaf
                    # print(container)

        # if material_name is None:
        #     selection = select(self.container)
        # else:
        #     selection = select(self.select_material(self.container, material_name))

    def print(self):
        """Print ``muda.Material.container`` lilypond code."""
        print(abjad.lilypond(self.container))

    def show(self):
        """Illustrate ``muda.Material.container``."""
        abjad.show(self.container)

    def change_staffs(self, staves_names_and_leaves: dict, material_name=None):
        if material_name is None:
            selectable = self.container
        else:
            selectable = self.select_material(
                self.container, material_name=material_name
            )

        for staff_name, select in staves_names_and_leaves.items():
            selection = select(selectable)
            literal = abjad.LilyPondLiteral(r'\change Staff = "' + staff_name + '"')
            # print(literal)
            if isinstance(selection, abjad.Leaf):
                abjad.attach(literal, selection)
            else:
                for _ in selection:
                    abjad.attach(literal, _)

    def guitar_bitones(
        self,
        select: abjad.Selection,
        material_name: str or list = None,
        hammering=False,
        parenthesized=False,
        playing=False,
        no_midi=False,
    ):
        """Make guitar bi-notes chords using note + string informed in container."""
        # if material_name is None:
        #     selection = select(self.container)
        # else:
        if isinstance(material_name, str):
            material_name = [material_name]
        if material_name is None:
            selectables = [self.container]
        else:
            selectables = []
            for mat_name in material_name:
                selectable = self.select_material(
                    self.container, material_name=mat_name
                )
                selectables.append(selectable)

        for selectable in selectables:
            selection = select(selectable)

            for a, leaf in enumerate(selection):
                if abjad.get.has_indicator(leaf, abjad.StringNumber):
                    indicator = abjad.get.indicator(leaf, abjad.StringNumber)
                    i = indicator.numbers[0]
                    ord_pitch = leaf.written_pitch.number

                    try:
                        pitches = binotes[i][ord_pitch]
                    except:
                        raise Exception(
                            f"{self.name}, leaf: {leaf}, indice: {a}, Pitch {ord_pitch} and string {i} don't match."
                        )
                    # pitches = abjad.PitchSet(pitches)
                    chord = abjad.Chord("<c' e'>4")
                    chord.written_duration = leaf.written_duration
                    if no_midi is True:
                        chord.written_pitches = pitches[1]
                    else:
                        chord.written_pitches = pitches

                        # change note head to square
                        square_note_head = chord.note_heads[1]
                        abjad.override(
                            chord
                        ).NoteHead.stencil = "#ly:text-interface::print"
                        abjad.tweak(
                            square_note_head
                        ).text = '\markup{ \musicglyph "noteheads.s0laFunk"}'

                        # change the original note to arrow (tapping) head or parenthesized head
                        other_note_head = chord.note_heads[0]
                        if hammering is True and playing is False:
                            abjad.tweak(
                                other_note_head
                            ).text = '\markup{ \musicglyph "arrowheads.open.01"}'
                        elif hammering is True and playing is True:
                            abjad.tweak(
                                other_note_head
                            ).text = '\markup{\musicglyph "arrowheads.close.01"}'
                        else:
                            abjad.tweak(
                                other_note_head
                            ).text = '\markup{\musicglyph "noteheads.s2"}'
                        if parenthesized is True:
                            other_note_head.is_parenthesized = True

                        string = abjad.LilyPondLiteral(f"\{i}", format_slot="after")
                        abjad.attach(string, chord)

                    abjad.mutate.replace(leaf, chord)

    @staticmethod
    def select_material(container, material_name, test_names=False):
        """Select container by name."""
        selection = abjad.select.components(container, abjad.Container)
        indices = [
            i
            for i, container in enumerate(selection)
            if (
                (isinstance(container, abjad.Tuplet or abjad.Voice or abjad.BeforeGraceContainer))
                or (container.name is None)
                or (material_name not in container.name)
            )
        ]

        selection = abjad.select.exclude(selection, indices)

        # print("NEW SELECTION")
        # for element in selection:
            # print(m or aterial_name, element.name)
        # print(selection)
        return selection

    def automatic_clefs(self, select: abjad.Selection, material_name: str):
        """Attach appropriate clef for selection."""
        clefs = [
            abjad.Clef("treble^15"),
            abjad.Clef("treble^8"),
            abjad.Clef("treble"),
            abjad.Clef("bass"),
            abjad.Clef("bass_8"),
        ]
        ranges = [
            abjad.PitchRange("[G#7, +inf]"),
            abjad.PitchRange("[G6, G7]"),
            abjad.PitchRange("[E4, E5]"),
            abjad.PitchRange("[A1, G3]"),
            abjad.PitchRange("[-inf, C1]"),
        ]
        if material_name is None:
            selection = select(self.container)
        else:
            selection = select(self.select_material(self.container, material_name))
        for element in selection:
            for clef, range_ in zip(clefs, ranges):
                if element.written_pitch in range_:
                    abjad.attach(clef, element)

    def make_skips(self, argument):
        r"""Write skips and time signatures to Context."""
        site = "muda.Material.make_skips()"
        tag = abjad.Tag(site)
        print(str(tag))

        if isinstance(argument, list or abjad.TimeSignature):
            time_signatures_abjad = []
            if isinstance(argument[0], abjad.TimeSignature):
                time_signatures_abjad = argument
            elif isinstance(argument, list):
                in_time_signatures = argument
                time_signatures_abjad = [
                    abjad.TimeSignature(_) for _ in in_time_signatures
                ]
            for time_sig in time_signatures_abjad:
                skip = abjad.Skip(1, multiplier=time_sig.pair)
                self.container.append(skip)
        else:
            self.container.extend(argument)

    def write_time_signatures(self, time_signatures):
        r"""Write time signatures."""
        site = "muda.Material.write_time_signatures()"
        tag = abjad.Tag(site)
        print(str(tag))
        # select skips to attach TIME SIGNATURES
        if isinstance(time_signatures[0], abjad.TimeSignature):
            in_time_signatures = [_.pair for _ in time_signatures]
        else:
            in_time_signatures = time_signatures
        result = abjad.select.leaves(self.container)
        result = abjad.select.partition_by_durations(
            result,
            in_time_signatures,
            cyclic=False,
            fill=abjad.Exact,
            in_seconds=False,
            overhang=True,
        )

        for time_sig, selection in zip(in_time_signatures, result):
            abjad.attach(
                abjad.TimeSignature(time_sig),
                abjad.select.leaf(selection, 0),
                tag=tag,
            )
            # print(abjad.select.leaf(selection, 0))
            # for i, item in enumerate(in_time_signatures):
            # a = in_time_signatures.index(item)
            # abjad.attach(
            #     time_signatures_abjad[a],
            #     self.container[i],
            #     tag=tag)

    def rewrite_meter(self, time_signatures):
        """Rewrite meter according to ``abjad.TimeSignature`` or ``tuple`` list."""
        if isinstance(time_signatures[0], abjad.TimeSignature):
            durations = [_.duration for _ in time_signatures]
        else:
            time_signatures = [abjad.TimeSignature(_) for _ in time_signatures]
            durations = time_signatures
        shards = abjad.mutate.split(self.container[:], durations)
        for shard, time_signature in zip(shards, time_signatures):
            abjad.Meter.rewrite_meter(
                shard,
                time_signature,
                # boundary_depth=1,
                # rewrite_tuplets=True,
                # maximum_dot_count=1,
            )

    def tuplet_number_tweak(container):
        selection = abjad.Selection(container).tuplets()
        for tuplet in selection:
            d = tuplet[0].written_duration
            d = d.lilypond_duration_string
            tweak = f'#(tuplet-number::append-note-wrapper tuplet-number::calc-fraction-text "{d}")'
            abjad.override(tuplet).TupletNumber.text = tweak

    def format_tuplets(self):
        selection = abjad.Selection(self.container).tuplets()
        for tuplet in selection:
            d = tuplet.multiplied_duration / tuplet.multiplier.numerator
            d = d.lilypond_duration_string
            dur = tuplet.multiplied_duration / 2
            dur = dur.lilypond_duration_string
            print(dur)
            print(tuplet.multiplied_duration, tuplet.multiplier, d)
            numerator = tuplet.multiplier.numerator
            denominator = tuplet.multiplier.denominator
            # print(numerator, denominator)
            tweak = f"#(tuplet-number::append-note-wrapper (tuplet-number::non-default-tuplet-fraction-text  {numerator} {denominator} (ly:make-duration {dur} 0))"
            override = abjad.LilyPondOverride(
                lilypond_type="Staff",
                grob_name="TupletNumber",
                once=True,
                property_path=("text",),
                value=tweak,
            )

            # abjad.override(tuplet, once=True).TupletNumber.text = tweak
