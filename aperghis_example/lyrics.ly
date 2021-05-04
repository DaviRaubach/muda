\version "2.20.0"   %! abjad.LilyPondFile._get_format_pieces()
\language "english" %! abjad.LilyPondFile._get_format_pieces()

\new Score
<<
    \new Lyrics
    {
        \lyricmode {o a -- to}
    }
    \context Staff = "Voice"
    {
        c'4
        d'4
        e'4
    }
    \context Staff = "Voice2"
    {
        c'4
        d'4
        e'4
    }
>>