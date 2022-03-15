\version "2.23"
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
  \include "./illustration_score.ly"
}


