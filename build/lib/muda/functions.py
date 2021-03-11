import abjad

def make_measures(
    durations,
    rhythm_maker,
    pitches,
):

    if rhythm_maker is not None:
        measures = rhythm_maker(durations)
        measures = abjad.Container(measures)


    if pitches is not None:
        logical_ties = abjad.select(measures).leaves().logical_ties(pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            index = i % len(pitches)
            pitch = pitches[index]
            for note in logical_tie:
                if isinstance(note, abjad.Rest):
                    pass
                else:
                    note.written_pitch = pitch

    return measures
    
    