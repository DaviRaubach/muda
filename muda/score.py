"""
Score.

These are classes to build a score.
"""
import abjad


class Instrument():
    r"""
    Create an instrument staff ``abjad.Staff()``.

    >>> import muda
    >>> import abjad
    >>> myinst = muda.Instrument(
    ...             abjad_instrument = abjad.Piano(),
    ...             name = "My Piano",
    ...             nstaffs = 2,  # number of staffs for the instrument
    ...             nvoices = [2, 1],  # number of voices for each staff)
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
        self,
        abjad_instrument,
        name,
        nstaffs,
        nvoices,
        lyrics_target=None
    ):
        """Initializer."""
        site = "muda.score.Instrument()"
        tag = abjad.Tag(site)
        print(str(tag), name)
        self.abjad_instrument = abjad_instrument
        self.name = name
        self.nstaffs = nstaffs
        self.nvoices = nvoices
        self.lyrics_target = lyrics_target
        self.__call__()

    def __call__(self):
        """Return ``self.ready_staff``."""
        site = "muda.score.Instrument()"
        tag = abjad.Tag(site)
        abjad_instrument = self.abjad_instrument
        name = self.name
        nstaffs = self.nstaffs
        nvoices = self.nvoices
        staffs = []
        voices = []
        for i in range(nstaffs):
            if nstaffs == 1:
                staffs.append(abjad.Staff(name=name + "_Staff", tag=tag))
                print("creating Staff: " + name + "_Staff_" + str(i + 1))
            else:
                staffs.append(
                    abjad.Staff(name=name + "_Staff_" + str(i + 1), tag=tag)
                )
                print("creating Staff: " + name + "_Staff_" + str(i + 1))

        for i in range(sum(nvoices)):
            if nvoices == 1:
                voices.append(abjad.Voice(name=name + "_Voice", tag=tag))
                print("creating Voice" + name + "_Voice_" + str(i + 1))
                if self.lyrics_target is not None:
                    if (name + "_Voice_" + str(i + 1)) == self.lyrics_target:
                        cont = abjad.Context(
                            lilypond_type='Lyrics',
                            name=(name + "_Voice_" + str(i + 1) + "_Lyrics"),
                            tag=tag)
                        voices.append(cont)
                        print("creating Context: ", cont.name)
            else:
                voices.append(
                    abjad.Voice(name=name + "_Voice_" + str(i + 1), tag=tag)
                )
                print("creating Voice: " + name + "_Voice_" + str(i + 1))
                if self.lyrics_target is not None:
                    if (name + "_Voice_" + str(i + 1)) == self.lyrics_target:
                        cont = abjad.Context(
                            lilypond_type='Lyrics',
                            name=(name + "_Voice_" + str(i + 1) + "_Lyrics"),
                            tag=tag)
                        voices.append(cont)
                        print("creating Context: ", cont.name)
        if self.lyrics_target is not None:
            nvoices[0] += 1
        for i, number_of_voices_in_each_staff in enumerate(nvoices):
            if number_of_voices_in_each_staff >= 1:
                staffs[i].simultaneous = True
            for n in range(number_of_voices_in_each_staff):
                if i == 0:
                    staffs[i].append(voices[n])
                if i >= 1:
                    staffs[i].append(voices[n + sum(nvoices[:i])])

        if nstaffs == 1:
            abjad.annotate(staffs[0], "default_instrument", abjad_instrument)
            self.ready_staff = staffs[0]
        else:
            if abjad_instrument == abjad.Piano():
                staffgroup = abjad.StaffGroup(
                    lilypond_type="PianoStaff",
                    name="Piano_StaffGroup",
                    tag=tag,
                    simultaneous=True,
                )
                for staff in staffs:
                    staffgroup.append(staff)

            else:
                staffgroup = abjad.StaffGroup(name=name, tag=tag)
                for staff in staffs:
                    staffgroup.append(staff)

            abjad.annotate(staffgroup, "default_instrument", abjad_instrument)

            self.ready_staff = staffgroup

        return self.ready_staff


class Score():
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
            abjad.Staff(
                lilypond_type="TimeSignatureContext",
                name="Global_Context")
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
        ...    nstaffs = 2,
        ...    nvoices = [2, 1],)
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
        r"""Create a "Global_Context" staff with skips and time signatures.

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
            time_signatures_abjad = [
                abjad.TimeSignature(_) for _ in in_time_signatures]

        for time_sig in time_signatures_abjad:
            skip = abjad.Skip(1, multiplier=(time_sig.pair))
            self.score["Global_Context"].append(skip)

        # select skips to attach TIME SIGNATURES
        for i, element in enumerate(in_time_signatures):
            # previous_element = time_signatures[i - 1] if i > 0 else None
            current_element = element

            # if current_element != previous_element:
            a = in_time_signatures.index(current_element)
            abjad.attach(
                time_signatures_abjad[a],
                self.score["Global_Context"][i],
                tag=tag)

        selection = abjad.select(self.score["Global_Context"]).leaves()
        # attach
        if attach:
            # print(abjad.lilypond(self.container))
            a, b = attach
            abjad.attach(a, selection[b])

    def write_materials(self, materials_list):
        r"""Write materials to voices.

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
        ...         muda.AnnotatedDuration((3, 8)),
        ...         muda.AnnotatedDuration((3, 8), annotation="Rest"),
        ...         muda.AnnotatedDuration((4, 8)),
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
                        }
                    >>
                >>
            >>

        """
        for material in materials_list:
            if material.lyrics is not None:
                lit = abjad.LilyPondLiteral(
                    r'\lyricsto "' + material.target +
                    r'" { \lyricmode {' + material.lyrics + '}}')
                abjad.attach(
                    lit,
                    self.score[material.name])
            else:
                self.score[material.name].extend(material.container)

    def rewrite_meter(self, time_signatures):
        """Rewrite meter according to ``abjad.TimeSignature`` or ``tuple`` list.

        >>> my_score.rewrite_meter(my_divisions)
        rewriting meter: Piano_Voice_1
        rewriting meter: Piano_Voice_3
        <Score-"Score"<<2>>>

        """
        # global_skips = [_ for _ in abjad.select(score["Global_Context"]).leaves()]
        # sigs = []
        # for skip in global_skips:
        #     for indicator in abjad.get.indicators(skip):
        #         if isinstance(indicator, abjad.TimeSignature):
        #             sigs.append(indicator)
        if isinstance(time_signatures[0], abjad.TimeSignature):
            time_signatures = time_signatures
            durations = [_.duration for _ in time_signatures]
        else:
            time_signatures = [abjad.TimeSignature(_) for _ in time_signatures]
            durations = time_signatures

        for voice in abjad.select(self.score).components(abjad.Voice):
            # voice_dur = abjad.get.duration(voice)
            if voice:
                print("rewriting meter:", voice.name)
                # sig_dur = sum(durations)
                # assert voice_dur == sig_dur, (voice_dur, sig_dur)
                shards = abjad.mutate.split(voice[:], durations)
                for shard, time_signature in zip(shards, time_signatures):
                    # leaf = abjad.get.leaf(shard, 0)
                    # time_signature = abjad.get.indicator(
                    #    leaf, abjad.TimeSignature)
                    # print(time_s)
                    # print(time_signature)
                    abjad.Meter.rewrite_meter(
                        shard[:],
                        time_signature,
                        boundary_depth=1,
                        rewrite_tuplets=False,
                        maximum_dot_count=1,
                    )
        return self.score

# Trash
# for time_signature, shard in zip(time_signatures, shards):
#     abjad.Meter.rewrite_meter(shard, time_signature, boundary_depth=1)

# inventories = [
#     x
#     for x in enumerate(
#         abjad.Meter(time_signature.pair).depthwise_offset_inventory
#     )
# ]
# if time_signature.denominator == 4:
#     abjad.Meter.rewrite_meter(
#         shard,
#         time_signature,
#         boundary_depth=inventories[-1][0],
#         rewrite_tuplets=False,
#     )
# else:
#     abjad.Meter.rewrite_meter(
#         shard,
#         time_signature,
#         boundary_depth=inventories[-2][0],
#         rewrite_tuplets=False,
#     )

# abjad.mutate().split(voice, in_time_signature, cyclic=True)

# time_signatures = []
# for item in in_time_signatures:
#     time_signatures.append(abjad.Meter(item))
# abjad.mutate().split(music, in_time_signature, cyclic=True)
# # selection
# abjad.Meter.rewrite_meter(music[:], time_signatures)
# selector = abjad.select(music).leaves()
# measures = selector.group_by_measure()
# for time, measure in zip(time_signatures, measures):
#     abjad.mutate(measure).rewrite_meter(time)
# return measures

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

    # def make_lilypond_file(self, includes=None):
    #     """Todo."""
    #     lilypond_file = abjad.LilyPondFile(
    #         items=[self.score], includes=includes)
    #     return lilypond_file

    def show(self):
        """Show ``self.score``."""
        return abjad.show(self.score)
