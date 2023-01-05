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

behindBridgeOff = {
  \revert Stem.stencil
  \revert Flag.stencil
}

