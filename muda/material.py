"""
Todo.

Todo.
"""
import abjad
from abjadext import rmakers


class Lyrics():
    """Todo."""

    def __init__(self, target):
        """Todo."""
        self.lyrics = None
        self.target = target
        self.name = target + "_Lyrics"

    def write_lyrics(self, lyrics):
        """Write lyrics atribute to a ``muda.Lyrics`` instance."""
        self.lyrics = lyrics

# trabalhar com a letra de tal maneira que tu tenha um target
# a unica especificação é o target
# pra onde tu quer que a letra seja attached
# cria o contexto de lyrics no momento de criar o instrumento
# cria muda.Lyrics como se fosse muda.Material
# coloca muda.Lyrics("target_voice") para adicionar a letra ao target
# usa o muda.Lyrics().write_lyrics para add letra


class Material():
    """Todo."""

    def __init__(self, name):
        """Todo."""
        self.name = name
        self.container = abjad.Container()
        self.lyrics = None
        self.container.name = name

    def write(self, lilypond_string):
        """Todo."""
        self.container.extend(lilypond_string)

    def alternating_materials(self, annotated_divisions, *makers):
        """Todo."""
        # maybe I should include *commands for rmaker.stack
        for dur in annotated_divisions:
            for maker in makers:
                # if isinstance(maker, abjad.Container):
                #     if maker.tag.string == dur.annotation:
                #         # print("appending", maker.tag.string)
                #         self.container.append(maker)
                # print("maker", maker.tag.string)
                # print("dur", dur.annotation)
                if maker.tag.string == dur.annotation:
                    selection = maker([dur])
                    # print("appending", maker.tag.string)
                    if isinstance(selection[0], abjad.Tuplet):
                        # print("sou tup")
                        # selection.tag = maker.tag
                        self.container.append(selection)
                    else:
                        self.container.append(
                            abjad.Container(selection, tag=maker.tag))
                # else:
                #     print('maker should be ``rmakers.stack`'
                #           ' or dictionary containing a lilypond string'
                #           ' such as: ``"mat01": ("c,4 d,4")`')

    def silence_and_rhythm_maker(self, maker, annotated_divisions, *commands):
        """Todo."""
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

    def write_lyrics(self, lyrics):
        """Todo."""
        self.lyrics = lyrics

    def write_pitches(self, pitches):
        """Todo."""
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
        """Todo."""
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
        """Todo."""
        selection = abjad.select(self.container).leaves(pitched=pitched)
        # see_leaves = selection._copy()
        for i, leaf in enumerate(selection):
            str_ = r"\tiny {\null { \raise #2 {%i}}}" % (i)
            abjad.attach(
                abjad.Markup(str_, direction=abjad.Up), leaf,
            )
        # abjad.show(abjad.Container(see_leaves))

    def write_indicators(
        self,
        material_name=None,
        dynamics={},
        articulations=[],
        slur_up=[],
        slur_down=[],
        literal_indicators=[],
        literal_leaves=[],
        change_staffs_names={},
        attach=(),  # tuple
        pitched=True,
    ):
        """Todo."""
        if material_name is not None:
            pass
            selection1 = abjad.select(self.container).components(abjad.Container)
            for container in selection1:
                if container.tag is not None:
                    if (isinstance(material_name, list) or
                       container.tag.string == material_name):
                            selection2 = abjad.select(container).leaves(pitched=pitched)
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
                                        abjad.attach(
                                            abjad.Articulation(key), selection2[i])

                            # literal
                            if literal_indicators:
                                for literal, n in zip(literal_indicators, literal_leaves):
                                    abjad.attach(
                                        abjad.LilyPondLiteral(literal), selection2[n])

                            # attach
                            if attach:
                                # print(abjad.lilypond(self.container))
                                a, b = attach
                                abjad.attach(a, selection2[b])

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

            # literal
            if literal_indicators:
                for literal, n in zip(literal_indicators, literal_leaves):
                    abjad.attach(
                        abjad.LilyPondLiteral(literal), selection[n])

            # attach
            if attach:
                # print(abjad.lilypond(self.container))
                a, b = attach
                abjad.attach(a, selection[b])

    #      # change staff
    # rh_staff = score['Piano_Staff'][0]
    # lh_staff = score['Piano_Staff'][1]
    # voice_four = score['LH_Voice_Four']

    # staff_change1 = abjad.StaffChange(lh_staff)
    # staff_change2 = abjad.StaffChange(rh_staff)
    # abjad.attach(staff_change2, voice_four[-5])
    # abjad.attach(staff_change1, voice_four[-2])

    def attach(self, material_name, argument, leaf, pitched=False):
        """Todo."""
        selection = abjad.select(self.container[:]).components(abjad.Container)
        if isinstance(argument, str):
            argument = abjad.LilyPondLiteral(argument)

        if material_name is not None:
            if isinstance(material_name, list):
                for container in selection:
                    if container.tag is not None:
                        if container.tag.string in material_name:
                            selection2 = abjad.select(
                                container).leaves(pitched=pitched)
                            if isinstance(container[0], abjad.Container):
                                pass
                            else:
                                abjad.attach(
                                    argument,
                                    selection2[leaf])
            else:
                for container in selection:
                    if container.tag is not None:
                        if container.tag.string == material_name:
                            selection2 = abjad.select(
                                container).leaves(pitched=pitched)
                            abjad.attach(
                                argument,
                                selection2[leaf])
        else:
            selection2 = abjad.select(
                self.container[:]).leaves(pitched=pitched)
            abjad.attach(
                argument,
                selection2[leaf])

    def note_heads(self, material_name, argument):
        """Todo."""
        selection = abjad.select(self.container[:]).components(abjad.Container)
        for container in selection:
            if container.tag is not None:
                if container.tag.string == material_name:
                    abjad.override(container).NoteHead.style = argument

    def get_container(self):
        """Todo."""
        return self.container

    def retrograde(self, material_name):
        """Todo."""
        selection = abjad.select(self.container[:]).components(abjad.Container)
        for container in selection:
            if container.tag.string == material_name:
                # print("cont", container)
                l = len(container)
                new_container = abjad.Container(tag=container.tag)
                while l > 0:
                    l -= 1
                    new_container.append(container[l])

                container.append(new_container)
                # print("new cont", new_container)

    def change(self, material_name, selection, change):
        """Todo."""
        selection1 = abjad.select(self.container).components(abjad.Container)
        for container in selection1:
            if container.tag.string == material_name:
                container[selection] = change

    def delete_material_leaves(self, material_name, leaves):
        """Todo."""
        selection = abjad.select(self.container).components(abjad.Container)
        for container in selection:
            print(container)
            if container.tag == material_name:
                for _ in leaves:
                    del container[_]

    def delete(
        self,
        leaves,
        material_name=None,
        replace_with_rests=False,
        replace_with_skips=False
    ):
        """Delete leaves by index."""
        if material_name is not None:
            selection1 = abjad.select(
                self.container).components(abjad.Container)
            for container in selection1:
                if container.tag is not None:
                    if (isinstance(material_name, list) or
                       container.tag.string == material_name):
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
