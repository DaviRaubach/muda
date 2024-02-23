import abjad


def attach_to_logical_tie(attachable, logical_tie: abjad.LogicalTie, attach_to_leaf_indices: list):
    for i in attach_to_leaf_indices:
        abjad.attach(attachable, logical_tie[i])


def attach_to_leaves(attachables: list, leaves: list[abjad.Leaf]):
    for att, leaf in zip(attachables, leaves):
        if att is not None:
            abjad.attach(att, leaf)
