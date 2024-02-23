import abjad
from .select import call_function_on_leaf_in_selection


def markup(string: str, selection, n=0, all_leaves=False, direction=abjad.UP):
    """Attach markup on leaf"""
    call_function_on_leaf_in_selection(
        selection,
        n=n,
        function=lambda _: abjad.attach(abjad.Markup(rf"\markup {string}"), _, direction=direction),
        all_leaves=all_leaves,
    )
