"""
Material.

Classes to create and manage music materials and lyrics.
"""
import abjad
from abjadext import rmakers


class Lyrics():
    """Lyrics."""

    def __init__(self, target):
        """Todo."""
        self.lyrics = None
        self.target = target
        self.name = target + "_Lyrics"

    def write_lyrics(self, lyrics):
        """Write lyrics atribute to a ``muda.Lyrics`` instance."""
        self.lyrics = lyrics


class Material():
    """Material."""

    def __init__(self, name):
        """Todo."""
        self.name = name
        self.container = abjad.Container()
        self.lyrics = None
        self.container.name = name

    def __call__(self):
        """Todo."""
        return self.container

    def write(self, lilypond_string):
        """Create container from lilypond string and append to a ``muda.Material()`` instance."""
        self.container.extend(abjad.Container(lilypond_string))

    def alternating_materials(self, annotated_divisions, *makers):
        """Create alternating materials according to a list of named durations."""
        # maybe I should include *commands for rmaker.stack
        material_names = []
        for dur in annotated_divisions:
            material_names.append(dur.annotation)
            for item in makers:
                if isinstance(item, dict):
                    rhythm_makers = item
                    for mat in rhythm_makers:
                        if mat == dur.annotation:
                            if isinstance(rhythm_makers[mat], str):
                                self.container.append(
                                    abjad.Container(
                                        rhythm_makers[mat],
                                        name=mat,
                                        identifier="% " + mat))
                            else:
                                selection = rhythm_makers[mat]([dur])
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
                if isinstance(item, rmakers.Stack):
                    maker = item
                    if maker.tag.string == dur.annotation:
                        selection = maker([dur])
                        if isinstance(selection[0], abjad.Tuplet):
                            self.container.append(selection)
                        else:
                            self.container.append(
                                abjad.Container(selection, tag=maker.tag))
        containers = abjad.select(self.container).components(abjad.Container)
        material_names = list(dict.fromkeys(material_names))
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
        annotated_durations
    ):
        """Write pitches to notes according to annotated durations."""
        abjad_durations = []
        for dur in annotated_durations:
            abjad_durations.append(dur)
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

        for selection, duration in zip(selections, annotated_durations):
            logical_ties = abjad.select(selection).leaves().logical_ties(
                pitched=True
            )
            for i, logical_tie in enumerate(logical_ties):
                if duration.annotation in annotated_pitches:
                    pitches = annotated_pitches[duration.annotation]
                    index = i % len(pitches)
                    pitch = pitches[index]
                    for note in logical_tie:
                        note.written_pitch = pitch

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
            pass
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
        leaf,
        material_name=None,
        pitched=False
    ):
        """Attach ``argument`` to leaves."""
        selection = abjad.select(self.container).components(abjad.Container)
        if pitched is True:
            grace = False
        else:
            grace = None
        if isinstance(argument, str) or isinstance(argument, list):
            argument = abjad.LilyPondLiteral(argument)

        if material_name is not None:
            if isinstance(material_name, list):
                for container in selection:
                    if container.name is not None:
                        for item in material_name:
                            if item in container.name:
                                selection2 = abjad.select(
                                    container).leaves(pitched=pitched, grace=grace)
                                if isinstance(container[0], abjad.Container):
                                    if isinstance(container[0], abjad.Tuplet):
                                        abjad.attach(
                                            argument,
                                            selection2[leaf])
                                else:
                                    abjad.attach(
                                        argument,
                                        selection2[leaf])
            else:
                for container in selection:
                    if container.name is not None:
                        # print(container)
                        test = container.name.startswith(material_name)
                        # print(test)
                        if test is True:
                            # leaf = abjad.get.leaf(container, 1)
                            # print(leaf)
                            selection2 = abjad.select(container[:]).leaves()
                            if isinstance(selection2[leaf], abjad.Leaf):
                                abjad.attach(
                                    argument,
                                    selection2[leaf])
        else:
            selection2 = abjad.select(
                self.container[:]).leaves(pitched=pitched, grace=grace)
            abjad.attach(
                argument,
                selection2[leaf])

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
