stemFlagForText= {
  % https://lsr.di.unimi.it/LSR/Snippet?id=374
  \once \override Stem.stencil =
  #(lambda (grob)
    (let* ((x-parent (ly:grob-parent grob X))
	   (is-rest? (ly:grob? (ly:grob-object x-parent 'rest))))
     (if is-rest?
      empty-stencil
      (ly:stencil-combine-at-edge
       (ly:stem::print grob)
       Y
       (+ (ly:grob-property grob 'direction))
       (grob-interpret-markup grob
	
	(markup  #:beam 0.5 0 0.5))
       ))))
}
aeolAndOrd= {
  % https://lsr.di.unimi.it/LSR/Snippet?id=374
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
       -2.3))))
}

% stemFLagAeol = {
%   \once \override Stem.stencil =
%   #(lambda (grob)
%     (let* ((x-parent (ly:grob-parent grob X))
% 	   (is-rest? (ly:grob? (ly:grob-object x-parent 'rest))))
%      (if is-rest?
%       empty-stencil
%       (ly:stencil-combine-at-edge
%        (ly:stem::print grob)
%        Y
%        (+ (ly:grob-property grob 'direction))
%        (grob-interpret-markup grob
	
% 	(markup  #:beam 0.5 0 0.5))
%        Y
%        (+ (ly:grob-property grob 'direction))
%        (grob-interpret-markup grob
	
% 	(markup
%        #:center-align #:fontsize 3 #:rotate -180
% 	 #:musicglyph "noteheads.s0doThin"))
%        ))))
% }
% aeolAndOrdDotted = {
%   \once \override Stem.stencil =
%   #(lambda (grob)
%     (let* ((x-parent (ly:grob-parent grob X))
% 	   (is-rest? (ly:grob? (ly:grob-object x-parent 'rest))))
%      (if is-rest?
%       empty-stencil
%       (ly:stencil-combine-at-edge
%        (let* ((stencil (ly:stem::print grob))
%             (X-ext (ly:stencil-extent stencil X))
%             (Y-ext (ly:stencil-extent stencil Y))
%             (width (interval-length X-ext))
%             (len (interval-length Y-ext)))
%   (ly:stencil-translate
%          (grob-interpret-markup grob
% 	  (markup
% 	   (#:override '((thickness . 3) (off . 0.1))
% 	    #:draw-dotted-line (cons 0 len)))) 
%          (cons 0 (interval-start Y-ext))))
%        Y
%        (- (ly:grob-property grob 'direction))
%        (grob-interpret-markup grob
% 	(markup #:center-align #:fontsize 3 #:rotate -180
% 	 #:musicglyph "noteheads.s0doThin"))
%        -2.5))))
% }

% slap =
% #(define-music-function (music) (ly:music?)
%   #{
%   \temporary \override NoteHead.stencil =
%   #(lambda (grob)
%     (grob-interpret-markup grob
%      (markup #:musicglyph "scripts.sforzato")))
%   \temporary \override NoteHead.stem-attachment =
%   #(lambda (grob)
%     (let* ((thickness (ly:staff-symbol-line-thickness grob))
% 	   (stem (ly:grob-object grob 'stem))
% 	   (dir (ly:grob-property stem 'direction UP)))
%      (cons 1 (+ (if (= dir DOWN)
% 		 0.5
% 		 0)
% 	      (/ thickness 2)))))
%   #music
%   \revert NoteHead.stencil
%   \revert NoteHead.stem-attachment
%   #})
slap = { \once \override NoteHead.stencil = #ly:text-interface::print
	 \once \override NoteHead.text =
	 \markup 
	 \translate #'(1 . 0) 
	 \override #'(thickness . 1.4) 
	 \overlay {
	   \draw-line #'(-1.2 . 0.4)
	   \draw-line #'(-1.2 . -0.4)
	 }
	 \once \override NoteHead.stem-attachment =
	 #(lambda (grob)
	   (let* ((stem (ly:grob-object grob 'stem))
		  (dir (ly:grob-property stem 'direction UP))
		  (is-up (eqv? dir UP)))
	    (cons dir (if is-up 0 -0.8))))
       }
   % #music

% aeol =
% #(define-music-function (music) (ly:music?)
%   #{
%   \temporary \override NoteHead.stencil =
%   #(lambda (grob)
%     (grob-interpret-markup grob
%      (markup #:center-align  #:vspace -5 #:fontsize 3 #:rotate -180
%       #:musicglyph "noteheads.s0doThin")))

%   % \temporary \override NoteHead.stem-attachment =
%   % #(lambda (grob)
%   %   (let* ((thickness (ly:staff-symbol-line-thickness grob))
%   % 	   (stem (ly:grob-object grob 'stem))
%   % 	   (dir (ly:grob-property stem 'direction UP)))
%   %    (cons 1 (+ (if (= dir DOWN)
%   % 		 0.5
%   % 		 0)
%   % 	      (/ thickness 2)))))
%   #music
%   \revert NoteHead.stencil
%   % \revert NoteHead.stem-attachment
%   #})

aeol = {
  \once \override Voice.NoteHead.stencil = #ly:text-interface::print
  \once \override Voice.NoteHead.text = \markup { \center-align  \vspace #-5 \fontsize #3 \rotate #-180 \musicglyph "noteheads.s0doThin"}
  }
  
upT = {
  \set stemLeftBeamCount = #0
  \once \autoBeamOff
  \once \override Stem.direction = #down
  \once \override Stem.X-offset = #0.622
  \once \override Stem.Y-offset  = #-0.2
  \once \override Stem.length-fraction  = #1.12
  \once \override NoteHead.stencil = #ly:text-interface::print
  \once \override NoteHead.text =
  \markup {
    \path #0.13
    #'((moveto -.1775 -.43)8
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
  \once \override NoteHead.stencil = #ly:text-interface::print
  \once \override NoteHead.text = \markup {
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
  \once \override NoteHead.stencil = #ly:text-interface::print
  \once \override NoteHead.text =
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
  \once \override NoteHead.stencil = #ly:text-interface::print
  \once \override NoteHead.text = \markup {
    \path #0.13
    #'((moveto  -.0775 .43)
       (lineto  .65625 -.43 )
       (lineto 1.39 .43)
       (closepath))
  }
}
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
