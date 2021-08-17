"""
Material.

Classes to create and manage music materials and lyrics.
"""
import abjad
import muda
from abjadext import rmakers
import random
from itertools import cycle


class Lyrics():
    """Lyrics."""

    def __init__(self, target):
        """Initializer."""
        self.lyrics = None
        self.target = target
        self.name = target + "_Lyrics"

    def write_lyrics(self, lyrics):
        """Method to write lyrics atribute to a ``muda.Lyrics`` instance."""
        self.lyrics = lyrics


class Material():
    """Material."""

    def __init__(self, name):
        """Initializer."""
        self.name = name
        self.container = abjad.Container()
        self.lyrics = None
        self.container.name = name

    def __call__(self):
        """It returns ``self.container``."""
        return self.container

    def write(self, lilypond_string):
        """It creates container from lilypond string and append to a ``muda.Material()`` instance."""
        self.container.extend(abjad.Container(lilypond_string))

    def alternating_materials(self, annotated_durations, makers_dict):
        """Create alternating materials according to a list of named durations."""
        assert isinstance(
            annotated_durations[0], list), "Each duration must be a list."

        material_names = []
        for dur in annotated_durations:
            material_names.append(dur[0].annotation)
        material_names = list(dict.fromkeys(material_names))

        assert isinstance(makers_dict, dict), "makers must be in a dictionary"
        for dur in annotated_durations:
                for mat in makers_dict:
                    if mat == dur[0].annotation:
                        if isinstance(makers_dict[mat], str):
                            self.container.append(
                                abjad.Container(
                                    makers_dict[mat],
                                    name=mat,
                                    identifier="% " + mat))
                        else:
                            selection = makers_dict[mat](dur)
                            if isinstance(selection[0], abjad.Tuplet):
                                sel = abjad.select(
                                    selection).components(abjad.Container)
                                for container in sel:
                                    container.name = mat
                                    container.identifier = "% " + mat
                                self.container.append(selection)
                            else:
                                self.container.append(
                                    abjad.Container(
                                        selection,
                                        name=mat,
                                        identifier="% " + mat))

        containers = abjad.select(self.container).components(abjad.Container)

        # write comments in lilypond code to identify materials
        for i, name in enumerate(material_names):
            j = 0
            for container in containers:
                if name in container.name:
                    container.name = container.name + "_" + str(j)
                    container.identifier = container.identifier + "_" + str(j)
                    if isinstance(container, abjad.Tuplet):
                        string = container.name
                        comment1 = abjad.LilyPondComment(string)
                        abjad.attach(comment1, container[0])
                        comment2 = abjad.LilyPondComment(string, format_slot="after")
                        abjad.attach(comment2, container[-1])
                    j += 1

    def silence_and_rhythm_maker(self, maker, annotated_divisions, *commands):
        """Create alternating rhythm and silence."""
        rest_maker = rmakers.stack(
            rmakers.note(),
            rmakers.force_rest(abjad.select())
        )
        for dur in annotated_divisions:
            if dur.annotation is not None:
                if dur.annotation.startswith("Rest") is True:
                    rests = rest_maker([dur])
                    self.container.extend(rests)
            else:
                selection = maker([dur], *commands)
                self.container.extend(selection)

    def write_pitches(self, pitches):
        """Write pitches to notes in the Material instance."""
        logical_ties = abjad.select(self.container).leaves().logical_ties(
            pitched=True
        )
        for i, logical_tie in enumerate(logical_ties):
            index = i % len(pitches)
            pitch = pitches[index]
            for note in logical_tie:
                if isinstance(note, abjad.Rest):
                    pass
                else:
                    note.written_pitch = pitch

    def write_pitches_by_duration(
        self,
        annotated_pitches,
        annotated_durations,
        randomize=0,
    ):
        """Write pitches to notes according to annotated durations."""
        try:
            assert isinstance(annotated_durations[0], list)
        except AssertionError(" error"):
            print("Each duration or set of durations should be inside a list.")

        chords_test = False
        for key in annotated_pitches:
            for item in annotated_pitches[key]:
                if isinstance(item, list):
                    chords_test = True

        if chords_test is True:
            # convert notes to chords
            convertion = abjad.select(self.container).leaves(pitched=True)
            for note in convertion:
                chord = abjad.Chord("c'", note.written_duration)
                abjad.mutate.replace(note, chord)

        # select by duration:
        abjad_durations = []
        for dur in annotated_durations:
            abjad_durations.append(sum(dur))
        selector = (
            abjad.select()
            .leaves()
            .partition_by_durations(
                abjad_durations,
                cyclic=True,
                fill=abjad.Exact,
                in_seconds=False,
                overhang=True,
            )
        )
        selections = selector(self.container)

        for key in annotated_pitches:
            pitches = cycle(annotated_pitches[key])
            for selection, duration in zip(selections, annotated_durations):
                logical_ties = abjad.select(selection).leaves().logical_ties(pitched=True)
                for a, logical_tie in enumerate(logical_ties):
                    pitch = next(pitches)
                    for item in duration:
                        if item.annotation == key:
                            for b, chord in enumerate(logical_tie):
                                if isinstance(chord, abjad.Chord):
                                    chord.written_pitches = pitch
                                else:
                                    chord.written_pitch = pitch
                                # if randomize != 0:
                                #     var = a + random.randrange(randomize)
                                #     index = var % len(pitches)
                                #     pitch = pitches[index]
                                #     chord.written_pitches = pitch
                                # else:
                                #     index = a % len(pitches)
                                #     pitch = pitches[index]
                                #     chord.written_pitches = pitch

        # for selection, duration in zip(selections, annotated_durations):
        #     logical_ties = abjad.select(selection).leaves().logical_ties(pitched=True)
        #     for a, logical_tie in enumerate(logical_ties):
        #         for item in duration:
        #             if item.annotation in annotated_pitches:
        #                 for b, chord in enumerate(logical_tie):
        #                     pitches = annotated_pitches[item.annotation]
        #                     if randomize != 0:
        #                         var = a + random.randrange(randomize)
        #                         index = var % len(pitches)
        #                         pitch = pitches[index]
        #                         chord.written_pitches = pitch
        #                     else:
        #                         index = a % len(pitches)
        #                         pitch = pitches[index]
        #                         chord.written_pitches = pitch
                        # pitches = annotated_pitches[item.annotation]
                        # index = i % len(pitches)
                        # pitch = pitches[index]
                        # if isinstance(logical_tie[0], abjad.Rest):
                        #     new_container.extend(logical_tie)
                        #     print(logical_tie)
                        # else:
                        #     for note in logical_tie:
                        #         if isinstance(pitch, list):
                        #             chord = abjad.Chord((pitch), (1, 4))
                        #             chord.written_duration = note.written_duration
                        #             new_container.extend(chord)
                        #             print(chord)
                        #         else:
                        #             note.written_pitch = pitch
                        #             new_container.extend(note)
                        #             print(note)
            # print(abjad.lilypond(self.container))
            # return new_container

        # containers = abjad.select(self.container).components(abjad.Container)
        # names = annotated_pitches.keys()
        # for name in names:
        #     for container in containers:
        #         if container.name is not None:
        #             if name in container.name:
        #                 logical_ties = abjad.select(container).leaves().logical_ties()
        #                 for a, logical_tie in enumerate(logical_ties):
        #                     for b, note in enumerate(logical_tie):
        #                         pitches = annotated_pitches[name]
        #                         index = a % len(pitches)
        #                         pitch = pitches[index]
        #                         if isinstance(pitch, list):
        #                             if b < len(logical_tie) - 1:
        #                                 chord = abjad.Chord(pitch, (1, 4))
        #                                 chord.written_duration = note.written_duration
        #                                 abjad.attach(abjad.Tie(), chord)
        #                                 abjad.mutate.replace(note, chord)
        #                             else:
        #                                 chord = abjad.Chord(pitch, (1, 4))
        #                                 chord.written_duration = note.written_duration
        #                                 abjad.mutate.replace(note, chord)
        #                         else:
        #                             note.written_pitch = pitch

        # selections = selector(self.container)
        # _write_mixed(selections, annotated_durations, annotated_pitches)

    def see_leaves_number(self, pitched=True):
        """Illustrate ``muda.Material.container`` with leaves number."""
        selection = abjad.select(self.container).leaves(
            pitched=pitched, grace=False)
        for i, leaf in enumerate(selection):
            str_ = r"\tiny {\null { \raise #2 {%i}}}" % (i)
            abjad.attach(
                abjad.Markup(str_, direction=abjad.Up), leaf,
            )
        abjad.show(self.container)

    def see_materials_leaves_number(self, pitched=True):
        """Illustrate ``muda.Material.container`` with materials leaves number."""
        selection1 = abjad.select(self.container).components(abjad.Container)

        for container in selection1:
            if container.name is not None:
                if container.name is not self.name:
                    if isinstance(container[0], abjad.Container):
                        if container[0].name is not container.name:
                            selection2 = abjad.select(container).leaves(
                                pitched=pitched, grace=False)
                            for i, leaf in enumerate(selection2):
                                # str_ = r"\tiny {\null { \raise #2 {%i}}}" %
                                # (i))
                                abjad.attach(
                                    abjad.Markup(
                                        str(i), direction=abjad.Up), leaf,
                                )
                                if i == 0:
                                    abjad.attach(
                                        abjad.Markup(
                                            container.name,
                                            direction=abjad.Up
                                        ),
                                        leaf,
                                    )
                    else:
                        selection2 = abjad.select(container).leaves(
                            pitched=pitched, grace=False)
                        for i, leaf in enumerate(selection2):
                            # str_ = r"\tiny {\null \null { \raise #2
                            # {%i}}}" % (i))
                            abjad.attach(
                                abjad.Markup(str(i), direction=abjad.Up), leaf,
                            )
                            if i == 0:
                                # str_name = r"\tiny {\null \null \null
                                # { \raise #2 {" + container.name + r"}}}"
                                abjad.attach(
                                    abjad.Markup(
                                        container.name,
                                        direction=abjad.Up
                                    ),
                                    leaf,
                                )
        abjad.show(self.container)

    def write_indicators(
        self,
        material_name=None,
        dynamics={},
        articulations=[],
        slur_up=[],
        slur_down=[],
        change_staffs_names={},
        pitched=True,
    ):
        """Write indicators to leaves."""
        if material_name is not None:
            selection1 = abjad.select(
                self.container).components(abjad.Container)
            for container in selection1:
                if container.name is not None:
                    if (isinstance(material_name, list) or
                       material_name in container.name):
                            selection2 = abjad.select(
                                container).leaves(pitched=pitched)
                            if dynamics:
                                for key in dynamics:
                                    if dynamics[key] == "all":
                                        for i, leaf in enumerate(selection2[0::2]):
                                            a = i
                                            b = i + 1
                                            abjad.hairpin(
                                                key,
                                                selection2[a:b])
                                    else:
                                        for i in dynamics[key]:
                                            if isinstance(i, tuple):
                                                a, b = i
                                                b = b + 1
                                                abjad.hairpin(
                                                    key,
                                                    selection2[a:b])
                                            else:
                                                abjad.hairpin(
                                                    key,
                                                    selection2[i])

                            # attach slurs
                            if slur_up:
                                for n in slur_up:
                                    a, b = n
                                    b = b
                                    abjad.attach(
                                        abjad.StartSlur(), selection2[a])
                                    abjad.attach(
                                        abjad.StopSlur(), selection2[b])

                            if slur_down:
                                for n in slur_down:
                                    a, b = n
                                    abjad.attach(
                                        abjad.StartSlur(direction=abjad.Down),
                                        selection2[a]
                                    )
                                    abjad.attach(
                                        abjad.StopSlur(),
                                        selection2[b])

                            if articulations:
                                for key in articulations:
                                    for i in articulations[key]:
                                        abjad.attach(
                                            abjad.Articulation(key),
                                            selection2[i])
        else:
            selection = abjad.select(self.container).leaves(pitched=pitched)

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
                    abjad.attach(
                        abjad.StartSlur(direction=abjad.Down), selection[a]
                    )
                    abjad.attach(abjad.StopSlur(), selection[b])

            if articulations:
                for key in articulations:
                    for i in articulations[key]:
                        abjad.attach(
                            abjad.Articulation(key), selection[i])

    #      # change staff
    # rh_staff = score['Piano_Staff'][0]
    # lh_staff = score['Piano_Staff'][1]
    # voice_four = score['LH_Voice_Four']

    # staff_change1 = abjad.StaffChange(lh_staff)
    # staff_change2 = abjad.StaffChange(rh_staff)
    # abjad.attach(staff_change2, voice_four[-5])
    # abjad.attach(staff_change1, voice_four[-2])

    def attach(
        self,
        argument,
        leaves,
        material_name=None,
        pitched=False,
        select="leaves"
    ):
        """Attach ``argument`` to leaves."""
        if pitched is True:
            grace = False
        else:
            grace = None
        if isinstance(argument, str) or isinstance(argument, list):
            argument = abjad.LilyPondLiteral(argument)

        if select == "logical_ties":
            def selector(argument):
                selection = abjad.select(
                    argument).logical_ties(pitched=True, grace=grace)
                return selection
        else:
            def selector(argument):
                selection = abjad.select(
                    argument).leaves(pitched=pitched, grace=grace)
                return selection

        if material_name is not None:
            selection = abjad.select(self.container).components(abjad.Container)
            indices = []
            for i, container in enumerate(selection):
                if container.name != material_name:
                    indices.append(i)
            containers = containers.exclude(indices)
            if isinstance(material_name, list):
                for container in selection:
                    if container.name is not None:
                        for item in material_name:
                            if item in container.name:
                                # print("1")
                                selection2 = selector(container)
                                if isinstance(leaves, int):
                                    abjad.attach(
                                        argument,
                                        selection2[leaves])
                                    # string = "material_name is list and leaves is int"
                                    # comment1 = abjad.LilyPondComment(string)
                                    # abjad.attach(comment1, selection2[leaves])
                                elif leaves == "all":
                                    for leaf in selection2:
                                        abjad.attach(
                                            argument,
                                            leaf)
                                        # string = "material_name is list and apply to all leaves"
                                        # comment1 = abjad.LilyPondComment(string)
                                        # abjad.attach(comment1, selection2[leaf])
                                else:
                                    for leaf in leaves:
                                        abjad.attach(
                                            argument,
                                            selection2[leaf])
                                        # string = "material_name is list and leaves is int"
                                        # comment1 = abjad.LilyPondComment(string)
                                        # abjad.attach(comment1, selection2[leaves])
            else:
                for container in selection:
                    # print(abjad.lilypond(container))
                    if material_name in container.name:
                        selection3 = selector(container)
                        # print("2", container.name)
                        if isinstance(leaves, int):
                            if isinstance(selection3[leaves], abjad.Leaf):
                                abjad.attach(
                                    argument,
                                    selection3[leaves])
                                # string = "material_name is string and leaves is int"
                                # comment1 = abjad.LilyPondComment(string)
                                # abjad.attach(comment1, selection3[leaves])
                        elif leaves == "all":
                            for leaf in selection3:
                                abjad.attach(
                                    argument,
                                    leaf)
                                # string = container.name + material_name + "material_name is string and leaves is all"
                                # comment1 = abjad.LilyPondComment(string)
                                # abjad.attach(comment1, leaf)
                        else:
                            for leaf in leaves:
                                if isinstance(selection3[leaf], abjad.Leaf):
                                    abjad.attach(
                                        argument,
                                        selection3[leaf])
                                    # string = container.name + material_name + "material_name is string and leaves is list"
                                    # comment1 = abjad.LilyPondComment(string)
                                    # abjad.attach(comment1, selection3[leaf])
        else:
            # print("3")
            selection2 = selector(self.container)
            if isinstance(leaves, int):
                abjad.attach(
                    argument,
                    selection2[leaves])
                # string = "material_name is None and leaves is int"
                # comment1 = abjad.LilyPondComment(string)
                # abjad.attach(comment1, selection2[leaves])
            else:
                for leaf in leaves:
                    if pitched == "logical_ties":
                        abjad.attach(
                            argument,
                            selection2[leaf][0])
                    else:
                        abjad.attach(
                            argument,
                            selection2[leaf])
                    # string = "material_name is None and leaves is list"
                    # comment1 = abjad.LilyPondComment(string)
                    # abjad.attach(comment1, selection2[leaf])

    def note_heads(self, material_name, argument, leaves=None):
        """Change leaves note heads."""
        selection = abjad.select(self.container[:]).components(abjad.Container)
        for container in selection:
            if container.name is not None:
                if material_name in container.name:
                    if leaves is None:
                        abjad.override(container).NoteHead.style = argument
                    else:
                        selection2 = abjad.select(container).leaves()
                        for i, leaf in enumerate(selection2):
                            if i in leaves:
                                abjad.override(leaf).NoteHead.style = argument

    def retrograde(self, material_name):
        """Retrograde components in container."""
        selection = abjad.select(self.container[:]).components(abjad.Container)
        for container in selection:
            if container.name is not None:
                if material_name in container.name:
                    items = abjad.select(container).items
                    # print(container.components)
                    new_container = abjad.Container(name=container.name)
                    for item in reversed(items):
                        for comp in reversed(item.components):
                            if isinstance(comp, abjad.Tuplet):
                                new_tuplet = abjad.Tuplet(
                                    multiplier=comp.multiplier,
                                    denominator=comp.denominator)
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
    #     selection1 = abjad.select(self.container).components(abjad.Container)
    #     for container in selection1:
    #         if material_name in container.name:
    #             container[selection] = change

    # def delete_material_leaves(self, material_name, leaves):
    #     """Todo."""
    #     selection = abjad.select(self.container).components(abjad.Container)
    #     for container in selection:
    #         print(container)
    #         if material_name in container.name:
    #             for _ in leaves:
    #                 del container[_]

    def delete(
        self,
        leaves,
        material_name=None,
        replace_with_rests=False,
        replace_with_skips=False
    ):
        """Delete leaves by index.

        Use ``material_name`` to delete a leaf in a
        specific material. Use ``replace_with_rests`` or
        ``replace_with_skips`` to replace leaves by rests or skips.
        """
        if material_name is not None:
            selection1 = abjad.select(
                self.container).components(abjad.Container)
            for container in selection1:
                if container.name is not None:
                    if (isinstance(material_name, list) or
                       material_name in container.name):
                            selection2 = abjad.select(container).leaves()
                            for l in leaves:
                                if (replace_with_rests is False and
                                   replace_with_skips is False):
                                        del selection2[l]
                                elif replace_with_skips is True:
                                    abjad.mutate.replace(
                                        selection2[l],
                                        abjad.Skip(
                                            selection2[l].written_duration))
                                elif replace_with_rests is True:
                                    abjad.mutate.replace(
                                        selection2[l],
                                        abjad.Rest(
                                            selection2[l].written_duration))
        else:
            selection = abjad.select(self.container).leaves()
            for l in leaves:
                if replace_with_rests is False and replace_with_skips is False:
                    del selection[l]
                elif replace_with_skips is True:
                    abjad.mutate.replace(
                        selection[l],
                        abjad.Skip(selection[l].written_duration))
                elif replace_with_rests is True:
                    abjad.mutate.replace(
                        selection[l],
                        abjad.Rest(selection[l].written_duration))

    def print(self):
        """Print ``muda.Material.container`` lilypond code."""
        print(abjad.lilypond(self.container))

    def show(self):
        """Illustrate ``muda.Material.container``."""
        abjad.show(self.container)
