# import abjad
# import muda

# staff = abjad.Staff(
#     [
#         abjad.Container("c'8 d'"),
#         abjad.Container("e'8 f'"),
#         abjad.Container("g'8 a'"),
#         abjad.Container("b'8 c''"),
# 		abjad.Container("b'8 c''"),
#         abjad.Container("b'8 c''"),
#         abjad.Container("b'8 c''"),

#         abjad.Container("b'4 c''"),


#     ]
# )

# abjad.setting(staff).autoBeaming = False 

# class myclass(abjad.Duration):
# 	def __init__(self, notation=None):
# 		self.annotation = annotation
# 		print(self.annotation)
# 		return None


# myclass(notation="this")

# dur = muda.AnnotatedDuration((3,4))
# dur.annotation = "e"
# durations = [
# 	dur, dur, dur

# ]
# abdurations = []
# for dur in durations:
# 	abdurations.append(dur.get_abjad_duration())

# selector = (
#     abjad.select()
#     .leaves()
#     .partition_by_durations(
#         abdurations,
#         cyclic=True,
#         fill=abjad.Exact,
#         in_seconds=False,
#         overhang=True,
#     )
# )
# result = selector(staff)

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



# SCORE
# import muda
# import abjad
# from abjadext import rmakers

# myinst = muda.Instrument(
#     abjad_instrument = abjad.Piano(),
#     lilypond_name = "Piano",
#     nstaffs = 2,
#     nvoices = [2, 1],
#     piano = True)

# myscore = muda.Score()
# myscore.add_instrument(myinst)
# mydivisions = [(4, 4), (5, 4)]
# myscore.make_skips(mydivisions)

# mymaterial = muda.Material("Piano_Voice_1")
# mymaterial.silence_and_rhythm_maker(
#     maker=rmakers.stack(rmakers.note()),
#     annotated_divisions=[
#         muda.AnnotatedDuration((1, 4)),
#         muda.AnnotatedDuration((1, 4), annotation="Rest"),
#         muda.AnnotatedDuration((1, 4)),
#         muda.AnnotatedDuration((1, 4)),
#         muda.AnnotatedDuration((1, 4), annotation="Rest"),
#         muda.AnnotatedDuration((1, 4)),
#         muda.AnnotatedDuration((1, 4)),
#         muda.AnnotatedDuration((1, 4), annotation="Rest"),
#         muda.AnnotatedDuration((1, 4)),
#         ]
#     )

# myscore.write_materials([mymaterial])
# myscore.rewrite_meter(mydivisions)
# abjad.show(myscore.score)




import muda
import abjad
from abjadext import rmakers

myinst = muda.Instrument(
    abjad_instrument = abjad.Piano(),
    lilypond_name = "Piano",
    nstaffs = 2,
    nvoices = [2, 1])

myscore = muda.Score()
myscore.add_instrument([myinst])
mydivisions = [(8, 4), (5, 4)]
myscore.make_skips(mydivisions)

mymaterial1 = muda.Material("Piano_Voice_1")
mymaterial1.silence_and_rhythm_maker(
    maker=rmakers.stack(
        rmakers.talea([1, -3, 1], 16),
        rmakers.extract_trivial(),
        rmakers.beam(),
        ),
    annotated_divisions=[
        muda.AnnotatedDuration((1, 4)),
        muda.AnnotatedDuration((2, 4), annotation="Rest"),
        muda.AnnotatedDuration((2, 4)),
        muda.AnnotatedDuration((2, 4), annotation="Rest"),
        muda.AnnotatedDuration((1, 4)),
        muda.AnnotatedDuration((2, 4), annotation="Rest"),
        muda.AnnotatedDuration((3, 4)),
        ]
    )
mymaterial1.write_pitches(["d'"])

mymaterial2 = muda.Material("Piano_Voice_3")
mymaterial2.silence_and_rhythm_maker(
    maker=rmakers.stack(
        rmakers.talea([-1, 1, 1, 1], 16),
        rmakers.extract_trivial(),
        rmakers.beam(),
        ),
    annotated_divisions=[
        muda.AnnotatedDuration((3, 8)),
        muda.AnnotatedDuration((3, 8), annotation="Rest"),
        muda.AnnotatedDuration((3, 8)),
        muda.AnnotatedDuration((3, 8), annotation="Rest"),
        muda.AnnotatedDuration((4, 8)),
        muda.AnnotatedDuration((3, 8)),
        muda.AnnotatedDuration((3, 8), annotation="Rest"),
        muda.AnnotatedDuration((4, 8)),
        ]
    )


material_list = [mymaterial1, mymaterial2]
myscore.write_materials(material_list)
myscore.rewrite_meter(mydivisions)
# abjad.show(myscore.score)
print(abjad.lilypond(myscore.score))