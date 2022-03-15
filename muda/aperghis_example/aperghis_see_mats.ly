\version "2.23.3"
\language "english"

% #(set-global-staff-size 7)
% #(set-default-paper-size "a4landscape")


%\header {
%  tagline = ##f
%  % breakbefore = ##t
%  title =  "Recitación 9"
%  poet = "Georges Aperghis (*1945)"
%}

\layout {
 % ragged-right = ##t
  % \context {
  %   \name TimeSignatureContext
  %   \type Engraver_group
  %   \numericTimeSignature
  % }
  \context {
    \Score
    % \numericTimeSignature
    % \remove Metronome_mark_engraver
    % \remove Bar_number_engraver
    % \remove Time_signature_engraver
    % \remove Mark_engraver
    % \consists "Horizontal_bracket_engraver"
    % \accepts TimeSignatureContext
    
    % \override BarLine.hair-thickness = #0.9
    % \override BarLine.thick-thickness = #8
    % \override Stem.thickness = #0.5
    % \override Staff.thickness = #0.5
    % \override Stem.stemlet-length = #1.15
    % \override TupletBracket.bracket-visibility = ##t
    % \override TupletBracket.minimum-length = #3
    % \override TupletBracket.padding = #2
    % \override TupletBracket.staff-padding = #2
    % \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
    % \override TupletBracket.direction = #down
    % \override TupletNumber.font-size = #1.2
    % \override TupletNumber.text = #tuplet-number::calc-fraction-text
    % % \override SpacingSpanner.strict-note-spacing = ##t
    proportionalNotationDuration = #(ly:make-moment 1 28)
    % % tupletFullLength = ##t
    \override HorizontalBracket.direction = #DOWN
    \override HorizontalBracket.Y-offset = #-10
  }

  \context {
    \Voice
				% \consists "Horizontal_bracket_engraver"
    % \override HorizontalBracket.padding = #3
  }

}


\paper {
  system-system-spacing = #'((basic-distance . 20) (padding . 15))
  indent = 0
  bottom-margin = 10\mm
  left-margin = 20\mm
  right-margin = 20\mm
  top-margin = 10\mm

}

\score{
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
}}}}


\markup{etc.}