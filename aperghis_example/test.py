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
    rmakers.talea([5, 2], 8),
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
    [36, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [34, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
    [32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2],
    [28, 0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 1, 2],
    [24, 0, 0, 0, 0, 0, 0, 0, 4, 4, 2, 1, 2],
    [22, 0, 0, 0, 0, 0, 0, 2, 4, 4, 2, 1, 2],
    [15, 0, 0, 0, 0, 0, 7, 2, 4, 4, 2, 1, 2],
    [12, 0, 0, 0, 0, 3, 7, 2, 4, 4, 2, 1, 2],
    [11, 0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
    [11, 0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
    [11, 0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
    [10, 0, 0, 0, 1, 4, 7, 2, 4, 4, 2, 1, 2],
    [6, 0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [6, 0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [6, 0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [5, 0, 0, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [4, 0, 1, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 4, 1, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2]]
timespans = muda.timespan.alternating_timespans(
    n_annotations=13,
    alternations=alternations,
    denominator=8,
    annotations=[
        "skips",
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
    skips,)

pitches = {
    "mat11": abjad.PitchSegment("b' a"),
}
mats.write_pitches_by_duration(pitches, durations)


"""I had to write the retrograde in the rhythm maker because abjad
would write the material in a given duration from left to right.
However, the Aperghis' piece expands from right to left. Below,
I use the ``muda.Material.retrograde()`` to get the right material."""

mats.retrograde("mat11")
mats.retrograde("mat04")
mats.retrograde("mat02")
mats.retrograde("mat01")
mats.retrograde("mat00")
mats.see_leaves_number()
pitches = {
    "mat10": abjad.PitchSegment("e''' ef'' b'' a' d'"),
    "mat08": abjad.PitchSegment("f'' e'' ef''"),
    "mat06": abjad.PitchSegment("e'' c'' e'' c'' g' b'"),
    "mat10": abjad.PitchSegment("b' b' b' b' a' b' b' b'"),
}
mats.write_pitches_by_duration(pitches, durations)

# BREAKS
selection = abjad.select(mats.container).components(abjad.Container)
for leaf, (i, leaf2) in zip(mats.container, enumerate(mats.container[1:])):
    if leaf.tag is not None:
        if leaf.tag.string == "mat11" and leaf2.tag.string != "mat11":
            abjad.attach(abjad.LilyPondLiteral(r"\break"), leaf2)

# SCORE
score = muda.Score()
inst = muda.Instrument(
    abjad_instrument=abjad.SopranoVoice(),
    lilypond_name="Soprano",
    nstaffs=1,
    nvoices=[1]
)
score.add_instrument([inst])
numerators = [4, 4, 4, 4, 4, 4, 4, 4, 4, 1] * 19
time_signatures = [(_, 8) for _ in numerators]
time_signatures = [abjad.TimeSignature(_) for _ in time_signatures]
score.make_skips(time_signatures)
score.write_materials([mats])
score.rewrite_meter(time_signatures)
block = abjad.Block(name="layout")
block.ragged_right = True
block.indent = 0
lilypond_file = abjad.LilyPondFile(
    default_paper_size=("a4", "landscape"),
    includes=["aperghis_stylesheet.ily"],
)
lilypond_file.items.append(block)
lilypond_file.items.append(score.score)
# print(abjad.lilypond(lilypond_file))
abjad.show(lilypond_file)
