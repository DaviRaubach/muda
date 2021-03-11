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


def MakeScore():
    site = "muda.score.create_score()"
    tag = abjad.Tag(site)
    score = abjad.Score(name="Score", tag=tag)
    score.append(
        abjad.Staff(lilypond_type="TimeSignatureContext", name="Global_Context")
    )
    print(str(tag))
    return score


def AddInstrument(instrument, score):
    site = "muda.score.add_instruments()"
    tag = abjad.Tag(site)
    print(str(tag))
    for inst in instrument:
        print("    " + str(inst.name))
    if isinstance(instrument, list):
        for inst in instrument:
            score.append(inst)
    else:
        score.append(instrument)


def MakeSkips(time_signatures, score):
    site = "muda.score.make_skips()"
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
        score["Global_Context"].append(skip)

    # select skips to attach TIME SIGNATURES
    for i, element in enumerate(in_time_signatures):
        previous_element = time_signatures[i - 1] if i > 0 else None
        current_element = element

        # if current_element != previous_element:
        a = in_time_signatures.index(current_element)
        abjad.attach(time_signatures_abjad[a], score["Global_Context"][i], tag=tag)


def WriteMaterial(voice_name, material):
    score[voice_name].extend(material)
    return material


def MakeLilyPondFile(score, includes):
    lilypond_file = abjad.LilyPondFile.new(score, includes=includes,)
    # midi_block = abjad.Block(name="midi")
    #     layout_block = abjad.Block(name="layout")
    #     lilypond_file["score"].items.append(layout_block)
    #     lilypond_file["score"].items.append(midi_block)
    return lilypond_file
