import abjad
import os

# import numpy as np
import roman
from .score import Instrument as _Instrument


def ftom(f, f_a4_in_hz=440):
    return 69 + 12 * np.log2(f / f_a4_in_hz)


def mtof(m, f_a4_in_hz=440):
    a = f_a4_in_hz  # frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((m - 9) / 12))
    # return (69 + 12 * np.log2(f / f_a4_in_hz))


def filter_pitches(pitches: list, pitch_range: str or abjad.PitchRange):
    if not isinstance(pitch_range, abjad.PitchRange):
        try:
            pitch_range = abjad.PitchRange(pitch_range)
        except:
            print("Cannot build abjad.PitchRange of", pitch_range)
    if not isinstance(pitches, list):
        pitches = [pitches]
    if pitches and not isinstance(pitches[0], abjad.NamedPitch):
        pitches = [abjad.NamedPitch(_) for _ in pitches]

    new_pitches = [p for p in pitches if p in pitch_range]
    return new_pitches


def macro_pitches(
    pitches: list[abjad.Pitch],
    outline: list[int],
    pitch_range: str or abjad.PitchRange = False,
    _min: float = 0,
    _max: float = 1,
):  # min = 0, max = 1
    _pitches = [abjad.NamedPitch(_).number for _ in pitches]
    _pitches = list(dict.fromkeys(_pitches))
    _pitches.sort()
    if pitch_range:
        _pitches = filter_pitches(_pitches, pitch_range)

    outline = [_ / max(outline) for _ in outline]

    _max = round(len(_pitches) * _max)
    _min = round(len(_pitches) * _min)

    _pitches = _pitches[_min:_max]
    outline_indices = [int(_ * (len(_pitches) - 1)) for _ in outline]
    _pitches = [_pitches[_] for _ in outline_indices]

    if pitch_range:
        toprint = [_.number for _ in _pitches]
    else:
        toprint = _pitches

    return _pitches


def transpose_outside_pitches(pitches: list, pitch_range: abjad.PitchRange):
    """Transpose pitches outside a pitch range by an octave (lower + 12, higher - 12)"""

    def get_higher_lower_pitch_ranges(pr):
        """For a given pitch range get the higher and the lower ones."""
        letters = [_ for _ in pr.range_string if _.isalpha()]
        numbers = [int(_) for _ in pr.range_string if _ in [str(_) for _ in range(10)]]

        lopr = abjad.PitchRange(
            "["
            + letters[0]
            + str(numbers[0] - 1)
            + ", "
            + letters[1]
            + str(numbers[1] - 1)
            + "]"
        )
        hipr = abjad.PitchRange(
            "["
            + letters[0]
            + str(numbers[0] + 1)
            + ", "
            + letters[1]
            + str(numbers[1] + 1)
            + "]"
        )
        return lopr, hipr

    lopr, hipr = get_higher_lower_pitch_ranges(pitch_range)
    hipitches = filter_pitches(pitches, hipr)
    lopitches = filter_pitches(pitches, lopr)
    pitches = (
        filter_pitches(pitches, pitch_range)
        + [_ - 12 for _ in hipitches]
        + [_ + 12 for _ in lopitches]
    )
    return [_ for _ in pitches if _ in pitch_range]


def write_pitches(container, pitches, grace=None):
    """Write pitches to logical ties in selection."""
    logical_ties = abjad.select.logical_ties(container, pitched=True, grace=grace)
    for i, logical_tie in enumerate(logical_ties):
        index = i % len(pitches)
        pitch = pitches[index]
        for note in logical_tie:
            note.written_pitch = pitch


def make_art_harmonic_from_target(
    pitched_logical_ties: list,
    finger_interval: int = 5,
    sound_interval: int = 24,
    respell: str = None,
    copy_indicators=True,
    lower_note=None,
):
    if isinstance(pitched_logical_ties, abjad.LogicalTie):
        inst = abjad.get.indicator(pitched_logical_ties[0], abjad.Instrument)
    elif isinstance(pitched_logical_ties, abjad.Note):
        inst = abjad.get.indicator(pitched_logical_ties, abjad.Instrument)
        # print("NOTE")
    elif pitched_logical_ties:
        # print(pitched_logical_ties)
        inst = abjad.get.indicator(pitched_logical_ties[0][0], abjad.Instrument)
    else:
        inst = None
    if inst:
        lower_note = inst.pitch_range.start_pitch
        # print(inst)
    else:
        lower_note = abjad.NumberedPitch(-24)
    # print(lower_note)

    def _art_harmonic_to_lt(lt):
        indicator = abjad.get.indicator(lt[0], abjad.Articulation)
        if (
            not isinstance(lt[0], abjad.Chord)
            and lt[0].written_pitch >= abjad.NamedPitch(lower_note + sound_interval)
            and (indicator is None or indicator.name != "flageolet")
        ):
            for i, note in enumerate(lt):
                note.written_pitch = note.written_pitch - sound_interval
                pitch2 = note.written_pitch + finger_interval
                chord = abjad.Chord(
                    [note.written_pitch, pitch2],
                    note.written_duration,
                    tag=abjad.Tag(f"art_harm_{finger_interval}"),
                )  # fr"art_{finger_interval}"))
                if respell in ["b", "f", "flat"]:
                    abjad.iterpitches.respell_with_flats(chord)
                elif respell in ["#", "s", "sharp"]:
                    abjad.iterpitches.respell_with_sharps(chord)

                if copy_indicators is True:
                    indicators = abjad.get.indicators(note)
                    for ind in indicators:
                        abjad.attach(ind, chord)
                abjad.tweak(chord.note_heads[-1], r"\tweak style #'harmonic")
                abjad.mutate.replace(note, chord)
                if i < len(lt) - 1:
                    abjad.attach(abjad.Tie(), chord)

    if isinstance(pitched_logical_ties, abjad.Note):
        _note = pitched_logical_ties
        _note.written_pitch = _note.written_pitch - sound_interval
        pitch2 = _note.written_pitch + finger_interval
        chord = abjad.Chord(
            [_note.written_pitch, pitch2],
            _note.written_duration,
            tag=abjad.Tag(f"art_harm_{finger_interval}"),
        )
        if respell in ["b", "f", "flat"]:
            abjad.iterpitches.respell_with_flats(chord)
        elif respell in ["#", "s", "sharp"]:
            abjad.iterpitches.respell_with_sharps(chord)
        if copy_indicators is True:
            indicators = abjad.get.indicators(_note)
            for ind in indicators:
                abjad.attach(ind, chord)
        abjad.tweak(
            chord.note_heads[-1],
            r"\tweak style #'harmonic",
        )
        abjad.mutate.replace(_note, chord)

    elif isinstance(pitched_logical_ties, abjad.LogicalTie):
        _art_harmonic_to_lt(pitched_logical_ties)

    elif isinstance(pitched_logical_ties, list):
        for lt in pitched_logical_ties:
            _art_harmonic_to_lt(lt)


def make_nat_harmonic(selection: list or abjad.Leaf, string_markup: str = None):
    def attach(selection):
        abjad.attach(
            abjad.Articulation(r"flageolet"), selection, tag=abjad.Tag(f"nat_harm")
        )

    if isinstance(selection, abjad.Leaf):
        attach(selection)
        if string_markup:
            abjad.attach(
                abjad.Markup(
                    rf'\markup \upright "{string_markup}"',
                ),
                selection,
                direction=abjad.UP,
            )

    elif isinstance(selection, abjad.LogicalTie):
        for note in selection:
            attach(note)
        if string_markup:
            abjad.attach(
                abjad.Markup(
                    rf'\markup \upright "{string_markup}"',
                ),
                selection[0],
                direction=abjad.UP,
            )

    elif isinstance(selection, list):
        if isinstance(selection[0], abjad.Leaf):
            for leaf in selection:
                attach(leaf)
                if string_markup:
                    abjad.attach(
                        abjad.Markup(
                            rf'\markup \upright "{string_markup}"',
                        ),
                        selection[0],
                        direction=abjad.UP,
                    )

        elif isinstance(selection[0], abjad.LogicalTie):
            for lt in selection:
                for note in lt:
                    attach(note)
                if string_markup:
                    abjad.attach(
                        abjad.Markup(
                            rf'\markup \upright "{string_markup}"',
                        ),
                        lt[0],
                        direction=abjad.UP,
                    )


def make_possible_nat_harmonics(
    selection, strings: list[str] | None = None, n_harmonics: int = 7
):
    try:
        leaf = abjad.select.leaf(selection, 0, pitched=True)
    except:
        print("no leaf in selection")
        leaf = None
        inst = None
    if leaf is not None:
        # indicators = abjad.get.indicators(leaf)
        # print(indicators)
        # inst = [_ for _ in indicators if isinstance(_, _Instrument)]
        # print(inst)
        # inst = inst[0]
        inst = abjad.get.indicator(leaf, abjad.Instrument)
    if inst is not None and strings is None:
        strings = inst.tuning.pitches
    if strings is not None:
        logical_ties = abjad.select.logical_ties(selection, pitched=True)
        if not isinstance(strings[0], abjad.Pitch):
            strings = [abjad.NamedPitch(_) for _ in strings]

        harmonics = [
            [abjad.NamedPitch.from_hertz(s.hertz * i) for i in range(1, n_harmonics)]
            for s in strings
        ]
        for logical_tie in logical_ties:
            find = True
            for i, _list in enumerate(harmonics[::-1]):
                if (
                    not isinstance(logical_tie[0], abjad.Chord)
                    and logical_tie[0].written_pitch in _list[1:]
                    and find is True
                ):
                    make_nat_harmonic(logical_tie, roman.toRoman(i + 1))
                    find = False
                elif isinstance(logical_tie[0], abjad.Chord):
                    art_to_nat_harmonics(abjad.select.chords(logical_tie), strings)
    else:
        print("Cannot find instrument on selection. Please provide instrument strings.")


def get_harmonic_fundamental(note, strings: list[str], n_harmonics: int = 7):
    if not isinstance(strings[0], abjad.Pitch):
        strings = [abjad.NamedPitch(_) for _ in strings]

    harmonics = [
        [abjad.NamedPitch.from_hertz(s.hertz * i) for i in range(1, n_harmonics)]
        for s in strings
    ]
    assert isinstance(note, abjad.Note)

    result = None
    for fundamental, harmonics in zip(strings, harmonics):
        for h in harmonics:
            if note.written_pitch == h:
                result = fundamental
                break
    return result


def art_to_nat_harmonics(chords, strings: list):
    for chord in chords:
        # print("ch", chord)
        for tweak in chord.note_heads[-1].tweaks:
            if "harmonic" in tweak.string:
                if chord.note_heads[0].written_pitch in strings:
                    interval = (
                        chord.note_heads[0].written_pitch
                        - chord.note_heads[-1].written_pitch
                    )
                    if (
                        interval == abjad.NamedInterval("+P4")
                        and chord.note_heads[0].written_pitch in strings
                    ):
                        note = abjad.Note("c'4")
                        note.written_duration = chord.written_duration
                        note.written_pitch = chord.note_heads[0].written_pitch + 24
                        make_possible_nat_harmonics(note, strings=strings)
                        abjad.mutate.replace(chord, note)


def art_harmonic_for_longer_notes(pitched_logical_ties, duration=abjad.Duration(4, 8)):
    """Write artificial harmonics for pitched logical ties with duration >= X."""
    selection = pitched_logical_ties
    selection = [lt for lt in selection if lt.written_duration >= duration]
    make_art_harmonic_from_target(selection)


def transpose_note_before_chord_to_the_same_octave(pitched_logical_ties, interval=12):
    """Change the note before a harmonic for near positions on string instruments."""
    if isinstance(pitched_logical_ties, abjad.LogicalTie):
        inst = abjad.get.indicator(pitched_logical_ties[0], abjad.Instrument)
    elif isinstance(pitched_logical_ties, abjad.Note):
        inst = abjad.get.indicator(pitched_logical_ties, abjad.Instrument)
    elif pitched_logical_ties:
        inst = abjad.get.indicator(pitched_logical_ties[0][0], abjad.Instrument)
    else:
        inst = None
    if inst:
        lower_note = inst.pitch_range.start_pitch
    else:
        lower_note = abjad.NumberedPitch(-24)

    selection = pitched_logical_ties
    for lt1, lt2 in zip(selection, selection[1:]):
        test1 = isinstance(lt1[0], abjad.Note) and isinstance(lt2[0], abjad.Chord)
        indicator = abjad.get.indicator(lt2[0], abjad.Articulation)
        test2 = True
        if indicator:
            test2 = (
                isinstance(lt1[0], abjad.Note)
                and isinstance(lt2[0], abjad.Note)
                and indicator.name == "flageolet"
            )

        if test1 and test2:
            if not test1:
                second_note = lt2[0].written_pitch
            else:
                second_note = lt2[0].written_pitches[0]
            difference = abs(lt1[0].written_pitch - second_note)
            if difference > interval:
                t = -interval
            if difference < -interval:
                t = +interval
            while difference > abjad.NamedInterval(7):
                if lt1[0].written_pitch >= lower_note + t:
                    abjad.mutate.transpose(lt1, t)
                difference = abs(lt1[0].written_pitch - second_note)
                if difference > interval:
                    t = -interval
                if difference < -interval:
                    t = +interval


def art_harmonics_sounding_pitch(pitched_logical_ties):
    """Write just the sounding pitch of harmonic notation for midi rendering purposes."""
    for lt in pitched_logical_ties:
        if isinstance(lt[0], abjad.Chord) and "art_harm" in lt[0].tag.string:
            for chord in lt:
                interval = (
                    chord.note_heads[1].written_pitch
                    - chord.note_heads[0].written_pitch
                )
                if interval == abjad.NamedInterval("-P4"):
                    transposition = 24
                    del chord.note_heads[1]
                    abjad.mutate.transpose(chord, transposition)
                elif interval == abjad.NamedInterval("-M3"):
                    transposition = 28
                    del chord.note_heads[1]
                    abjad.mutate.transpose(chord, transposition)


def pitches_in_staff(pitches, chord=False):
    """Show abjad.PitchSegment in two staffs."""
    G_staff = abjad.Staff()
    F_staff = abjad.Staff()
    staff_group = abjad.StaffGroup([G_staff, F_staff])
    pitch_range = abjad.PitchRange("[C4, +inf]")
    if not isinstance(pitches[0], abjad.NamedPitch):
        pitches = [abjad.NamedPitch(_) for _ in pitches]

    if chord is False:
        for pitch in pitches:
            test = pitch in pitch_range
            if test is True:
                note = abjad.Note.from_pitch_and_duration(pitch, (1, 4))
                G_staff.append(note)
                F_staff.append(abjad.Skip((1, 4)))
            if test is False:
                note = abjad.Note.from_pitch_and_duration(pitch, (1, 4))
                G_staff.append(abjad.Skip((1, 4)))
                F_staff.append(note)

        for i, note in enumerate(F_staff):
            abjad.attach(abjad.Markup(rf"\markup {str(i)}"), note)

    if chord is True:
        chord = abjad.Chord(r"<c>4")
        chord.written_pitches = pitches
        F_staff.append(chord)

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

    # add tempo
    # abjad.attach(
    #     abjad.MetronomeMark(
    #         abjad.Duration(1, 4),
    #         72,
    #         custom_markup=abjad.Markup(r"\markup{ }"),
    #     ),
    #     abjad.select.leaf(selection, 0),
    # )
    # abjad.attach(abjad.Dynamic("pp"), abjad.select.leaf(selection, 0))

    # abjad.attach(abjad.Dynamic("pp"), abjad.select.leaf(selection2, 0))

    abjad.override(staff_group).BarLine.stencil = False
    abjad.override(staff_group).TextScript.padding = 5
    abjad.override(staff_group).BarNumber.stencil = False
    abjad.override(staff_group).Beam.stencil = False
    abjad.override(staff_group).Flag.stencil = False
    abjad.override(staff_group).Rest.stencil = False
    abjad.override(staff_group).SpacingSpanner.strict_note_spacing = True
    abjad.override(staff_group).SpanBar.stencil = False
    abjad.override(staff_group).Stem.stencil = False
    abjad.override(staff_group).TimeSignature.stencil = False
    abjad.setting(staff_group).proportionalNotationDuration = "#(ly:make-moment 1 25)"
    # abjad.show(staff_group)

    return staff_group


def illustrate_pitches_in_staff(
    markups: list = None,
    scores: list = None,
    midi=False,
    pdf_path: str = None,
    open_in_emacs=False,
):
    """Creates lilypond file and generates pdf with associated markups and scores."""
    # score_block = abjad.Block("score")

    items = []
    if markups is None:
        markups = [abjad.Markup(rf"\markup{ {i} }") for i, _ in enumerate(scores)]
    for score, markup in zip(scores, markups):
        items.append(markup)
        if midi is True:
            midi_block = abjad.Block("midi")
            layout_block = abjad.Block("layout")
            score_block = abjad.Block("score", items=[score, midi_block, layout_block])
            # score_block.items.append(midi_block)
        else:
            score_block = abjad.Block("score", items=[score])
        items.append(score_block)

    if pdf_path is None:
        pdf_path = input("Enter a file path: ")

    lyfile = abjad.LilyPondFile(
        items=items,
    )
    print(pdf_path)
    abjad.persist.as_pdf(lyfile, pdf_path)
    if open_in_emacs is True:
        os.system("emacsclient " + pdf_path)


def otoacoustic_derivation(f1, f2, iterations):
    fs = [f1, f2]
    for i in range(iterations):
        inlist = []
        for j in fs[:-1]:
            # print(j)
            inlist.append(abs(fs[-1] - j))
            inlist.append(abs(2 * fs[-1] - j))
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
def ring_modulation(
    pitches,
    pitch_range=abjad.PitchRange("[-inf, +inf]"),
    keep_originals=True,
    last=False,
    chords=False,
    quarter_tone=True,
    sort=False,
    frequencies: list = None,
    hertz=False,
):
    if pitches and not isinstance(pitches, abjad.PitchSegment):
        pitches = abjad.PitchSegment(pitches)

    if pitches is None and frequencies:
        pitches_in = frequencies
    else:
        pitches_in = [abjad.NumberedPitch(_).hertz for _ in pitches]

    pitches_out = []
    if chords is False:
        for (i, pitch1), pitch2 in zip(enumerate(pitches_in), pitches_in[1:]):
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
            new_pitch_C = 2 * pitch2 + pitch1
            pitches_out.append(new_pitch_C)

            # 2xFREQ_B - FREQ_A
            new_pitch_D = 2 * pitch2 - pitch1
            pitches_out.append(new_pitch_D)

            # 2xFREQ_A + FREQ_B
            new_pitch_E = 2 * pitch1 + pitch2
            pitches_out.append(new_pitch_E)

            # 2xFREQ_A - FREQ_B
            new_pitch_F = 2 * pitch1 - pitch2
            pitches_out.append(new_pitch_F)
            if keep_originals is True and last is True:
                if i == (len(pitches_in) - 2) or len(pitches_in) == 2:
                    pitches_out.append(pitch2)
                    print(pitch2)

    if chords is True:
        chords_out = []
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
            chords_out.append(chord)

    # pitches_out = [round(_, 2) for _ in pitches_out]
    new_pitches_out = []
    for frequency in pitches_out:
        if not isinstance(frequency, abjad.Chord) and frequency > 20:
            try:
                new_pitches_out.append(abjad.NumberedPitch.from_hertz(frequency))
            except ValueError:
                print(
                    "Cannot transform frequency:", frequency, "to abjad.NumberedPitch"
                )

    # pitches_out=[abjad.NumberedPitch.from_hertz(_) for _ in pitches_out]
    if hertz is False:
        pitches_out = [_.number for _ in new_pitches_out]

    if hertz is False and quarter_tone is False:
        pitches_out = [round(_) for _ in pitches_out]

    # pitches_out = list(pitches_out)
    if sort is True:
        pitches_out.sort()
        pitches_out = abjad.sequence.remove_repeats(pitches_out)
        if hertz is True:
            indices = []
            for i, freq in enumerate(pitches_out):
                j = i - 1
                if freq - pitches_out[j] < 5:
                    indices.append(i)
            for i in reversed(indices):
                del pitches_out[i]

    # print(pitches_out)
    # for i in pitches_out:
    # print(i)
    if hertz is False:
        pitches_out = [abjad.NamedPitch(_) for _ in pitches_out]
        pitches_out = [_ for _ in pitches_out if _ in pitch_range]
    # print(pitches_out)

    if chords is True:
        if not isinstance(chords_out, list):
            chords_out = [chords_out]
        return chords_out
    else:
        if not isinstance(pitches_out, list):
            pitches_out = [pitches_out]
        return pitches_out


def new_ring_modulation(
    pitches,
    pitch_range=abjad.PitchRange("[-inf, +inf]"),
    keep_originals=True,
    chords=False,
    quarter_tone=True,
    sort=False,
    frequencies: list = None,
    hertz=False,
):
    if pitches and not isinstance(pitches, abjad.PitchSegment):
        pitches = abjad.PitchSegment(pitches)

    if pitches is None and frequencies:
        pitches_in = frequencies
    else:
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

            if keep_originals is True:
                # ORIGINAL
                pitches_out.append(pitch2)
            # FREQ_B + FREQ_A
            new_pitch_B = pitch1 + pitch2
            pitches_out.append(new_pitch_B)

            # # 2xFREQ_B + FREQ_A
            # new_pitch_C = 2 * pitch2 + pitch1
            # pitches_out.append(new_pitch_C)

            # # 2xFREQ_B - FREQ_A
            # new_pitch_D = 2 * pitch2 - pitch1
            # pitches_out.append(new_pitch_D)

            # # 2xFREQ_A + FREQ_B
            # new_pitch_E = 2 * pitch1 + pitch2
            # pitches_out.append(new_pitch_E)

            # # 2xFREQ_A - FREQ_B
            # new_pitch_F = 2 * pitch1 - pitch2
            # pitches_out.append(new_pitch_F)

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
                print("Cannot transform frequency:", pitch, "to abjad.NumberedPitch")

    # pitches_out=[abjad.NumberedPitch.from_hertz(_) for _ in pitches_out]
    if hertz is False:
        pitches_out = [_.number for _ in new_pitches_out]

    if hertz is False and quarter_tone is False:
        pitches_out = [round(_) for _ in pitches_out]

    # pitches_out = list(pitches_out)
    if sort is True:
        pitches_out.sort()
        pitches_out = abjad.sequence.remove_repeats(pitches_out)
        if hertz is True:
            indices = []
            for i, freq in enumerate(pitches_out):
                j = i - 1
                if freq - pitches_out[j] < 5:
                    indices.append(i)
            for i in reversed(indices):
                del pitches_out[i]

    # print(pitches_out)
    # for i in pitches_out:
    # print(i)
    if hertz is False:
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
