"""Tests.

Tests to keep muda library consistent.
"""
import muda
import abjad
from abjadext import rmakers
s = abjad.select


def guitar_bitones_test():
    print("Running guitar bitones test using ``muda.Material.guitar_bitones()`` method.")
    timespans = muda.alternating_timespans(
        [[1, 1], [1, 1], [1, 1]], 4, ["matA", "matB"])
    durations = timespans.annotated_durations(subdivision=(2, 4))
    makers = {
        "matA": rmakers.stack(rmakers.note()),
        "matB": rmakers.stack(rmakers.note())
    }
    mat = muda.Material("A")
    mat.alternating_materials(durations, makers)
    pitches = {
        "matA": abjad.PitchSegment("fs'"),
        "matB": abjad.PitchSegment("ds'"),
    }
    def pitched_leaves(_): return abjad.select.leaves(_)
    mat.write_pitches_by_name(pitches)
    mat.attach(abjad.StringNumber([2]), pitched_leaves, "matA")
    mat.attach(abjad.StringNumber([3]), pitched_leaves, "matB")
    mat.guitar_bitones(pitched_leaves, "matA", hammering=True)
    mat.print()


def tuplet_number_tweak_test():
    print("Running format tuplets test using ``muda.Material.tuplet_number_tweak()`` method.")
    tup = abjad.Tuplet((2, 3), "c'8 d'8 d'8 d'8 d'16 d'16 e'8")
    cont = abjad.Container()
    cont.append(tup)
    muda.Material.tuplet_number_tweak(cont)
    print(abjad.lilypond(cont))


def material_test():
    print("Running material test using ``muda.Material()`` class and its methods.")
    timespans = muda.alternating_timespans(
        [[1, 1], [1, 1], [1, 1]], 2, ["matA", "matB"])
    durations = timespans.annotated_durations(subdivision=(2, 4))
    makers = {
        "matA": rmakers.stack(
            rmakers.talea([-1, 2, -1], 16), rmakers.extract_trivial()
        ),

        "matB": rmakers.stack(
            rmakers.talea([1, 1, 1, 1], 16), rmakers.extract_trivial()
        ),
    }
    mat = muda.Material("A")
    mat.alternating_materials(durations, makers)
    pitches = {
        "matA": abjad.PitchSegment([6]),
        "matB": abjad.PitchSegment([3]),
    }
    mat.write_pitches_by_name(pitches)
    mat.annotate_material_names(["matA", "matB"])
    print(abjad.lilypond(mat.container))


timespans = muda.alternating_timespans(
    [[1, 1], [1, 1], [1, 1]], 2, ["matA", "matB"])
durations = timespans.annotated_durations(subdivision=(2, 4))
makers = {
    "matA": rmakers.stack(
        rmakers.talea([-1, 2, -1], 16), rmakers.extract_trivial()
    ),

    "matB": rmakers.stack(
        rmakers.talea([1, 1, 1, -1], 16), rmakers.extract_trivial()
    ),
}
mat = muda.Material("A")
mat.alternating_materials(durations, makers)
mat.rewrite_meter([(1, 4)]*8)


def attach_test():
    mat.attach(abjad.Articulation("staccato"),
               lambda _: s.logical_ties(_, pitched=True),
               "matA")
    mat.attach(abjad.Articulation("marcato"),
               lambda _: s.get(s.leaves(_, pitched=True), [0, 1], 10),
               "matB")
    print(abjad.lilypond(mat.container))


def select_test():
    print(abjad.lilypond(mat.container))
    selection = mat.select("matA", submaterials=True)
    print(selection)


def select_material_test():
    print(abjad.lilypond(mat.container))
    selection = mat.select_material(
        mat.container, "matA", submaterials=True)
    print(selection)


def run_tests():
    # guitar_bitones_test()
    # tuplet_number_tweak_test()
    # material_test()
    # attach_test()
    # select_test()
    select_material_test()


if __name__ == '__main__':
    run_tests()
