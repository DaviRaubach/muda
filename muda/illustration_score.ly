\version "2.23.9"
\language "english"
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
                {   % a_0
                    % OPEN_BRACKETS:
                    \times 2/3
                    {
                    % OPENING:
                        % COMMANDS:
                        \once \override HorizontalBracketText.text = "a_0"
                        r16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {0}}}
                        % SPANNER_STARTS:
                        \startGroup
                        c'16
                        % AFTER:
                        % ARTICULATIONS:
                        \pp
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {1}}}
                        r16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {2}}}
                        % SPANNER_STOPS:
                        \stopGroup
                    % CLOSE_BRACKETS:
                    }
                % CLOSE_BRACKETS:
                }   % a_0
                % OPEN_BRACKETS:
                {   % r_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "r_0"
                    r2
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    \startGroup
                % CLOSE_BRACKETS:
                }   % r_0
                % OPEN_BRACKETS:
                {   % b_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "b_0"
                    r8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    % BEFORE:
                    % OPEN_BRACKETS:
                    \grace {
                    % OPENING:
                        % COMMANDS:
                        \slash
                        fs'16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {1}}}
                        % SPANNER_STARTS:
                        - \tweak stencil #abjad-flared-hairpin
                        \<
                        c'16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {2}}}
                        f,16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {3}}}
                    % CLOSE_BRACKETS:
                    }
                    c'8
                    % AFTER:
                    % ARTICULATIONS:
                    \mf
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    c''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    e''16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    r8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    r8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    c'8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {9}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % b_0
                % OPEN_BRACKETS:
                {   % a_1
                    % OPEN_BRACKETS:
                    \times 2/3
                    {
                    % OPENING:
                        % COMMANDS:
                        \once \override HorizontalBracketText.text = "a_1"
                        r16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {0}}}
                        % SPANNER_STARTS:
                        \startGroup
                        d,,16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {1}}}
                        r16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {2}}}
                        % SPANNER_STOPS:
                        \stopGroup
                    % CLOSE_BRACKETS:
                    }
                % CLOSE_BRACKETS:
                }   % a_1
                % OPEN_BRACKETS:
                {   % r_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "r_1"
                    r4.
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    \startGroup
                % CLOSE_BRACKETS:
                }   % r_1
                % OPEN_BRACKETS:
                {   % b_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "b_1"
                    r8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    % BEFORE:
                    % OPEN_BRACKETS:
                    \grace {
                    % OPENING:
                        % COMMANDS:
                        \slash
                        fs'16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {1}}}
                        % SPANNER_STARTS:
                        - \tweak stencil #abjad-flared-hairpin
                        \<
                        c'16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {2}}}
                        f,16
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {3}}}
                    % CLOSE_BRACKETS:
                    }
                    fs,8
                    % AFTER:
                    % ARTICULATIONS:
                    \mf
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {4}}}
                    g'16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {5}}}
                    e16
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {6}}}
                    r8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {7}}}
                    r8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {8}}}
                    fs'8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {9}}}
                    % SPANNER_STOPS:
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % b_1
                % OPEN_BRACKETS:
                {   % c_0_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "c_0_1"
                    \once \override HorizontalBracketText.text = "c_0_1"
                    <c' c''>2
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \startGroup
                    \startGroup
                    ~
                    <c' c''>8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    \stopGroup
                % CLOSE_BRACKETS:
                }   % c_0_1
            % CLOSE_BRACKETS:
            }
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    }
% CLOSE_BRACKETS:
>>
