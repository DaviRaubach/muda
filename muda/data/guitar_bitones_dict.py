"""Bi-tones guitar chords according to 
Vishnick, Martin Lawrence 2014. A Survey of Extended Techniques on the Classical Six-String Guitar with Appended Studies in New Morphological Notation. (Unpublished Doctoral thesis, City University London)
"""

import abjad

binotes_str6 = {
    -3: ["a", "bf,"],
    -4: ["gs", "b"],
    -5: ["g", "dqf"],
    -6: ["fs", "ds"],
    -7: ["f", "e"],
    -8: ["e", "f"],
    -9: ["ds", "fs"],
    -10: ["d", "aqf"],
    -11: ["cs", "a"],
    -12: ["c", "b"],
    -13: ["b,", "cs"],
    -14: ["bf,", "e'"],
    -15: ["a,", "gf'"],
    -16: ["af,", "cqf'"],
    -17: ["g,", "fs'"]
}

binotes_str5 = {
    2: ["d", "ef"],
    1: ["cs", "e"],
    0: ["c", "gqf"],
    -1: ["b", "gqs"],
    -2: ["bf", "a"],
    -3: ["a", "bf"],
    -4: ["gs", "bqs"],
    -5: ["g", "cqs'"],
    -6: ["fs", "dqs'"],
    -7: ["f", "eqs'"],
    -8: ["e", "gqf'"],
    -9: ["ef", "a'"],
    -10: ["d", "cqf''"],
    -11: ["df", "f'"],
    -12: ["c", "bqs''"],
}
binotes_str4 = {
    7: ["g' af"],
    6: ["fs'", "a"],
    5: ["f'", "cqf'"],
    4: ["e'", "cqs'"],
    3: ["ef'", "d'"],
    2: ["d'", "ef'"],
    1: ["cs'", "eqs'"],
    0: ["c'", "fqs'"],
    -1: ["b", "g'"],
    -2: ["bf", "a'"],
    -3: ["a", "bqs'"],
    -4: ["af", "d''"],
    -5: ["g", "fqf''"],
    -6: ["gf", "as''"],
    -7: ["f", "eqs'''"],
}

binotes_str3 = {
    12: ["c''", "df'"],
    11: ["b'", "d'"],
    10: ["bf'", "fqf'"],
    9: ["a'", "g'"],
    8: ["af'", "af'"],
    7: ["g'", "aqs'"],
    6: ["fs'", "cqs''"],
    5: ["f'", "cqs''"],
    4: ["e'", "g'"],
    3: ["ef'", "d''"],
    2: ["d'", "eqs''"],
    1: ["df'", "g''"],
    0: ["c'", "bqf''"],
    -1: ["b", "ds'''"],
    -2: ["bf", "aqs''''"],
}

binotes_str2 = {
    16: ["e''", "f'"],
    15: ["ds''", "fs'"],
    14: ["d''", "aqf'"],
    13: ["cs''", "as'"],
    12: ["c''", "b'"],
    11: ["b'", "c''"],
    10: ["as'", "dqf''"],
    9: ["a'", "dqs''"],
    8: ["gs'", "eqs''"],
    7: ["g'", "fs''"],
    6: ["fs'", "aqf''"],
    5: ["f'", "b''"],
    4: ["e'", "dqs'''"],
    3: ["ef'", "g'''"],
    2: ["d'", "dqf'''''"],
}

binotes_str1 = {
    21: ["a''", "bf'"],
    20: ["gs''", "b'"],
    19: ["g''", "cs''"],
    18: ["fs''", "dqs''"],
    17: ["f''", "e''"],
    16: ["e'", "f''"],
    15: ["ds'", "gqf''"],
    14: ["d'", "gs''"],
    13: ["cs'", "a''"],
    12: ["c''", "b''"],
    11: ["b'", "dqf'''"],
    10: ["bf'", "e'''"],
    9: ["a'", "gqs'''"],
    8: ["af'", "c''''"],
    7: ["g'", "fs'''''"],
}


binotes = {
    6: binotes_str6,
    5: binotes_str5,
    4: binotes_str4,
    3: binotes_str3,
    2: binotes_str2,
    1: binotes_str1,    
}
