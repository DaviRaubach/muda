import abjad


def ftom(f, f_a4_in_hz=440):
    return (69 + 12 * np.log2(f / f_a4_in_hz))


def mtof(m, f_a4_in_hz=440):
    a = f_a4_in_hz  # frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((m - 9) / 12))
    # return (69 + 12 * np.log2(f / f_a4_in_hz))


def filter_pitches(pitches, pitch_range):
    if not isinstance(pitch_range, abjad.PitchRange):
        try:
            pitch_range = abjad.PitchRange(pitch_range)
        except:
            print("Cannot build abjad.PitchRange of", pitch_range)
    if not isinstance(pitches[0], abjad.NamedPitch):
        pitches = [abjad.NamedPitch(_) for _ in pitches]

    new_pitches = [p for p in pitches if p in pitch_range]
    return new_pitches


def write_pitches(container, pitches, grace=None):
    """Write pitches to logical ties in selection."""
    logical_ties = abjad.select.logical_ties(
        container, pitched=True, grace=grace)
    for i, logical_tie in enumerate(logical_ties):
        index = i % len(pitches)
        pitch = pitches[index]
        for note in logical_tie:
            note.written_pitch = pitch


def pitches_in_staff(pitches):
    """Show abjad.PitchSegment in two staffs."""
    G_staff = abjad.Staff()
    F_staff = abjad.Staff()
    staff_group = abjad.StaffGroup([G_staff, F_staff])
    pitch_range = abjad.PitchRange("[C4, +inf]")
    if not isinstance(pitches[0], abjad.NamedPitch):
        pitches = [abjad.NamedPitch(_) for _ in pitches]
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
        abjad.attach(abjad.Markup(str(i)), note)

    clef4 = abjad.Clef("treble^15")
    clef4_range = abjad.PitchRange("[G#7, +inf]")
    clef3 = abjad.Clef("treble^8")
    clef3_range = abjad.PitchRange("[G6, G7]")
    clef2 = abjad.Clef("treble")
    clef2_range = abjad.PitchRange("[E4, E5]")
    clef1 = abjad.Clef("bass")
    clef1_range = abjad.PitchRange("[A1, G3]")
    clef0 = abjad.Clef("bass_8")
    clef0_range = abjad.PitchRange("[-inf, C1]")

    selection = abjad.select.leaves(G_staff)
    for i, leaf in enumerate(selection):
        if isinstance(leaf, abjad.Note):
            test4 = leaf.written_pitch in clef4_range
            test3 = leaf.written_pitch in clef3_range
            test2 = leaf.written_pitch in clef2_range
            if test4 is True:
                abjad.attach(clef4, G_staff[i])
            elif test3 is True:
                abjad.attach(clef3, G_staff[i])
            elif test2 is True:
                abjad.attach(clef2, G_staff[i])

    selection2 = abjad.select.leaves(F_staff)
    for i, leaf in enumerate(selection2):
        if isinstance(leaf, abjad.Note):
            test3 = leaf.written_pitch in clef3_range
            test2 = leaf.written_pitch in clef2_range
            test1 = leaf.written_pitch in clef1_range
            test0 = leaf.written_pitch in clef0_range
            if test2 is True:
                abjad.attach(clef2, F_staff[i])
            elif test1 is True:
                abjad.attach(clef1, F_staff[i])
            elif test0 is True:
                abjad.attach(clef0, F_staff[i])

    # abjad.show(staff_group)

    return staff_group


def otoacoustic_derivation(f1, f2, iterations):
    fs = [f1, f2]
    for i in range(iterations):
        inlist = []
        for j in fs[:-1]:
            # print(j)
            inlist.append(abs(fs[-1] - j))
            inlist.append(abs(2*fs[-1] - j))
        fs.extend(inlist)
    return fs

# print(otoacoustic_derivation(800, 600, 2))

# RECURSES TO MODIFY PITCH SEGMENTS
# A C B D C E


def permut_thirds(pitches):
    pitch_list = []
    i = 0
    pitch_list.append(pitches[i])
    while i < len(pitches) - 2:
        i = i + 2
        note = pitches[i]
        pitch_list.append(note)
        i = i - 1
        note = pitches[i]
        pitch_list.append(note)
    return pitch_list


# FREQ_B - FREQ_A
# FREQ_B + FREQ_A
# 2xFREQ_B + FREQ_A
# 2xFREQ_B - FREQ_A
# 2xFREQ_A + FREQ_B
# 2xFREQ_A - FREQ_B
def ring_modulation(pitches, pitch_range=abjad.PitchRange(abjad.Piano().pitch_range), keep_originals=True, chords=False, quarter_tone=True, sort=False):
    if not isinstance(pitches, abjad.PitchSegment):
        pitches = abjad.PitchSegment(pitches)
    pitches_in = [abjad.NumberedPitch(_).hertz for _ in pitches]
    pitches_out = []
    if chords is False:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            if keep_originals is True:
                # ORIGINAL
                pitches_out.append(pitch1)

            # FREQ_B - FREQ_A
            new_pitch_A = pitch2 - pitch1
            pitches_out.append(new_pitch_A)

            # FREQ_B + FREQ_A
            new_pitch_B = pitch1 + pitch2
            pitches_out.append(new_pitch_B)

            # 2xFREQ_B + FREQ_A
            new_pitch_C = 2*pitch2 + pitch1
            pitches_out.append(new_pitch_C)

            # 2xFREQ_B - FREQ_A
            new_pitch_D = 2*pitch2 - pitch1
            pitches_out.append(new_pitch_D)

            # 2xFREQ_A + FREQ_B
            new_pitch_E = 2*pitch1 + pitch2
            pitches_out.append(new_pitch_E)

            # 2xFREQ_A - FREQ_B
            new_pitch_F = 2*pitch1 - pitch2
            pitches_out.append(new_pitch_F)

    if chords is True:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            new_pitch_A = pitch2 - pitch1
            new_pitch_B = pitch1 + pitch2
            new_pitch_A = abjad.NamedPitch.from_hertz(new_pitch_A)
            new_pitch_B = abjad.NamedPitch.from_hertz(new_pitch_B)
            pitch1 = abjad.NamedPitch.from_hertz(pitch1)
            if keep_originals is True:
                pitch_list = [new_pitch_A, pitch1, new_pitch_B]
            else:
                pitch_list = [new_pitch_A, new_pitch_B]
            chord = abjad.Chord(pitch_list, (1, 1))
            pitches_out.append(chord)

    # pitches_out = [round(_, 2) for _ in pitches_out]
    new_pitches_out = []
    for pitch in pitches_out:
        if pitch > 20:
            try:
                new_pitches_out.append(abjad.NumberedPitch.from_hertz(pitch))
            except ValueError:
                print("Cannot transform frequency:",
                      pitch, "to abjad.NumberedPitch")

    # pitches_out=[abjad.NumberedPitch.from_hertz(_) for _ in pitches_out]
    pitches_out = [_.number for _ in new_pitches_out]

    if quarter_tone is False:
        pitches_out = [round(_) for _ in pitches_out]

    # pitches_out = list(pitches_out)
    if sort is True:
        pitches_out.sort()
        pitches_out = abjad.sequence.remove_repeats(pitches_out)

    # print(pitches_out)
    # for i in pitches_out:
        # print(i)
    pitches_out = [abjad.NamedPitch(_) for _ in pitches_out]
    pitches_out = [_ for _ in pitches_out if _ in pitch_range]
    # print(pitches_out)
    return pitches_out


# # ORIGINAL CHORD
# pitches = []
# original_chord = abjad.pitch.PitchSegment(
#     "cqs' f' gs' c'' e'' ftqs'' gqs''"
#     + " gs'' b'' cs''' ctqs''' f''' fs''' ftqs'''  gs'''"
#     )
# pitches = ring_modulation(original_chord, sum=True)
# # pitches.sort()
# print(pitches)
# pitches = [abjad.NamedPitch.from_hertz(_) for _ in pitches]
# electronics_pitches = list.copy(pitches)
# num_pitches = [abjad.NamedPitch(_).number for _ in pitches]
# named_pitches = [abjad.NumberedPitch(_).get_name() for _ in num_pitches]
# num_pitches_rev = num_pitches
# num_pitches_rev.sort(reverse=True)
# num_pitches_rev = permut_thirds(num_pitches_rev)
# pitch_range = abjad.PitchRange("[C2, G7]")
# pitch_list = []
# for i, pitch in enumerate(num_pitches_rev):
#     test = pitch in pitch_range
#     if test is True:
#         pitch_list.append(pitch)

# pitches = abjad.pitch.PitchSegment(pitch_list)
# staff_group = see_pitches(pitches)
# pitches_voice_one = pitches
# # abjad.f(pitches_voice_one)
# pitches_voice_four = pitches[7:]
# # abjad.f(pitches_voice_four)


# # para funcionar com a debaixo
# # conforme primeira versão
# # não pode fazer o retrogrado (sort reverse)
# # nem fazer as terças
# # select notes
# # modifiquei para num_pitches_rev para poder funcionar tanto o de cima quanto o de baixo
# chord_down = []
# notes_down = [8, 9, 11, 12, 13, 14]
# for i, note in enumerate(num_pitches):
#     if i in notes_down:
#         chord_down.append(note)

# chord_up = []
# notes_up = [15, 16, 17, 18, 19, 20]
# for i, note in enumerate(num_pitches):
#     if i in notes_up:
#         chord_up.append(note)

# chord_up_longer = []
# chord_down_longer = []

# for i in range(8):
#     random.seed(i+3)
#     random.shuffle(chord_up)
#     random.seed(i+3)
#     random.shuffle(chord_down)
#     for note_up in chord_up:
#         chord_up_longer.append(note_up)
#     for note_down in chord_down:
#         chord_down_longer.append(note_down)
