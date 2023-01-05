\version "2.23.3"
\include "/Users/Davi/github/muda/muda/stylesheet/wind-diagrams.ily"
pestaninhaIV = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " IV"
} 
pestaninhaV = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " V"
} 
pestaninhaVII = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " VII"
} 
pestaninhaIX = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " IX"
} 
pestaninhaXII = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " XII"
} 
glissandoSkipOn = {
  \override NoteColumn.glissando-skip = ##t
  \hide NoteHead
  \override NoteHead.no-ledgers = ##t
}
glissandoSkipOff = {
  \revert NoteColumn.glissando-skip
  \undo \hide NoteHead
  \revert NoteHead.no-ledgers
}
subito = \markup { \fontsize #-2 \italic \center-align "subito"}
half = \markup {\fontsize #-3 \note-by-number #1 #0 #0.9 }
head = \markup  {\fontsize #-2 \musicglyph "noteheads.s2" \musicglyph "ties.lyric.short" }
dottedquarter = \markup {\fontsize #-3 \note-by-number #2 #1 #-0.9 }
xMark = \markup {\fontsize #-3 \override #'(style . cross) \note-by-number #2 #0 #0 }
Rdo = {
  \once \override NoteHead.stencil = #ly:text-interface::print
  \once \override NoteHead.text = \markup {
    %\combine
      %\halign #3 \draw-line #'(0 . 3)
        \fontsize #2 \musicglyph "arrowheads.close.11"
  }
}
hideStaff = {\stopStaff \startStaff \omit Staff.StaffSymbol}
showStaff = {\stopStaff \startStaff \undo \omit Staff.StaffSymbol}

halfSquare = {\once \override NoteHead.stencil = #ly:text-interface::print
	      \once \override NoteHead.text = \markup  { \musicglyph "noteheads.s0la"}}

quarterSquare = {\once \override NoteHead.stencil = #ly:text-interface::print
		 \once \override NoteHead.text = \markup  { \musicglyph "noteheads.s2la"}}
% #(print-keys-verbose 'bass-clarinet (current-error-port))

behindBridgeOn = {
  \once \override Stem.stencil =
    #(lambda (grob)
       (let* ((x-parent (ly:grob-parent grob X))
              (is-rest? (ly:grob? (ly:grob-object x-parent 'rest))))
         (if is-rest?
             empty-stencil
             (ly:stencil-combine-at-edge
              (ly:stem::print grob)
              Y
              (- (ly:grob-property grob 'direction))
              (grob-interpret-markup grob
                                     (markup #:center-align #:fontsize 3 #:rotate -90
                                             #:musicglyph "accidentals.leftparen"))
              -3))))
}

aeolAndOrd= {
  \once \override Stem.stencil =
    #(lambda (grob)
       (let* ((x-parent (ly:grob-parent grob X))
              (is-rest? (ly:grob? (ly:grob-object x-parent 'rest))))
         (if is-rest?
             empty-stencil
             (ly:stencil-combine-at-edge
              (ly:stem::print grob)
              Y
              (- (ly:grob-property grob 'direction))
              (grob-interpret-markup grob
                                     (markup #:center-align #:fontsize 3 #:rotate -180
                                             #:musicglyph "noteheads.s0doThin"))
              -2.5))))
}

slap =
#(define-music-function (music) (ly:music?)
#{
  \temporary \override NoteHead.stencil =
  #(lambda (grob)
     (grob-interpret-markup grob
      (markup #:musicglyph "scripts.sforzato")))
  \temporary \override NoteHead.stem-attachment =
  #(lambda (grob)
     (let* ((thickness (ly:staff-symbol-line-thickness grob))
            (stem (ly:grob-object grob 'stem))
            (dir (ly:grob-property stem 'direction UP)))
       (cons 1 (+ (if (= dir DOWN)
                      0.5
                      0)
                  (/ thickness 2)))))
  #music
  \revert NoteHead.stencil
  \revert NoteHead.stem-attachment
#})

aeol =
#(define-music-function (music) (ly:music?)
#{
  \temporary \override NoteHead.stencil =
  #(lambda (grob)
     (grob-interpret-markup grob
      (markup #:center-align  #:vspace -5 #:fontsize 3 #:rotate -180
       #:musicglyph "noteheads.s0doThin")))
  % \temporary \override NoteHead.stem-attachment =
  % #(lambda (grob)
  %    (let* ((thickness (ly:staff-symbol-line-thickness grob))
  %           (stem (ly:grob-object grob 'stem))
  %           (dir (ly:grob-property stem 'direction UP)))
  %      (cons 1 (+ (if (= dir DOWN)
  %                     0.5
  %                     0)
  %                 (/ thickness 2)))))
  #music
  \revert NoteHead.stencil
  % \revert NoteHead.stem-attachment
#})

behindBridgeOff = {
  \revert Stem.stencil
  \revert Flag.stencil
}


samplePath =
  #'(
     (moveto 0 0)
     (curveto 0 0 0 1 1 1)
     (curveto 1 1 2 1 2 0)
     (curveto 2 0 2 -1 3 -1)
     (curveto 3 -1 4 -1 4 0)
     )

vib = \markup {

  \scale #'(0.3 . 1)
  \path #0.4 #samplePath
  \hspace #-0.71
  \scale #'(0.3 . 0.5)
  \path #0.4 #samplePath
  \hspace #-0.71
  \scale #'(0.3 . 0.2)
  \path #0.4 #samplePath

}

upT = {
  \set stemLeftBeamCount = #0
  \once \autoBeamOff
  \once \override Stem.direction = #down
  \once \override Stem.X-offset = #0.622
  \once \override Stem.Y-offset  = #-0.2
  \once \override Stem.length-fraction  = #1.12
  \once \override NoteHead  #'stencil = #ly:text-interface::print
  \once \override NoteHead #'text =
  \markup {
    \path #0.13
    #'((moveto -.1775 -.43)
       (lineto .65625 .43)
       (lineto 1.39 -.43)
       (closepath))
  }
}
dT = {
  \set stemLeftBeamCount = #0
  \once \autoBeamOff
  \once \override Stem.direction = #up
  \once \override Stem.X-offset = #0.64
  \once \override Stem.Y-offset  = #0.2
  \once \override Stem.length-fraction  = #1.12
  \once \override NoteHead  #'stencil = #ly:text-interface::print
  \once \override NoteHead #'text = \markup {
    \path #0.13
    #'((moveto  -.0775 .43)
       (lineto  .65625 -.43 )
       (lineto 1.39 .43)
       (closepath))
  }
}
upTg = {
  \once \autoBeamOff
  \once \override Stem.direction = #down
  \once \override Stem.X-offset = #0.622
  \once \override Stem.Y-offset  = #-0.2
  \once \override NoteHead  #'stencil = #ly:text-interface::print
  \once \override NoteHead #'text =
  \markup {
    \path #0.13
    #'((moveto -.1775 -.43)
       (lineto .65625 .43)
       (lineto 1.39 -.43)
       (closepath))
  }
}
dTg = {
  \once \autoBeamOff
  \once \override Stem.direction = #up
  \once \override Stem.X-offset = #0.64
  \once \override Stem.Y-offset  = #0.2
  \once \override NoteHead  #'stencil = #ly:text-interface::print
  \once \override NoteHead #'text = \markup {
    \path #0.13
    #'((moveto  -.0775 .43)
       (lineto  .65625 -.43 )
       (lineto 1.39 .43)
       (closepath))
  }
}
subito = \markup { \fontsize #-2 \italic \center-align "subito"}
quarter = \markup {\fontsize #-3 \note-by-number #2 #0 #0.9 }
dottedquarter = \markup {\fontsize #-3 \note-by-number #2 #1 #0.9 }
%quartos de tom: ceseh1 ces ceh c cih cis cisih
positionFlute = ^\markup \override #'(size . 0.8) {
  \woodwind-diagram
          #'flute
          #'()
}
sTg = {\once \hide NoteHead
  \once \autoBeamOff
  \once \override Stem.X-offset = #0.64
  \once \override Stem.Y-offset  = #0.2
}


\paper {
  print-page-number = ##t
  #(set-paper-size "a4landscape")
  system-system-spacing = #'((basic-distance . 10)
      (minimum-distance . 6)
      (padding . 6)
      (stretchability . 1))
  top-margin = 30
  left-margin = 16
  right-margin = 12
  bottom-margin = 40
}

\layout{
    \context{
        \name TimeSignatureContext
        \type Engraver_group
        \consists Axis_group_engraver
        \consists Mark_engraver
        \consists Metronome_mark_engraver
        \consists Text_engraver
        \consists Text_spanner_engraver
        \consists Time_signature_engraver
        
    }
    \context{
        \Voice
	\consists Duration_line_engraver
	% \override LyricText.self-alignment-X = #CENTER
        \consists "Horizontal_bracket_engraver"
        \override HorizontalBracket.direction = #UP
    }

    \context{
        \StaffGroup
        \omit TimeSignature
        % \omit BarLine
        \omit SpanBar
        % \consists "Horizontal_bracket_engraver"
      }
     \context{
        \PianoStaff
        \omit TimeSignature
        % \omit BarLine
        \omit SpanBar
        % \consists "Horizontal_bracket_engraver"
    }
    \context {
      \Lyrics
      % \override VerticalAxisGroup.staff-affinity = #DOWN
      % \override VerticalAxisGroup.staff-staff-spacing =
      %   #'((basic-distance . 0)
      % 	   (minimum-distance . 0)
      % 	   (padding . 0))
      % \override Lyrics.LyricSpace.minimum-distance = #0.01
      % \override Lyrics.VerticalAxisGroup.staff-affinity = #DOWN
 
}

    \context{
        \Score
        \accepts TimeSignatureContext
        \accepts StaffGroup
        \remove Metronome_mark_engraver
        \remove Mark_engraver
        
        \override SpacingSpanner.strict-grace-spacing = ##t
        \override SpacingSpanner.strict-note-spacing = ##t
        \override SpacingSpanner.uniform-stretching = ##t
        \override TextScript.X-extent = ##f
        \override TextScript.whiteout-style = #'outline
        \override TextScript.whiteout = ##t
        \override line-spanner-interface.to-barline = ##t
        
        \override TupletBracket.minimum-length = #3
        \override TupletBracket.padding = #1.5 % was 2
	\override TupletBracket.staff-padding = #1.5 %}
	\override TupletBracket.staff-padding = #1.3
        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
	\override TupletBracket.direction = #down % occasionally tweak up
        \override TupletNumber.font-size = #1
        \override TupletNumber.text = #tuplet-number::calc-fraction-text
        autoBeaming = ##f
        markFormatter = #format-mark-box-alphabet
        proportionalNotationDuration = #(ly:make-moment 1 24)
        tupletFullLength = ##t
        \override StaffGrouper.staff-staff-spacing =
        #'((basic-distance . 6)
            (minimum-distance . 6)
            (padding . 6)
            (stretchability . 6))
  }

}