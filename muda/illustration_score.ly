\version "2.23.3"
\language "english"
\new Score
<<
    \new Staff
    {
        \new Voice
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
            {
                {   % matL_0
                    {
                        \once \override HorizontalBracketText.text = "matL_0"
                        \time 1/8
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \stopGroup
                        \startGroup
                    }
                }   % matL_0
                {   % matL_1
                    {
                        \once \override HorizontalBracketText.text = "matL_1"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_1
                {   % matK_0
                    \break
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_0"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_0
                {   % matL_2
                    {
                        \once \override HorizontalBracketText.text = "matL_2"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_2
                {   % matJ_0
                    \break
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_0"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_0
                {   % matK_1
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_1"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_1
                {   % matL_3
                    {
                        \once \override HorizontalBracketText.text = "matL_3"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_3
                {   % matI_0
                    \break
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_0"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_0
                {   % matJ_1
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_1"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_1
                {   % matK_2
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_2"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_2
                {   % matL_4
                    {
                        \once \override HorizontalBracketText.text = "matL_4"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_4
                {   % matH_0
                    \break
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_0"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_0
                {   % matI_1
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_1"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_1
                {   % matJ_2
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_2"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_2
                {   % matK_3
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_3"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_3
                {   % matL_5
                    {
                        \once \override HorizontalBracketText.text = "matL_5"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_5
                {   % matG_0
                    \break
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_0"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_0
                {   % matH_1
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_1"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_1
                {   % matI_2
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_2"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_2
                {   % matJ_3
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_3"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_3
                {   % matK_4
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_4"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_4
                {   % matL_6
                    {
                        \once \override HorizontalBracketText.text = "matL_6"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_6
                {   % matF_0
                    \break
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_0"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_0
                {   % matG_1
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_1"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_1
                {   % matH_2
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_2"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_2
                {   % matI_3
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_3"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_3
                {   % matJ_4
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_4"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_4
                {   % matK_5
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_5"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_5
                {   % matL_7
                    {
                        \once \override HorizontalBracketText.text = "matL_7"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_7
                {   % matE_0
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matE_0"
                        \time 1/4
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matE_0
                {   % matF_1
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_1"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_1
                {   % matG_2
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_2"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_2
                {   % matH_3
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_3"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_3
                {   % matI_4
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_4"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_4
                {   % matJ_5
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_5"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_5
                {   % matK_6
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_6"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_6
                {   % matL_8
                    {
                        \once \override HorizontalBracketText.text = "matL_8"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_8
                {   % matE_1
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matE_1"
                        \time 3/8
                        r32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        \stopGroup
                    }
                }   % matE_1
                {   % matF_2
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_2"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_2
                {   % matG_3
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_3"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_3
                {   % matH_4
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_4"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_4
                {   % matI_5
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_5"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_5
                {   % matJ_6
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_6"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_6
                {   % matK_7
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_7"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_7
                {   % matL_9
                    {
                        \once \override HorizontalBracketText.text = "matL_9"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_9
                {   % matE_2
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matE_2"
                        r32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {8}}}
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {9}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {10}}}
                        \stopGroup
                    }
                }   % matE_2
                {   % matF_3
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_3"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_3
                {   % matG_4
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_4"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_4
                {   % matH_5
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_5"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_5
                {   % matI_6
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_6"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_6
                {   % matJ_7
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_7"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_7
                {   % matK_8
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_8"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_8
                {   % matL_10
                    {
                        \once \override HorizontalBracketText.text = "matL_10"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_10
                {   % matE_3
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matE_3"
                        r32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {8}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {9}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {10}}}
                        \stopGroup
                    }
                }   % matE_3
                {   % matF_4
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_4"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_4
                {   % matG_5
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_5"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_5
                {   % matH_6
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_6"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_6
                {   % matI_7
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_7"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_7
                {   % matJ_8
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_8"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_8
                {   % matK_9
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_9"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_9
                {   % matL_11
                    {
                        \once \override HorizontalBracketText.text = "matL_11"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_11
                {   % matE_4
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matE_4"
                        \time 1/2
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {8}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {9}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {10}}}
                        \stopGroup
                    }
                }   % matE_4
                {   % matF_5
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_5"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_5
                {   % matG_6
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_6"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_6
                {   % matH_7
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_7"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_7
                {   % matI_8
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_8"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_8
                {   % matJ_9
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_9"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_9
                {   % matK_10
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_10"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_10
                {   % matL_12
                    {
                        \once \override HorizontalBracketText.text = "matL_12"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_12
                {   % matD_0
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matD_0"
                        \times 2/3
                        {
                            \time 1/8
                            r16
                            ^ \markup \tiny {\null { \raise #2 {0}}}
                            \startGroup
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {1}}}
                            \stopGroup
                        }
                    }
                }   % matD_0
                {   % matE_5
                    {
                        \once \override HorizontalBracketText.text = "matE_5"
                        \time 1/2
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {8}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {9}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {10}}}
                        \stopGroup
                    }
                }   % matE_5
                {   % matF_6
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_6"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_6
                {   % matG_7
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_7"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_7
                {   % matH_8
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_8"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_8
                {   % matI_9
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_9"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_9
                {   % matJ_10
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_10"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_10
                {   % matK_11
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_11"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_11
                {   % matL_13
                    {
                        \once \override HorizontalBracketText.text = "matL_13"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_13
                {   % matD_1
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matD_1"
                        \times 2/3
                        {
                            s8
                            ^ \markup \tiny {\null { \raise #2 {0}}}
                            \startGroup
                            s16
                            ^ \markup \tiny {\null { \raise #2 {1}}}
                            s16
                            ^ \markup \tiny {\null { \raise #2 {2}}}
                            s16
                            ^ \markup \tiny {\null { \raise #2 {3}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {4}}}
                            r8
                            ^ \markup \tiny {\null { \raise #2 {5}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {6}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {7}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {8}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {9}}}
                            \stopGroup
                        }
                    }
                }   % matD_1
                {   % matE_6
                    {
                        \once \override HorizontalBracketText.text = "matE_6"
                        \time 1/2
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {8}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {9}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {10}}}
                        \stopGroup
                    }
                }   % matE_6
                {   % matF_7
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_7"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_7
                {   % matG_8
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_8"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_8
                {   % matH_9
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_9"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_9
                {   % matI_10
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_10"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_10
                {   % matJ_11
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_11"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_11
                {   % matK_12
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_12"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_12
                {   % matL_14
                    {
                        \once \override HorizontalBracketText.text = "matL_14"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_14
                {   % matD_2
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matD_2"
                        \times 2/3
                        {
                            s8
                            ^ \markup \tiny {\null { \raise #2 {0}}}
                            \startGroup
                            s16
                            ^ \markup \tiny {\null { \raise #2 {1}}}
                            s16
                            ^ \markup \tiny {\null { \raise #2 {2}}}
                            s16
                            ^ \markup \tiny {\null { \raise #2 {3}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {4}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {5}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {6}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {7}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {8}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {9}}}
                            \stopGroup
                        }
                    }
                }   % matD_2
                {   % matE_7
                    {
                        \once \override HorizontalBracketText.text = "matE_7"
                        \time 1/2
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {8}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {9}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {10}}}
                        \stopGroup
                    }
                }   % matE_7
                {   % matF_8
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_8"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_8
                {   % matG_9
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_9"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_9
                {   % matH_10
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_10"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_10
                {   % matI_11
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_11"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_11
                {   % matJ_12
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_12"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_12
                {   % matK_13
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_13"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_13
                {   % matL_15
                    {
                        \once \override HorizontalBracketText.text = "matL_15"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_15
                {   % matD_3
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matD_3"
                        \times 2/3
                        {
                            \time 5/8
                            r8
                            ^ \markup \tiny {\null { \raise #2 {0}}}
                            \startGroup
                            b'16
                            ^ \markup \tiny {\null { \raise #2 {1}}}
                            ~
                            b'16
                            ^ \markup \tiny {\null { \raise #2 {2}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {3}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {4}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {5}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {6}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {7}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {8}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {9}}}
                            \stopGroup
                        }
                    }
                }   % matD_3
                {   % matE_8
                    {
                        \once \override HorizontalBracketText.text = "matE_8"
                        \time 1/2
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {8}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {9}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {10}}}
                        \stopGroup
                    }
                }   % matE_8
                {   % matF_9
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_9"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_9
                {   % matG_10
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_10"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_10
                {   % matH_11
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_11"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_11
                {   % matI_12
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_12"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_12
                {   % matJ_13
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_13"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_13
                {   % matK_14
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_14"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_14
                {   % matL_16
                    {
                        \once \override HorizontalBracketText.text = "matL_16"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_16
                {   % matC_0
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matC_0"
                        \time 1/8
                        r32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matC_0
                {   % matD_4
                    {
                        \once \override HorizontalBracketText.text = "matD_4"
                        \times 2/3
                        {
                            \time 5/8
                            r8
                            ^ \markup \tiny {\null { \raise #2 {0}}}
                            \startGroup
                            b'16
                            ^ \markup \tiny {\null { \raise #2 {1}}}
                            ~
                            b'16
                            ^ \markup \tiny {\null { \raise #2 {2}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {3}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {4}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {5}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {6}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {7}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {8}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {9}}}
                            \stopGroup
                        }
                    }
                }   % matD_4
                {   % matE_9
                    {
                        \once \override HorizontalBracketText.text = "matE_9"
                        \time 1/2
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {8}}}
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {9}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {10}}}
                        \stopGroup
                    }
                }   % matE_9
                {   % matF_10
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_10"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_10
                {   % matG_11
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_11"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_11
                {   % matH_12
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_12"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_12
                {   % matI_13
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_13"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_13
                {   % matJ_14
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_14"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_14
                {   % matK_15
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_15"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_15
                {   % matL_17
                    {
                        \once \override HorizontalBracketText.text = "matL_17"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_17
                {   % matA_0
                    \break
                    {
                        \once \override HorizontalBracketText.text = "matA_0"
                        \time 1/2
                        r16.
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r16
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        r4
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        \stopGroup
                    }
                }   % matA_0
                {   % matB_0
                    {
                        \once \override HorizontalBracketText.text = "matB_0"
                        \times 2/3
                        {
                            \time 1/8
                            r16
                            ^ \markup \tiny {\null { \raise #2 {0}}}
                            \startGroup
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {1}}}
                            \stopGroup
                        }
                    }
                }   % matB_0
                {   % matC_1
                    {
                        \once \override HorizontalBracketText.text = "matC_1"
                        \time 1/8
                        r32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matC_1
                {   % matD_5
                    {
                        \once \override HorizontalBracketText.text = "matD_5"
                        \times 2/3
                        {
                            \time 5/8
                            r8
                            ^ \markup \tiny {\null { \raise #2 {0}}}
                            \startGroup
                            b'16
                            ^ \markup \tiny {\null { \raise #2 {1}}}
                            ~
                            b'16
                            ^ \markup \tiny {\null { \raise #2 {2}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {3}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {4}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {5}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {6}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {7}}}
                            r16
                            ^ \markup \tiny {\null { \raise #2 {8}}}
                            b'8
                            ^ \markup \tiny {\null { \raise #2 {9}}}
                            \stopGroup
                        }
                    }
                }   % matD_5
                {   % matE_10
                    {
                        \once \override HorizontalBracketText.text = "matE_10"
                        \time 1/2
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {5}}}
                        r32
                        ^ \markup \tiny {\null { \raise #2 {6}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {7}}}
                        b'32
                        ^ \markup \tiny {\null { \raise #2 {8}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {9}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {10}}}
                        \stopGroup
                    }
                }   % matE_10
                {   % matF_11
                    \time 7/8
                    \once \override HorizontalBracketText.text = "matF_11"
                    e'8
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    _ (
                    \startGroup
                    s2
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    g''4
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    )
                    \stopGroup
                }   % matF_11
                {   % matG_12
                    \time 1/4
                    \once \override HorizontalBracketText.text = "matG_12"
                    r16
                    ^ \markup \tiny {\null { \raise #2 {0}}}
                    \startGroup
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {1}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {2}}}
                    \once \override NoteHead.style = #'cross
                    e''32
                    ^ \markup \tiny {\null { \raise #2 {3}}}
                    \once \override NoteHead.style = #'cross
                    c''32
                    ^ \markup \tiny {\null { \raise #2 {4}}}
                    \once \override NoteHead.style = #'cross
                    g'32
                    ^ \markup \tiny {\null { \raise #2 {5}}}
                    \once \override NoteHead.style = #'cross
                    b'32
                    ^ \markup \tiny {\null { \raise #2 {6}}}
                    \stopGroup
                }   % matG_12
                {   % matH_13
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matH_13"
                        \time 1/2
                        r4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        r16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'16
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        r4.
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        \stopGroup
                    }
                }   % matH_13
                {   % matI_14
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matI_14"
                        \time 1/2
                        f''4
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        e''4
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        ef''4
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        )
                        \stopGroup
                    }
                }   % matI_14
                {   % matJ_15
                    \times 2/3
                    {
                        \once \override HorizontalBracketText.text = "matJ_15"
                        \time 1/4
                        r8
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        r8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matJ_15
                {   % matK_16
                    \times 4/5
                    {
                        \once \override HorizontalBracketText.text = "matK_16"
                        \time 1/8
                        e'''32
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        (
                        \startGroup
                        ef''32
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b''32
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        a'32
                        ^ \markup \tiny {\null { \raise #2 {3}}}
                        d'32
                        ^ \markup \tiny {\null { \raise #2 {4}}}
                        )
                        \stopGroup
                    }
                }   % matK_16
                {   % matL_18
                    {
                        \once \override HorizontalBracketText.text = "matL_18"
                        \time 1/4
                        r16
                        ^ \markup \tiny {\null { \raise #2 {0}}}
                        \startGroup
                        a'16
                        ^ \markup \tiny {\null { \raise #2 {1}}}
                        b'8
                        ^ \markup \tiny {\null { \raise #2 {2}}}
                        \stopGroup
                    }
                }   % matL_18
            }
        }
    }
>>
