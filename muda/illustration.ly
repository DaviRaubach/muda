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
            % OPENING:
                % GROB_OVERRIDES:
                \override Tie.stencil = ##f
                % OPEN_BRACKETS:
                {   % A_0
                % OPENING:
                    % COMMANDS:


                            \footnote #'(0.5 . 0.5) \markup  \justify {
                            Apenas ruído de corda: para amplificar o efeito, pressionar em silêncio previamente, soltar e mudar a posição com o dedo sobre as cordas. Manter a mão esquerda levemente pressionada para obter em seguida sons abafados e harmônicos ocasionais. } Stem
                     \omit Voice.Flag
                     \omit StaffGroup.SpanBar
                     \hide Voice.Beam
                     \omit Voice.Rest
                     \omit Voice.TupletNumber
                     \omit Voice.TupletBracket
                     \omit Voice.Dots
                    % BEFORE:
                    % COMMANDS:
                    \ottava 1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "A_0"
                    \time 9/8
                    <
                        \tweak stencil \seminimaSquare
                        e
                        \tweak stencil \seminimaSquare
                        b
                        \tweak stencil \seminimaSquare
                        ds'
                        \tweak stencil \seminimaSquare
                        as'
                    >8
                    % AFTER:
                    % ARTICULATIONS:
                    \ff
                    % MARKUP:
                    - \markup \fontsize #-3 \column {\circle "5" \circle "6"}
                    - \markup \tiny {\null { \raise #2 {0}}}
                    ^ \markup \fontsize #-3 \column {\circle 3 \circle 4 }
                    ^ \markup {pressionando levemente sempre}
                    % SPANNER_STARTS:
                    \glissando
                    \startGroup
                    % OPENING:
                    % COMMANDS:
                    \hide NoteHead
                    \override Accidental.stencil = ##f
                    \override NoteColumn.glissando-skip = ##t
                    \override NoteHead.no-ledgers = ##t
                    \override Dots.transparent = ##t
                    \override Stem.transparent = ##t
                    <b f' as' f''>2..
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STARTS:
                    \glissando
                    % OPENING:
                    % COMMANDS:
                    \revert Accidental.stencil
                    \revert NoteColumn.glissando-skip
                    \revert NoteHead.no-ledgers
                    \undo \hide NoteHead
                    \revert Dots.transparent
                    \revert Stem.transparent
                    <
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        ds'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        as'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        c''
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        g''
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    \glissando
                    % COMMANDS:
                    \breathe
                % CLOSE_BRACKETS:
                }   % A_0
                % OPEN_BRACKETS:
                {   % B_0
                    % OPENING:
                    % COMMANDS:
                    \time 2/4
                    r2
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    ^  \markup {"B_0"}
                    % COMMANDS:
                    \bar "!"
                % CLOSE_BRACKETS:
                }   % B_0
                % OPEN_BRACKETS:
                {   % A_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "A_1"
                    \time 9/8
                    <
                        \tweak stencil \seminimaSquare
                        ds'
                        \tweak stencil \seminimaSquare
                        as'
                        \tweak stencil \seminimaSquare
                        c''
                        \tweak stencil \seminimaSquare
                        g''
                    >8
                    % AFTER:
                    % ARTICULATIONS:
                    \ff
                    % MARKUP:
                    - \markup \fontsize #-3 \column {\circle "5" \circle "6"}
                    - \markup \tiny {\null { \raise #2 {0}}}
                    ^ \markup \fontsize #-3 \column {\circle 3 \circle 4 }
                    % SPANNER_STARTS:
                    \glissando
                    \startGroup
                    % OPENING:
                    % COMMANDS:
                    \hide NoteHead
                    \override Accidental.stencil = ##f
                    \override NoteColumn.glissando-skip = ##t
                    \override NoteHead.no-ledgers = ##t
                    \override Dots.transparent = ##t
                    \override Stem.transparent = ##t
                    <b f' as' f''>2..
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STARTS:
                    \glissando
                    % OPENING:
                    % COMMANDS:
                    \revert Accidental.stencil
                    \revert NoteColumn.glissando-skip
                    \revert NoteHead.no-ledgers
                    \undo \hide NoteHead
                    \revert Dots.transparent
                    \revert Stem.transparent
                    <
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        e
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        b
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        ds'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        as'
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    \glissando
                    % COMMANDS:
                    \breathe
                % CLOSE_BRACKETS:
                }   % A_1
                % OPEN_BRACKETS:
                {   % B_1
                    % OPENING:
                    % COMMANDS:
                    \time 2/4
                    r2
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    ^  \markup {"B_1"}
                    % COMMANDS:
                    \bar "!"
                % CLOSE_BRACKETS:
                }   % B_1
                % OPEN_BRACKETS:
                {   % A_2
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "A_2"
                    \time 9/8
                    <
                        \tweak stencil \seminimaSquare
                        e
                        \tweak stencil \seminimaSquare
                        b
                        \tweak stencil \seminimaSquare
                        ds'
                        \tweak stencil \seminimaSquare
                        as'
                    >8
                    % AFTER:
                    % ARTICULATIONS:
                    \ff
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \glissando
                    \startGroup
                    % OPENING:
                    % COMMANDS:
                    \hide NoteHead
                    \override Accidental.stencil = ##f
                    \override NoteColumn.glissando-skip = ##t
                    \override NoteHead.no-ledgers = ##t
                    \override Dots.transparent = ##t
                    \override Stem.transparent = ##t
                    <b f' as' f''>2..
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STARTS:
                    \glissando
                    % OPENING:
                    % COMMANDS:
                    \revert Accidental.stencil
                    \revert NoteColumn.glissando-skip
                    \revert NoteHead.no-ledgers
                    \undo \hide NoteHead
                    \revert Dots.transparent
                    \revert Stem.transparent
                    <
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        ds'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        as'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        c''
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        g''
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    \glissando
                    % COMMANDS:
                    \breathe
                % CLOSE_BRACKETS:
                }   % A_2
                % OPEN_BRACKETS:
                {   % B_2
                    % OPENING:
                    % COMMANDS:
                    \time 2/4
                    r2
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    ^  \markup {"B_2"}
                    % COMMANDS:
                    \bar "!"
                % CLOSE_BRACKETS:
                }   % B_2
                % OPEN_BRACKETS:
                {   % C_0
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "C_0"
                    \time 9/8
                    <
                        \tweak stencil \seminimaSquare
                        e
                        \tweak stencil \seminimaSquare
                        b
                        \tweak stencil \seminimaSquare
                        ds'
                        \tweak stencil \seminimaSquare
                        as'
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \glissando
                    \startGroup
                    % OPENING:
                    % COMMANDS:
                    \hide NoteHead
                    \override Accidental.stencil = ##f
                    \override NoteColumn.glissando-skip = ##t
                    \override NoteHead.no-ledgers = ##t
                    \override Dots.transparent = ##t
                    \override Stem.transparent = ##t
                    <b f' as' f''>2..
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STARTS:
                    \glissando
                    % OPENING:
                    % COMMANDS:
                    \revert Accidental.stencil
                    \revert NoteColumn.glissando-skip
                    \revert NoteHead.no-ledgers
                    \undo \hide NoteHead
                    \revert Dots.transparent
                    \revert Stem.transparent
                    <
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        ds'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        as'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        c''
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        g''
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    \glissando
                % CLOSE_BRACKETS:
                }   % C_0
                % OPEN_BRACKETS:
                {   % D_0
                    % OPEN_BRACKETS:
                    \tweak edge-height #'(0.7 . 0)
                    \times 2/3
                    {
                        % OPENING:
                        % COMMANDS:
                        \once \override HorizontalBracketText.text = "D_0"
                        \time 4/4
                        <
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            e
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            b
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            ds'
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            as'
                        >2
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {0}}}
                        % SPANNER_STARTS:
                        \glissando
                        \startGroup
                    % CLOSE_BRACKETS:
                    }
                    % OPEN_BRACKETS:
                    \tweak edge-height #'(0.7 . 0)
                    \times 2/3
                    {
                        <
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            ds'
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            as'
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            c''
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            g''
                        >2
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {1}}}
                        % SPANNER_STARTS:
                        \glissando
                    % CLOSE_BRACKETS:
                    }
                    % OPEN_BRACKETS:
                    \tweak edge-height #'(0.7 . 0)
                    \times 2/3
                    {
                        <
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            e
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            b
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            ds'
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            as'
                        >2
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {2}}}
                        % SPANNER_STOPS:
                        \stopGroup
                        % SPANNER_STARTS:
                        \glissando
                    % CLOSE_BRACKETS:
                    }
                % CLOSE_BRACKETS:
                }   % D_0
                % OPEN_BRACKETS:
                {   % C_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "C_1"
                    \time 9/8
                    <
                        \tweak stencil \seminimaSquare
                        ds'
                        \tweak stencil \seminimaSquare
                        as'
                        \tweak stencil \seminimaSquare
                        c''
                        \tweak stencil \seminimaSquare
                        g''
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \glissando
                    \startGroup
                    % OPENING:
                    % COMMANDS:
                    \hide NoteHead
                    \override Accidental.stencil = ##f
                    \override NoteColumn.glissando-skip = ##t
                    \override NoteHead.no-ledgers = ##t
                    \override Dots.transparent = ##t
                    \override Stem.transparent = ##t
                    <b f' as' f''>2..
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STARTS:
                    \glissando
                    % OPENING:
                    % COMMANDS:
                    \revert Accidental.stencil
                    \revert NoteColumn.glissando-skip
                    \revert NoteHead.no-ledgers
                    \undo \hide NoteHead
                    \revert Dots.transparent
                    \revert Stem.transparent
                    <
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        e
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        b
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        ds'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        as'
                    >8
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    \glissando
                    % COMMANDS:
                    \breathe
                % CLOSE_BRACKETS:
                }   % C_1
                % OPEN_BRACKETS:
                {   % B_3
                    % OPENING:
                    % COMMANDS:
                    \time 4/4
                    r1
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    ^  \markup {"B_3"}
                    % COMMANDS:
                    \bar "!"
                % CLOSE_BRACKETS:
                }   % B_3
                % OPEN_BRACKETS:
                {   % C_2
                    % OPEN_BRACKETS:
                    \tweak edge-height #'(0.7 . 0)
                    \times 8/9
                    {
                        % OPENING:
                        % COMMANDS:
                        \once \override HorizontalBracketText.text = "C_2"
                        <
                            \tweak stencil \seminimaSquare
                            e
                            \tweak stencil \seminimaSquare
                            b
                            \tweak stencil \seminimaSquare
                            ds'
                            \tweak stencil \seminimaSquare
                            as'
                        >8
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {0}}}
                        % SPANNER_STARTS:
                        \glissando
                        \startGroup
                    % CLOSE_BRACKETS:
                    }
                    % OPEN_BRACKETS:
                    \tweak edge-height #'(0.7 . 0)
                    \times 8/9
                    {
                        % OPENING:
                        % COMMANDS:
                        \hide NoteHead
                        \override Accidental.stencil = ##f
                        \override NoteColumn.glissando-skip = ##t
                        \override NoteHead.no-ledgers = ##t
                        \override Dots.transparent = ##t
                        \override Stem.transparent = ##t
                        <b f' as' f''>2..
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {1}}}
                        % SPANNER_STARTS:
                        \glissando
                    % CLOSE_BRACKETS:
                    }
                    % OPEN_BRACKETS:
                    \tweak edge-height #'(0.7 . 0)
                    \times 8/9
                    {
                        % OPENING:
                        % COMMANDS:
                        \revert Accidental.stencil
                        \revert NoteColumn.glissando-skip
                        \revert NoteHead.no-ledgers
                        \undo \hide NoteHead
                        \revert Dots.transparent
                        \revert Stem.transparent
                        <
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            ds'
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            as'
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            c''
                            \tweak Accidental.transparent ##t
                            \tweak transparent ##t
                            g''
                        >8
                        % AFTER:
                        % MARKUP:
                        - \markup \tiny {\null { \raise #2 {2}}}
                        % SPANNER_STOPS:
                        \stopGroup
                        % SPANNER_STARTS:
                        \glissando
                    % CLOSE_BRACKETS:
                    }
                % CLOSE_BRACKETS:
                }   % C_2
                % OPEN_BRACKETS:
                {   % D_1
                    % OPENING:
                    % COMMANDS:
                    \once \override HorizontalBracketText.text = "D_1"
                    \time 12/8
                    <
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        e
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        b
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        ds'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        as'
                    >2
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    % SPANNER_STARTS:
                    \glissando
                    \startGroup
                    <
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        ds'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        as'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        c''
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        g''
                    >2
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {1}}}
                    % SPANNER_STARTS:
                    \glissando
                    <
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        e
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        b
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        ds'
                        \tweak Accidental.transparent ##t
                        \tweak transparent ##t
                        as'
                    >2
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {2}}}
                    % SPANNER_STOPS:
                    \stopGroup
                    % SPANNER_STARTS:
                    \glissando
                    % COMMANDS:
                    \breathe
                % CLOSE_BRACKETS:
                }   % D_1
                % OPEN_BRACKETS:
                {   % B_4
                    % OPENING:
                    % COMMANDS:
                    \time 4/4
                    r1
                    % AFTER:
                    % MARKUP:
                    - \markup \tiny {\null { \raise #2 {0}}}
                    ^  \markup {"B_4"}
                    % COMMANDS:
                    \bar "!"
                    \bar "||"
                    \ottava 0
                % CLOSE_BRACKETS:
                }   % B_4
                % AFTER:
                % COMMANDS:
                 \mergeDifferentlyHeadedOff \mergeDifferentlyDottedOff \shiftOff
                 \revert Voice.Beam.stencil
                 \revert Voice.Beam.text
                 \undo \omit Voice.Flag
                 \undo \omit Staff.SpanBar
                 \undo \hide Voice.Beam
                 \undo \omit Voice.Rest
                 \undo \omit Voice.TupletNumber
                 \undo \omit Voice.TupletBracket
                 \undo \omit Voice.Dots
                % CLOSING:
                % GROB_REVERTS:
                \revert Tie.stencil
            % CLOSE_BRACKETS:
            }
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    }
% CLOSE_BRACKETS:
>>
