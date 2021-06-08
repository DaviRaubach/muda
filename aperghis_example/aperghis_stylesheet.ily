\version "2.20"
\language "english"

#(set-default-paper-size "a4landscape")
#(set-global-staff-size 9)

\header {
  tagline = ##f
  % breakbefore = ##t
  title =  "Recitación 9"
  poet = "Georges Aperghis (*1945)"
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

\paper {
  #(set-paper-size "b4landscape")
  indent = 0
  bottom-margin = 10\mm
  left-margin = 50\mm
  right-margin = 20\mm
  top-margin = 10\mm

}


