"""
Visualization utilities for Timespan and TimespanList with annotations.
"""

import abjad


def make_annotated_timespan_markup(
    timespans,
    key="annotation",
    range_=None,
    scale=None,
    draw_offsets=True,
    sortkey=None,
    colored=False,
    line_width=0.2,
):
    """
    Creates a LilyPond markup where all timespans are drawn on a single line,
    with annotations displayed above each timespan segment.

    Args:
        timespans (TimespanList): The timespans to visualize.
        key (str): Attribute name to use as annotation (default "annotation").
        range_ (tuple | Timespan | None): Range to display.
        scale (float | None): Scaling factor for the drawing.
        draw_offsets (bool): Whether to draw offset markers.
        sortkey (callable | None): Function to sort timespans before drawing.
        colored (bool): Whether to color annotations and timespans by character.
                        Each unique character in annotations gets a distinct color.
        line_width (float): Width of the timespan lines (default 0.2).
                            The offset markers will use half this width.

    Returns:
        Markup: A LilyPond markup object.
    """
    if not timespans:
        return abjad.Markup(r"\markup \null")

    # Determine display range
    if isinstance(range_, abjad.Timespan):
        minimum, maximum = range_.start_offset, range_.stop_offset
    elif range_ is not None:
        minimum, maximum = range_
    else:
        minimum, maximum = timespans.start_offset, timespans.stop_offset

    if scale is None:
        scale = 1.0
    assert 0 < scale

    minimum_float = float(abjad.Offset(minimum))
    maximum_float = float(abjad.Offset(maximum))
    postscript_scale = 150.0 / (maximum_float - minimum_float)
    postscript_scale *= float(scale)
    postscript_x_offset = (minimum_float * postscript_scale) - 1

    # Sort timespans if needed
    items = list(timespans)
    if sortkey is not None:
        items.sort(key=sortkey)
    else:
        items.sort()

    # Prepare color palette (RGB values for distinct, legible colors on white background)
    color_palette = [
        (0.0, 0.0, 1.0),  # blue
        (1.0, 0.0, 0.0),  # red
        (0.0, 0.5, 0.0),  # dark green
        (0.5, 0.0, 0.5),  # purple
        (0.0, 0.75, 0.75),  # cyan
        (0.75, 0.75, 0.0),  # olive
        (1.0, 0.5, 0.0),  # orange
        (0.5, 0.25, 0.0),  # brown
        (0.75, 0.0, 0.75),  # magenta
        (0.0, 0.0, 0.5),  # dark blue
        (0.5, 0.5, 0.5),  # gray
        (0.0, 0.5, 0.5),  # teal
    ]

    # Build character-to-color mapping if colored is True
    char_to_color = {}
    if colored:
        unique_chars = set()
        for timespan in items:
            annotation = getattr(timespan, key, None)
            if annotation is not None:
                for char in str(annotation):
                    unique_chars.add(char)
        # Assign colors to characters
        for i, char in enumerate(sorted(unique_chars)):
            color_idx = i % len(color_palette)
            char_to_color[char] = color_palette[color_idx]

    # Prepare postscript commands for the timespan line
    postscript_strings = []
    # We'll draw all timespans on a single horizontal line at y = 0.5
    postscript_y_offset = 0.5

    # Collect offsets for vertical markers
    offset_mapping = {}

    for timespan in items:
        offset_mapping[timespan.start_offset] = 0
        offset_mapping[timespan.stop_offset] = 0

        # Determine color for this timespan based on first character of annotation
        if colored:
            annotation = getattr(timespan, key, None)
            if annotation is not None and str(annotation):
                first_char = str(annotation)[0]
                if first_char in char_to_color:
                    r, g, b = char_to_color[first_char]
                    postscript_strings.append(f"{r} {g} {b} setrgbcolor")
            else:
                # Default to black if no annotation
                postscript_strings.append("0 0 0 setrgbcolor")
            # Set line width for colored mode (before drawing the timespan)
            postscript_strings.append(f"{line_width} setlinewidth")
        else:
            # Default linewidth when not colored (set once at the beginning)
            pass

        strings = timespan._as_postscript(
            postscript_x_offset, postscript_y_offset, postscript_scale
        )
        postscript_strings.extend(strings)

        # Reset to black for next timespan if colored, to avoid affecting other elements
        if colored:
            postscript_strings.append("0 0 0 setrgbcolor")

    # Ensure linewidth is set if not colored (when colored, linewidth is set per timespan)
    if not colored:
        # Insert at beginning if not already present
        if not any("setlinewidth" in s for s in postscript_strings):
            postscript_strings.insert(0, f"{line_width} setlinewidth")

    # Add dashed vertical lines for offsets if requested
    if draw_offsets:
        offset_line_width = line_width / 2.0
        postscript_strings.extend(
            [
                f"{offset_line_width} setlinewidth",
                "[ 0.1 0.2 ] 0 setdash",
            ]
        )
        for offset in sorted(offset_mapping):
            x_offset = float(offset) * postscript_scale
            x_offset -= postscript_x_offset
            postscript_strings.extend(
                [
                    f"{_fpa(x_offset)} 2.5 moveto",
                    f"{_fpa(x_offset)} 0.0 lineto",
                    "stroke",
                ]
            )
        # Reset dash
        postscript_strings.append("[] 0 setdash")

    # Add a tiny gray line to ensure bounding box
    postscript_strings.extend(
        [
            "0 0 moveto",
            "0.99 setgray",
            "0 0.01 rlineto",
            "stroke",
        ]
    )

    postscript = "\n".join(postscript_strings)

    # Build the overlay with offset fractions
    fraction_strings = []
    for offset in sorted(offset_mapping):
        offset = abjad.Offset(offset)
        numerator, denominator = offset.numerator, offset.denominator
        x_translation = float(offset) * postscript_scale
        x_translation -= postscript_x_offset
        fraction_strings.append(rf"\translate #'({x_translation} . 1)")
        fraction_strings.append(
            rf"\sans \fontsize #-5 \center-align \fraction {numerator} {denominator}"
        )

    # Build annotation texts
    annotation_strings = []
    for timespan in items:
        annotation = getattr(timespan, key, None)
        if annotation is None:
            continue
        # Center the annotation above the timespan segment
        start_x = (
            float(timespan.start_offset) * postscript_scale
            - postscript_x_offset
        )
        stop_x = (
            float(timespan.stop_offset) * postscript_scale - postscript_x_offset
        )
        center_x = (start_x + stop_x) / 2.0
        # Place text at y = 3.0 (above the line)
        annotation_str = str(annotation)
        # Apply color if requested
        if colored and annotation_str:
            # Use color of first character for the entire annotation
            first_char = annotation_str[0]
            if first_char in char_to_color:
                r, g, b = char_to_color[first_char]
                # Convert to LilyPond color command
                color_cmd = rf"\with-color #(rgb-color {r} {g} {b})"
                annotation_strings.append(rf"\translate #'({center_x} . 3.0)")
                annotation_strings.append(
                    rf"{color_cmd} \sans \fontsize #-3 \center-align {repr(annotation_str)}"
                )
            else:
                annotation_strings.append(rf"\translate #'({center_x} . 3.0)")
                annotation_strings.append(
                    rf"\sans \fontsize #-3 \center-align {repr(annotation_str)}"
                )
        else:
            annotation_strings.append(rf"\translate #'({center_x} . 3.0)")
            annotation_strings.append(
                rf"\sans \fontsize #-3 \center-align {repr(annotation_str)}"
            )

    # Combine fractions and annotations into a single overlay
    overlay_items = []
    if fraction_strings:
        overlay_items.append("\n".join(fraction_strings))
    if annotation_strings:
        overlay_items.append("\n".join(annotation_strings))

    overlay_content = "\n".join(overlay_items)
    if overlay_content:
        fraction_and_annotation_block = f"\\overlay {{\n{overlay_content}\n}}"
    else:
        fraction_and_annotation_block = ""

    # Determine bounding box
    x_extent = (
        float(timespans.stop_offset) * postscript_scale + postscript_x_offset
    )
    y_extent = 3.5  # enough space for annotations above
    lines_string = rf"\pad-to-box #'(0 . {x_extent}) #'(0 . {y_extent})"
    lines_string += f'\n\\postscript #"\n{postscript}"'

    # Final column structure
    if fraction_and_annotation_block:
        final_string = f"\\markup {{ \\column {{\n{fraction_and_annotation_block}\n{lines_string}\n}} }}"
    else:
        final_string = f"\\markup {{ \\column {{\n{lines_string}\n}} }}"

    return abjad.Markup(final_string)


def _format_postscript_argument(argument):
    """Helper to format PostScript arguments (copied from timespan.py)."""
    if isinstance(argument, str):
        if argument.startswith("/"):
            return argument
        return f"({argument})"
    elif isinstance(argument, (list, tuple)):
        if not argument:
            return "[ ]"
        string = " ".join(_format_postscript_argument(_) for _ in argument)
        return f"[ {string} ]"
    elif isinstance(argument, bool):
        return str(argument).lower()
    elif isinstance(argument, (int, float)):
        argument = abjad.math.integer_equivalent_number_to_integer(argument)
        return str(argument)
    return str(argument)


_fpa = _format_postscript_argument
