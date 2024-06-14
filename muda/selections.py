import abjad

# class Selection(abjad.Selection):
#      r"""Select pitched leaves"""
#      def __init__(self, items=None, previous=None):
#          abjad.Selection.__init__(self, items=None, previous=None)

#      def __call__(self, argument):
#          items = argument
#          return self

# def pitched_leaves(argument):
#     leaves = abjad.Selection(argument).leaves(pitched=True)
#     return leaves

# def leaves(argument):
#     leaves = abjad.Selection(argument).leaves()
#     return leaves

# def pitched_logical_ties(argument):
#     lt = abjad.Selection(argument).logical_ties(pitched=True)
#     return lt

# def logical_ties(argument):
#     lt = abjad.Selection(argument).logical_ties()
#     return lt


def leaves(_):
    return abjad.select.leaves(_)


def pitched_leaves(_):
    return abjad.select.leaves(_, pitched=True)


def logical_ties(_):
    return abjad.select.logical_ties(_)


def pitched_logical_ties(_):
    return abjad.select.logical_ties(_, pitched=True)


def leaf(argument, n):
    return abjad.select.leaf(argument, n)


def leaf_0(_):
    return abjad.select.leaf(_, 0)


def leaf_1(_):
    return abjad.select.leaf(_, 1)


def leaf_2(_):
    return abjad.select.leaf(_, 2)


def leaf_3(_):
    return abjad.select.leaf(_, 3)


def leaf_4(_):
    return abjad.select.leaf(_, 4)


def leaf_5(_):
    return abjad.select.leaf(_, 5)


def leaf_6(_):
    return abjad.select.leaf(_, 6)


def leaf_7(_):
    return abjad.select.leaf(_, 7)


def leaf_8(_):
    return abjad.select.leaf(_, 8)


def leaf_9(_):
    return abjad.select.leaf(_, 9)


def leaf_10(_):
    return abjad.select.leaf(_, 10)


def leaf_r1(_):
    return abjad.select.leaf(_, -1)


def leaves_get(container, indices: list, periods: int = None):
    sel = abjad.select.leaves(container)
    if periods is None:
        sel = abjad.select.get(sel, indices)
    else:
        sel = abjad.select.get(sel, indices, periods)
    return sel
