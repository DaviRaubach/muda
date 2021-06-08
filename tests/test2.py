"""
Aperghis Example.

Rewriting Aperghis Recitación 9 using ``muda.Material()``.
"""
import abjad
import muda

cont = abjad.Container("c4 d4 e4", name="test")

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
numerators = [4, 4, 4, 4, 4, 4, 4, 4, 4, 1] * 19
time_signatures = [(_, 8) for _ in numerators]
time_signatures = [abjad.TimeSignature(_) for _ in time_signatures]
score.make_skips(time_signatures)
score.write_materials([cont])
score.rewrite_meter(time_signatures)
lilypond_file = abjad.LilyPondFile(
    items=[score.score],
)
abjad.show(lilypond_file)
# print(abjad.lilypond(score.score))
# abjad.persist.as_ly(lilypond_file, "aperghis_score.ly")