\version "2.23.9"
#(define-markup-command (strikethrough layout props arg)
   (markup?)
   #:category font
   #:properties ((thickness 1))
   "
@cindex strikethrough, text

Draw an horizontal line through the markup's middle.

@lilypond[verbatim,quote]
\\markup {
  The \\strikethrough Well- Tempered Clavier
}
@end lilypond"
   (let* ((th (* (ly:output-def-lookup layout 'line-thickness)
                 thickness))
          (stil (interpret-markup layout props arg))
          (xextent (ly:stencil-extent stil X))
          (yextent (ly:stencil-extent stil Y))
          (y-pos (/ (- (cdr yextent) (car yextent)) 2)))
     (ly:stencil-add
      stil
      (make-line-stencil
       th (car xextent) y-pos (cdr xextent) y-pos))))
% stemToText = {
%   \override Voice.TextScript.parent-alignment-X = #0
%   (markup #:center-align #:fontsize 3 #:rotate -180
%   #:override '((thickness . 2) (off . 0.5)) #:draw-dotted-line '(0 . 7)))
				%        -2.5))))
				%   ^\markup {
				%     \override #'((thickness . 2) (off . 0.1))
				%     \draw-dotted-line #'(0 . 2)
				%   }
				% }

				% #(define-markup-command (columns layout props args) (markup-list?)
				%    (let ((line-width (/ (chain-assoc-get 'line-width props
				%                          (ly:output-def-lookup layout 'line-width))
				%                         (max (length args) 1))))
				%      (interpret-markup layout props
				%        (make-line-markup (map (lambda (line)
				%                                 (markup #:pad-to-box `(0 . ,line-width) '(0 . 0)
				%                                   #:override `(line-width . ,line-width)
				%                                   line))
				%                                args)))))

  % \once \override Stem.stencil =
  % #(lambda (grob)
  %   (let* ((x-parent (ly:grob-parent grob X))
  % 	   (is-rest? (ly:grob? (ly:grob-object x-parent 'rest))))
  %    (if is-rest?
  %     empty-stencil
  %     (ly:stencil-combine-at-edge
  %      (ly:stem::print grob)
  %      Y
  %      % (- (ly:grob-property grob 'direction))
  %      (grob-interpret-markup grob
  % 	(markup #:center-align #:fontsize 3 #:rotate -180
  % 	 #:override '((thickness . 2) (off . 0.5)) #:draw-dotted-line '(0 . 7)))
  %      -2.5))))

#(define (dotted-stem grob)
   (if (ly:stencil? (ly:stem::print grob))
     (let* ((stencil (ly:stem::print grob))
            (X-ext (ly:stencil-extent stencil X))
            (Y-ext (ly:stencil-extent stencil Y))
            (width (interval-length X-ext))
            (len (interval-length Y-ext)))
  (ly:stencil-translate
         (grob-interpret-markup grob
	  (markup
	   (#:override '((thickness . 3) (off . 0.1))
	    #:draw-dotted-line (cons 0 len)))) 
         (cons 0 (interval-start Y-ext))))
      #f))

  % \override Stem.stencil = #path-stem



% {
%   \once \override Stem.stencil =
%   #(lambda (grob)
%     (let* ((x-parent (ly:grob-parent grob X))
% 	   (is-rest? (ly:grob? (ly:grob-object x-parent 'rest))))
%      (if is-rest?
%       empty-stencil
%       (ly:stencil-combine-at-edge
%        (ly:stem::print grob)
%        Y
%        (- (ly:grob-property grob 'direction))
%        (grob-interpret-markup grob
% 	(markup #:center-align #:fontsize 3 #:rotate -180
% 	 #:musicglyph "noteheads.s0doThin"))
%        -2.5))))
% }

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
hideStaff = {\stopStaff \startStaff \omit Staff.StaffSymbol}
showStaff = {\stopStaff \startStaff \undo \omit Staff.StaffSymbol}


vibPath =
#'(
  (moveto 0 0)
  (curveto 0 0 0 1 1 1)
  (curveto 1 1 2 1 2 0)
  (curveto 2 0 2 -1 3 -1)
  (curveto 3 -1 4 -1 4 0)
)

vib = \markup {

  \scale #'(0.3 . 1)
  \path #0.4 #vibPath
  \hspace #-0.71
  \scale #'(0.3 . 0.5)
  \path #0.4 #vibPath
  \hspace #-0.71
  \scale #'(0.3 . 0.2)
  \path #0.4 #vibPath

}
