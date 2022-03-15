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

leaves = lambda _: abjad.select.leaves(_)
pitched_leaves = lambda _: abjad.select.leaves(_, pitched=True)
logical_ties = lambda _: abjad.select.logical_ties(_)
pitched_logical_ties = lambda _: abjad.select.logical_ties(_, pitched=True)
leaf = lambda argument, n: abjad.select.leaf(argument, n)
leaf_0 = lambda _: abjad.select.leaf(_, 0)
leaf_1 = lambda _: abjad.select.leaf(_, 1)
leaf_2 = lambda _: abjad.select.leaf(_, 2)
leaf_3 = lambda _: abjad.select.leaf(_, 3)
leaf_4 = lambda _: abjad.select.leaf(_, 4)
leaf_5 = lambda _: abjad.select.leaf(_, 5)
leaf_6 = lambda _: abjad.select.leaf(_, 6)
leaf_7 = lambda _: abjad.select.leaf(_, 7)
leaf_8 = lambda _: abjad.select.leaf(_, 8)
leaf_9 = lambda _: abjad.select.leaf(_, 9)
leaf_10 = lambda _: abjad.select.leaf(_, 10)


leaf_r1 = lambda _: abjad.select.leaf(_, -1)

def leaves_get(container, indices: list, periods: int = None):
    sel = abjad.select.leaves(container)
    if periods is None:
        sel = abjad.select.get(sel, indices)
    else:
        sel = abjad.select.get(sel, indices, periods)
    return sel
