"""
Score.

Classes to build a score.
"""
import abjad
import os
from dataclasses import dataclass
from . import material as material_module


@dataclass
class Instrument:
    r"""
    Create an instrument staff ``abjad.Staff()``.

    >>> import muda
    >>> import abjad
    >>> myinst = muda.Instrument(
    ...             abjad_instrument = abjad.Piano(),
    ...             name = "My Piano",
    ...             staff_count = 2,  # number of staves for the instrument
    ...             voice_count = [2, 1],  # number of voices for each staff
    ... )
    muda.score.Instrument()
    My Piano
        creating My Piano_Staff_1
        creating My Piano_Staff_2
            creating My Piano_Voice_1
            creating My Piano_Voice_2
            creating My Piano_Voice_3
                attaching My Piano_Voice_1 to My Piano_Staff_1
                attaching My Piano_Voice_2 to My Piano_Staff_1
                attaching My Piano_Voice_3 to My Piano_Staff_2
    >>> print(abjad.lilypond(myinst.ready_staff))
    \context PianoStaff = "Piano_StaffGroup"
    <<
        \context Staff = "My Piano_Staff_1"
        <<
            \context Voice = "My Piano_Voice_1"
            {
                \voiceOne
            }
            \context Voice = "My Piano_Voice_2"
            {
            }
        >>
        \context Staff = "My Piano_Staff_2"
        <<
            \context Voice = "My Piano_Voice_3"
            {
            }
        >>
    >>


    """
    abjad_instrument: abjad.Instrument
    name: str
    staff_count: int
    voice_count: list[int]
    clefs: list[str] = None
    lyrics_target: str = None
    markup: str = None
    short_markup: str = None
    rhythmic: bool = False
    tag = abjad.Tag("muda.score.Instrument()")

    def __post_init__(self):
        self.__call__()
        print('\033[1;95m', self.tag.string, '\033[0;0m', self.name)

    # def __init__(
    #     self, abjad_instrument,  name, staff_count, voice_count, lyrics_target=None,  markup=None
    # ):
    #     """Initializer."""
    #     site = "muda.score.Instrument()"
    #     self.tag = abjad.Tag(site)
    #     print(self.tag.string, name)
    #     self.abjad_instrument = abjad_instrument
    #     self.markup = markup
    #     self.name = name
    #     self.staff_count = staff_count
    #     self.voice_count = voice_count
    #     self.lyrics_target = lyrics_target

    #     self.__call__()

    def __call__(self):
        """Return ``self.ready_staff``."""
        if self.markup is None:
            string = type(self.abjad_instrument).__name__

            glue = ' '
            result = ''.join(glue + x if x.isupper()
                             else x for x in string).strip(glue).split(glue)
            self.markup = ' '.join(result)

        if self.short_markup is None:
            string = type(self.abjad_instrument).__name__

            glue = ' '
            result = ''.join(glue + x if x.isupper()
                             else x for x in string).strip(glue).split(glue)
            self.short_markup = ' '.join(result)[:4] + "."

        # abjad_instrument = self.abjad_instrument
        staves = self.append_staves(self)
        self.append_voices(self, staves)
        staff_count = self.staff_count

        if staff_count == 1:
            # abjad.annotate(staves[0], "default_instrument", abjad_instrument)
            self.ready_staff = staves[0]

        else:
            if self.abjad_instrument == abjad.Piano():
                staffgroup = abjad.StaffGroup(
                    lilypond_type="PianoStaff",
                    name="Piano_StaffGroup",
                    tag=self.tag,
                    simultaneous=True,
                )
                for staff in staves:
                    staffgroup.append(staff)

            else:
                staffgroup = abjad.StaffGroup(name=self.name, tag=self.tag)
                for staff in staves:
                    staffgroup.append(staff)

            self.ready_staff = staffgroup

        abjad.setting(self.ready_staff).instrumentName = f'"{self.markup}"'
        abjad.setting(
            self.ready_staff
        ).shortInstrumentName = f'"{self.short_markup}"'

        return self.ready_staff

    @ staticmethod
    def append_staves(self):
        """Method to create instrument staves."""
        name = self.name
        staves = []
        for i in range(self.staff_count):
            if self.staff_count == 1:
                staff_name = name + "_Staff"
            else:
                staff_name = name + "_Staff_" + str(i + 1)
            if self.rhythmic is True:
                staff = abjad.Staff(
                    name=staff_name, lilypond_type='RhythmicStaff', tag=self.tag)
            else:
                staff = abjad.Staff(name=staff_name, tag=self.tag)
            staves.append(staff)

            # print("creating Staff:", staff_name)
        return staves

    @ staticmethod
    def append_voices(self, staves):
        """Method to append voices to instrument staves."""
        voice_count = self.voice_count
        voices = []

        # create voices
        for i in range(sum(voice_count)):
            if voice_count == 1:
                voice_name = self.name + "_Voice"
            else:
                voice_name = self.name + "_Voice_" + str(i + 1)

            if self.lyrics_target is not None:
                if voice_name == self.lyrics_target:
                    ly_type = "NullVoice"
                else:
                    ly_type = "Voice"

            voice = abjad.Voice(
                name=voice_name, lilypond_type=ly_type, tag=self.tag)
            # if self.lyrics_target is not None:
            # if voice_name == self.lyrics_target:
            # literal = abjad.LilyPondLiteral(r"\voiceThree")
            # abjad.attach(literal, voice)
            # abjad.override(voice).NoteHead.stencil = "##f"
            # # abjad.override(voice).NoteHead.no_ledgers = "##t"
            # abjad.override(voice).Stem.stencil = "##f"
            # abjad.override(voice).Beam.stencil = "##f"
            # abjad.override(voice).TupletBracket.stencil = "##f"
            # abjad.override(voice).TupletNumber.stencil = "##f"
            # abjad.override(voice).Rest.stencil = "##f"
            # abjad.override(voice).Tie.stencil = "##f"
            # abjad.override(voice).Flag.stencil = "##f"
            # abjad.override(voice).Dots.stencil = "##f"

            # abjad.annotate(voice[0], "default_instrument",
            # self.abjad_instrument)
            voices.append(voice)
            # print("creating Voice:", voice_name)
            # will be there lyrics for that voice?
            if self.lyrics_target is not None:
                if voice_name == self.lyrics_target:
                    context = abjad.Context(
                        lilypond_type="Lyrics",
                        name=voice_name + "_Lyrics",
                        tag=self.tag,
                    )
                    voices.append(context)
                    # print("creating Context: ", context.name)

        # append voices
        if self.lyrics_target is not None:
            voice_count[0] += 1
        for i, number_of_voices_in_each_staff in enumerate(voice_count):
            if number_of_voices_in_each_staff >= 1:
                staves[i].simultaneous = True
            for n in range(number_of_voices_in_each_staff):
                if i == 0:
                    staves[i].append(voices[n])
                if i >= 1:
                    staves[i].append(voices[n + sum(voice_count[:i])])


class Score:
    r"""Make Score.

    >>> import muda
    >>> import abjad
    >>> my_score = muda.Score()
    muda.Score()
    >>> print(abjad.lilypond(my_score.score))
    \context Score = "Score"
    <<
        \context TimeSignatureContext = "Global_Context"
        {
        }
    >>

    Use stylesheet to add markup names and hide or modify the time signatures (skips) staff.
    """

    def __init__(self, global_context=True, name=None):
        """Todo."""
        site = "muda.Score()"
        tag = abjad.Tag(site)
        self.global_context = global_context
        self.score = abjad.Score(name="Score", tag=tag)
        if self.global_context is True:
            self.score.append(
                abjad.Staff(lilypond_type="TimeSignatureContext",
                            name="Global_Context")
            )
        self.name = name
        print('\033[1;95m', tag.string, '\033[0;0m')
        # print(self.score)

    def __call__(self):
        """Return ``self.score``."""
        return self.score

    def set_instruments(self, instruments=list[Instrument]):
        self.instruments = instruments

    def work_on(instrument_name: str):
        for staff in abjad.select.component(self.score, abjad.Staff):
            pass

    def append(self, context):
        r"""Add ``muda.Instrument.ready_staff`` to the score.

        >>> my_inst = muda.Instrument(
        ...    abjad_instrument = abjad.Piano(),
        ...    name = "Piano",
        ...    staff_count = 2,
        ...    voice_count = [2, 1],)
        muda.score.Instrument() Piano
        creating Staff: Piano_Staff_1
        creating Staff: Piano_Staff_2
        creating Voice: Piano_Voice_1
        creating Voice: Piano_Voice_2
        creating Voice: Piano_Voice_3

        >>> my_score.append([my_inst])
        muda.Score.append() Piano
        >>> print(abjad.lilypond(my_score.score)
        ... )
        \context Score = "Score"
        <<
            \context TimeSignatureContext = "Global_Context"
            {
            }
            \context PianoStaff = "Piano_StaffGroup"
            <<
                \context Staff = "Piano_Staff_1"
                <<
                    \context Voice = "Piano_Voice_1"
                    {
                    }
                    \context Voice = "Piano_Voice_2"
                    {
                    }
                >>
                \context Staff = "Piano_Staff_2"
                <<
                    \context Voice = "Piano_Voice_3"
                    {
                    }
                >>
            >>
        >>
        """
        site = "muda.Score.append()"
        tag = abjad.Tag(site)
        if isinstance(context, list):
            for inst in context:
                # print('\033[1;95m', tag.string, '\033[0;0m', inst.name)
                # print(inst)
                self.score.append(inst.ready_staff)
        else:
            self.score.append(context)

    def make_skips(self, time_signatures, attach=()):
        r"""Write skips and time signatures to "Global_Context".

        >>> my_score.make_skips([(4, 4), (5, 4)])
        muda.Score.make_skips()
        >>> print(abjad.lilypond(my_score.score))
        \context Score = "Score"
        <<
            \context TimeSignatureContext = "Global_Context"
            {
                \time 4/4
                s1 * 1
                \time 5/4
                s1 * 5/4
            }
            \context PianoStaff = "Piano_StaffGroup"
            <<
                \context Staff = "Piano_Staff_1"
                <<
                    \context Voice = "Piano_Voice_1"
                    {
                    }
                    \context Voice = "Piano_Voice_2"
                    {
                    }
                >>
                \context Staff = "Piano_Staff_2"
                <<
                    \context Voice = "Piano_Voice_3"
                    {
                    }
                >>
            >>
        >>
        """
        site = "muda.Score.make_skips()"
        tag = abjad.Tag(site)
        # print(tag.string)

        if isinstance(time_signatures[0], abjad.TimeSignature):
            time_signatures_abjad = time_signatures
            in_time_signatures = [_.pair for _ in time_signatures]
        else:
            in_time_signatures = time_signatures
            time_signatures_abjad = [
                abjad.TimeSignature(_) for _ in in_time_signatures]

        for time_sig in time_signatures_abjad:
            skip = abjad.Skip(1, multiplier=(time_sig.pair))
            self.score["Global_Context"].append(skip)

        # select skips to attach TIME SIGNATURES
        for i, item in enumerate(in_time_signatures):
            a = in_time_signatures.index(item)
            abjad.attach(
                time_signatures_abjad[a], self.score["Global_Context"][i], tag=tag
            )

        def attach(argument, select):
            selection = select(self.score["Global_Context"])
            if isinstance(selection, abjad.Leaf):
                abjad.attach(argument, selection)
            else:
                for skip_ in selection:
                    abjad.attach(argument, skip_)

    # def write_ond_materials(self, materials, fn_dict_list: list[dict{key: fn}]):
    #     """Junta os materiais e executa funções de acordo com um dicinário"""
    #     for material in materials:
    #         for fn_dict in fn_dict_list:
    #             if material.name in fn_dict.keys:
    #                 fn_dict[material.name](material)

    def write_materials(self, materials_list, fn_dict_list: list[dict] = None):
        # TODO
        r"""Write materials to voices. (TODO)

        >>> material_01 = muda.Material("Piano_Voice_1")
        >>> material_01.silence_and_rhythm_maker(
        ...     maker=rmakers.stack(
        ...             rmakers.talea([1, -3, 1], 16),
        ...             rmakers.extract_trivial(),
        ...             rmakers.beam()),
        ...     annotated_divisions=[
        ...             muda.AnnotatedDuration((1, 4)),
        ...             muda.AnnotatedDuration((2, 4), annotation="Rest"),
        ...             muda.AnnotatedDuration((1, 4)),
        ...             muda.AnnotatedDuration((2, 4), annotation="Rest"),
        ...             muda.AnnotatedDuration((3, 4)),]
        ... )
        >>> material_01.write_pitches(["d'"])

        >>> material_02 = muda.Material("Piano_Voice_3")
        >>> material_02.silence_and_rhythm_maker(
        ...     maker=rmakers.stack(
        ...         rmakers.talea([-1, 1, 1, 1], 16),
        ...         rmakers.extract_trivial(),
        ...         rmakers.beam(),
        ...         ),
        ...     annotated_divisions=[
        ...         muda.AnnotatedDuration((3, 8)),
        ...         muda.AnnotatedDuration((3, 8), annotation="Rest"),
        ...         muda.AnnotatedDuration((3, 8)),
        ...         muda.AnnotatedDuration((3, 8), annotation="Rest"),
        ...         muda.AnnotatedDuration((4, 8)),
        ...         muda.AnnotatedDuration((2, 8)),
        ...         ]
        ...     )

        >>> material_list = [material_01, material_02]
        >>> my_score.write_materials(material_list)
        >>> my_score.rewrite_meter(my_divisions)
        rewriting meter: Piano_Voice_1
        rewriting meter: Piano_Voice_3
        <Score-"Score"<<2>>>
        >>> print(abjad.lilypond(my_score.score))
        \context Score = "Score"
        <<
            \context TimeSignatureContext = "Global_Context"
            {
                \time 4/4
                s1 * 1
                \time 5/4
                s1 * 5/4
            }
            \context PianoStaff = "Piano_StaffGroup"
            <<
                \context Staff = "Piano_Staff_1"
                <<
                    \context Voice = "Piano_Voice_1"
                    {
                        d'16
                        r8.
                        r4
                        r4
                        d'16
                        r8.
                        r2
                        d'16
                        r8.
                        d'16
                        d'16
                        r8
                        r16
                        d'16
                        d'16
                        r16
                    }
                    \context Voice = "Piano_Voice_2"
                    {
                    }
                >>
                \context Staff = "Piano_Staff_2"
                <<
                    \context Voice = "Piano_Voice_3"
                    {
                        r16
                        c'16
                        c'16
                        c'16
                        r16
                        c'16
                        r8
                        r4
                        r16
                        c'16
                        c'16
                        c'16
                        r16
                        c'16
                        r4.
                        r16
                        c'16
                        c'16
                        c'16
                        r16
                        c'16
                        c'16
                        c'16
                        r16
                        c'16
                        c'16
                        c'16
                   }
                >>
            >>
        >>


        .. lily::
            :noedge:
            :audio:

            \version "2.20.0"

            \context Score = "Score"
            <<
                \context TimeSignatureContext = "Global_Context"
                {
                    \time 4/4
                    s1 * 1
                    \time 5/4
                    s1 * 5/4
                }
                \context PianoStaff = "Piano_StaffGroup"
                <<
                    \context Staff = "Piano_Staff_1"
                    <<
                        \context Voice = "Piano_Voice_1"
                        {
                            d'16
                            r8.
                            r4
                            r4
                            d'16
                            r8.
                            r2
                            d'16
                            r8.
                            d'16
                            d'16
                            r8
                            r16
                            d'16
                            d'16
                            r16
                        }
                        \context Voice = "Piano_Voice_2"
                        {
                        }
                    >>
                    \context Staff = "Piano_Staff_2"
                    <<
                        \context Voice = "Piano_Voice_3"
                        {
                            r16
                            c'16
                            c'16
                            c'16
                            r16
                            c'16
                            r8
                            r4
                            r16
                            c'16
                            c'16
                            c'16
                            r16
                            c'16
                            r4.
                            r16
                            c'16
                            c'16
                            c'16
                            r16
                            c'16
                            c'16
                            c'16
                            r16
                            c'16
                            c'16
                            c'16
                                                 }
                    >>
                >>
            >>

        """
        if fn_dict_list is not None:
            for material in materials_list:
                for fn_dict in fn_dict_list:
                    if material.name in fn_dict.keys:
                        fn_dict[material.name](material)

        for material in materials_list:
            if not isinstance(material, material_module.Lyrics):
                self.score[material.name].append(material.container)
            else:
                if material.lyrics is not None:
                    align_str = r" \override LyricText.self-alignment-X = #" + material.align
                    lit = abjad.LilyPondLiteral(
                        r'\lyricsto "'
                        + material.target
                        + r'" { \lyricmode {'
                        + align_str
                        + material.lyrics
                        + "}}"
                    )
                    abjad.attach(lit, self.score[material.name])

    def attach_instruments(self):
        for instrument in self.instruments:
            for i in range(sum(instrument.voice_count)-1):
                a = i + 1
                string = instrument.name + "_Voice_" + str(a)
                if self.score[string]:
                    leaf = abjad.select.leaf(
                        self.score[string],
                        0
                    )
                    abjad.attach(
                        instrument.abjad_instrument,
                        abjad.select.leaf(self.score[string], 0)
                    )

    def attach_clefs(self):
        for instrument in self.instruments:
            for i in range(instrument.staff_count):
                a = i + 1
                if instrument.staff_count == 1:
                    string = instrument.name + "_Staff"
                else:
                    string = instrument.name + "_Staff_" + str(a)

                voices = abjad.select.components(
                    self.score[string], abjad.Voice)
                containers = abjad.select.components(
                    voices, abjad.Container)[0]

                if abjad.select.components(self.score[string], abjad.Leaf):
                    # print(self.score[string])
                    leaf = abjad.select.leaf(
                        self.score[string],
                        0
                    )

                    if instrument.clefs is not None:
                        abjad.attach(
                            abjad.Clef(
                                instrument.clefs[i]
                            ),
                            abjad.select.leaf(self.score[string], 0)
                        )
                else:
                    # string = module.__name__ + ': ' + fn.__name__ + ' on ' + name
                    # print('\033[96m', string.ljust(80, '-'), '\033[0;0m')
                    print('\033[1;93m', "muda.Score.attach_clefs(): no clef or leaf", '\033[0;0m',
                          self.score[string].name)
                    # print("attached",
                    #       instrument.clefs[i], self.score[string])

    def rewrite_meter(self, time_signatures):
        """Rewrite meter according to ``abjad.TimeSignature`` or ``tuple`` list.

        >>> my_score.rewrite_meter(my_divisions)
        rewriting meter: Piano_Voice_1
        rewriting meter: Piano_Voice_3
        <Score-"Score"<<2>>>

        """
        if isinstance(time_signatures[0], abjad.TimeSignature):
            durations = [_.duration for _ in time_signatures]
        else:
            time_signatures = [abjad.TimeSignature(_) for _ in time_signatures]
            durations = time_signatures

        # print([abjad.select.components(self.score, abjad.Voice)])
        for voice in abjad.select.components(self.score, abjad.Voice):
            if voice:
                print("rewriting meter:", voice.name)
                shards = abjad.mutate.split(voice[:], durations)
                for shard, time_signature in zip(shards, time_signatures):
                    abjad.Meter.rewrite_meter(
                        shard,
                        time_signature,
                        # boundary_depth=1,
                        # rewrite_tuplets=True,
                        # maximum_dot_count=1,
                    )
        return self.score

    def lilypond(self):
        r"""Print ``self.score`` lilypond code.

        >>> import muda
        >>> my_score = muda.Score()
        muda.Score()
        >>> my_score.lilypond()
        \context Score = "Score"
            <<
                \context TimeSignatureContext = "Global_Context"
                {
                }
            >>
        >>>
        """
        lilypond = abjad.lilypond(self.score)
        print(lilypond)
        return lilypond

    def show(self):
        """Show ``self.score``."""
        return abjad.show(self.score)

    def play(self):
        pass

    def save_ly(self, file_name: str = None, output_dir: str = None):
        """Save score in lilypond file."""
        if file_name is None:
            file_name = f'{output_dir}{self.score.name}.ly'
        lilypond_file = abjad.LilyPondFile(
            items=[self.score],
        )
        abjad.persist.as_ly(lilypond_file, file_name)
        # abjad.persist.as_midi(lilypond_file, file_name)
        print("Current working directory: {0}".format(os.getcwd()))

    def save_pdf(self, file_name: str = None, includes=None, output_dir=None):
        """Compile pdf file."""
        if file_name is None:
            file_name = f'{output_dir}{self.score.name}.pdf'
        items = []
        if includes is not None:
            items.append(includes)
        items.append(self.score)
        lilypond_file = abjad.LilyPondFile(
            items=items,
        )
        abjad.persist.as_pdf(lilypond_file, file_name)
        # abjad.persist.as_midi(lilypond_file, file_name)
        print("Current working directory: {0}".format(os.getcwd()))

    def save_midi(self, file_name: str):
        """Save .midi files."""
        midi_block = abjad.Block("midi")
        score_block = abjad.Block("score", items=[self.score, midi_block])
        lilypond_file = abjad.LilyPondFile(
            items=[score_block],
        )
        # abjad.persist.as_ly(lilypond_file, file_name)
        abjad.persist.as_midi(lilypond_file, file_name)
        print("Current working directory: {0}".format(os.getcwd()))

    def save_parts_ly(self, ly_file_path: str = None, staff_names: list[str] = None):
        """Save lilypond file of parts."""
        if staff_names is None:
            staff_groups = abjad.select.components(
                self.score, abjad.StaffGroup)
            staffs = abjad.select.components(self.score, abjad.Staff)
            # new_staff_list = []
            # for staff in staffs:
            # for staff_group in staff_groups:
            # parentage = abjad.get.parentage(staff)
            # print(staff)
            # print(parentage)
            # if staff_group != parentage.parent:
            # print(staff)
            # new_staff_list.append(staff)

            parts_strings = []  # parts_strings = [_.name for _ in staff_groups]
            for _ in staffs:
                parts_strings.append(_.name)
            for _ in staff_groups:
                parts_strings.append(_.name)
            create_path = True
        else:
            create_path = False

        for staff in parts_strings:
            if create_path is True:
                path = ""
                path = ly_file_path + staff + ".ily"
            print(staff.name)
            if staff != "Global_Context":
                lilypond_file = abjad.LilyPondFile(
                    items=[self.score[staff]],
                )
                abjad.persist.as_ly(lilypond_file, path)

    def pluri_lyrics(
        self,
        names=[
                    ("Fl_Staff", "Fl_Voice_1_Lyrics"),
                    ("Cl_Staff", "Cl_Voice_1_Lyrics"),
                    ("Pno_Staff_1", "Pno_Voice_1_Lyrics"),
                    ("Gtr_Staff", "Gtr_Voice_1_Lyrics"),
                    ("Vn_Staff", "Vn_Voice_1_Lyrics"),
                    ("Vc_Staff", "Vc_Voice_1_Lyrics")
        ]
    ):
        for name in names:
            abjad.attach(
                abjad.LilyPondLiteral(
                    f'\context Lyrics = "{name[1]}"',
                    "absolute_before"
                ),
                self.score[name[0]])


def make_group(instruments: list, group_name: str):
    group = abjad.StaffGroup(name=group_name)
    for instrument in instruments:
        group.append(instrument.ready_staff)
    return group


if __name__ == "__main__":
    inst = Instrument(abjad.Piano(), "Piano", 2, [2, 2])
    score = Score()
    score.append([inst])
