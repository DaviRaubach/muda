\version "2.20.0"   %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

\include "/Users/Davi/github/muda/aperghis_example/aperghis_stylesheet.ily" %! abjad.LilyPondFile._get_formatted_includes()


\markuplist {
  \right-column {
    \pad-around #1
    \score-lines {
      \include "/Users/Davi/github/muda/aperghis_example/aperghis_score.ly"
    }
  }
}