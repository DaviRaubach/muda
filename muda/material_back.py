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

    def __call__(self) -> abjad.Container():
        """It returns ``self.container``."""
        return self.container

    def write(self, lilypond_string, name=None):
        """It creates container from lilypond string and append to a ``muda.Material()`` instance."""
        self.container.extend(
            abjad.Container(lilypond_string, name=name))

    def alternating_materials(self, annotated_durations: list, makers: dict):
        """Create alternating materials according to a list of named durations."""
        assert isinstance(
            annotated_durations[0], list), "Each duration set must be a list."

        material_names = []
        for dur in annotated_durations:
            material_names.append(dur[0].annotation)
        material_names = list(dict.fromkeys(material_names))

        assert isinstance(makers, dict), "makers must be in a dictionary"
        for dur in annotated_durations:
            for mat in makers:
                if mat == dur[0].annotation:
                    if isinstance(makers[mat], str):
                        self.container.append(
                            abjad.Container(
                                makers[mat],
                                name=mat,
                                identifier="% " + mat))
                    else:
                        selection = makers[mat](dur)
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

    def write_pitches(self, pitches):
        """Write pitches to notes in the Material instance."""
        logical_ties = abjad.select(self.container).leaves().logical_ties(
            pitched=True
        )
        for i, logical_tie in enumerate(logical_ties):
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
        """Write pitches to notes according to annotated durations."""
        assert isinstance(
            annotated_durations[0], list), "Each duration set must be a list."

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
                logical_ties = abjad.select(
                    selection).leaves().logical_ties(pitched=True)
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

    def see_leaves_number(self, select="leaves", pitched=True):
        """Illustrate ``muda.Material.container`` with leaves number."""
        if select == "leaves":
            selection = abjad.select(self.container).leaves(
                pitched=pitched, grace=False)
            for i, leaf in enumerate(selection):
                str_ = r"\tiny {\null { \raise #2 {%i}}}" % (i)
                abjad.attach(
                    abjad.Markup(str_, direction=abjad.Up), leaf,
                )

        elif select == "logical_ties":
            selection = abjad.select(self.container).leaves().logical_ties(
                pitched=pitched, grace=False)
            for i, leaf in enumerate(selection):
                str_ = r"\tiny {\null { \raise #2 {%i}}}" % (i)
                abjad.attach(
                    abjad.Markup(str_, direction=abjad.Up), leaf[0],
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
                            abjad.attach(
                                abjad.Markup(str(i), direction=abjad.Up), leaf,
                            )
                            if i == 0:
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
        argument: str or list,
        leaves: list,
        material_name=None,
        pitched=False,
        select="leaves"
    ):
        """Attach ``argument`` to leaves."""
        if pitched is True:
            grace = False
        else:
            grace = None

        if isinstance(argument, str or list):
            argument = abjad.LilyPondLiteral(argument)

        if select == "logical_ties":
            def selector(argument):
                selection = abjad.select(
                    argument).logical_ties(pitched=True, grace=grace)
                return selection
        elif select == "leaves":
            def selector(argument):
                selection = abjad.select(
                    argument).leaves(pitched=pitched, grace=grace)
                return selection

        if isinstance(material_name, str):
            material_name = [material_name]

        if not isinstance(leaves, list):
            leaves = [leaves]

        def attach_to_materials():
            for mat_name in material_name:
                selection = self._select_material(self, mat_name)
                for container in selection:
                    container_selection = selector(container)
                    if leaves == "all":
                        for leaf in container_selection:
                            abjad.attach(
                                argument,
                                leaf)
                    else:
                        for leaf in leaves:
                            abjad.attach(
                                argument,
                                container_selection[leaf])

        def attach_to_parent_container():
            selection = selector(self.container)
            for leaf in leaves:
                if isinstance(selection[leaf], abjad.LogicalTie):
                    abjad.attach(
                        argument,
                        selection[leaf][0])
                else:
                    abjad.attach(
                        argument,
                        selection[leaf])

        if material_name is not None:
            attach_to_materials()  # attaches to leaves in specified materials.
        else:
            attach_to_parent_container()  # attaches to ``self.container`` leaves.

    def change_staffs(self, *staves_names):
        selection = abjad.select(
            self.container).leaves(pitched=True)

        staff1 = staves_names[0]
        staff2 = staves_names[1]

        pitch_range1 = abjad.PitchRange("[C4, +inf]")

        string = r'\change Staff = '

        for leaf in selection:
            if isinstance(leaf, abjad.Note):
                if leaf.written_pitch in pitch_range1:
                    




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

    @staticmethod
    def _select_material(self, material_name):
        """Select container by name."""
        selection = abjad.select(
            self.container).components(abjad.Container)
        indices = []
        for i, container in enumerate(selection):
            if container.name != material_name:
                indices.append(i)
        filtered_selection = selection.exclude(indices)
        return filtered_selection

if __name__ == "__main__":
    mat = Material("A")
    mat.write("c,4 d,4", "material_1")
    mat.attach(abjad.Clef("bass"), 0)
    mat.attach(r"\stopStaff", 1, "material_1")
    mat.print()
