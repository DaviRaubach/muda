				% https://lsr.di.unimi.it/LSR/Item?id=1066

lengthen-gliss = 
#(define-music-function (nmbr)(number?)
#{
  \once \override Glissando.springs-and-rods = #ly:spanner::set-spacing-rods
  \once \override Glissando.minimum-length = #nmbr
#})
            
fancy-gliss =
#(define-music-function (pts-list)(list?)
#{
 \once \override Glissando.after-line-breaking =
  #(lambda (grob)
    (let ((stil (ly:line-spanner::print grob)))
     (if (ly:stencil? stil)
         (let* 
           ((left-bound-info (ly:grob-property grob 'left-bound-info))
            (left-bound (ly:spanner-bound grob LEFT))
            (y-off (assoc-get 'Y left-bound-info))
            (padding (assoc-get 'padding left-bound-info))
            (note-column (ly:grob-parent left-bound X))
            (note-heads (ly:grob-object note-column 'note-heads))
            (ext-X 
              (if (null? note-heads)
                  '(0 . 0)
                  (ly:relative-group-extent note-heads grob X)))
            (dot-column (ly:note-column-dot-column note-column))
            (dots 
              (if (null? dot-column)
                  '()
                  (ly:grob-object dot-column 'dots)))
            (dots-ext-X 
              (if (null? dots)
                  '(0 . 0)
                  (ly:relative-group-extent dots grob X)))
            (factor 
              (/ (interval-length (ly:stencil-extent stil X))
                 (car (take-right (last pts-list) 2))))
            (new-stil
              (make-connected-path-stencil 
                (map
                  (lambda (e)
                    (cond ((= (length e) 2)
                           (cons (* (car e) factor) (cdr e)))
                          ((= (length e) 6)
                           (list
                             (* (car e) factor)
                             (cadr e)
                             (* (third e) factor)
                             (fourth e)
                             (* (fifth e) factor)
                             (sixth e)))
                          (else 
                            (ly:error 
                              "Some element(s) of the given list do not fit"))))   
                  pts-list)
                (layout-line-thickness grob) ;line-width                     
                1   ;scaling
                1   ;scaling
                #f
                #f)))
         (ly:grob-set-property! grob 'stencil
           (ly:stencil-translate
            new-stil
            (cons (+ (interval-length ext-X) 
                     (interval-length dots-ext-X) 
                     padding) 
                  y-off))))
       (begin
         (ly:warning 
           "Cannot find stencil. Please set 'minimum-length accordingly")
         #f))))
#})

%% comment me
%#(display "\n\tLimitations: 
%\t-Does not work with line-break
%\t-dotted notes with glissando may return a warning for unknown reasons,
%\t strange things may happen, if contexts die prematurely")

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% EXAMPLE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% \paper { indent = 28 }

% music = <<
%   \new Staff \with { instrumentName = "fancy-gliss " }
%     \relative c' {
%       \set Score.measureBarType = #""
%       %% If spacing is very tight Glissando sometimes is omitted.
%       %% Use 'lengthen-gliss' with an apropiate value in this case.
%       %\lengthen-gliss #10
%       \override Glissando.cross-staff = ##t
%       \fancy-gliss
%         #'(
%          (1 3)
%          (2 -10)
%          (3 3)
%          (4 1)
%          (5 3.5)
%          (6 0)
%          (7 0 8 5 12 0)
%          )
%       f1\glissando
%       f1
%     }
  
%   \new Staff \with { instrumentName = "skipping a column" }
%     \relative c' {
%       %\lengthen-gliss #10
%       \fancy-gliss
%         #'(
%          (1 3)
%          (2 0)
%          (3 3)
%          (4 1)
%          (5 3.5)
%          (6 0)
%          (7 0 8 5 12 0))
%       f1.
%       \glissando
%       s1
%       f1
%     }
  
%   \new Staff \with { instrumentName = "control-staff " }
%     \relative c' { a'1 a1 a1 a1 }
% >>

%{
\score {
  \transpose c b \music
%% uncomment to let happen very tight spacing happen, use 'lengthen-gliss' then.
% \layout {
%   line-width = 10
% }
}
%}
% 				% 
% \score {
%   \music
%   \layout {
%     ragged-right = ##f
%   }
% }

% { R1 }