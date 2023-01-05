% #(define-markup-command (casa-x layout props text) (markup?)
%   #:properties ()
%   "Draw a double box around text."
%   (interpret-markup layout props
%     #{\markup \fontsize #-2 { #text } #})) 
\version "2.23.9"
casaIV = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " IV"
} 
casaV = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " V"
} 
casaVII = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " VII"
} 
casaIX = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " IX"
} 
casaXII = \markup \concat {
  \combine
  \fontsize #-2 \roman C 
  \translate #'(0.6 . -0.4) \draw-line #'(0 . 2.0) 
  \fontsize #-2 " XII"
} 
