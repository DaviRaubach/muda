#!$HOME/github/my_venv/bin/python

import abjad
from abjadext import rmakers


class Material:
    def __init__(self, name):
        self.name = name
        self.container = abjad.Container()
        self.container.name = name

    def SilenceAndRythmMaker(self, maker, annotated_divisions, *commands):
        rest_maker = rmakers.stack(rmakers.note(), rmakers.force_rest(abjad.select()))
        for dur in annotated_divisions:
            if dur.annotation.startswith("Rests ") is True:
                rests = rest_maker([dur])
                self.container.extend(rests)
            else:
                selection = maker([dur], *commands)
                self.container.extend(selection)
        return self.container

    def WritePitches(self, pitches):
        logical_ties = abjad.select(self.container).leaves().logical_ties(pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            index = i % len(pitches)
            pitch = pitches[index]
            for note in logical_tie:
                if isinstance(note, abjad.Rest):
                    pass
                else:
                    note.written_pitch = pitch
        return self.container

    def WriteIndicators(
        self,
        see_leaves_number=False,
        dynamic_list=[],
        attach_dyn_lists=[],
        slur_up=[],
        slur_down=[],
        articulation_names=[],
        articulation_leafs=[],
        abjad_literal_indicators=[],
        abjad_literal_leafs=[],
    ):
        selection = abjad.select(self.container).leaves()
        if see_leaves_number == True:
            for i, leaf in enumerate(selection):
                str_ = r"\tiny {\null { \raise #2 {%i}}}" % (i)
                abjad.attach(
                    abjad.Markup(str_, direction=abjad.Up), leaf,
                )

        if dynamic_list and attach_dyn_lists:
            for dyn, leaf in zip(dynamic_list, attach_dyn_lists):
                for i in leaf:
                    if isinstance(i, tuple):
                        a, b = i
                        b = b + 1
                        abjad.hairpin(dyn, selection[a:b])
                    else:
                        abjad.hairpin(dyn, selection[i])

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
                b = b + 1
                abjad.attach(abjad.StartSlur(direction=abjad.Down), selection[a])
                abjad.attach(abjad.StopSlur(), selection[b])

        return self.container

    def MakeMaterial(self):
        return self.container

    def AlternatingMaterials(
        self, annotated_divisions, *makers
    ):  # maybe I should include *commands for rmaker.stack
        n_materials = len(makers)
        for dur in annotated_divisions:
            for maker in makers:
                if maker.tag.string == dur.annotation:
                    selection = maker([dur])
                    self.container.extend(selection)
        return self.container


# test = Material()
# test.WriteIndicators(pp=[1, 2])
