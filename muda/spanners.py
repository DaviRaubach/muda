import abjad


def dashed_right_arrow_text_spanner(
    selection,
    left: str = "",
    right: str = "",
    left_markup_str: str | bool = False,
    right_markup_str: str | bool = False,
    left_padding: str | None = None,
    right_padding: str | None = None,
):
    """

    :param selection:
    :param left: str:  (Default value = "")
    :param right: str:  (Default value = "")
    :param left_markup_str: str | bool:  (Default value = False)
    :param right_markup_str: str | bool:  (Default value = False)
    :param left_padding: str | None:  (Default value = None)
    :param right_padding: str | None:  (Default value = None)

    """
    left_markup_str = left_markup_str or r"\markup \upright " + left
    right_markup_str = right_markup_str or r"\markup \upright " + right

    start_text_span = abjad.StartTextSpan(
        left_text=abjad.Markup(left_markup_str),
        right_text=abjad.Markup(right_markup_str),
        # right_padding=right_padding,
        
    )

    lit = r"""
        \once \override TextSpanner.bound-details.right.arrow = ##t
        \once \override TextSpanner.dash-fraction = #0.5
        \once \override TextSpanner.dash-period = #1.5
        \once \override TextSpanner.bound-details.right.stencil-align-dir-y = #CENTER
        \once \override TextSpanner.bound-details.left.stencil-align-dir-y = #CENTER
        \once \override TextSpanner.arrow-width = #0.3
        \once \override TextSpanner.bound-details.right-broken.text = " "
        \once \override TextSpanner.bound-details.left-broken.text = " "
        """

        
    if left_padding is not None:
        lit += f"""
        \once \override TextSpanner.bound-details.left.padding = #{left_padding}
        """

    if right_padding is not None:
        lit += f"""
        \once \override TextSpanner.bound-details.right.padding = #{right_padding}
        """

    lit = abjad.LilyPondLiteral(lit)
    abjad.attach(lit, abjad.select.leaf(selection, 0))

    abjad.text_spanner(selection, direction=abjad.UP,
                       start_text_span=start_text_span)
    


def spanner_after(
        material: abjad.Container,
        points_list: list[list[int]],
        markups: list[list[str]],
        padding: list[list[int]] | None = None,
        staff_padding=2,
        denominator=16,
        new_container=True,
        parent_component=None

):

    duration = abjad.get.duration(material)
    total_points = int(duration/abjad.Duration(1, denominator))
    total_list = []
    for _l in points_list:
        total_list += _l
    # total_list = points_list
    _max = max(total_list)
    proportions = [_/_max for _ in total_list]
    points = [int(_ * total_points) for _ in proportions if _ != 1]
    points.append(total_points - 1)
    points = [(_, denominator) for _ in points]
    str_points = [fr"1 * {a}/{b}" for a, b in points]
    str_points = [[a, b] for a, b in zip(str_points[0::2], str_points[1::2])]

    literals = []
    overrides = r"""
        \override TextSpanner.bound-details.right.arrow = ##t
        \override TextSpanner.dash-fraction = #0.5
        \override TextSpanner.dash-period = #1.5
        \override TextSpanner.bound-details.right.stencil-align-dir-y = #CENTER
        \override TextSpanner.bound-details.left.stencil-align-dir-y = #CENTER
        \override TextSpanner.arrow-width = #0.3
        """

    reverts = r"""
        \revert TextSpanner.bound-details.right.arrow
        \revert TextSpanner.dash-fraction
        \revert TextSpanner.dash-period
        \revert TextSpanner.bound-details.right.stencil-align-dir-y
        \revert TextSpanner.bound-details.left.stencil-align-dir-y
        \revert TextSpanner.arrow-width
        """
    if staff_padding:
        overrides += rf" \override TextSpanner.staff-padding = {staff_padding}"
        reverts += r" \revert TextSpanner.staff-padding"

    literals.append(overrides)
    for i, pair in enumerate(str_points):
        start = markups[i][0] if len(markups[i]) > 0 else None
        stop = markups[i][1] if len(markups[i]) > 1 else None

        literals.append(rf"\after {pair[0]}")
        if padding is not None and padding[i][0] != 0:
            literals.append(
                rf"""- \tweak bound-details.left.padding #{padding[i][0]}""")
        if padding is not None and padding[i][1] != 0:
            literals.append(
                rf"""- \tweak bound-details.right.padding #{padding[i][1]}""")

        if start:
            literals.append(
                rf"""- \tweak bound-details.left.text \markup \upright {start}""")
        if stop:
            literals.append(
                rf"""- \tweak bound-details.right.text \markup \upright {stop}""")
        literals.append(r"\startTextSpan")
        literals.append(rf"\after {pair[1]}")
        literals.append(r"""\stopTextSpan""")

    if new_container:
        literals.append(r"{")

    literals = abjad.LilyPondLiteral(literals, site="absolute_before")
    parentage = abjad.get.parentage(material[0])
    # parentage.parent)
    if parent_component is not None and isinstance(parentage.parent, parent_component):
        # pass
        abjad.attach(literals, parentage.parent)
        # print(parentage.parent)
    else:
        # pass
        abjad.attach(literals, material[0])
    # if parent_component is not None and isinstance(parentage.parent, parent_component):
    #     abjad.attach(abjad.LilyPondLiteral(
    #             r"}", site="after"), parentage.parent)
    # else:
    #     abjad.attach(abjad.LilyPondLiteral(
    #             r"}", site="after"), material[-1])
    
    if new_container:
        parentage = abjad.get.parentage(material[-1])
        if parent_component is not None and isinstance(parentage.parent, parent_component):
            abjad.attach(abjad.LilyPondLiteral(
                r"}", site="after"), parentage.parent)
        else:
            abjad.attach(abjad.LilyPondLiteral(
                r"}", site="after"), material[-1])
    # abjad.attach(literals, material[0])

    # if new_container:
    #     abjad.attach(abjad.LilyPondLiteral(
    #         r"}", site="after"), material[-1])

    abjad.attach(abjad.LilyPondLiteral(
        reverts, site="after"), material[-1])
