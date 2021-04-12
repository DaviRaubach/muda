\header { tagline = ##f }\paper {

evenFooterMarkup = ##f

oddFooterMarkup = ##f
}
\version "2.20.0"

\context Score = "Score"
<<
    \context TimeSignatureContext = "Global_Context"
    {
        \time 8/4
        s1 * 2
        \time 5/4
        s1 * 5/4
    }
    \context PianoStaff = "Piano_StaffGroup"
    <<
        \context Staff = "Piano_Staff_1"
        <<
            \context Voice = "Piano_Voice_1"
            {
                \voiceOne
                d'16
                r8.
                r4
                r4
                d'16
                r8.
                d'16
                d'16
                r4.
                r4
                d'16
                r8.
                r2
                d'16
                r8.
                d'16
                d'16
                r8
                r16
                d'16
                d'16
                r16
            }
            \context Voice = "Piano_Voice_2"
            {
            }
        >>
        \context Staff = "Piano_Staff_2"
        <<
            \context Voice = "Piano_Voice_3"
            {
                r16
                c'16
                c'16
                c'16
                r16
                c'16
                r8
                r4
                r16
                c'16
                c'16
                c'16
                r16
                c'16
                r4.
                r16
                c'16
                c'16
                c'16
                r16
                c'16
                c'16
                c'16
                r16
                c'16
                c'16
                c'16
                r16
                c'16
                r4.
                r16
                c'16
                c'16
                c'16
                r16
                c'16
                c'16
                c'16
            }
        >>
    >>
>>