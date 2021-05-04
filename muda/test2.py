# import abjad
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

# staff = abjad.Staff("s1 s1 s1")
# selection = abjad.select(staff).leaves(pitched=False)
# abjad.attach(abjad.MetronomeMark((1, 4), (45, 54), "Lento"), selection[0])
# print(abjad.lilypond(staff))

# MICROTONES
# import evans
# from abjadext import microtones
# import abjad

# l = [0, 1.111, 4.5, 2.23, 6.4, 7.3, 7.15]
# l = [evans.to_nearest_eighth_tone(_, frac=True) for _ in l]
# notes = [abjad.Note("c'4") for item in l]
# for note, step in zip(notes, l):
#     microtones.apply_alteration(note.note_head, step)
# staff = abjad.Staff(notes)
# score = abjad.Score([staff])
# # moment = abjad.SchemeMoment((1, 25))
# # abjad.setting(score).proportional_notation_duration = moment
# lilypond_file = abjad.LilyPondFile(
#     items=[score, abjad.Block(name="layout")],
#     includes=[
#         "/Users/Davi/github/evans/docs/source/_stylesheets/default.ily",
#         "abjad.ily",
#         "/Users/Davi/github/abjad-ext-microtones/abjadext/microtones/lilypond/ekmelos-edo-accidental-markups.ily ",
#     ],
#     global_staff_size=16,
# )
# style = '"dodecaphonic"'
# lilypond_file.layout_block.items.append(fr"\accidentalStyle dodecaphonic")
# abjad.show(lilypond_file)


# import abjad

# parent = abjad.Container()
# child1 = abjad.Container("c'4", tag=abjad.Tag("mat01"))
# child2 = abjad.Container("d'8", tag=abjad.Tag("mat02"))

# parent.append(child1)
# parent.append(child2)
# selection = abjad.select(parent).components(abjad.Container)
# print(selection)
# for i, cont in enumerate(selection):
#     if i == 0:
#         pass
#     else:
#         print(cont.tag)
#         print(cont)

# import muda
# dur = muda.AnnotatedDuration((1, 4), annotation="this")
# print(dur.annotation)


import abjad
import muda  # my library
from abjadext import rmakers

rmaker01 = rmakers.stack(
    rmakers.talea([2, -1], 16, extra_counts=[1]),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat01"),)
rmaker02 = rmakers.stack(
    rmakers.talea([1, -2], 16, extra_counts=[1]),
    rmakers.extract_trivial(),
    tag=abjad.Tag("mat02"),)
makers = [rmaker01, rmaker02]

annotated_divisions = [
    muda.AnnotatedDuration((1, 2), annotation="mat01"),
    muda.AnnotatedDuration((1, 2), annotation="mat02")
]

container = abjad.Container()
for division in annotated_divisions:
    for maker in makers:
        if maker.tag.string == division.annotation:
            selection = maker([division])
            container.append(abjad.Container(selection, tag=maker.tag))
lilypond_file = abjad.LilyPondFile(items=[container])
abjad.persist.as_ly(lilypond_file, "example.ly")
print(abjad.lilypond(lilypond_file))
