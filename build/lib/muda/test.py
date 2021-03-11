import abjad
import muda.functions as functions
import abjadext.rmakers as rmakers

violin = instrument(abjad_instrument=abjad.Violin(), lilypond_name="Violin", nstaffs=1, nvoices=[2])
piano = instrument(abjad_instrument=abjad.Piano(), lilypond_name="Piano", nstaffs=2, nvoices=[2, 2], piano=True)
instruments = [violin, piano]
include = ["/Users/Davi/github/packaging_tutorial/muda/stylesheet.ly"]
score = create_score()

add_instrument(instruments, score)
time_signatures = [(4, 4), (4, 4), (4, 4), (3, 4), (5, 4)]
make_skips(time_signatures, score)

measures = functions._make_measures(
    durations=time_signatures,
    rhythm_maker=rhythm,
    pitches=pitch,
)

piano_measures = functions._make_measures(
    durations=time_signatures,
    rhythm_maker=rhythm_piano,
    pitches=pitch,
)


write_material("Violin_Voice_1", measures)
write_material("Piano_Voice_1", piano_measures)



score = create_lilypond_file(includes=include, score=score)
# segment_maker(score_elements)
abjad.show(score)