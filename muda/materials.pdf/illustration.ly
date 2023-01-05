\version "2.23.6"
\language "english"
\include "/Users/Davi/.pyenv/versions/abjad36/lib/python3.10/site-packages/abjad/scm/abjad.ily"
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
                    \once \override HorizontalBracketText.text = "A_0"
                    \time 3/8
                    g''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    \f
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % START_BEAM:
                    [
                    % SPANNER_STARTS:
                    \startGroup
                    ef'''16.
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    c'''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % STOP_BEAM:
                    ]
                    % COMMANDS:
                    \breathe
                    r16.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    r8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % A_0
                % OPEN_BRACKETS:
                {   % A_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "A_0"
                    \time 2/4
                    g''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % START_BEAM:
                    [
                    % SPANNER_STARTS:
                    \startGroup
                    fs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    c'''16
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    bqs''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    % STOP_BEAM:
                    ]
                    % COMMANDS:
                    \breathe
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    g''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    % START_BEAM:
                    [
                    fs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    bqs''16.
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    fs''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    % STOP_BEAM:
                    ]
                    % COMMANDS:
                    \breathe
                    r8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {9}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % A_0
                % OPEN_BRACKETS:
                {   % A_0
                    % OPENING:
                    % COMMANDS:
                    \time 3/4
                    r16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    ^  \markup {"A_0"}
                % CLOSE_BRACKETS:
                }   % A_0
                % OPEN_BRACKETS:
                {   % B_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "B_0"
                    bqs''16
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % START_BEAM:
                    [
                    % SPANNER_STARTS:
                    \startGroup
                    g''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    ef'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % SPANNER_STARTS:
                    ~
                    ef'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    g''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    bqs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    fs''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    g''16
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    % SPANNER_STARTS:
                    ~
                    g''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    % STOP_BEAM:
                    ]
                    r16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {9}}}
                    bqs''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {10}}}
                    % START_BEAM:
                    [
                    c'''16.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {11}}}
                    % SPANNER_STARTS:
                    ~
                    c'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {12}}}
                    g''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {13}}}
                    % SPANNER_STARTS:
                    ~
                    g''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {14}}}
                    ef'''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {15}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % STOP_BEAM:
                    ]
                % CLOSE_BRACKETS:
                }   % B_0
                % OPEN_BRACKETS:
                {   % B_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "B_0"
                    \time 5/8
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    c'''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % START_BEAM:
                    [
                    g''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    fs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    % SPANNER_STARTS:
                    ~
                    fs''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    c'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    bqs''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    g''8
                    % AFTER:
                    % ARTICULATIONS:
                    - \bendAfter #'0
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    % SPANNER_STARTS:
                    ~
                    g''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    % STOP_BEAM:
                    ]
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {9}}}
                    fs''8.
                    % AFTER:
                    % ARTICULATIONS:
                    - \bendAfter #'0
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {10}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % START_BEAM:
                    [
                % CLOSE_BRACKETS:
                }   % B_0
                % OPEN_BRACKETS:
                {   % B_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "B_0"
                    \time 3/8
                    bqs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    fs''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    bqs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    g''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % STOP_BEAM:
                    ]
                % CLOSE_BRACKETS:
                }   % B_0
                % OPEN_BRACKETS:
                {   % A_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "A_1"
                    ef'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % START_BEAM:
                    [
                    % SPANNER_STARTS:
                    \startGroup
                    g''16
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STARTS:
                    ~
                    g''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    bqs''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    % STOP_BEAM:
                    ]
                    % COMMANDS:
                    \breathe
                    r16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % A_1
                % OPEN_BRACKETS:
                {   % A_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "A_1"
                    \time 2/4
                    r8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    fs''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % START_BEAM:
                    [
                    g''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {3}}}
                    bqs''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    % SPANNER_STARTS:
                    ~
                    bqs''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    c'''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    % STOP_BEAM:
                    ]
                    % COMMANDS:
                    \breathe
                    r32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    g''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    % START_BEAM:
                    [
                    ef'''32
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {9}}}
                    c'''16.
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {10}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % A_1
                % OPEN_BRACKETS:
                {   % A_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "A_1"
                    \time 3/8
                    g''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % STOP_BEAM:
                    ]
                    % SPANNER_STARTS:
                    \startGroup
                    % COMMANDS:
                    \breathe
                    r8.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % A_1
                % OPEN_BRACKETS:
                {   % B_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "B_1"
                    fs''16
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % START_BEAM:
                    [
                    % SPANNER_STARTS:
                    \startGroup
                    c'''32
                    % AFTER:
                    % ARTICULATIONS:
                    - \accent
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    bqs''16
                    % AFTER:
                    % ARTICULATIONS:
                    - \staccato
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % STOP_BEAM:
                    ]
                % CLOSE_BRACKETS:
                }   % B_1
            % CLOSE_BRACKETS:
            }
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    }
% CLOSE_BRACKETS:
>>
