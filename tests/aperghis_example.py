"""
Aperghis Example.

Rewriting Aperghis Recitación 9 using ``muda.Material()``.
"""
import abjad
import muda
from abjadext import rmakers

# COMPONENTS
# Rhythms
rmaker11 = rmakers.stack(
    rmakers.talea([2, 1, -1], 16),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat11"),)
rmaker10 = rmakers.stack(
    rmakers.talea([1, 1, 1, 1, 1], 32, extra_counts=[1]),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat10"),)
rmaker09 = rmakers.stack(
    rmakers.talea([-1, 1, -1], 8, extra_counts=[1]),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat09"),)
rmaker08 = rmakers.stack(
    rmakers.talea([1, 1, 1], 4, extra_counts=[1]),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat08"),)
rmaker07 = rmakers.stack(
    rmakers.talea([-3, -2, 1, -3, -3], 16, extra_counts=[4]),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat07"),)
rmaker06 = rmakers.stack(
    rmakers.talea([-2, 1, 1, 1, 1, 1, 1], 32),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat06"),)
rmaker05 = rmakers.stack(
    rmakers.talea([1, 4, 2], 8),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat05"),)
rmaker04 = rmakers.stack(
    rmakers.talea([-4, 2, 1, 1, -1, 1, 1, -1, 2, 1, 1], 32),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat04"),)
rmaker03 = rmakers.stack(
    rmakers.talea([2, -1, 2, 2, 2, -2, 2, -2], 16, extra_counts=[5]),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat03"),)
rmaker02 = rmakers.stack(
    rmakers.talea([-1, 1, 1, -1], 32),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat02"),)
rmaker01 = rmakers.stack(
    rmakers.talea([2, -1], 16, extra_counts=[1]),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat01"),)
rmaker00 = rmakers.stack(
    rmakers.talea([-8, -2, 2, 1, -3], 32),
    # rmakers.beam(),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat00"),)
skips = rmakers.multiplied_duration(abjad.Skip, tag=abjad.Tag("skips"),)

# Timespans
alternations = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 0, 0, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 0, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 2, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 3, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 1, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [4, 1, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2]]
timespans = muda.timespan.alternating_timespans(
    n_annotations=12,
    alternations=alternations,
    denominator=8,
    annotations=[
        # "skips",
        "mat00",
        "mat01",
        "mat02",
        "mat03",
        "mat04",
        "mat05",
        "mat06",
        "mat07",
        "mat08",
        "mat09",
        "mat10",
        "mat11"])
durations = timespans.annotated_durations(subdivision=(2, 4))

# Pitches
pitches11 = {"mat11": abjad.PitchSegment("b' a'")}
pitches = {
    "mat10": abjad.PitchSegment("e''' ef'' b'' a' d'"),
    "mat09": abjad.PitchSegment("b'"),
    "mat08": abjad.PitchSegment("f'' e'' ef''"),
    "mat07": abjad.PitchSegment("b'"),
    "mat06": abjad.PitchSegment("e'' c'' e'' c'' g' b'"),
    "mat05": abjad.PitchSegment("e' g' e''"),
    "mat04": abjad.PitchSegment("b' b' b' a' b' b' b'"),
    "mat03": abjad.PitchSegment("b'"),
    "mat02": abjad.PitchSegment("b'"),
    "mat01": abjad.PitchSegment("b'"),
    "mat00": abjad.PitchSegment("b'"),
}

# MATERIALS
mats = muda.Material("Soprano_Voice_1")
mats.alternating_materials(
    durations,
    rmaker11,
    rmaker10,
    rmaker09,
    rmaker08,
    rmaker07,
    rmaker06,
    rmaker05,
    rmaker04,
    rmaker03,
    rmaker02,
    rmaker01,
    rmaker00,
    # skips,
)

"""I had to write the retrograde in the rhythm maker because abjad
would write the material in a given duration from left to right.
However, the Aperghis' piece expands from right to left. Below,
I use the ``muda.Material.retrograde()`` to get the right material."""

mats.write_pitches_by_duration(pitches11, durations)

mats.retrograde("mat11")
mats.retrograde("mat04")
mats.retrograde("mat03")
mats.retrograde("mat02")
mats.retrograde("mat01")
mats.retrograde("mat00")

mats.write_pitches_by_duration(pitches, durations)

# mats.see_leaves_number(pitched=False)

mats.delete([181, 182, 221, 346], replace_with_rests=True)
mats.delete([343, 344, 345, 391, 392, 393], replace_with_skips=True)
mats.delete([1], material_name="mat05", replace_with_skips=True)
mats.attach("mat07", abjad.BeforeGraceContainer("b'8"), 2)

# BREAKS AND DIFFERENT STAFFS
selection = abjad.select(mats.container).components(abjad.Container)
selection2 = abjad.select(mats.container).leaves()

literal00 = [
    r"\override Score.BarLine.stencil = ##f",
    r"\override Staff.NoteHead.no-ledgers = ##t",
    r"\override Staff.StaffSymbol.line-count = 1",
    r"\omit Clef"]

# when material_name is None attach to mats.container leaves pitched or not.
mats.attach(
    None,  # material_name
    literal00,
    0)

mats.attach(None, r"\break", 1)

for leaf, (i, leaf2) in zip(mats.container, enumerate(mats.container[1:])):
    if leaf.tag is not None:
        if leaf.tag.string == "mat11" and leaf2.tag.string != "mat11":
            abjad.attach(abjad.LilyPondLiteral(r"\break"), leaf2)

five_lines = r"\stopStaff \startStaff \revert Staff.StaffSymbol.line-count"
one_line = r'\stopStaff \startStaff \override Staff.StaffSymbol.line-count = 1'
arrowdown_head = [
    r"\stemUp",
    r"\once \override Staff.Stem.X-offset  = #-0.07",
    r"\once \override Staff.Stem.Y-offset  = #0.3",
    r"\once \override Staff.Flag.Y-offset  = #1.5",
    r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
    r"\once \override Staff.NoteHead #'text = \markup{",
    r" \arrow-head #Y #DOWN ##f}"]
arrowup_head = [
    r"\stemNeutral",
    r"\once \override Staff.Stem.Y-offset  = #-1.3",
    r"\once \override Staff.Stem.X-offset  = #-0.1",
    r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
    r"\once \override Staff.NoteHead #'text = markup{",
    r" \arrow-head #Y #UP ##f}"]

mats.attach(["mat08", "mat10"], five_lines, 0)
mats.attach(["mat09", "mat11"], one_line, 0)
mats.attach("mat05", arrowdown_head, 0)
mats.attach("mat05", arrowup_head, -1)

mats.write_indicators(material_name="mat05", slur_down=[(0, 1)])
mats.write_indicators(material_name="mat08", slur_up=[(0, 2)])
mats.write_indicators(material_name="mat10", slur_up=[(0, 4)])

# materials_names = ["mat00", "mat01", "mat02", "mat03", "mat04", "mat05",
#                    "mat06", "mat07", "mat08", "mat09", "mat10", "mat11"]
# mats.attach(
#     materials_names,
#     r"\revert Score.BarLine.stencil",
#     0)

mats.note_heads("mat06", "#'cross")

lyrics = muda.Lyrics("Soprano_Voice_1")
lyrics.write_lyrics(r"""
    Sir
    Dé -- sir
    _ Dé -- sir
    Ce _ Dé -- sir
    _ Ce _  Dé -- sir
    Porquoi  _ Ce _ Dé -- sir
    _ _ _ _ _ _ Porquoi _ Ce _  Dé -- sir
    _ _ _ _ _ _ _ Porquoi _ Ce _  Dé -- sir
    """)



# SCORE
score = muda.Score()
inst = muda.Instrument(
    abjad_instrument=abjad.SopranoVoice(),
    name="Soprano",
    nstaffs=1,
    nvoices=[1],
    lyrics_target="Soprano_Voice_1",
)
score.append([inst])
# numerators = [4, 4, 4, 4, 4, 4, 4, 4, 4, 1] * 19
# time_signatures = [(_, 8) for _ in numerators]
time_signatures = [abjad.TimeSignature(_) for _ in durations]
score.make_skips(time_signatures)
score.write_materials([mats, lyrics])
score.rewrite_meter(time_signatures)
lilypond_file = abjad.LilyPondFile(
    items=[score.score],
)
abjad.persist.as_ly(lilypond_file, "aperghis_score.ly")

