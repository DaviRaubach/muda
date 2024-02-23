import abjad


def best_clef_for_logical_ties(
    pitched_logical_ties,
    high_clef=abjad.Clef("treble"),
    low_clef=abjad.Clef("bass"),
    lowest_treble_line_pitch=abjad.NamedPitch("E4"),
    highest_bass_line_pitch=abjad.NamedPitch("A3"),
):
    for lt in pitched_logical_ties:
        pitches = abjad.iterate.pitches(lt)
        clef = clef_from_pitches(
            pitches,
            high_clef=high_clef,
            low_clef=low_clef,
            lowest_treble_line_pitch=lowest_treble_line_pitch,
            highest_bass_line_pitch=highest_bass_line_pitch,
        )
        old_clef = abjad.get.indicator(lt[0], abjad.Clef)
        if old_clef:
            abjad.detach(abjad.Clef, lt[0])
        abjad.attach(clef, lt[0])


def clef_from_pitches(
    pitches,
    high_clef=abjad.Clef("treble"),
    low_clef=abjad.Clef("bass"),
    lowest_treble_line_pitch=abjad.NamedPitch("E4"),
    highest_bass_line_pitch=abjad.NamedPitch("A3"),
) -> abjad.Clef:
    """
    Makes clef from ``pitches``.

    ..  container:: example

        >>> notes = abjad.makers.make_notes(list(range(-12, -6)), [(1, 4)])
        >>> staff = abjad.Staff(notes)
        >>> pitches = abjad.iterate.pitches(staff)
        >>> abjad.Clef.from_pitches(pitches)
        Clef(name='bass', hide=False)

        Chooses between treble and bass based on minimal number of ledger lines.

    """
    diatonic_pitch_numbers = [pitch._get_diatonic_pitch_number() for pitch in pitches]
    max_diatonic_pitch_number = max(diatonic_pitch_numbers)
    min_diatonic_pitch_number = min(diatonic_pitch_numbers)
    lowest_treble_line_diatonic_pitch_number = (
        lowest_treble_line_pitch._get_diatonic_pitch_number()
    )
    candidate_steps_below_treble = (
        lowest_treble_line_diatonic_pitch_number - min_diatonic_pitch_number
    )
    highest_bass_line_diatonic_pitch_number = (
        highest_bass_line_pitch._get_diatonic_pitch_number()
    )
    candidate_steps_above_bass = (
        max_diatonic_pitch_number - highest_bass_line_diatonic_pitch_number
    )
    if candidate_steps_above_bass < candidate_steps_below_treble:
        return low_clef
    else:
        return high_clef


def clef_for_logical_ties(
    pitched_logical_ties,
    clef_data={
        "treble^15": ["E6", "F7"],
        "treble^8": ["E5", "F6"],
        "treble": ["E4", "F5"],
        "alto": ["F4", "G5"],
        "tenor": ["D4", "E5"],
        "bass": ["G2", "A3"],
        "bass_8": ["C1", "A2"],
        "bass_15": ["C0", "A1"],
    },
):
    # for lt in pitched_logical_ties:
    pitches = abjad.iterate.pitches(pitched_logical_ties)
    clef = any_clef_from_pitches(pitches, clef_data)
    try:
        note = abjad.select.note(pitched_logical_ties, 0)
    except:
        note = abjad.select.chord(pitched_logical_ties, 0)
    old_clef = abjad.get.indicator(note, abjad.Clef)
    if old_clef:
        abjad.detach(abjad.Clef, note)
    abjad.attach(clef, note)


def any_clef_from_pitches(
    pitches,
    clef_data: dict,
) -> abjad.Clef:
    """
    Makes clef from ``pitches``.

    ..  container:: example

        >>> notes = abjad.makers.make_notes(list(range(-12, -6)), [(1, 4)])
        >>> staff = abjad.Staff(notes)
        >>> pitches = abjad.iterate.pitches(staff)
        >>> abjad.Clef.from_pitches(pitches)
        Clef(name='bass', hide=False)

        Chooses between treble and bass based on minimal number of ledger lines.

    """
    diatonic_pitch_numbers = [pitch._get_diatonic_pitch_number() for pitch in pitches]
    max_diatonic_pitch_number = max(diatonic_pitch_numbers)
    min_diatonic_pitch_number = min(diatonic_pitch_numbers)

    for key, value in clef_data.items():
        new_value = []
        for p in value:
            if p is not None:
                new_value.append(abjad.NamedPitch(p)._get_diatonic_pitch_number())
        clef_data[key] = new_value

    for key, value in clef_data.items():
        value.append(value[0] - min_diatonic_pitch_number)
        value.append(max_diatonic_pitch_number - value[1])

    clefs = {}
    keys = list(clef_data.keys())
    for k1, k2 in zip(keys, keys[1:]):
        candidate_steps_above_low_clef = clef_data[k2][-1]
        candidate_steps_below_high_clef = clef_data[k1][-2]
        if candidate_steps_above_low_clef < candidate_steps_below_high_clef:
            clefs[k2] = candidate_steps_below_high_clef - candidate_steps_above_low_clef
        else:
            clefs[k1] = candidate_steps_above_low_clef - candidate_steps_below_high_clef

    clef_string = min(clefs, key=clefs.get)
    clef = abjad.Clef(clef_string)

    return clef


def ottava(pitched_logical_ties, clef: abjad.Clef):
    for lt in pitched_logical_ties:
        if isinstance(lt[0], abjad.Chord):
            pitch = lt[0].written_pitches[-1]
        elif isinstance(lt[0], abjad.Note):
            pitch = lt[0].written_pitch
        if clef.to_staff_position(pitch).number > 22:
            abjad.attach(
                abjad.Ottava(1),
                lt[0],
            )
            abjad.attach(
                abjad.Ottava(0, site="after"),
                lt[-1],
            )
        elif clef.to_staff_position(pitch).number < -10:
            abjad.attach(
                abjad.Ottava(-1),
                lt[0],
            )
            abjad.attach(
                abjad.Ottava(0, site="after"),
                lt[-1],
            )
