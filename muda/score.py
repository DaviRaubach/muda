"""
Score.

Classes to build a score.
"""
import abjad
import os


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

    def __init__(
        self, abjad_instrument, name, staff_count, voice_count, lyrics_target=None
    ):
        """Initializer."""
        site = "muda.score.Instrument()"
        self.tag = abjad.Tag(site)
        print(str(self.tag), name)
        self.abjad_instrument = abjad_instrument
        self.name = name
        self.staff_count = staff_count
        self.voice_count = voice_count
        self.lyrics_target = lyrics_target
        self.__call__()

    def __call__(self):
        """Return ``self.ready_staff``."""
        abjad_instrument = self.abjad_instrument
        staves = self.append_staves(self)
        self.append_voices(self, staves)
        staff_count = self.staff_count

        if staff_count == 1:
            abjad.annotate(staves[0], "default_instrument", abjad_instrument)
            self.ready_staff = staves[0]
        else:
            if abjad_instrument == abjad.Piano():
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

            abjad.annotate(staffgroup, "default_instrument", abjad_instrument)

            self.ready_staff = staffgroup

        return self.ready_staff

    @staticmethod
    def append_staves(self):
        """Method to create instrument staves."""
        name = self.name
        staves = []
        for i in range(self.staff_count):
            if self.staff_count == 1:
                staff_name = name + "_Staff"
            else:
                staff_name = name + "_Staff_" + str(i + 1)

            staff = abjad.Staff(name=staff_name, tag=self.tag)
            staves.append(staff)

            print("creating Staff: ", staff_name)
        return staves

    @staticmethod
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
            voices.append(abjad.Voice(name=voice_name, tag=self.tag))
            print("creating Voice:", voice_name)
            # will be there lyrics for that voice?
            if self.lyrics_target is not None:
                if voice_name == self.lyrics_target:
                    context = abjad.Context(
                        lilypond_type="Lyrics",
                        name=voice_name + "_Lyrics",
                        tag=self.tag,
                    )
                    voices.append(context)
                    print("creating Context: ", context.name)

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

    def __init__(self):
        """Todo."""
        site = "muda.Score()"
        tag = abjad.Tag(site)
        self.score = abjad.Score(name="Score", tag=tag)
        self.score.append(
            abjad.Staff(lilypond_type="TimeSignatureContext", name="Global_Context")
        )
        print(str(tag))

    def __call__(self):
        """Return ``self.score``."""
        return self.score

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
                print(str(tag), str(inst.name))
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
        print(str(tag))

        if isinstance(time_signatures[0], abjad.TimeSignature):
            time_signatures_abjad = time_signatures
            in_time_signatures = [_.pair for _ in time_signatures]
        else:
            in_time_signatures = time_signatures
            time_signatures_abjad = [abjad.TimeSignature(_) for _ in in_time_signatures]

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

    def write_materials(self, materials_list):
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
        for material in materials_list:
            if material.lyrics is not None:
                lit = abjad.LilyPondLiteral(
                    r'\lyricsto "'
                    + material.target
                    + r'" { \lyricmode {'
                    + material.lyrics
                    + "}}"
                )
                abjad.attach(lit, self.score[material.name])
            else:
                self.score[material.name].extend(material.container)

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

    def save_ly(self, file_name: str):
        lilypond_file = abjad.LilyPondFile(
            items=[self.score],
        )
        abjad.persist.as_ly(lilypond_file, file_name)
        print("Current working directory: {0}".format(os.getcwd()))



def make_group(instruments: list, group_name: str):
    group = abjad.StaffGroup(name=group_name)
    for instrument in instruments:
        group.append(instrument.ready_staff)
    return group


if __name__ == "__main__":
    inst = Instrument(abjad.Piano(), "Piano", 2, [2, 2])
    score = Score()
    score.append([inst])
