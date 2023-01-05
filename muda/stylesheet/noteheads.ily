arrowUp = {
  \once \override NoteHead.stencil = #ly:text-interface::print
  \once \override NoteHead.text = \markup {
				%\combine
				%\halign #3 \draw-line #'(0 . 3)
    \fontsize #2 \musicglyph "arrowheads.close.11"
  }
}

halfSquare = {\once \override NoteHead.stencil = #ly:text-interface::print
	      \once \override NoteHead.text = \markup  { \musicglyph "noteheads.s0la"}}

quarterSquare = {\once \override NoteHead.stencil = #ly:text-interface::print
		 \once \override NoteHead.text = \markup  { \musicglyph "noteheads.s2la"}}

