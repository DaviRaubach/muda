import abjad
# from abjadext import rmakers
# import muda


# maker = rmakers.stack(rmakers.note()),
# annotated_divisions=[
#         muda.AnnotatedDuration(1, 4),
#         muda.AnnotatedDuration((1, 4), annotation="Rest"),
#         muda.AnnotatedDuration(1, 4),
#         muda.AnnotatedDuration(1, 4),
#         muda.AnnotatedDuration((1, 4), annotation="Rest"),
#         muda.AnnotatedDuration(1, 4),
#         muda.AnnotatedDuration(1, 4),
#         muda.AnnotatedDuration((1, 4), annotation="Rest"),
#         ]

# # print(divisionsu)
# print(maker())
# divisions = [(1, 4)]
# for i in annotated_divisions:
#     sele = maker([i])

# print(muda.AnnotatedDuration(1, 2))
# print(abjad.Duration(1, 2))

# dur = abjad.Duration(8, 4)
# frac = abjad.NonreducedFraction(2, 4)
# div = dur / frac
# mult = dur * frac
# mod = dur % frac
# print("div", div)
# print("mult", mult)
# print("mod", mod)


# new_dur = abjad.Duration(mult)
# print(new_dur.pair)
# dur = abjad.Duration(23, 8)
# print(dur % abjad.Duration(2, 4))
# timespan = abjad.Timespan((0, 1), (8, 1))
# for x in timespan.divide_by_ratio(4):
#     print(x)

# dur1 = abjad.Duration(25, 8)
# dur2 = abjad.Duration(1, 8)

# print(dur1 - dur2)

# ts = abjad.Timespan(1, 4)
# dur3 = abjad.Duration(dur1 + dur2)
# du = dur3.pair
# print(ts.set_duration(dur1 + dur2))
# print(ts)

staff = abjad.Staff("s1 s1 s1")
selection = abjad.select(staff).leaves(pitched=False)
abjad.attach(abjad.MetronomeMark((1, 4), (45, 54), "Lento"), selection[0])
print(abjad.lilypond(staff))
