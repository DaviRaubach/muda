import abjad


def see_pitches(pitches):
    G_staff = abjad.Staff()
    F_staff = abjad.Staff()
    staff_group = abjad.StaffGroup([G_staff, F_staff])
    pitch_range = abjad.pitch.PitchRange("[C4, +inf]")
    for pitch in pitches:
        test = pitch in pitch_range
        if test is True:
            note = abjad.Note.from_pitch_and_duration(pitch, (1, 1))
            G_staff.append(note)
            F_staff.append(abjad.Skip((1, 1)))
        if test is False:
            note = abjad.Note.from_pitch_and_duration(pitch, (1, 1))
            G_staff.append(abjad.Skip((1, 1)))
            F_staff.append(note)

    for i, note in enumerate(F_staff):
        abjad.attach(abjad.Markup(i), note)

    clef3 = abjad.Clef("treble^8")
    clef3_range = abjad.pitch.PitchRange("[G6, +inf]")
    clef2 = abjad.Clef("treble")
    clef2_range = abjad.pitch.PitchRange("[E4, E5]")
    clef1 = abjad.Clef("bass")
    clef1_range = abjad.pitch.PitchRange("[A1, G3]")
    clef0 = abjad.Clef("bass_8")
    clef0_range = abjad.pitch.PitchRange("[-inf, C1]")

    selection = abjad.select(G_staff).leaves()
    for i, leaf in enumerate(selection):
        if isinstance(leaf, abjad.Note):
            test3 = leaf in clef3_range
            test2 = leaf in clef2_range
            if test3 is True:
                abjad.attach(clef3, G_staff[i])
            elif test2 is True:
                abjad.attach(clef2, G_staff[i])

    selection2 = abjad.select(F_staff).leaves()
    for i, leaf in enumerate(selection2):
        if isinstance(leaf, abjad.Note):
            test3 = leaf in clef3_range
            test2 = leaf in clef2_range
            test1 = leaf in clef1_range
            test0 = leaf in clef0_range
            if test2 is True:
                abjad.attach(clef2, F_staff[i])
            elif test1 is True:
                abjad.attach(clef1, F_staff[i])
            elif test0 is True:
                abjad.attach(clef0, F_staff[i])

    abjad.show(staff_group)

    return staff_group
