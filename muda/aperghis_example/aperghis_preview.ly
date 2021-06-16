\version "2.20.0"
\language "english"
#(set-global-staff-size 13)
%#(set! paper-alist (cons '("my size" . (cons (* 150 in) (* 2 in))) paper-alist))

\paper {
  system-system-spacing = #'((basic-distance . 16) (minimum-distance . 16) (padding . 10))

  %#(set-paper-size "my size")
}
\layout {
  ragged-right = ##t
  \context {
    \name TimeSignatureContext
    \type Engraver_group
    \numericTimeSignature
  }
  \context {
    \Score
    \numericTimeSignature
    \remove Metronome_mark_engraver
    \remove Bar_number_engraver
    \remove Mark_engraver
    \accepts TimeSignatureContext
    \override BarLine.hair-thickness = #0.9
    \override BarLine.thick-thickness = #8
    \override Stem.thickness = #0.5
    \override Staff.thickness = #0.5
    \override Stem.stemlet-length = #1.15
    \override TupletBracket.bracket-visibility = ##t
    \override TupletBracket.minimum-length = #3
    \override TupletBracket.padding = #2
    \override TupletBracket.staff-padding = #2
    \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
    \override TupletBracket.direction = #down
    \override TupletNumber.font-size = #1.2
    \override TupletNumber.text = #tuplet-number::calc-fraction-text
    \override SpacingSpanner.strict-note-spacing = ##t
    proportionalNotationDuration = #(ly:make-moment 1 28)
    tupletFullLength = ##t
  }

  \context {
    \Staff
    \remove Time_signature_engraver
    \remove Clef_engraver
  }
}

\score {
  {
    \include "/Users/Davi/github/muda/muda/aperghis_example/aperghis_score.ly"
  }
  \layout { }
  \midi { }
}