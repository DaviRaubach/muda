\version "2.20.0"   %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

\context Score = "Score" %! muda.Score()
<<                       %! muda.Score()
    \context TimeSignatureContext = "Global_Context"
    {
        \time 1/8 %! muda.Score.make_skips()
        s1 * 1/8
        \time 1/4 %! muda.Score.make_skips()
        s1 * 1/4
        \time 1/8 %! muda.Score.make_skips()
        s1 * 1/8
        \time 1/4 %! muda.Score.make_skips()
        s1 * 1/4
        \time 1/4 %! muda.Score.make_skips()
        s1 * 1/4
        \time 1/8 %! muda.Score.make_skips()
        s1 * 1/8
        \time 1/4 %! muda.Score.make_skips()
        s1 * 1/4
        \time 1/2 %! muda.Score.make_skips()
        s1 * 1/2
        \time 1/4 %! muda.Score.make_skips()
        s1 * 1/4
        \time 1/8 %! muda.Score.make_skips()
        s1 * 1/8
        \time 1/4 %! muda.Score.make_skips()
        s1 * 1/4
        \time 1/2 %! muda.Score.make_skips()
        s1 * 1/2
        \time 1/2 %! muda.Score.make_skips()
        s1 * 1/2
        \time 1/4 %! muda.Score.make_skips()
        s1 * 1/4
        \time 1/8 %! muda.Score.make_skips()
        s1 * 1/8
        \time 1/4 %! muda.Score.make_skips()
        s1 * 1/4
        \time 1/4 %! muda.Score.make_skips()
        s1 * 1/4
    }
    \context Staff = "Soprano_Staff" %! muda.score.Instrument()
    <<                               %! muda.score.Instrument()
        \context Voice = "Soprano_Voice_1" %! muda.score.Instrument()
        {                                  %! muda.score.Instrument()
            {   % mat11_0
                {
                    a'8
                    ^ \markup { 0 }
                    ^ \markup { mat11_0 }
                }
            }   % mat11_0
            {   % mat11_1
                {
                    r16
                    ^ \markup { 0 }
                    ^ \markup { mat11_1 }
                    a'16
                    ^ \markup { 1 }
                    b'8
                    ^ \markup { 2 }
                }
            }   % mat11_1
            \times 4/5 {
                e'''32
                ^ \markup { 0 }
                ^ \markup { mat10_0 }
                ef''32
                ^ \markup { 1 }
                b''32
                ^ \markup { 2 }
                a'32
                ^ \markup { 3 }
                d'32
                ^ \markup { 4 }
            }
            {   % mat11_2
                {
                    r16
                    ^ \markup { 0 }
                    ^ \markup { mat11_2 }
                    a'16
                    ^ \markup { 1 }
                    b'8
                    ^ \markup { 2 }
                }
            }   % mat11_2
            \times 2/3 {
                r8
                ^ \markup { 0 }
                ^ \markup { mat09_0 }
                b'8
                ^ \markup { 1 }
                r8
                ^ \markup { 2 }
            }
            \times 4/5 {
                e'''32
                ^ \markup { 0 }
                ^ \markup { mat10_1 }
                ef''32
                ^ \markup { 1 }
                b''32
                ^ \markup { 2 }
                a'32
                ^ \markup { 3 }
                d'32
                ^ \markup { 4 }
            }
            {   % mat11_3
                {
                    r16
                    ^ \markup { 0 }
                    ^ \markup { mat11_3 }
                    a'16
                    ^ \markup { 1 }
                    b'8
                    ^ \markup { 2 }
                }
            }   % mat11_3
            \times 2/3 {
                f''4
                ^ \markup { 0 }
                ^ \markup { mat08_0 }
                e''4
                ^ \markup { 1 }
                ef''4
                ^ \markup { 2 }
            }
            \times 2/3 {
                r8
                ^ \markup { 0 }
                ^ \markup { mat09_1 }
                b'8
                ^ \markup { 1 }
                r8
                ^ \markup { 2 }
            }
            \times 4/5 {
                e'''32
                ^ \markup { 0 }
                ^ \markup { mat10_2 }
                ef''32
                ^ \markup { 1 }
                b''32
                ^ \markup { 2 }
                a'32
                ^ \markup { 3 }
                d'32
                ^ \markup { 4 }
            }
            {   % mat11_4
                {
                    r16
                    ^ \markup { 0 }
                    ^ \markup { mat11_4 }
                    a'16
                    ^ \markup { 1 }
                    b'8
                    ^ \markup { 2 }
                }
            }   % mat11_4
            \times 2/3 {
                r8.
                ^ \markup { 0 }
                ^ \markup { mat07_0 }
                r8
                ^ \markup { 1 }
                b'16
                ^ \markup { 2 }
                r8.
                ^ \markup { 3 }
                r8.
                ^ \markup { 4 }
            }
            \times 2/3 {
                f''4
                ^ \markup { 0 }
                ^ \markup { mat08_1 }
                e''4
                ^ \markup { 1 }
                ef''4
                ^ \markup { 2 }
            }
            \times 2/3 {
                r8
                ^ \markup { 0 }
                ^ \markup { mat09_2 }
                b'8
                ^ \markup { 1 }
                r8
                ^ \markup { 2 }
            }
            \times 4/5 {
                e'''32
                ^ \markup { 0 }
                ^ \markup { mat10_3 }
                ef''32
                ^ \markup { 1 }
                b''32
                ^ \markup { 2 }
                a'32
                ^ \markup { 3 }
                d'32
                ^ \markup { 4 }
            }
            {   % mat11_5
                {
                    r16
                    ^ \markup { 0 }
                    ^ \markup { mat11_5 }
                    a'16
                    ^ \markup { 1 }
                    b'8
                    ^ \markup { 2 }
                }
            }   % mat11_5
            {   % mat06_0
                r16
                ^ \markup { 0 }
                ^ \markup { mat06_0 }
                e''32
                ^ \markup { 1 }
                c''32
                ^ \markup { 2 }
                e''32
                ^ \markup { 3 }
                c''32
                ^ \markup { 4 }
                g'32
                ^ \markup { 5 }
                b'32
                ^ \markup { 6 }
            }   % mat06_0
            
        } %! muda.score.Instrument()
        \context Lyrics = "Soprano_Voice_1_Lyrics" %! muda.score.Instrument()
        {                                          %! muda.score.Instrument()
        } %! muda.score.Instrument()
    >> %! muda.score.Instrument()
>> %! muda.Score()

\markup{etc.}