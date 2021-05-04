import abjad
import muda





# myinst = muda.Instrument(
#     abjad_instrument=abjad.SopranoVoice(),
#     name="Soprano",
#     nstaffs=1,
#     nvoices=[2])
# mylyr = muda.Lyrics(name="lyrics")

# mat = muda.Material("Soprano_Voice_1")
# mat.write("c'4 d'4 e'4")
# lyrics = muda.Material("lyrics")
# lyrics.write_lyrics("o a -- to")
# materials_list = [mat, lyrics]

# myscore = muda.Score()
# myscore.append([myinst, mylyr])
# myscore.write_materials(materials_list)
# myscore.lilypond()
# myscore.show()



staff = abjad.Staff("c'4 d'4 e'4", name="Voice")
staff2 = abjad.Staff("c'4 d'4 e'4", name="Voice2")
cont = abjad.Context(lilypond_type='Lyrics', name="this")
abjad.attach(abjad.LilyPondLiteral(r'\lyricmode {o a -- to}'), cont)

score = abjad.Score([staff, cont], simultaneous=True)
print(score["this"])

# score.append(staff2)

# selection = abjad.select(score).components(abjad.Staff)
# for i, item in enumerate(selection):
#     score.insert(i, cont)
#     print(item)

# # score.insert(0, cont)
# # lyrics = abjad.LilyPondLiteral(r' \addlyrics {\lyricmode {o a -- to}}'))
# # abjad.attach(lyrics, score)
# # score.insert(0, staff)
# lilypond_file = abjad.LilyPondFile(items=[score])
# abjad.persist.as_ly(lilypond_file, "lyrics.ly")
# # abjad.show(lilypond_file)
# print(abjad.lilypond(lilypond_file))
