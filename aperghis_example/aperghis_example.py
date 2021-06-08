"""
Aperghis Example.

Rewriting Aperghis Recitación 9 using ``muda.Material()``.
"""
import abjad
import muda
from abjadext import rmakers

# COMPONENTS

# Timespans
"""Create timespans using ``muda.timespan.alternating_timespans``.
Each column refers to in the list below refers to a material.
It represents the material presence (duration).
"""

alternations = [
# mat00, mat01, mat02, ..., mat11
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

# names for the materials in the list above:
annotations = [
    "mat00", "mat01", "mat02", "mat03", "mat04", "mat05", "mat06",
    "mat07", "mat08", "mat09", "mat10", "mat11"]

timespans = muda.timespan.alternating_timespans(
    n_annotations=12,
    alternations=alternations,
    denominator=8,
    annotations=annotations)

# Transform it to a list of ``muda.AnnotatedDuration``
durations = timespans.annotated_durations(subdivision=(2, 4))
# It is a list of durations where each one is annotated with 
# the material name.

# Rhythms of each material
makers = {
    "mat11": rmakers.stack(
        rmakers.talea([2, 1, -1], 16),
        rmakers.extract_trivial()),
    "mat10": rmakers.stack(
        rmakers.talea([1, 1, 1, 1, 1], 32, extra_counts=[1]),
        rmakers.extract_trivial()),
    "mat09": rmakers.stack(
        rmakers.talea([-1, 1, -1], 8, extra_counts=[1]),
        rmakers.extract_trivial()),
    "mat08": rmakers.stack(
        rmakers.talea([1, 1, 1], 4, extra_counts=[1]),
        rmakers.extract_trivial()),
    "mat07": rmakers.stack(
        rmakers.talea([-3, -2, 1, -3, -3], 16, extra_counts=[4]),
        rmakers.extract_trivial()),
    "mat06": rmakers.stack(
        rmakers.talea([-2, 1, 1, 1, 1, 1, 1], 32),
        rmakers.extract_trivial()),
    "mat05": rmakers.stack(
        rmakers.talea([1, 4, 2], 8),
        rmakers.extract_trivial()),
    "mat04": rmakers.stack(
        rmakers.talea([-4, 2, 1, 1, -1, 1, 1, -1, 2, 1, 1], 32),
        rmakers.extract_trivial()),
    "mat03": rmakers.stack(
        rmakers.talea([2, -1, 2, 2, 2, -2, 2, -2], 16, extra_counts=[5]),
        rmakers.extract_trivial()),
    "mat02": rmakers.stack(
        rmakers.talea([-1, 1, 1, -1], 32),
        rmakers.extract_trivial()),
    "mat01": rmakers.stack(
        rmakers.talea([2, -1], 16, extra_counts=[1]),
        rmakers.extract_trivial()),
    "mat00": rmakers.stack(
        rmakers.talea([-8, -2, 2, 1, -3], 32),
        rmakers.extract_trivial())
}

# Pitches for each material
pitches = {
    "mat11": abjad.PitchSegment("a' b'"),
    "mat10": abjad.PitchSegment("e''' ef'' b'' a' d'"),
    "mat09": abjad.PitchSegment("b'"),
    "mat08": abjad.PitchSegment("f'' e'' ef''"),
    "mat07": abjad.PitchSegment("b'"),
    "mat06": abjad.PitchSegment("e'' c'' e'' c'' g' b'"),
    "mat05": abjad.PitchSegment("e' e'' g''"),
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
    makers,
)

"""I had to write the retrograde in some rhythm makers because abjad
would write the material in a given duration from left to right.
However, the Aperghis' piece expands from right to left. Below,
I use the ``muda.Material.retrograde()`` to get it right."""


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

# LITERALS

literal00 = [
    r"\override Score.BarLine.stencil = ##f",
    r"\override Staff.NoteHead.no-ledgers = ##t",
    r"\override Staff.StaffSymbol.line-count = 1",
    r"\omit Clef"]

# when material_name is None, it attaches to ``mats.container`` leaves, pitched or not.
mats.attach(
    None,  # material_name
    literal00, # literal
    0 # leaf)

mats.attach(None, r"\break", 1)

# breaks
for leaf, (i, leaf2) in zip(mats.container, enumerate(mats.container[1:])):
    if leaf.name is not None:
        if leaf.name == "mat11" and leaf2.name != "mat11":
            abjad.attach(abjad.LilyPondLiteral(r"\break"), leaf2)

# stop and start staff
five_lines = r"\stopStaff \startStaff \revert Staff.StaffSymbol.line-count"
one_line = r'\stopStaff \startStaff \override Staff.StaffSymbol.line-count = 1'
mats.attach(["mat08", "mat10"], five_lines, 0)
mats.attach(["mat09", "mat11"], one_line, 0)

# noteheads
arrowdown_head = [
    r"\stemUp",
    r"\once \override Staff.Stem.X-offset  = #-0.07",
    r"\once \override Staff.Stem.Y-offset  = #0.3",
    r"\once \override Staff.Flag.Y-offset  = #1.5",
    r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
    r"\once \override Staff.NoteHead #'text = \markup{" +
    r" \arrow-head #Y #DOWN ##f}"]
arrowup_head = [
    r"\stemNeutral",
    r"\once \override Staff.Stem.Y-offset  = #-1.3",
    r"\once \override Staff.Stem.X-offset  = #-0.1",
    r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
    r"\once \override Staff.NoteHead #'text = \markup{" +
    r" \arrow-head #Y #UP ##f}"]

mats.note_heads("mat06", "#'cross")
mats.attach("mat05", arrowdown_head, 0)
mats.attach("mat05", arrowup_head, -1)

# mats.see_leaves_number(pitched=True)

# texts
mats.attach(
    None, abjad.Markup("expirar", direction=abjad.Up), 59, pitched=True)
mats.attach(
    None, abjad.Markup("inspirar", direction=abjad.Up), 60, pitched=True)
mats.attach(
    None, abjad.Markup("(potrinaire)", direction=abjad.Up), 18, pitched=True)
mats.attach(
    None, abjad.Markup("(souffle)", direction=abjad.Up), 41, pitched=True)

# slurs
mats.write_indicators(material_name="mat05", slur_down=[(0, 1)])
mats.write_indicators(material_name="mat08", slur_up=[(0, 2)])
mats.write_indicators(material_name="mat10", slur_up=[(0, 4)])

# Lyrics
lyrics = muda.Lyrics("Soprano_Voice_1")
lyrics.write_lyrics(r"""
    sir
    dé -- sir
    _ dé -- sir
    ce _ dé -- sir
    donc __ ce _  dé -- sir
    porquoi  donc __ ce _ dé -- sir
    _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
    _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
    je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
    par -- fois je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
    jé par -- fois je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
    tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
        porquoi donc __ ce _  dé -- sir
    san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
        porquoi donc __ ce _  dé -- sir
    vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
        porquoi donc __ ce _  dé -- sir
    en -- vie vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
        porquoi donc __ ce _  dé -- sir
    mon en -- vie vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
        porquoi donc __ ce _  dé -- sir
    à mon en -- vie vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
        porquoi donc __ ce _  dé -- sir
    ré -- siste à mon en -- vie vé san tu -- jé par -- fois je lui cède
        _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
    par -- fois je ré -- siste à mon en -- vie vé san tu -- jé
        par -- fois je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
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
time_signatures = [abjad.TimeSignature(_) for _ in durations]
score.make_skips(time_signatures)
score.write_materials([mats, lyrics])
score.rewrite_meter(time_signatures)
lilypond_file = abjad.LilyPondFile(
    items=[score.score],
)
abjad.persist.as_ly(lilypond_file, "aperghis_score.ly")
