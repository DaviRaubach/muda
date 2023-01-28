import abjad


# class FancyGlissando(abjad.LilyPondLiteral):
#     def __init__(literal: string):
#         self.literal = literal

#     def __call__():
#         return self(literal)


def fancy_glissando(points: list = [(1, 3), (2, 0), (3, 3), (4, 1),
                                    (5, 3.5), (6, 0), (7, 0, 8, 5, 12, 0)]):

    sub_string_list = ""
    for t in points:
        lytup = "("
        for i, n in enumerate(t):
            lytup += (f"{str(n)}")
            if i != len(t) - 1:
                lytup += " "
        lytup += ") "
        sub_string_list += lytup

    string = r"\fancy-gliss" + f" #'({sub_string_list})"
    return abjad.LilyPondLiteral(string)


def slap_tongue():
    return abjad.LilyPondLiteral(r"\slap")


def p_possibile():
    return abjad.Markup(r"\markup { \fontsize #-2 \dynamic p possibile}")
