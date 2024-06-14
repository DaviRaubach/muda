import abjad
from .material import Material

s = abjad.select


def glcontext_hide_time_signature(glcontext: Material):
    glcontext.attach(r" \omit TimeSignature", lambda _: s.leaf(_, 0))
    glcontext.attach(
        abjad.LilyPondLiteral(r" \undo \omit TimeSignature", "after"),
        lambda _: s.leaf(_, -1),
    )


def text_rule_override_old(material: Material):
    hide_rule = [
        # r" \voiceTwo",
        # r" \stemDown",
        r" \override Voice.NoteHead.stencil = ##f",
        r" \override Voice.Rest.stencil = ##f",
        r" \override Voice.Stem.stencil = ##f",
        r" \override Voice.Flag.stencil = ##f",
        r" \omit TupletNumber",
        r" \override Voice.TupletBracket.stencil = ##f",
        r" \override Voice.Beam.stencil = ##f",
        r" \omit Voice.Accidental",
        r" \override LyricText.self-alignment-X = #LEFT",
    ]

    material.attach(abjad.LilyPondLiteral(hide_rule), lambda _: s.leaf(_, 0))

    revert_rule = [
        # r" \voiceTwo",
        # r" \stemDown",
        r" \revert Voice.NoteHead.stencil",
        r" \revert Voice.Rest.stencil",
        r" \revert Voice.Stem.stencil",
        r" \revert Voice.Flag.stencil",
        r" \undo \omit Voice.TupletNumber",
        r" \revert Voice.TupletBracket.stencil",
        r" \revert Voice.Beam.stencil",
        r" \undo \omit Voice.Accidental",
    ]

    material.attach(
        abjad.LilyPondLiteral(revert_rule, "after"), lambda _: s.leaf(_, -1)
    )


def text_rule_override(selection):
    # voice colisions
    abjad.attach(
        abjad.LilyPondLiteral(
            [
                r" \hideNotes",
                r" \mergeDifferentlyHeadedOn \mergeDifferentlyDottedOn \shiftOn",
            ]
        ),
        abjad.select.leaf(selection, 0),
    )

    hide_rule = [
        # r" \voiceTwo",
        # r" \stemDown",
        # r" \hide Voice.NoteHead",
        # r" \override Voice.Rest.stencil = ##f",
        # r" \override Voice.NoteHead.no_ledgers = ##t",
        # r" \override Voice.Stem.stencil = ##f",
        # r" \override Voice.Flag.stencil = ##f",
        r" \omit Voice.TupletNumber",
        # r" \omit Voice.Dots",
        r" \override Voice.TupletBracket.stencil = ##f",
        # r" \override Voice.Beam.stencil = ##f",
        r" \override Voice.Tie.stencil = ##f",
        # r" \omit Voice.Accidental",
        # r" \override LyricText.self-alignment-X = #LEFT",
    ]

    abjad.attach(
        abjad.LilyPondLiteral(hide_rule), abjad.select.leaf(selection, 0)
    )

    revert_rule = [
        # r" \voiceTwo",
        # r" \stemDown",
        # r" \undo \hide Voice.NoteHead",
        # r" \revert Voice.NoteHead.no_ledgers",
        # r" \revert Voice.Rest.stencil",
        # r" \revert Voice.Stem.stencil",
        # r" \revert Voice.Flag.stencil",
        # r" \revert Voice.Dots.stencil",
        r" \undo \omit Voice.TupletNumber",
        # r" \undo \omit Voice.Dots",
        r" \revert Voice.TupletBracket.stencil",
        # r" \revert Voice.Beam.stencil",
        r" \revert Voice.Tie.stencil",
        # r" \undo \omit Voice.Accidental",
    ]

    abjad.attach(
        abjad.LilyPondLiteral(
            [
                r" \unHideNotes",
                r" \mergeDifferentlyHeadedOff \mergeDifferentlyDottedOff \shiftOff",
            ],
            "after",
        ),
        abjad.select.leaf(selection, -1),
    )

    abjad.attach(
        abjad.LilyPondLiteral(revert_rule, "after"),
        abjad.select.leaf(selection, -1),
    )


# def hide_engravers_for_text(material: Material):
#     # voice colisions
#     material.attach(
#         r" \mergeDifferentlyHeadedOn \mergeDifferentlyDottedOn \shiftOn",
#         lambda _: s.leaf(_, 0)
#     )

#     overrides = [
#         # r" \override Voice.Stem.length = #15",

#         # r" \override Voice.Beam.stencil = #ly:text-interface::print",
#         # r' \override Voice.Beam.text = " "',
#         r" \omit Voice.Flag",
#         r" \omit StaffGroup.SpanBar",
#         r" \hide Voice.Beam",
#         r" \omit Voice.TupletNumber",
#         r" \omit Voice.TupletBracket",
#         r" \omit Voice.Dots",
#         # r" \override Stem.stem-begin-position = 2"
#         # r" \override Voice.TextSpanner.staff-padding = # 10",
#         # r" \textLengthOn",
#         # r" \override TextScript.outside-staff-priority = #1",
#         # r" \override TextScript.self-alignment-X = #CENTER",
#         # r" \override TextScript.Y-offset = # -6",
#     ]
#     material.attach(abjad.LilyPondLiteral(
#         overrides), lambda _: s.leaf(_, 0))
#     print(s.leaf(material.container, 0))
#     material.attach(abjad.LilyPondLiteral(
#         r" \omit Staff.BarLine", "after"), lambda _: s.leaf(_, 0))
#     # REVERT
#     material.attach(
#         abjad.LilyPondLiteral(
#             r" \mergeDifferentlyHeadedOff \mergeDifferentlyDottedOff \shiftOff",
#             'after'
#         ),
#         lambda _: s.leaf(_, -1)
#     )

#     revert = [
#         r" \undo \omit Staff.BarLine",
#         r" \revert Voice.Beam.stencil",
#         r' \revert Voice.Beam.text',
#         r" \undo \omit Voice.Flag",
#         r" \undo \omit Staff.SpanBar",
#         r" \undo \hide Voice.Beam",
#         r" \undo \omit Voice.TupletNumber",
#         r" \undo \omit Voice.TupletBracket",
#         r" \undo \omit Voice.Dots",
#         # r" \revert Stem.stem-begin-position
#         # r" \override Voice.TextSpanner.staff-padding
#         # r" \textLengthOn",
#         # r" \override TextScript.outside-staff-priority = #1",
#         # r" \override TextScript.self-alignment-X = #CENTER",
#         # r" \override TextScript.Y-offset = # -6",
#     ]
#     material.attach(abjad.LilyPondLiteral(
#         revert, 'after'), lambda _: s.leaf(_, -1))


#     # material.attach(
#     #     abjad.BarLine("||"),
#     #     lambda _: abjad.select.leaf(_, -1))
def hide_bar_line(selection):
    abjad.attach(
        abjad.LilyPondLiteral(
            r' \bar " " \omit BarLine \omit StaffGroup.SpanBar', "after"
        ),
        selection[0],
    )

    abjad.attach(
        abjad.LilyPondLiteral(
            r' \bar " " \undo \omit BarLine \undo \omit StaffGroup.SpanBar',
            "after",
        ),
        selection[-1],
    )


def hide_bar_line_before(selection):
    abjad.attach(
        abjad.LilyPondLiteral(
            r' \bar "" \omit BarLine \omit StaffGroup.SpanBar'
        ),
        selection[0],
    )

    abjad.attach(
        abjad.LilyPondLiteral(
            r" \undo \omit BarLine \undo \omit StaffGroup.SpanBar", "after"
        ),
        selection[-1],
    )


def hide_last_bar_line(selection):
    abjad.attach(
        abjad.LilyPondLiteral(
            r" \omit Staff.BarLine \omit StaffGroup.SpanBar", "after"
        ),
        selection[0],
    )

    abjad.attach(
        abjad.LilyPondLiteral(
            r" \undo \omit Staff.BarLine \undo \omit StaffGroup.SpanBar",
            "after",
        ),
        selection[-1],
    )


def hide_engravers_for_text(selection, no_bar_lines=False):
    # voice colisions
    abjad.attach(
        r" \mergeDifferentlyHeadedOn \mergeDifferentlyDottedOn \shiftOn",
        selection[0],
    )
    if no_bar_lines:
        abjad.attach(
            abjad.LilyPondLiteral(
                r" \omit Staff.BarLine \omit StaffGroup.SpanBar"
            ),
            selection[0],
        )

    overrides = [
        # r" \override Voice.Stem.length = #15",
        # r" \override Voice.Beam.stencil = #ly:text-interface::print",
        # r' \override Voice.Beam.text = " "',
        r" \omit Voice.Flag",
        r" \omit StaffGroup.SpanBar",
        r" \hide Voice.Beam",
        r" \omit Voice.Rest",
        r" \omit Voice.TupletNumber",
        r" \omit Voice.TupletBracket",
        r" \omit Voice.Dots",
        # r" \override Stem.stem-begin-position = 2"
        # r" \override Voice.TextSpanner.staff-padding = # 10",
        # r" \textLengthOn",
        # r" \override TextScript.outside-staff-priority = #1",
        # r" \override TextScript.self-alignment-X = #CENTER",
        # r" \override TextScript.Y-offset = # -6",
    ]
    abjad.attach(abjad.LilyPondLiteral(overrides), selection[0])
    # print(s.leaf(material.container, 0))
    # abjad.attach(abjad.LilyPondLiteral(
    #     r" \omit Staff.BarLine", "after"), selection[0])
    # REVERT
    rev = abjad.LilyPondLiteral(
        r" \mergeDifferentlyHeadedOff \mergeDifferentlyDottedOff \shiftOff",
        site="after",
    )

    abjad.attach(rev, selection[-1])

    revert = [
        # r" \undo \omit Staff.BarLine",
        r" \revert Voice.Beam.stencil",
        r" \revert Voice.Beam.text",
        r" \undo \omit Voice.Flag",
        r" \undo \omit Staff.SpanBar",
        r" \undo \hide Voice.Beam",
        r" \undo \omit Voice.Rest",
        r" \undo \omit Voice.TupletNumber",
        r" \undo \omit Voice.TupletBracket",
        r" \undo \omit Voice.Dots",
        # r" \revert Stem.stem-begin-position
        # r" \override Voice.TextSpanner.staff-padding
        # r" \textLengthOn",
        # r" \override TextScript.outside-staff-priority = #1",
        # r" \override TextScript.self-alignment-X = #CENTER",
        # r" \override TextScript.Y-offset = # -6",
    ]
    rev3 = abjad.LilyPondLiteral(revert, site="after")
    abjad.attach(rev3, selection[-1])

    if no_bar_lines:
        rev2 = abjad.LilyPondLiteral(
            [r" \undo \omit Staff.BarLine", r" \undo \omit StaffGroup.SpanBar"],
            site="after",
        )

        abjad.attach(
            rev2,
            selection[-1],
        )

    # material.attach(
    #     abjad.BarLine("||"),
    #     lambda _: abjad.select.leaf(_, -1))


def stems_for_text(material: Material, pivot):
    material.attach(
        r" \stemUp \override Beam.positions = #'(5 . 5)", lambda _: s.leaf(_, 0)
    )
    lts = s.logical_ties(material.container, pitched=True)
    # inverte a direção do stem para notas muito agudas
    # beam em cada nota para alinhar o final do stem no limite do text
    for lt in lts:
        if lt[0].written_pitch > abjad.NamedPitch(pivot):
            string = abjad.LilyPondLiteral(
                r" \once \override Stem.direction = #DOWN"
            )
            for note in lt:
                abjad.attach(string, note)
        else:
            for note in lt:
                abjad.attach(abjad.LilyPondLiteral(r"[] ", site="after"), note)


def voice_overrides(material: Material):
    material.attach(
        r" \once \override Voice.NoteHead.no-ledgers = ##t",
        lambda _: s.leaves(_, pitched=True),
    )
    material.attach(
        abjad.Markup(r'\markup {"voice" \italic "ad libitum"}'),
        lambda _: s.leaf(_, 0, pitched=True),
        direction=abjad.UP,
    )

    material.attach(r" \stemDown \tieDown", lambda _: s.leaf(_, 0))


# def replace_rest_by_skip_old(mat: Material):
#     rests = abjad.select.components(mat.container, abjad.Rest)
#     for rest in rests:
#         abjad.mutate.replace(rest, abjad.Skip(rest.written_duration))


def replace_rest_by_skip(selection):
    rests = abjad.select.components(selection, abjad.Rest)
    for rest in rests:
        abjad.mutate.replace(rest, abjad.Skip(rest.written_duration))
