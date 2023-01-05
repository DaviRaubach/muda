mVinteOito = \markup {
  \scale #'(0.5 . 0.5)
  \whiteout
				% \override #'(graphical . #f)
  % \combine 
  % \woodwind-diagram #'bass-clarinet #'()
  \woodwind-diagram #'bass-clarinet
                    #'((cc . (one two three four five six))
                       (lh . (R thumb f cis))
                       (rh . (fis)))
} 

mTres = \markup {
  \scale #'(0.5 . 0.5)
  \whiteout
  % \combine 
  % \woodwind-diagram #'bass-clarinet #'()
  % \override #'(graphical . #f)
  \woodwind-diagram #'bass-clarinet
                    #'((cc . (one two three four six))
                       (lh . (R thumb fis))
                       (rh . ()))
"multifônico" } 
mQuinze = \markup {
  \scale #'(0.5 . 0.5)
  \whiteout
  % \combine 
  % \woodwind-diagram #'bass-clarinet #'()
  % \override #'(graphical . #f)
  \woodwind-diagram #'bass-clarinet
                    #'((cc . (one two three))
                       (lh . (R thumb gis))
                       (rh . ()))
"multifônico" } 
mOito = \markup {
  \scale #'(0.5 . 0.5)
  \whiteout
  % \combine 
  % \woodwind-diagram #'bass-clarinet #'()
  % \override #'(graphical . #f)
  \woodwind-diagram #'bass-clarinet
                    #'((cc . (one two three four six))
                       (lh . ())
                       (rh . (e)))
"multifônico" } 

