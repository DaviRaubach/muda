import abjad
import muda

staff = abjad.Staff(
    [
        abjad.Container("c'8 d'"),
        abjad.Container("e'8 f'"),
        abjad.Container("g'8 a'"),
        abjad.Container("b'8 c''"),
		abjad.Container("b'8 c''"),
        abjad.Container("b'8 c''"),
        abjad.Container("b'8 c''"),

        abjad.Container("b'4 c''"),


    ]
)

abjad.setting(staff).autoBeaming = False 

class myclass(abjad.Duration):
	def __init__(self, notation=None):
		self.annotation = annotation
		print(self.annotation)
		return None


myclass(notation="this")

dur = muda.AnnotatedDuration((3,4))
dur.annotation = "e"
durations = [
	dur, dur, dur

]
abdurations = []
for dur in durations:
	abdurations.append(dur.get_abjad_duration())

selector = (
    abjad.select()
    .leaves()
    .partition_by_durations(
        abdurations,
        cyclic=True,
        fill=abjad.Exact,
        in_seconds=False,
        overhang=True,
    )
)
result = selector(staff)

# for selection, pitches in zip(result, annotated_pitches):
# 	logical_ties = abjad.select(selection).leaves().logical_ties(pitched=True)
#     for i, logical_tie in enumerate(logical_ties):
#         index = i % len(pitches)
#         pitch = pitches[index]
#         for note in logical_tie:
#             if isinstance(note, abjad.Rest):
#                 pass
#             else:
#                 note.written_pitch = pitch



# for selection, pitches, duration in zip(result, annotated_pitches, annotated_durations):
# 	logical_ties = abjad.select(selection).leaves().logical_ties(pitched=True)
# 	if pitches.annotation == duration.annotation:
#         for i, logical_tie in enumerate(logical_ties):
#             index = i % len(pitches)
#             pitch = pitches[index]
#             for note in logical_tie:
#                 if isinstance(note, abjad.Rest):
#                     pass
#                 else:
#                     note.written_pitch = pitch




# selector.print(result)