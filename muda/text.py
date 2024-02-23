import abjad
import muda
# sílaba, nota para régua, número de notas para música
# neste caso, 5 seria 4 grace notes mais uma semínima


def make_lyrics_rule_and_music(verses=list[list]):
    lyrics = []
    rule = abjad.Container()
    music = abjad.Container()
    for i, verse in enumerate(verses):
        # sílaba, nota para régua, número de notas para música
        # neste caso, 5 seria 4 grace notes mais uma semínima
        vlyr = ""
        vrule = abjad.Container(name="r1")
        vmusic = abjad.Container(name="m1")
        for tup in v1:
            # lyrics
            vlyr += tup[0] + " "

            # rule
            if tup[1] > 0:
                vrule.append(abjad.Note("c'4", multiplier=(tup[1])))
            elif tup[1] < 0:
                vrule.append(abjad.Rest((1, 4), multiplier=(abs(tup[1]))))

            # music
            if tup[2] > 0:
                grace_string = ""
                note = abjad.Note("c'4", multiplier=(tup[1]))
                if tup[2] > 1:
                    for i in range(tup[2]-1):
                        grace_string += "c'16 "
                        grace = abjad.BeforeGraceContainer(grace_string)
                        abjad.attach(grace, note)
                vmusic.append(note)
            elif tup[2] < 0:
                vmusic.append(abjad.Rest((1, 4), multiplier=(abs(tup[1]))))

        def articulations(attachable):
            # articulations
            if tup[3]:
                for string in tup[3:]:
                    if string == "(":
                        abjad.attach(abjad.StartSlur(), attachable)
                    if string == ")":
                        abjad.attach(abjad.StopSlur(), attachable)
                    if abjad.is_articulation:
                        abjad.attach(abjad.Articulation(string), attachable)
        lyrics.append(vlyr)
        rule.extend(vrule)
        music.extend(vmusic)

    return lyrics, rule, music


def main():
    v1 = [
        ('we', 1, 1, "(", ".", "pp"),
        ('dream', 1, 5),
        ('to --', 1, 1),
        ('ge --', 1, 1),
        ('ther', 1, 2),
        ('', -1, -1),
        ('we', 1, -1),
        ('"wake up and"', 3, 1),
        ('keep', 1, 1),
        ('drea --', 1, 5),
        ('ming', 1, 1)
    ]
    verses = [v1]

    lyrics, rule, music = make_lyrics_rule_and_music(verses)
    # rule = abjad.mutate.eject_contents(rule[0])
    # print(v1lyr)
    # print(abjad.lilypond(v1rule))
    # print(abjad.lilypond(v1music))
    lyr = abjad.Context(
        lilypond_type="Lyrics",
        name="lyr",
    )
    align_str = r" \override LyricText.self-alignment-X = #LEFT  \override LyricText.X-offset = #-1 "
    print(lyrics)
    lit = abjad.LilyPondLiteral(
        r'\lyricsto "'
        + "v1rule"
        + r'" { \lyricmode {'
        + align_str + r' '
        + lyrics[0]
        + "}}"
    )
    abjad.attach(lit, lyr)

    v1rule = abjad.Voice([rule], lilypond_type="NullVoice", name="v1rule")
    v1music = abjad.Voice([music], name="v1music")
    muda.pitch.write_pitches(music, [24])
    staff = abjad.Staff([v1rule, lyr, v1music], simultaneous=True)

    lf = abjad.LilyPondFile(
        items=[

            r'\include "org_stylesheet.ily"',
            r'\paper { page-breaking = #ly:one-line-auto-height-breaking }',
            staff
        ]
    )

    abjad.persist.as_pdf(lf, "texst.pdf")


if __name__ == "__main__":
    main()
