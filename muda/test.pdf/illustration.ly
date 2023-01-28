\version "2.23.6"
\language "english"
\include "/Users/Davi/.pyenv/versions/abjad314/lib/python3.10/site-packages/abjad/scm/abjad.ily"
\include "/Users/Davi/github/muda/muda/stylesheet.ily"
#(set-default-paper-size "a4" 'portrait)
% OPEN_BRACKETS:
\new Score
<<
    % OPEN_BRACKETS:
    \new Staff
    {
        % OPEN_BRACKETS:
        \new Voice
        \with
        {
            \consists Horizontal_bracket_engraver
        }
        {
            % OPEN_BRACKETS:
            {
                % OPEN_BRACKETS:
                {   % A_0
                % OPENING:
                    % COMMANDS:
                     \omit Voice.Flag
                     \omit StaffGroup.SpanBar
                     \hide Voice.Beam
                     \hide Voice.Rest
                     \omit Voice.TupletNumber
                     \omit Voice.TupletBracket
                     \omit Voice.Dots
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "A_0"
                    \time 7/8
                    r8.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    <
                        \tweak stencil \minima
                        aqs
                        \tweak style #'harmonic
                        dqs'
                    >8
                    % AFTER:
                    % ARTICULATIONS:
                    \p
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STARTS:
                    ~
                    <
                        \tweak stencil \minima
                        aqs
                        \tweak style #'harmonic
                        dqs'
                    >32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    <
                        \tweak stencil \minima
                        g'
                        \tweak style #'harmonic
                        c''
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    % SPANNER_STARTS:
                    ~
                    <
                        \tweak stencil \minima
                        g'
                        \tweak style #'harmonic
                        c''
                    >32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    <
                        \tweak stencil \minima
                        cs'
                        \tweak style #'harmonic
                        fs'
                    >4
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    % SPANNER_STARTS:
                    ~
                    <
                        \tweak stencil \minima
                        cs'
                        \tweak style #'harmonic
                        fs'
                    >16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % A_0
                % AFTER:
                % COMMANDS:
                 \bar "" \omit BarLine \omit StaffGroup.SpanBar
                % OPEN_BRACKETS:
                {   % A_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "A_0"
                    \time 9/8
                    r16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    % OPENING:
                    % COMMANDS:
                    \clef "bass"
                    <
                        \tweak stencil \minima
                        aqs
                        \tweak style #'harmonic
                        dqs'
                    >4
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STARTS:
                    ~
                    <
                        \tweak stencil \minima
                        aqs
                        \tweak style #'harmonic
                        dqs'
                    >16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    r16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % A_0
                % OPEN_BRACKETS:
                {   % B_0
                    % OPENING:
                    % COMMANDS:
                    \clef "bass"
                    \once \override HorizontalBracketText.text = "B_0"
                    b32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    <
                        \tweak stencil \minima
                        fs
                        \tweak style #'harmonic
                        b
                    >8.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "bass"
                    cqs16.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    <
                        \tweak stencil \minima
                        c
                        \tweak style #'harmonic
                        f
                    >8.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % B_0
                % OPEN_BRACKETS:
                {   % C_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "C_0"
                    c'32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    <
                        \tweak stencil \minima
                        bf
                        \tweak style #'harmonic
                        ef'
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    ~
                % CLOSE_BRACKETS:
                }   % C_0
                % OPEN_BRACKETS:
                {   % C_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "C_0"
                    \time 2/4
                    <
                        \tweak stencil \minima
                        bf
                        \tweak style #'harmonic
                        ef'
                    >16.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    fs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    ef''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    g'32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    c'32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    <
                        \tweak stencil \minima
                        d'
                        \tweak style #'harmonic
                        g'
                    >8..
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % C_0
                % OPEN_BRACKETS:
                {   % D_0
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    \once \override HorizontalBracketText.text = "D_0"
                    c''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    bf''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    fs''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    ef''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    g'32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    c'32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    <
                        \tweak stencil \minima
                        d'
                        \tweak style #'harmonic
                        g'
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    c'32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {9}}}
                    <bf ef'>32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {10}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    ~
                % CLOSE_BRACKETS:
                }   % D_0
                % OPEN_BRACKETS:
                {   % D_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "D_0"
                    \time 7/8
                    <bf ef'>16.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    r16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    fs''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    ef''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    g''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    c''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    d''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    c''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    r16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {9}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    bf'32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {10}}}
                    <
                        \tweak stencil \minima
                        fs'
                        \tweak style #'harmonic
                        b'
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {11}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {12}}}
                    ef32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {13}}}
                    <
                        \tweak stencil \minima
                        g
                        \tweak style #'harmonic
                        c'
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {14}}}
                    % SPANNER_STARTS:
                    ~
                    <
                        \tweak stencil \minima
                        g
                        \tweak style #'harmonic
                        c'
                    >32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {15}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    ~
                % CLOSE_BRACKETS:
                }   % D_0
                % OPEN_BRACKETS:
                {   % D_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "D_0"
                    \time 4/4
                    <
                        \tweak stencil \minima
                        g
                        \tweak style #'harmonic
                        c'
                    >32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % D_0
                % OPEN_BRACKETS:
                {   % E_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "E_0"
                    bqs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    g'''16.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    ef'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {9}}}
                    bqs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {10}}}
                    g'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {11}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    ef'''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {12}}}
                    bqs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {13}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {14}}}
                    g'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {15}}}
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    ef'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {16}}}
                    bqs''16.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {17}}}
                    g'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {18}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {19}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {20}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {21}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {22}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {23}}}
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {24}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % E_0
                % AFTER:
                % COMMANDS:
                 \mergeDifferentlyHeadedOff \mergeDifferentlyDottedOff \shiftOff
                 \revert Voice.Beam.stencil
                 \revert Voice.Beam.text
                 \undo \omit Voice.Flag
                 \undo \omit Staff.SpanBar
                 \undo \hide Voice.Beam
                 \undo \hide Voice.Rest
                 \undo \omit Voice.TupletNumber
                 \undo \omit Voice.TupletBracket
                 \undo \omit Voice.Dots
                 \undo \omit BarLine \undo \omit StaffGroup.SpanBar
            % CLOSE_BRACKETS:
            }
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    }
% CLOSE_BRACKETS:
>>
