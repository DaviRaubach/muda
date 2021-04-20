import abjad
import re


class Instrument():
    r"""
    Creates instrument and returns ``abjad.Staff()`` of the instrument.
    
    >>> import muda
    >>> import abjad
    >>> myinst = muda.Instrument(
    ...             abjad_instrument = abjad.Piano(),
    ...             lilypond_name = "My Piano",
    ...             nstaffs = 2,
    ...             nvoices = [2, 1],)
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

    def __init__(self, abjad_instrument, lilypond_name, nstaffs, nvoices):
        site = "muda.score.Instrument()"
        tag = abjad.Tag(site)
        print(str(tag))
        print(lilypond_name)
        self.abjad_instrument = abjad_instrument
        self.lilypond_name = lilypond_name
        self.nstaffs = nstaffs
        self.nvoices = nvoices
        self.__call__()

    def __call__(self):
        site = "muda.score.Instrument()"
        tag = abjad.Tag(site)
        abjad_instrument = self.abjad_instrument
        lilypond_name = self.lilypond_name
        nstaffs = self.nstaffs
        nvoices = self.nvoices
        staffs = []
        voices = []
        for i in range(nstaffs):
            if nstaffs == 1:
                staffs.append(abjad.Staff(name=lilypond_name + "_Staff", tag=tag))
                print("    creating " + lilypond_name + "_Staff_" + str(i + 1))
            else:
                staffs.append(
                    abjad.Staff(name=lilypond_name + "_Staff_" + str(i + 1), tag=tag)
                )
                print("    creating " + lilypond_name + "_Staff_" + str(i + 1))

        for i in range(sum(nvoices)):
            if nvoices == 1:
                voices.append(abjad.Voice(name=lilypond_name + "_Voice", tag=tag))
                print("        creating " + lilypond_name + "_Voice_" + str(i + 1))
            else:
                voices.append(
                    abjad.Voice(name=lilypond_name + "_Voice_" + str(i + 1), tag=tag)
                )
                print("        creating " + lilypond_name + "_Voice_" + str(i + 1))

        for i, number_of_voices_in_each_staff in enumerate(nvoices):
            if number_of_voices_in_each_staff >=1:
                staffs[i].simultaneous = True
            for n in range(number_of_voices_in_each_staff):
                if i == 0:
                    staffs[i].append(voices[n])
                    print(
                        "            attaching " + voices[n].name + " to " + staffs[i].name
                    )
                if i >= 1:
                    staffs[i].append(voices[n + sum(nvoices[:i])])
                    print(
                        "            attaching "
                        + voices[n + sum(nvoices[:i])].name
                        + " to "
                        + staffs[i].name
                    )
                    if n == 0:
                        abjad.attach(abjad.LilyPondLiteral(r"\voiceOne"), voices[n])
                    if n == 1:
                        abjad.attach(abjad.LilyPondLiteral(r"\voiceTwo"), voices[n])
                    if n == 2:
                        abjad.attach(abjad.LilyPondLiteral(r"\voiceThree"), voices[n])
                    


        if nstaffs == 1:
            # abjad_instrument.markup = abjad.Markup(lilypond_name)
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
                staffgroup = abjad.StaffGroup(name=lilypond_name, tag=tag)
                for staff in staffs:
                    staffgroup.append(staff)

            abjad.annotate(staffgroup, "default_instrument", abjad_instrument)

            self.ready_staff = staffgroup

        # Separate lilypond_name to have a markup for the instrument.
        # separated_name = re.findall('[A-Z][^A-Z]*', lilypond_name)
        #     if len(separated_name) > 1:
        #         separated_name = separated_name[0] + " " + separated_name[1]
        #         instrumentName = abjad.LilyPondLiteral(
        #             r"\set " + lilypond_name + ".instrumentName = \markup{" + separated_name + "}"
        #             )
        #         abjad.attach(instrumentName, ready_staff)
        #     else:
        #         instrumentName = abjad.LilyPondLiteral(
        #             r"\set " + lilypond_name + ".instrumentName = \markup{" + lilypond_name + "}"
        #             )
        #         abjad.attach(instrumentName, ready_staff)

        return self.ready_staff

class Score:
    """
    >>> import muda
    >>> import abjad
    >>> from abjadext import rmakers
    >>> myinst = muda.Instrument(
    ...     abjad_instrument = abjad.Piano(),
    ...     lilypond_name = "Piano",
    ...     nstaffs = 2,
    ...     nvoices = [2, 1],
    ...     piano = True)
    muda.score.Instrument()
    Piano
        creating Piano_Staff_1
        creating Piano_Staff_2
            creating Piano_Voice_1
            creating Piano_Voice_2
            creating Piano_Voice_3
                attaching Piano_Voice_1 to Piano_Staff_1
                attaching Piano_Voice_2 to Piano_Staff_1
                attaching Piano_Voice_3 to Piano_Staff_2
    >>> myscore = muda.Score()
    muda.Score()
    >>> myscore.add_instrument(myinst)
    muda.Score.add_instrument()
    >>> mydivisions = [(4, 4), (5, 4)]
    >>> myscore.make_skips(mydivisions)
    muda.Score.make_skips()
    >>> mymaterial = muda.Material("Piano_Voice_1")
    >>> mymaterial.silence_and_rhythm_maker(
    ...     maker=rmakers.stack(rmakers.note()),
    ...     annotated_divisions=[
    ...         muda.AnnotatedDuration((1, 4)),
    ...         muda.AnnotatedDuration((1, 4), annotation="Rest"),
    ...         muda.AnnotatedDuration((1, 4)),
    ...         muda.AnnotatedDuration((1, 4)),
    ...         muda.AnnotatedDuration((1, 4), annotation="Rest"),
    ...         muda.AnnotatedDuration((1, 4)),
    ...         muda.AnnotatedDuration((1, 4)),
    ...         muda.AnnotatedDuration((1, 4), annotation="Rest"),
    ...         muda.AnnotatedDuration((1, 4)),
    ...         ]
    ...     )
    >>> myscore.write_materials([mymaterial])
    >>> myscore.rewrite_meter(mydivisions)
    rewriting meter: Piano_Voice_1
    <Score-"Score"<<2>>>
    >>> abjad.show(myscore.score)


    Use stylesheet to add markup names and hide or modify the time signatures (skips) staff.
    """
    def __init__(self):
        site = "muda.Score()"
        tag = abjad.Tag(site)
        self.score = abjad.Score(name="Score", tag=tag)
        self.score.append(
            abjad.Staff(lilypond_type="TimeSignatureContext", name="Global_Context")
        )
        print(str(tag))

    def __call__(self):
        return self.score

    def add_instrument(self, instrument):
        """ Adds ``muda.Instrument()`` to the score.   
        >>> myscore.add_instrument(myinst)
        muda.Score.add_instrument()
        """
        site = "muda.Score.add_instrument()"
        tag = abjad.Tag(site)
        print(str(tag))
        if isinstance(instrument, list):
            for inst in instrument:
                print("    " + str(inst.lilypond_name))
                self.score.append(inst.__call__())
        else:
            self.score.append(instrument)

    def make_skips(self, time_signatures, attach=()):
        """Create a "Global_Context" staff with skips and time signatures.

        >>> myscore.make_skips([(4, 4), (5, 4)])
        muda.Score.make_skips()
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

        >>> import muda
        >>> import abjad
        >>> from abjadext import rmakers
        >>>
        >>> myinst = muda.Instrument(
        ...     abjad_instrument = abjad.Piano(),
        ...     lilypond_name = "Piano",
        ...     nstaffs = 2,
        ...     nvoices = [2, 1])
        muda.score.Instrument()
        Piano
            creating Piano_Staff_1
            creating Piano_Staff_2
                creating Piano_Voice_1
                creating Piano_Voice_2
                creating Piano_Voice_3
                    attaching Piano_Voice_1 to Piano_Staff_1
                    attaching Piano_Voice_2 to Piano_Staff_1
                    attaching Piano_Voice_3 to Piano_Staff_2
        >>> myscore = muda.Score()
        muda.Score()
        >>> myscore.add_instrument(myinst)
        muda.Score.add_instrument()
        >>> mydivisions = [(8, 4), (5, 4)]
        >>> myscore.make_skips(mydivisions)
        muda.Score.make_skips()
        >>> 
        >>> mymaterial1 = muda.Material("Piano_Voice_1")
        >>> mymaterial1.silence_and_rhythm_maker(
        ...     maker=rmakers.stack(
        ...         rmakers.talea([1, -3, 1], 16),
        ...         rmakers.extract_trivial(),
        ...         rmakers.beam(),
        ...         ),
        ...     annotated_divisions=[
        ...         muda.AnnotatedDuration((1, 4)),
        ...         muda.AnnotatedDuration((2, 4), annotation="Rest"),
        ...         muda.AnnotatedDuration((2, 4)),
        ...         muda.AnnotatedDuration((2, 4), annotation="Rest"),
        ...         muda.AnnotatedDuration((1, 4)),
        ...         muda.AnnotatedDuration((2, 4), annotation="Rest"),
        ...         muda.AnnotatedDuration((3, 4)),
        ...         ]
        ...     )
        >>> mymaterial1.write_pitches(["d'"])
        >>> 
        >>> mymaterial2 = muda.Material("Piano_Voice_3")
        >>> mymaterial2.silence_and_rhythm_maker(
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
        >>> 
        >>> 
        >>> material_list = [mymaterial1, mymaterial2]
        >>> myscore.write_materials(material_list)
        >>> myscore.rewrite_meter(mydivisions)
        rewriting meter: Piano_Voice_1
        rewriting meter: Piano_Voice_3
        <Score-"Score"<<2>>>
        >>> abjad.show(myscore.score)

        .. lily::
            :noedge:
            :audio:

            \version "2.20.0"

            \context Score = "Score"
            <<
                \context TimeSignatureContext = "Global_Context"
                {
                    \time 8/4
                    s1 * 2
                    \time 5/4
                    s1 * 5/4
                }
                \context PianoStaff = "Piano_StaffGroup"
                <<
                    \context Staff = "Piano_Staff_1"
                    <<
                        \context Voice = "Piano_Voice_1"
                        {
                            \voiceOne
                            d'16
                            r8.
                            r4
                            r4
                            d'16
                            r8.
                            d'16
                            d'16
                            r4.
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
            self.score[material.name].extend(material.container)

    # rewrite meter
    def rewrite_meter(self, time_signatures):
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
                    # time_signature = abjad.get.indicator(leaf, abjad.TimeSignature)
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
        lilypond = abjad.lilypond(self.score)
        return lilypond

    def make_lilypond_file(self, includes=None):
        lilypond_file = abjad.LilyPondFile(items=[self.score], includes=includes,)
        return lilypond_file

    def show(self):
        return abjad.show(self.score)

