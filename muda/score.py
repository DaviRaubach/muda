import abjad
import re


def Instrument(abjad_instrument, lilypond_name, nstaffs, nvoices, piano=None):
    site = "muda.score.instrument()"
    tag = abjad.Tag(site)
    staffs = []
    voices = []

    print(str(tag))
    print(lilypond_name)
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
        for n in range(number_of_voices_in_each_staff):
            if i == 0:
                staffs[i].append(voices[n])
                print(
                    "            attaching " + voices[n].name + " to " + staffs[i].name
                )
            if i >= 1:
                staffs[i].simultaneous = True
                staffs[i].append(voices[n + sum(nvoices[:i])])
                print(
                    "            attaching "
                    + voices[n + sum(nvoices[:i])].name
                    + " to "
                    + staffs[i].name
                )

    if nstaffs == 1:
        # abjad_instrument.markup = abjad.Markup(lilypond_name)
        abjad.annotate(staffs[0], "default_instrument", abjad_instrument)
        ready_staff = staffs[0]

    else:
        if piano is True:
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

        ready_staff = staffgroup

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

    return ready_staff

class Score:
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

    def AddInstrument(self, instrument):
        site = "muda.Score.AddInstrument()"
        tag = abjad.Tag(site)
        print(str(tag))
        if isinstance(instrument, list):
            for inst in instrument:
                print("    " + str(inst.name))
                self.score.append(inst)
        else:
            self.score.append(instrument)


    def MakeSkips(self, time_signatures):
        site = "muda.Score.MakeSkips()"
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
        for i, element in enumerate(in_time_signatures):
            previous_element = time_signatures[i - 1] if i > 0 else None
            current_element = element

            # if current_element != previous_element:
            a = in_time_signatures.index(current_element)
            abjad.attach(time_signatures_abjad[a], self.score["Global_Context"][i], tag=tag)


    def WriteMaterials(self, materials_list):
        """ Write materials to voices """
        for material in materials_list:
            self.score[material.name].extend(material.container)

    # rewrite meter
    def RewriteMeter(self, time_signatures):
        # global_skips = [_ for _ in abjad.select(score["Global_Context"]).leaves()]
        # sigs = []
        # for skip in global_skips:
        #     for indicator in abjad.get.indicators(skip):
        #         if isinstance(indicator, abjad.TimeSignature):
        #             sigs.append(indicator)
        durations = [_.duration for _ in time_signatures]
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

    def MakeLilyPondFile(self, includes=None):
        lilypond_file = abjad.LilyPondFile(items=[self.score], includes=includes,)
        return lilypond_file

