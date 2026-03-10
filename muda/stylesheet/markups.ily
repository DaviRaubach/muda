subito = \markup { \fontsize #-2 \italic \center-align "subito"}
Ppossibile = \markup { \dynamic p possibile }
half = \markup {\fontsize #-3 \note-by-number #1 #0 #0.9 }
quarter = \markup {\fontsize #-3 \note-by-number #2 #0 #0.9 }
dottedQuarter = \markup {\fontsize #-3 \note-by-number #2 #1 #-0.9 }
noteheadTied = \markup  {\fontsize #-2 \musicglyph "noteheads.s2" \musicglyph "ties.lyric.short" }
xMark = \markup {\fontsize #-3 \override #'(style . cross) \note-by-number #2 #0 #0 }

#(define-markup-command (scratched layout props text) (markup?)
  "Scratch text."
  (interpret-markup layout props
   #{ \markup \override #'(offset . -4) \underline { #text } #} ))


#(define-markup-command (scratched-dotted layout props text) (markup?)
  "Riscado pontilhado usando uma abordagem direta de overlay."
  (interpret-markup layout props
    #{ 
      \markup \combine
        #text
        \with-dimensions-from #text
        \translate #'(0 . 0.6)  
        \override #'(thickness . 0.1)
        \override #'(on . 0.3)
        \override #'(off . 0.5)
      \draw-dashed-line #'(4 . 0)
      % \override #'((thickness . 2) (off . 0.2))
      % \draw-dotted-line #'(4 . 0)
  % \draw-dotted-line #'(5.1 . 2.3)
    #}))