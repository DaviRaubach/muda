"""
Material.

Classes to cte and manage music materials and lyrics.
"""
import abjad
import muda
import inspect
import time
import os
from itertools import cycle
from copy import copy
from .data.guitar_bitones_dict import binotes
from . import score as _score


class Lyrics:
    """Lyrics."""

    def __init__(self, target):
        """Initializer."""
        self.lyrics = None
        self.target = target
        self.name = target + "_Lyrics"
        self.align = "CENTER"

    def write_lyrics(self, lyrics):
        """Method to write lyrics attribute to a ``muda.Lyrics`` instance."""
        self.lyrics = lyrics

    # def align(self, align: str):
    #     """Method to align lyrics on the left."""
    #     self.align = align


def write_on_materials(materials, fn_dict_list: list[dict]):
    """Junta os materiais e executa funções de acordo com um dicinário"""
    for material in materials:
        for fn_dict in fn_dict_list:
            if material.name in fn_dict.keys:
                fn_dict[material.name](material)


class Box:
    """Armazena funções para operar materiais."""

    def __init__(self, name=None, functions=[]):
        self.name = name
        self.functions = functions
        # if functions:
        #     self.append_function(functions)
        #     print(functions, "1")

    def append_function(self, function_list: list):
        for function in function_list:
            # print(function)
            self.functions.append(function)


class TimespanRhythmBox(Box):
    """Armazena funções rítmicas para operar materiais."""

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
                        parser = abjad.parser.LilyPondParser()
                        contents = parser(makers[maker])
                        container = abjad.Container(
                            name=maker, identifier="% " + maker)
                        internal = abjad.Container(makers[maker])
                        cont_dur = internal._get_duration()
                        container.append(contents)
                        self.container.append(container)
                        difference = sum(dur) - cont_dur
                        while difference >= cont_dur:
                            copy = abjad.mutate.copy(contents)
                            new_container = abjad.Container(
                                name=maker, identifier="% " + maker
                            )
                            new_container.append(copy)
                            self.container.append(new_container)
                            difference = difference - cont_dur
                    else:
                        selection = makers[maker](dur)

                        appendice = abjad.Container(
                            selection, name=maker, identifier="% " + maker
                        )
                        for item in appendice:
                            if isinstance(item, abjad.Tuplet):
                                item.name = "_"
                                item.identifier = "_"
                        self.container.append(appendice)

        # add indices to materials and write comments
        # in lilypond code to identify materials
        for i, name in enumerate(material_names):
            selectable = self.select_material(self.container, name)
            containers = abjad.select.components(selectable, abjad.Container)
            j = 0
            for container in containers:
                if container.name and container.identifier:
                    if name in container.name:
                        container.name = container.name + "_" + str(j)
                        container.identifier = container.identifier + \
                            "_" + str(j)
                        if isinstance(container, abjad.Tuplet):
                            string = container.name
                            comment1 = abjad.LilyPondComment(string)
                            abjad.attach(comment1, container[0])
                            comment2 = abjad.LilyPondComment(
                                string, format_slot="after"
                            )
                            abjad.attach(comment2, container[-1])
                        j += 1


class AlternatingMaterialsBox(Box):
    """
    TODO Armazena funções para inscrever submateriais alternados nos materiais.
    """

    def __init__(self, name=None):
        self.name = name


class Material:
    """Material."""

    def __init__(self, name):
        """Initializer."""
        self.name = name
        self.container = abjad.Container()
        self.lyrics = None
        self.container.name = name
        self.fn_list: list = None or []
        # self.rhythm: TimespanRhythmBox = None
        self.box_list: list[Box] = None or []

    def __call__(self) -> abjad.Container:
        """It returns ``self.container``."""
        return self.container

    def leaves(self):
        return abjad.select.leaves(self.container)

    def append_box(self, box: Box):
        """Append Box to box_list."""
        self.box_list.append(box)

    def append_fn(self, segment_fn_list: list):
        self.fn_list = segment_fn_list

    def append(self, argument):
        """self.container.append(argument)"""
        self.container.append(argument)

    def write(self, lilypond_string, name: str):
        """It creates container from lilypond string and append to a
        ``muda.Material()`` instance."""
        self.container.append(abjad.Container(lilypond_string, name=name))

    def chords(self):
        """Select chords in self.container"""
        return abjad.select.chords(self.container)

    def logical_ties(self, pitched=False):
        """Select logical ties in self.container"""
        return abjad.select.logical_ties(self.container, pitched=pitched)

    def leaves(self, pitched=False):
        """Select leaves in self.container"""
        return abjad.select.leaves(self.container, pitched=pitched)

    def leaf(self, argument=None, n=0, pitched=False):
        """Select leaf in self.container"""
        if argument is None:
            argument = self.container
        return abjad.select.leaf(self.container, n, pitched=pitched)

    def alternating_materials(self, annotated_durations: list, makers: dict):
        """Create alternating materials according to a list of named durations."""
        # print(annotated_durations)
        assert annotated_durations
        assert isinstance(
            annotated_durations[0], list
        ), "Each duration set must be a list."

        material_names = [dur[0].annotation for dur in annotated_durations]
        material_names = list(dict.fromkeys(material_names))
        for dur in annotated_durations:
            # print(dur)
            for maker, value in makers.items():
                # print(maker, value)
                if maker == dur[0].annotation:
                    if isinstance(value, str):
                        parser = abjad.parser.LilyPondParser()
                        contents = parser(makers[maker])
                        container = abjad.Container(
                            name=maker, identifier="% " + maker)
                        internal = abjad.Container(makers[maker])
                        cont_dur = internal._get_duration()
                        container.append(contents)
                        self.container.append(container)
                        difference = sum(dur) - cont_dur
                        # keep adding the same until it reaches the duration
                        while difference >= cont_dur:
                            copy = abjad.mutate.copy(contents)
                            new_container = abjad.Container(
                                name=maker, identifier="% " + maker
                            )
                            new_container.append(copy)
                            self.container.append(new_container)
                            difference = difference - cont_dur
                    else:
                        selection = makers[maker](dur)
                        appendice = abjad.Container(
                            selection, name=maker, identifier="% " + maker
                        )

                        for item in appendice:
                            if isinstance(item, abjad.Tuplet):
                                item.name = "_"
                                item.identifier = "_"
                        self.container.append(appendice)

        # add indices to materials and write comments
        # in lilypond code to identify materials
        for i, name in enumerate(material_names):
            selectable = self.select_material(self.container, name)
            containers = abjad.select.components(selectable, abjad.Container)
            j = 0
            for container in containers:
                if container.name and container.identifier:
                    if name in container.name:
                        container.name = container.name + "_" + str(j)
                        container.identifier = container.identifier + \
                            "_" + str(j)
                        if isinstance(container, abjad.Tuplet):
                            string = container.name
                            comment1 = abjad.LilyPondComment(string)
                            abjad.attach(comment1, container[0])
                            comment2 = abjad.LilyPondComment(
                                string, format_slot="after"
                            )
                            abjad.attach(comment2, container[-1])
                        j += 1

    def write_pitches(self, pitches: list, grace=None):
        """Write pitches to notes in the Material instance."""
        logical_ties = abjad.select.logical_ties(
            self.container, pitched=True, grace=grace
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
            selection = abjad.select.logical_ties(selectable, pitched=True)

            for i, logical_tie in enumerate(selection):
                index = i % len(pitches)
                pitch = pitches[index]
                if isinstance(pitch, list):
                    for chord in logical_tie:
                        chord.written_pitches = pitch
                else:
                    for note in logical_tie:
                        note.written_pitch = pitch
                    # print(material_name, note.written_pitch)

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
            conversion = abjad.selection.leaves(self.container, pitched=True)
            for note in conversion:
                chord = abjad.Chord("c'", note.written_duration)
                abjad.mutate.replace(note, chord)

        # select by duration:
        abjad_durations = [sum(dur) for dur in annotated_durations]

        def selector(_):
            return abjad.select.leaves(_).partition_by_durations(
                abjad_durations,
                cyclic=False,
                fill=abjad.Exact,
                in_seconds=False,
                overhang=True,
            )

        selections = selector(self.container)

        for key in annotated_pitches:
            pitches = cycle(annotated_pitches[key])
            for selection, duration in zip(selections, annotated_durations):
                logical_ties = abjad.select.logical_ties(
                    selection, pitched=True)
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
            conversion = abjad.select.leaves(self.container, pitched=True)
            for note in conversion:
                chord = abjad.Chord("c'", note.written_duration)
                abjad.mutate.replace(note, chord)

        logical_ties = abjad.select.logical_ties(self.container, pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            index = i % len(pitches)
            pitch = pitches[index]
            if isinstance(pitch, list):
                for note in logical_tie:
                    note.written_pitches = pitch
            else:
                for note in logical_tie:
                    note.written_pitches = [pitch]

    def write_chords_pitches(self, pitches, container=None):
        if container is None:
            container = self.container
        chords_test = False
        for item in pitches:
            if isinstance(item, list):
                chords_test = True

        if chords_test:
            # convert notes to chords
            conversion = abjad.select.logical_ties(container, pitched=True)
            for lt in conversion:
                for note in lt:
                    chord = abjad.Chord("c'", note.written_duration)
                    for indicator in abjad.get.indicators(note):

                        abjad.attach(indicator, chord)
                    abjad.mutate.replace(note, chord)

            # print(abjad.lilypond(container))

        logical_ties = abjad.select.logical_ties(container, pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            index = i % len(pitches)
            pitch = pitches[index]
            if isinstance(pitch, list):
                for note in logical_tie:
                    note.written_pitches = pitch
            else:
                for note in logical_tie:
                    note.written_pitches = [pitch]
            # print(pitch)

    def annotate_material_names(
        self,
        material_name=None,
        path=None,
        select=lambda _: abjad.select.leaves(_),
        submaterials=False,
        piano=False,
    ):
        """Add markups to identify materials in a copy and illustrate it."""
        # general_container = abjad.select.components(
        # self.container, abjad.Container)
        # copied_container = abjad.mutate.copy(self.container)
        copied_container = self.container

        if isinstance(material_name, str):
            material_name = [material_name]

        if material_name is None:
            selectables = [copied_container]
            # selectables = [copied_container]
        else:
            selectables = []
            for mat_name in material_name:
                selectable = self.select_material(
                    copied_container, material_name=mat_name, submaterials=submaterials
                )
                selectables.append(selectable)

        for material in selectables:
            for submaterial in material:
                container = abjad.select.components(
                    submaterial, abjad.Container)
                s = container[0].name
                leaves = abjad.select.leaves(submaterial)
                if len(leaves) == 1:
                    string = r' \markup \with-color "red" {"' + s + r'"}'
                    abjad.attach(
                        abjad.Markup(string),
                        abjad.select.leaf(submaterial, 0),
                        direction=abjad.UP,
                    )
                else:
                    lit = r'''
                    \once \override HorizontalBracketText.color = #(x11-color 'red)
                    \once \override HorizontalBracket.color = #(x11-color 'red)
                    \once \override HorizontalBracketText.text = "%s"''' % s

                    try:
                        abjad.attach(
                            abjad.LilyPondLiteral(lit),
                            abjad.select.leaf(submaterial, 0),
                        )
                        abjad.horizontal_bracket(submaterial)
                    except IndexError:
                        continue
                if select is not None:
                    for i, item in enumerate(select(submaterial)):
                        if isinstance(item, abjad.LogicalTie):
                            item = item[0]
                        str_ = r'\markup \with-color "red" \tiny {\null { \raise #2 {%i}}}' % i
                        abjad.attach(
                            abjad.Markup(str_),  # direction=abjad.Up),
                            item,
                        )

        # for i, name in enumerate(material_name):
        #     selectable = self.select_material(copied_container, name)
        #     # for container in selectable:
        #     # print(name, container.name, container)
        #     containers = abjad.select.components(selectable, abjad.Container)
        #     for container in containers:
        #         if (
        #             (
        #                 not isinstance(
        #                     container,
        #                     abjad.Tuplet or abjad.Voice or abjad.BeforeGraceContainer,
        #                 )
        #             )
        #             and (container.name and container.identifier)
        #             and (name in container.name)
        #         ):
        #             s = container.name
        #             lit = r'\once \override HorizontalBracketText.text = "%s"' % s
        #             abjad.attach(abjad.LilyPondLiteral(lit),
        #                          abjad.select.leaf(container, 0))

        #             abjad.horizontal_bracket(container)
        #             if select is not None:
        #                 for i, l in enumerate(select(container)):
        #                     if isinstance(l, abjad.LogicalTie):
        #                         l = l[0]
        #                     str_ = r"\markup \tiny {\null { \raise #2 {%i}}}" % i
        #                     abjad.attach(
        #                         abjad.Markup(str_),  # direction=abjad.Up),
        #                         l,
        #                     )

        # illustration_score = abjad.Score()
        # illustration_staff = abjad.Staff()
        # illustration_voice = abjad.Voice()
        # illustration_voice.consists_commands.append(
        #     "Horizontal_bracket_engraver")
        # illustration_voice.append(copied_container)
        # illustration_staff.append(illustration_voice)
        # illustration_score.append(illustration_staff)
        # lilypond_file = abjad.LilyPondFile(
        #     items=[
        #         r'\include "/Users/Davi/.pyenv/versions/abjad314/lib/python3.10/site-packages/abjad/scm/abjad.ily"',
        #         r'\include "/Users/Davi/github/muda/muda/stylesheet.ily"',
        #         """#(set-default-paper-size "a4" 'portrait)""",
        #         illustration_score,
        #     ],
        # )
        # import os

        # os.chdir(os.path.dirname(__file__))
        # if path is None:
        #     path = os.path.dirname(__file__)
        # # print(abjad.lilypond(lilypond_file))
        # abjad.persist.as_ly(lilypond_file, path + "/illustration.ly")
        # # abjad.persist.as_pdf(lilypond_file, path + "/illustration.pdf")
        # # print(abjad.lilypond(illustration_score))

        # os.system("lilypond " + path + "/illustration.ly")
        # # os.system("open "+ path + "/illustration.pdf")

    def material_spanner(self, material_name: str or list = None):

        if isinstance(material_name, str):
            material_name = [material_name]

        if material_name is None:
            material_name = ["A", "B", "C", "D", "E"]
        selectables = []
        names = []
        for mat_name in material_name:
            selectable = (
                self.select_material(
                    self.container, material_name=mat_name
                ),
                mat_name
            )
            selectables.append(selectable)
            names.append(mat_name)
        # print(selectables)
        for selectable, name in selectables:
            # try:
            containers = abjad.select.components(
                selectable, abjad.Container)

            # print(containers)
            try:
                name = containers[0].name
            except:
                print(f"Material spanner using this name: {name}")

            try:
                abjad.attach(
                    abjad.LilyPondLiteral(
                        [
                            r'\once \override HorizontalBracketText.text = ' +
                            f'"{name}"',
                            r"\once \override HorizontalBracketText.color = #(x11-color 'red)",
                            r"\once \override HorizontalBracket.color = #(x11-color 'red)",
                            r'\startGroup',

                            # r'\tweak text' + f'"{name}"',
                            # r'\tweak direction #DOWN',
                            # r'\startMeasureSpanner',
                        ],
                    ),
                    abjad.select.leaf(selectable, 0),
                )
                abjad.attach(
                    abjad.LilyPondLiteral(
                        r'\stopGroup',
                        "after"
                    ),
                    abjad.select.leaf(selectable, -1),
                )
            except:
                print(f"Cannot span material {name}")

    def annotate_indices_on_selection(self, select, material_name: str = None):
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
                if isinstance(leaf, abjad.LogicalTie):
                    abjad.attach(
                        abjad.Markup(str_),  # direction=abjad.Up),
                        leaf[0],
                    )
                else:
                    abjad.attach(
                        abjad.Markup(str_),  # direction=abjad.Up),
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

    # , material_name=None):
    def dynamics(self, dynamics: list[tuple()], submaterials=False, exclude_material=None, leak=False):
        # """

        # :param dynamics: dict (key: str, value: abjad.Selection)
        # :param material_name: str
        # """

        # if material_name is None:
        #     selectable = self.container
        # else:
        #     selectable = self.select_material(
        #         self.container, material_name=material_name
        #     )
        exclude_material = exclude_material or []

        def _dyn_for_materials():
            if abjad.Dynamic.is_dynamic_name(dyn):
                if isinstance(selection, abjad.Leaf):
                    abjad.attach(abjad.Dynamic(dyn, leak=leak), selection)
                else:
                    for _ in selection:
                        abjad.attach(abjad.Dynamic(dyn, leak=leak), _)
            else:
                if isinstance(selection[0], list):
                    for sel in selection:
                        abjad.hairpin(dyn, sel)
                else:
                    abjad.hairpin(dyn, selection)

        for arguments in dynamics:
            dyn = arguments[2]
            select = arguments[1]
            material_name = arguments[0]
            if material_name is None:
                selectables = self.container
                selection = select(selectables)
                if abjad.Dynamic.is_dynamic_name(dyn):
                    if isinstance(selection, abjad.Leaf):
                        abjad.attach(abjad.Dynamic(dyn, leak=leak), selection)
                    else:
                        for _ in selection:
                            abjad.attach(abjad.Dynamic(dyn), _)
                elif isinstance(selection, list):
                    if isinstance(selection[0], list):
                        for sel in selection:
                            abjad.hairpin(dyn, sel)
                else:
                    abjad.hairpin(dyn, selection)

            else:
                if not isinstance(material_name, list):
                    material_name = [material_name]
                for i, name in enumerate(material_name):
                    selectables = self.select_material(
                        self.container, name, submaterials=submaterials, exclude_material=exclude_material
                    )
                    # print(selectables)
                    if submaterials is True:
                        for submaterial in selectables:
                            try:
                                selection = select(submaterial)
                                _dyn_for_materials()
                            except IndexError:
                                print("Warning:")
                                print("Selection for dynamics failed")
                                print(self.name, material_name, dyn)
                    else:
                        selection = select(selectables)
                        _dyn_for_materials()

        # for key, value in dynamics.items():
        #     dyn = value[0]
        #     select = value[1]
        #     if key is None:
        #         selectables = self.container
        #     else:
        #         selectables = self.select_materialn(self.container, material_name=key)
        #     selection = select(selectables)
        #     if abjad.Dynamic.is_dynamic_name(dyn):
        #         if isinstance(selection, abjad.Leaf):
        #             abjad.attach(abjad.Dynamic(dyn), selection)
        #         else:
        #             for _ in selection:
        #                 abjad.attach(abjad.Dynamic(dyn), _)
        #     elif isinstance(selection[0], list):
        #         for sel in selection:
        #             abjad.hairpin(dyn, sel)
        #     else:
        #         abjad.hairpin(dyn, selection)

        # for key, select in dynamics.items():
        #     selection = select(selectable)
        #     if abjad.Dynamic.is_dynamic_name(key):
        #         if isinstance(selection, abjad.Leaf):
        #             abjad.attach(abjad.Dynamic(key), selection)
        #         else:
        #             for _ in selection:
        #                 abjad.attach(abjad.Dynamic(key), _)
        #     elif isinstance(selection[0], list):
        #         for sel in selection:
        #             abjad.hairpin(key, sel)
        #     else:
        #         abjad.hairpin(key, selection)

    def write_slurs(self, commands: list[abjad.select]):
        for arguments in commands:
            try:
                direction = arguments[2]
            except:
                direction = None
            select = arguments[1]
            material_name = arguments[0]

            if material_name is None:
                selectables = self.container
            else:
                selectables = self.select_material(
                    self.container, material_name=material_name
                )
            sel = select(selectables)
            # print(sel)
            abjad.attach(abjad.StartSlur(), sel[0], direction=direction)
            abjad.attach(abjad.StopSlur(), sel[-1])

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
            selection1 = abjad.select.components(
                self.container, abjad.Container)
            for container in selection1:
                if container.name is not None and (
                    (isinstance(material_name, list)
                     or material_name in container.name)
                ):
                    selection2 = abjad.select.leaves(
                        container, pitched=pitched)
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
                                abjad.StartSlur(
                                    direction=abjad.Down), selection2[a]
                            )
                            abjad.attach(abjad.StopSlur(), selection2[b])

                    if articulations:
                        for key in articulations:
                            for i in articulations[key]:
                                abjad.attach(abjad.Articulation(
                                    key), selection2[i])
        else:
            selection = abjad.select.leaves(self.container, pitched=pitched)

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
                    abjad.attach(abjad.StartSlur(
                        direction=abjad.Down), selection[a])
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
        exclude_material=None,
        direction=None,
        logical_tie_index=0,
        submaterials=False,
    ):
        """Attach ``argument`` to leaves."""
        #     techniques = {
        #         "pizz_bartok": abjad.LilyPondLiteral(r"\snappizzicato"),
        #     "pizz_sec": abjad.Markup(r'\markup "pizz."'),
        #     "pizz_lv": abjad.Markup(r'\markup "pizz. L.V."'),
        #         "behind_bridge": behind_bridge,
        #         "flatt": {"attach": [abjad.StemTremolo(64), abjad.Markup('\markup "flatt."')]},
        #     "aeol_and_ord": abjad.LilyPondLiteral(r"\aeolAndOrd"),
        #     "key_cl": {"command": abjad.override(leaf).NoteHead.style = "#'cross"},
        #     # "jet_wh":
        # }
        def _attach_argument_conditions(argument, leaf):
            if argument == "flatt":
                abjad.attach(abjad.StemTremolo(64), leaf)
                markup = abjad.Markup(r' \markup {"fr."} ')
                bundle = abjad.bundle(
                    markup,
                    # r"- \tweak halign -3",
                )
                abjad.attach(bundle, leaf, direction=direction)
            elif argument == "behind_bridge":
                literal = abjad.LilyPondLiteral(r"\behindBridgeOn")
                abjad.attach(literal, leaf)
                leaf.note_head.is_parenthesized = True
            elif argument == "key_cl":
                abjad.override(leaf).NoteHead.style = "#'cross"
            elif isinstance(argument, str or list):
                new_argument = abjad.LilyPondLiteral(argument)
                abjad.attach(new_argument, leaf, direction=direction)
            else:
                abjad.attach(argument, leaf, direction=direction)

        def _attach_target_conditions(selection, name="global container"):
            if isinstance(selection, abjad.Leaf):
                _attach_argument_conditions(argument, selection)
            else:
                for leaf in selection:
                    if isinstance(leaf, abjad.LogicalTie):
                        _attach_argument_conditions(
                            argument, leaf[logical_tie_index])
                    elif isinstance(leaf, abjad.Leaf):
                        _attach_argument_conditions(argument, leaf)
                    elif isinstance(leaf, list):
                        for item in leaf:
                            _attach_argument_conditions(argument, item)
                    else:
                        try:
                            _attach_argument_conditions(argument, leaf)
                        except:
                            print("Warning:")
                            print(
                                self.name,
                                "cannot attach",
                                argument,
                                "to",
                                leaf,
                                "in",
                                name,
                            )

                    # print("Attached in:", self.name)
                    # print(argument, "in", name, leaf)

        exclude_material = exclude_material or []

        if isinstance(select, int):
            index = select
            select = [lambda _: abjad.select.leaf(_, index)]

        else:
            try:
                iter(select)
            except:
                select = [select]

        if isinstance(material_name, str):
            material_name = [material_name]

        if material_name is None:
            for sel in select:
                selection = sel(self.container)
                try:
                    iter(selection)
                except:
                    selection = [selection]
                _attach_target_conditions(selection)

        else:
            for name in material_name:
                selectables = self.select_material(
                    self.container, name, submaterials, exclude_material
                )
                for sel in select:
                    if submaterials is True:
                        for submaterial in selectables:
                            try:
                                selection = sel(submaterial)
                            except:
                                print("Warning:")
                                print(
                                    self.name,
                                    "selection failed trying to attach",
                                    argument,
                                    "in",
                                    material_name,
                                    submaterial,
                                )
                                continue
                            _attach_target_conditions(selection, name)
                    else:
                        try:
                            selection = sel(selectables)
                        except:
                            print("Warning:")
                            print(
                                self.name,
                                "selection failed trying to attach",
                                argument,
                                material_name,
                                selectables,
                            )
                            continue
                        _attach_target_conditions(selection, name)

                # containers = abjad.select.components(selectable, abjad.Container)
                # print(containers)
                # for container in containers:
                #     if (
                #         (not isinstance(container, abjad.Tuplet or abjad.Voice))
                #         and (container.name and container.identifier)
                #         and (name in container.name)
                #     ):
                # print("each container")
                # print("attach container:", container)
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
        selection = abjad.select.components(self.container[:], abjad.Container)
        for container in selection:
            if container.name is not None and material_name in container.name:
                items = abjad.select(container).items
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

    def fit_in_duration(self, duration: abjad.Duration, final=False):
        shards = abjad.mutate.split(self.container, [duration])
        n = 0
        if final is True:
            n = -1
        copy = abjad.mutate.copy(shards[n])
        del self.container[:]
        self.container.append(copy[0])

    # def fit_in_duration(self, duration: abjad.Duration):
    #     result = abjad.select.partition_by_durations(
    #         self.container,
    #         [duration],
    #         cyclic=False,
    #         fill=abjad.EXACT,
    #         in_seconds=False,
    #         overhang=False,
    #     )
    #     L = []
    #     for item in result:
    #         copy = abjad.mutate.copy(item)
    #         L.append(copy)
    #     del self.container[:]
    #     self.container.append(L[0][0])

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

        # for i, name in enumerate(material_name):
        # selectable = self.select_material(self.container, name)
        containers = abjad.select.components(selectables, abjad.Container)
        # print(containers)
        for container in containers:
            # if (
            #     (not isinstance(container, abjad.Tuplet or abjad.Voice))
            #     and (container.name and container.identifier)
            #     and (material_name in container.name)
            # ):
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
        #     selection = select(self.select_material(self.container, material_name))2

    def print(self):
        """Print ``muda.Material.container`` lilypond code."""
        print(abjad.lilypond(self.container))

    def show(self):
        """Illustrate ``muda.Material.container``."""
        abjad.show(self.container)

    def auto_change(
        self,
        staves_names: list,
        pitch_ranges: list = None,
        material_name=None,
        submaterials=False,
    ):
        if pitch_ranges is None:
            pitch_ranges = [
                abjad.PitchRange("[C4, +inf]"),
                abjad.PitchRange("[-inf, B3]"),
            ]
        staff1 = staves_names[0]
        range1 = pitch_ranges[0]
        staff2 = staves_names[1]
        range2 = pitch_ranges[1]
        if material_name is None:
            selectable = self.container
        else:
            selectable = self.select_material(
                self.container, material_name=material_name, submaterials=submaterials
            )

        selection = abjad.select.notes(selectable)  # pitched=True, grace=True)

        for leaf in selection:
            if isinstance(leaf, abjad.Note):
                if leaf.written_pitch in range1:
                    change_to_staff = staff1
                else:
                    change_to_staff = staff2
            elif isinstance(leaf, abjad.Chord):
                chord_notes = leaf.note_heads
                for note in chord_notes:
                    if note.written_pitch in range1:
                        change_to_staff = staff1
                    else:
                        change_to_staff = staff2
            literal = abjad.LilyPondLiteral(
                r'\change Staff = "' + change_to_staff + '"', "absolute_before"
            )
            abjad.attach(literal, leaf)

    def change_staffs(self, staves_names_and_leaves: dict, material_name=None, show_staff_switch=True, submaterials=True, self_staff_name="Staff", selectables=None, return_after=True):
        self_staff_name = self.name.split("_")[0]+"_Staff"
        if material_name is None and selectables is None:
            selectables = self.container

        elif selectables is None:
            selectables = self.select_material(
                self.container, material_name=material_name, submaterials=submaterials
            )

        if show_staff_switch is True:
            show_staff_switch = r'''
            \override VoiceFollower.style = #'dashed-line
            \override VoiceFollower.breakable = ##t
            \override VoiceFollower.after-line-breaking = ##t
            #'((right (attach-dir . 0) (padding . 8)) (left (attach-dir . 0) (padding . 11)))
            \override VoiceFollower.bound-details =
            \override VoiceFollower.bound-details.right.arrow = ##t
            \showStaffSwitch '''
            after_staff_switch = r'''
            \revert VoiceFollower.style
            \revert VoiceFollower.arrow
            \revert VoiceFollower.bound-details

            \hideStaffSwitch '''
        else:
            show_staff_switch = r''
            after_staff_switch = r''

        for staff_name, select in staves_names_and_leaves.items():
            selection = select(selectables)
            literal = abjad.LilyPondLiteral(
                [
                    show_staff_switch,
                    r'\change Staff = "' + staff_name + '"'
                ],
                "absolute_before"
            )
            after = abjad.LilyPondLiteral(
                [
                    after_staff_switch,
                    r'\change Staff = "' + self_staff_name + '"'
                ],
                "after"
            )
            # print(literal)
            if submaterials is True:
                for submaterial in selectables:
                    try:
                        selection = select(submaterial)
                        abjad.attach(literal, selection)
                        abjad.attach(after, selection)
                    except IndexError:
                        print("Warning:")
                        print("Selection for staff change failed")
                        print(self.name, material_name, staff_name, select)
            else:
                selection = select(selectables)
                abjad.attach(literal, selection)
                if return_after is True:
                    abjad.attach(after, selection)

            # if isinstance(selection, abjad.Leaf):
            #     abjad.attach(literal, selection)
            # else:
            #     for _ in selection:
            #         abjad.attach(literal, _)

    def transpose_instrument(self, abjad_instrument: abjad.Instrument):
        leaves = abjad.select.leaves(self.container)
        for leaf in leaves:
            if not abjad.get.indicator(leaf, abjad.Instrument):
                abjad.attach(abjad_instrument, leaf)
        abjad.iterpitches.transpose_from_sounding_pitch(self.container)

    def guitar_bitones(
        self,
        select: list,
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

                        string = abjad.LilyPondLiteral(
                            f"\{i}", format_slot="after")
                        abjad.attach(string, chord)

                    abjad.mutate.replace(leaf, chord)

    @ staticmethod
    def select_material(
        container: abjad.Container,
        material_name: str,
        submaterials: bool = False,
        exclude_material: list[str] = None,
    ):
        """Select container by name."""
        exclude_material = exclude_material or []

        def _select(container, material_name):
            selection = abjad.select.components(container, abjad.Container)
            indices = [
                i
                for i, container in enumerate(selection)
                if (
                    (
                        isinstance(
                            container,
                            abjad.Tuplet or abjad.Voice or abjad.BeforeGraceContainer,
                        )
                    )
                    or (container.name is None)
                    or (not container.name.startswith(material_name))
                    or (container.name in exclude_material)
                )
            ]
            selection = abjad.select.exclude(selection, indices)
            return selection

        selection = _select(container, material_name)
        containers = abjad.select.components(selection, abjad.Container)
        names = [_.name for _ in containers]
        new_selection = []
        if submaterials is True:
            for i in range(len(selection)):
                string = material_name + "_" + str(i)
                if string in names:
                    result = _select(selection, string)
                    new_selection.append(result)
            selection = new_selection
        return selection

    def select(
            self, material_name: str, container: abjad.Container = None, submaterials=False, exclude_material=None
    ):
        """Select container by name."""
        if container is None:
            container = self.container

        exclude_material = exclude_material or []
        selection = abjad.select.components(container, abjad.Container)
        indices = [
            i
            for i, container in enumerate(selection)
            if (
                (
                    isinstance(
                        container,
                        abjad.Tuplet or abjad.Voice or abjad.BeforeGraceContainer,
                    )
                )
                or (container.name == exclude_material)
                or (container.name is None)
                or (material_name not in container.name)
            )
        ]

        selection = abjad.select.exclude(selection, indices)
        containers = abjad.select.components(selection, abjad.Container)
        names = [_.name for _ in containers]
        new_selection = []
        if submaterials is True:
            for i in range(len(selection)):
                string = material_name + "_" + str(i)
                if string in names:
                    result = self.select(string)
                    new_selection.append(result)
            selection = new_selection
        # print("NEW SELECTION")
        # for element in selection:
        # print(m or aterial_name, element.name)
        # print(selection)
        return selection

    def automatic_clefs(self, select: list = None, material_name: str = None):
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
            abjad.PitchRange("[C4, F#6]"),
            abjad.PitchRange("[A1, B3]"),
            abjad.PitchRange("[-inf, G#1]"),
        ]
        if select is None:

            def select(_):
                return abjad.select.logical_ties(_, pitched=True)

        if material_name is None:
            selection = select(self.container)
        else:
            selection = select(self.select_material(
                self.container, material_name))
        for element, element2, element3 in zip(
            selection[0::3], selection[1:][0::3], selection[2:][0::3]
        ):
            if isinstance(element[0], abjad.Note):
                pitch1 = element[0].written_pitch
            elif isinstance(element[0], abjad.Chord):
                pitch1 = element[0].written_pitches[0]
            if isinstance(element2[0], abjad.Note):
                pitch2 = element2[0].written_pitch
            elif isinstance(element2[0], abjad.Chord):
                pitch2 = element2[0].written_pitches[0]
            if isinstance(element3[0], abjad.Note):
                pitch3 = element3[0].written_pitch
            elif isinstance(element3[0], abjad.Chord):
                pitch3 = element3[0].written_pitches[0]

            # if (pitch3 - pitch2) >= 10 and (pitch2 - pitch1) >= 10:
            for clef, range_ in zip(clefs, ranges):
                if pitch1 in range_ and pitch2 in range_ and pitch3 in range_:
                    abjad.attach(clef, element[0])
                if pitch1 in range_ and pitch2 in range_:
                    abjad.attach(clef, element[0])
                if pitch2 in range_ and pitch3 in range_:
                    abjad.attach(clef, element2[0])

    def make_skips(self, argument):
        r"""Write skips and time signatures to Context."""
        site = "muda.Material.make_skips()"
        tag = abjad.Tag(site)
        # print(tag)
        # print(argument)

        def _append_skips():
            for time_sig in time_signatures_abjad:
                skip = abjad.Skip(1, multiplier=time_sig.pair)
                # print(time_sig, skip)
                self.container.append(skip)

        if isinstance(argument, list):
            if isinstance(argument[0], abjad.TimeSignature):
                time_signatures_abjad = argument
            if isinstance(argument[0], tuple):
                time_signatures_abjad = [
                    abjad.TimeSignature(_) for _ in argument]
            _append_skips()
        else:
            time_signatures_abjad = [argument]
            _append_skips()

        # if isinstance(argument, list or abjad.TimeSignature):
        #     time_signatures_abjad = []
        #     if isinstance(argument[0], abjad.TimeSignature):
        #         # print("argument is time s")
        #         time_signatures_abjad = argument
        #     else:
        #         in_time_signatures = argument
        #         time_signatures_abjad = [
        #             abjad.TimeSignature(_) for _ in in_time_signatures
        #         ]
        #     print(time_signatures_abjad)
        #     for time_sig in time_signatures_abjad:
        #         skip = abjad.Skip(1, multiplier=time_sig.pair)
        #         print(time_sig, skip)
        #         self.container.append(skip)
        # else:
        #     print("what !!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #     self.container.extend(argument)

    def write_time_signatures(self, time_signatures):
        r"""Write time signatures."""
        site = "muda.Material.write_time_signatures()"
        tag = abjad.Tag(site)
        # print(tag)
        # select skips to attach TIME SIGNATURES
        if isinstance(time_signatures[0], abjad.TimeSignature):
            in_time_signatures = [_.pair for _ in time_signatures]
        else:
            in_time_signatures = time_signatures
        shards = abjad.mutate.split(self.container[:], in_time_signatures)
        result = abjad.select.leaves(self.container)

        result = abjad.select.partition_by_durations(
            result,
            in_time_signatures,
            cyclic=False,
            fill=abjad.EXACT,
            in_seconds=False,
            overhang=True,
        )
        for (i, time_sig), selection in zip(enumerate(in_time_signatures), result):
            j = i
            if i != 0:
                j = i - 1
                if in_time_signatures[j] == time_sig:
                    pass
                else:
                    abjad.attach(
                        abjad.TimeSignature(time_sig, ),
                        abjad.select.leaf(selection, 0),
                        # site="absolute_before",
                        tag=tag,
                    )
            else:
                abjad.attach(
                    abjad.TimeSignature(time_sig),
                    abjad.select.leaf(selection, 0),
                    tag=tag,
                )

        # for time_sig, selection in zip(in_time_signatures, result):
        #     abjad.attach(
        #         abjad.TimeSignature(time_sig),
        #         abjad.select.leaf(selection, 0),
        #         tag=tag,
        #     )
        # print(abjad.select.leaf(selection, 0))
        # for i, item in enumerate(in_time_signatures):
        # a = in_time_signatures.index(item)
        # abjad.attach(
        #     time_signatures_abjad[a],
        #     self.container[i],
        #     tag=tag)

    def rewrite_meter(
        self,
        time_signatures,
        boundary_depth=0,
        rewrite_tuplets=True,
        maximum_dot_count=1,
    ):
        """Rewrite meter according to ``abjad.TimeSignature`` or ``tuple`` list."""
        if isinstance(time_signatures[0], abjad.TimeSignature):
            durations = [_.duration for _ in time_signatures]
        else:
            time_signatures = [abjad.TimeSignature(_) for _ in time_signatures]
            durations = time_signatures
        if self.container:
            shards = abjad.mutate.split(self.container[:], durations)
            for shard, time_signature in zip(shards, time_signatures):
                abjad.Meter.rewrite_meter(
                    shard,
                    time_signature,
                    boundary_depth=boundary_depth,
                    rewrite_tuplets=rewrite_tuplets,
                    maximum_dot_count=maximum_dot_count,
                )

    def tuplet_number_tweak(container):
        selection = abjad.select.tuplets(container)
        for tuplet in selection:
            d = tuplet[0].written_duration
            d = d.lilypond_duration_string
            tweak = f'#(tuplet-number::append-note-wrapper tuplet-number::calc-fraction-text "{d}")'
            abjad.override(tuplet).TupletNumber.text = tweak

    def format_tuplets(self):
        selection = abjad.select.tuplets(self.container)
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

            abjad.override(tuplet).PianoStaff.TupletNumber.text = tweak


def segment_print(self):
    elapsed_time = round(time.time() - self.startTime, 2)
    print(
        "\033[95m",
        "Building segment",
        self.name,
        "took",
        elapsed_time,
        "seconds\033[0;0m",
    )


class Segment:
    """Opperates modules over materials."""

    def __init__(
        self,
        material_list: list[Material],
        modules: list,
        score: _score.Score = None,
        timespans: dict = None,
        # lyrics_list: list[Lyrics] = None,
        name=None,
    ):
        """Inicia associando as caixas aos respectivos materiais"""
        self.name = name
        self.material_list = material_list
        self.material_dict = self.make_material_dict(self.material_list)
        self.modules = modules
        self.timespans = timespans
        self.score = score()
        self.startTime = time.time()

        self.parts_paths = {}

    def __call__(self):
        """Call modules functions and write materials on score"""
        self.call_modules_functions(
            modules=self.modules,
            material_dict=self.material_dict,
            timespans=self.timespans,
        )
        for material in self.material_list:
            self.score.write_materials([material])

        self.score.attach_clefs()

        # if self.lyrics_list:
        #     for lyrics in self.lyrics_list:
        #         self.score.write_lyrics([lyrics])

        segment_print()

        return self.score

    def call_by_material(self, material_names: list, make_part=False, part_template=None):

        new_material_dict = {}
        if make_part:
            self.score = part_template()

        for name in material_names:
            self.material_dict[name].container = abjad.Container(name=name)
            new_material_dict[name] = self.material_dict[name]

        self.call_modules_functions(
            modules=self.modules,
            material_dict=new_material_dict,
            timespans=self.timespans,
            make_part=make_part
        )
        if make_part:
            for material_name in material_names:
                self.score.write_materials(
                    [new_material_dict[material_name]])
            self.score.attach_clefs()

        else:
            for material in self.material_list:
                self.score.write_materials([material])

            self.score.attach_clefs()

        elapsed_time = round(time.time() - self.startTime, 2)
        print(
            "\033[95m",
            self.name,
            "Illustrating these materials",
            "took",
            elapsed_time,
            "seconds\033[0;0m",
        )

    def make_part(self, staff_names: list, part_templates: list, parts_dir: str):
        for name in staff_names:
            self.parts_paths[name] = []

        for name, template in zip(staff_names, part_templates):
            new_parts_material_dict = {}
            score = template()
            voices = abjad.select.components(score.score, abjad.Context)
            voices = [
                _ for _ in voices if "Score" not in _.name and "Staff" not in _.name]
            # voices.append(copy(score.score["Global_Context"]))
            for voice in voices:
                new_parts_material_dict[voice.name] = self.parts_material_dict[voice.name]
                print(
                    abjad.lilypond(
                        self.parts_material_dict[voice.name].container)
                )

            self.call_modules_functions(
                modules=self.modules,
                material_dict=new_parts_material_dict,
                timespans=self.timespans,
            )
            for voice in voices:
                score.write_materials([new_parts_material_dict[voice.name]])
                print(voice.name)
            score.attach_clefs()
            path = f"{parts_dir}{self.name}_{name}.ily"
            print(path)

            score.save_ly(path)
            elapsed_time = round(time.time() - self.startTime, 2)
            self.parts_paths[name].append(path)

            print(
                "\033[95m",
                "Making parts",
                self.name,
                "took",
                elapsed_time,
                "seconds\033[0;0m",
            )
            # print(abjad.lilypond(score.score))
            # self.score.save_parts_ly

    # def write_material_on_score

    # def process_material(self, name: str):
    #     material = [_ for _ in self.material_list if _.name == name]
    #     # self.process_material_boxes(self, material)
    #     self.process_material_functions(self, material)

    @ staticmethod
    def make_material_dict(material_list: list, make_part=False):
        material_dict = {}
        for material in material_list:
            material_dict[material.name] = material
        return material_dict

    @ staticmethod
    def call_modules_functions(
            modules: list, material_dict: dict, timespans=None, make_part=False, parts_material_dict=None
    ):
        print(
            "\033[1;94m", __name__, "muda.material.Segment.call_modules_functions()", "\033[0;0m"
        )

        for module in modules:
            # assert
            functions = [f for _, f in module.__dict__.items() if callable(f)]
            functions = [f for f in functions if hasattr(f, "apply_to")]
            if make_part:
                functions = [
                    f for f in functions if not hasattr(f, "score_only")]
            else:
                functions = [
                    f for f in functions if not hasattr(f, "part_only")]
            for fn in functions:
                assert isinstance(fn.apply_to, list)
                for name in fn.apply_to:
                    if name in material_dict.keys():
                        string = module.__name__ + ": " + fn.__name__ + " on " + name
                        print("\033[94m", string.ljust(80, "-"), "\033[0;0m")
                        ts_test = "timespans" in inspect.signature(
                            fn).parameters.keys()
                        time_sig_test = (
                            "time_signatures" in inspect.signature(
                                fn).parameters.keys()
                        )
                        if ts_test and time_sig_test and timespans is not None:
                            fn(
                                material_dict[name],
                                timespans=timespans[name],
                                time_signatures=timespans["Time_Signatures"],
                            )
                        elif (
                            "timespans" in inspect.signature(
                                fn).parameters.keys()
                            and timespans is not None
                        ):
                            fn(material_dict[name], timespans=timespans[name])
                        elif (
                            "time_signatures" in inspect.signature(
                                fn).parameters.keys()
                            and time_sig_test is not None
                        ):
                            fn(
                                material_dict[name],
                                time_signatures=timespans["Time_Signatures"],
                            )

                        else:
                            fn(material_dict[name])

    # @ staticmethod
    # def process_material_functions(self, material: Material):
    #     for function in material.fn_list:
    #         if hasattr(function, 'needs_timespan'):
    #             print("it has needs ts")
    #             ts = self.timespans()
    #             function(material, timespans=[material.name])
    #         else:
    #             function(material)

    # @ staticmethod
    # def process_material_boxes(self, material: Material):
    #     for box in material.box_list:
    #         if isinstance(box, muda.TimespanRhythmBox) and self.timespans is not None:
    #             self.timespans = self.timespans()
    #             for function in box.functions:
    #                 import inspect
    #                 sig = inspect.signature(function)
    #                 print("OOOOOOO")
    #                 print(sig)
    #                 print(sig.parameters)
    #                 function(material, timespans=self.timespans[material.name])
    #         else:
    #             for function in box.functions:
    #                 if hasattr(function, 'needs_timespan'):
    #                     self.timespans = self.timespans()
    #                     function(
    #                         material, timespans=self.timespans[material.name])
    #                 else:
    #                     function(material)
