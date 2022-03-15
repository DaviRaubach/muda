"""Bi-tones guitar chords according to 
Vishnick, Martin Lawrence (2014). A Survey of Extended Techniques on the Classical Six-String Guitar with Appended Studies in New Morphological Notation. (Unpublished Doctoral thesis, City University London)
"""

import abjad

binotes_str6 = {
    -3: abjad.Chord("<a bf,>4"),
    -4: abjad.Chord("<gs b>4"),
    -5 : abjad.Chord("<g dqf>4"),
    -6: abjad.Chord("<fs ds>4"),
    -7: abjad.Chord("<f e>4"),
    -8: abjad.Chord("<e f>4"),
    -9: abjad.Chord("<ds fs>4"),
    -10: abjad.Chord("<d aqf>4"),
    -11: abjad.Chord("<cs a>4"),
    -12: abjad.Chord("<c b>4"),
    -13: abjad.Chord("<b, cs>4"),
    -14: abjad.Chord("<bf, e'>4"),
    -15: abjad.Chord("<a, gf'>4"),
    -16: abjad.Chord("<af, cqf'>4"),
    -17: abjad.Chord("<g, fs'>4")
}

binotes_str5 = {
            2: abjad.Chord("<d ef>4"),
    1: abjad.Chord("<cs e>4"),
    0: abjad.Chord("<c gqf>4"),
    -1: abjad.Chord("<b gqs>4"),
    -2: abjad.Chord("<bf a>4"),
    -3: abjad.Chord("<a bf>4"),
    -4: abjad.Chord("<gs bqs>4"),
    -5: abjad.Chord("<g cqs'>4"),
    -6: abjad.Chord("<fs dqs'>4"),
    -7: abjad.Chord("<f eqs'>4"),
    -8: abjad.Chord("<e gqf'>4"),
    -9: abjad.Chord("<ef a'>4"),
    -10: abjad.Chord("<d cqf'>4"),
    -11: abjad.Chord("<df f'>4"),
    -12: abjad.Chord("<c bqs''>4"),
}
binotes_str4 = {
            7: abjad.Chord("<g' af>4"),
    6: abjad.Chord("<fs' a>4"),
    5: abjad.Chord("<f' cqf'>4"),
    4: abjad.Chord("<e' cqs'>4"),
    3: abjad.Chord("<ef' d'>4"),
    2: abjad.Chord("<d' ef'>4"),
    1: abjad.Chord("<cs' eqs'>4"),
    0: abjad.Chord("<c' fqs'>4"),
    -1: abjad.Chord("<b g'>4"),
    -2: abjad.Chord("<bf a'>4"),
    -3: abjad.Chord("<a bqs'>4"),
    -4: abjad.Chord("<af d''>4"),
    -5: abjad.Chord("<g fqf''>4"),
    -6: abjad.Chord("<gf as''>4"),
    -7: abjad.Chord("<f eqs'''>4"),
}

binotes_str3 = {
    12: abjad.Chord("<c'' df'>4"),
    11: abjad.Chord("<b' d'>4"),
    10: abjad.Chord("<bf' fqf'>4"),
    9: abjad.Chord("<a' g'>4"),
    8: abjad.Chord("<af' af'>4"),
    7: abjad.Chord("<g' aqs'>4"),
    6: abjad.Chord("<fs' cqs''>4"),
    5: abjad.Chord("<f' cqs''>4"),
    4: abjad.Chord("<e' g'>4"),
    3: abjad.Chord("<ef' d''>4"),
    2: abjad.Chord("<d' eqs''>4"),
    1: abjad.Chord("<df' g'''>4"),
    0: abjad.Chord("<c' bqf'''>4"),
    -1: abjad.Chord("<b ds'''>4"),
    -2: abjad.Chord("<bf aqs''''>4"),
}

binotes_str2 = {
    16: abjad.Chord("<e'' f'>4"),
    15: abjad.Chord("<ds'' fs'>4"),
    14: abjad.Chord("<d'' aqf'>4"),
    13: abjad.Chord("<cs'' as'>4"),
    12: abjad.Chord("<c'' b'>4"),
    11: abjad.Chord("<b' c''>4"),
    10: abjad.Chord("<as' dqf''>4"),
    9: abjad.Chord("<a' dqs''>4"),
    8: abjad.Chord("<gs' eqs''>4"),
    7: abjad.Chord("<g' fs''>4"),
    6: abjad.Chord("<fs' aqf''>4"),
    5: abjad.Chord("<f' b''>4"),
    4: abjad.Chord("<e' dqs'''>4"),
    3: abjad.Chord("<ef' g'''>4"),
    2: abjad.Chord("<d' dqf'''''>4"),
}

binotes_str1 = {
    21: abjad.Chord("<a'' bf'>4"),
    20: abjad.Chord("<gs'' b'>4"),
    19: abjad.Chord("<g'' cs''>4"),
    18: abjad.Chord("<fs'' dqs''>4"),
    17: abjad.Chord("<f'' e''>4"),
    16: abjad.Chord("<e' f''>4"),
    15: abjad.Chord("<ds' gqf''>4"),
    14: abjad.Chord("<d' gs''>4"),
    13: abjad.Chord("<cs' a''>4"),
    12: abjad.Chord("<c' b''>4"),
    11: abjad.Chord("<b' dqf''>4"),
    10: abjad.Chord("<bf' e'''>4"),
    9: abjad.Chord("<a' gqs'''>4"),
    8: abjad.Chord("<af' c''''>4"),
    7: abjad.Chord("<g' fs'''''>4"),
}


binotes = {
    6: binotes_str6,
    5: binotes_str5,
    4: binotes_str4,
    3: binotes_str3,
    2: binotes_str2,
    1: binotes_str1,    
}
