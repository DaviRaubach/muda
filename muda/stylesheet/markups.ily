subito = \markup { \fontsize #-2 \italic \center-align "subito"}
half = \markup {\fontsize #-3 \note-by-number #1 #0 #0.9 }
quarter = \markup {\fontsize #-3 \note-by-number #2 #0 #0.9 }
dottedQuarter = \markup {\fontsize #-3 \note-by-number #2 #1 #-0.9 }
noteheadTied = \markup  {\fontsize #-2 \musicglyph "noteheads.s2" \musicglyph "ties.lyric.short" }
xMark = \markup {\fontsize #-3 \override #'(style . cross) \note-by-number #2 #0 #0 }
