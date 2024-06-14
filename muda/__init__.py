from .literals import fancy_glissando, slap_tongue, p_possibile
from .selections import (
    leaves,
    pitched_leaves,
    logical_ties,
    pitched_logical_ties,
    leaf,
    leaf_0,
    leaf_1,
    leaf_2,
    leaf_3,
    leaf_4,
    leaf_5,
    leaf_6,
    leaf_7,
    leaf_8,
    leaf_9,
    leaf_10,
    leaf_r1,
    leaves_get,
)
from .material import (
    Lyrics,
    Material,
    Segment,
    apply_to,
    select_named_containers,
)
from .indicators import (
    best_clef_for_logical_ties,
    any_clef_from_pitches,
    clef_for_logical_ties,
    ottava,
)
from .timespan import (
    TimespanList,
    alternating_timespans,
    make_alternations,
    illustrate_timespans,
)
from .override import (
    hide_engravers_for_text,
    stems_for_text,
    replace_rest_by_skip,
    text_rule_override,
    hide_bar_line,
    hide_bar_line_before,
    hide_last_bar_line,
)
from .score import (
    Instrument,
    Group,
    Score,
    make_group,
)
from .pitch import (
    ftom,
    mtof,
    filter_pitches,
    write_pitches,
    make_art_harmonic_from_target,
    make_nat_harmonic,
    make_possible_nat_harmonics,
    get_harmonic_fundamental,
    art_to_nat_harmonics,
    pitches_in_staff,
    illustrate_pitches_in_staff,
    otoacoustic_derivation,
    permut_thirds,
    ring_modulation,
    new_ring_modulation,
    transpose_outside_pitches,
    art_harmonic_for_longer_notes,
    art_harmonics_sounding_pitch,
    transpose_note_before_chord_to_the_same_octave,
    macro_pitches,
    outline_pitches,
)
from .functions import (
    operation_in_nested_lists,
    make_measures,
    make_skips,
    rewrite_meter,
    auto_change,
    voice_number,
)
from .rhythm import (
    AnnotatedDuration,
    silence_and_rhythm_maker,
    rest_maker,
    note_maker,
    make_sync_alternations,
    make_in_out_alternations,
    rmaker,
    delete,
)
from .spanners import (
    dashed_right_arrow_text_spanner,
    spanner_after,
)

from .attach import (
    attach_to_leaves,
    attach_to_logical_tie,
)
from .dynamics import (
    dynamics,
    make_dynamics,
    dynamics_after,
    make_velocity,
    make_arc_velocities,
    # Velocity
)

from .select import (
    select_contiguous_containers_by_name,
    select_not_contiguous_containers_by_name,
    select_contiguous_materials,
    select_not_contiguous_materials,
    call_function_on_leaf_in_selection,
)

from .markups import markup

# import time

# startTime = time.time()


# from .analysis import IracemaAnalysis

# from .tests import run_tests

# from .aperghis_example import aperghis_example


# elapsed_time = round(time.time() - startTime, 2)
# print('\033[95m', "Initialize Muda took",
# elapsed_time, "seconds\033[0;0m")
