"""
Todo.

Todo.
"""
import abjad
from abjadext import rmakers


class Material:
    """Todo."""

    def __init__(self, name):
        """Todo."""
        self.name = name
        self.container = abjad.Container()
        self.container.name = name

    def write(self, lilypond_string):
        """Todo."""
        pass

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
                b = b + 1
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
