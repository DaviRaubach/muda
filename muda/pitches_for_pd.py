import abjad
import random
from organi.tools.see_pitches import see_pitches

# RECURSES TO MODIFY PITCH SEGMENTS
# A C B D C E
def permut_thirds(pitches):
    pitch_list = []
    i = 0
    pitch_list.append(pitches[i])
    while i < len(pitches) - 2:
        i = i + 2
        note = pitches[i]
        pitch_list.append(note)
        i = i - 1
        note = pitches[i]
        pitch_list.append(note)
    return pitch_list


# FREQ_B - FREQ_A AND FREQ_B + FREQ_A
def ring_modulation(pitches, sum=True, chords=False):
    pitches_in = pitches.hertz
    pitches_out = []
    if sum is True and chords is False:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            new_pitch_A = pitch2 - pitch1
            pitches_out.append(new_pitch_A)
            pitches_out.append(pitch1)
            new_pitch_B = pitch1 + pitch2
            pitches_out.append(new_pitch_B)
    if sum is False and chords is False:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            new_pitch_A = pitch2 - pitch1
            pitches_out.append(new_pitch_A)
            new_pitch_B = pitch1 + pitch2
            pitches_out.append(new_pitch_B)
    if sum is True and chords is True:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            new_pitch_A = pitch2 - pitch1
            new_pitch_B = pitch1 + pitch2
            new_pitch_A = abjad.NamedPitch.from_hertz(new_pitch_A)
            new_pitch_B = abjad.NamedPitch.from_hertz(new_pitch_B)
            pitch1 = abjad.NamedPitch.from_hertz(pitch1)
            chord = abjad.Chord([new_pitch_A, pitch1, new_pitch_B], (1, 1))
            pitches_out.append(chord)
    if sum is False and chords is True:
        for pitch1, pitch2 in zip(pitches_in, pitches_in[1:]):
            new_pitch_A = pitch2 - pitch1
            new_pitch_B = pitch1 + pitch2
            new_pitch_A = abjad.NamedPitch.from_hertz(new_pitch_A)
            new_pitch_B = abjad.NamedPitch.from_hertz(new_pitch_B)
            chord = abjad.Chord([new_pitch_A, new_pitch_B], (1, 1))
            print(chord)
            pitches_out.append(chord)
    return pitches_out


# ORIGINAL CHORD
pitches = []
original_chord = abjad.pitch.PitchSegment(
    "cqs' f' gs' c'' e'' ftqs'' gqs''"
    + " gs'' b'' cs''' ctqs''' f''' fs''' ftqs'''  gs'''"
    )
pitches = ring_modulation(original_chord, sum=True)
# pitches.sort()
print(pitches)
pitches = [abjad.NamedPitch.from_hertz(_) for _ in pitches]
electronics_pitches = list.copy(pitches)
num_pitches = [abjad.NamedPitch(_).number for _ in pitches]
# NO MICROTONAL
for item, i in zip(num_pitches, range(len(num_pitches))):
    if isinstance(item, float):
        item = item - 0.5
        num_pitches[i] = item
named_pitches = [abjad.NumberedPitch(_).get_name() for _ in num_pitches]
num_pitches_rev = num_pitches
num_pitches_rev.sort(reverse=True)
num_pitches_rev = permut_thirds(num_pitches_rev)
pitch_range = abjad.PitchRange("[C2, G7]")
pitch_list = []
for i, pitch in enumerate(num_pitches_rev):
    test = pitch in pitch_range
    if test is True:
        pitch_list.append(pitch)
        
pitches = abjad.pitch.PitchSegment(pitch_list)
staff_group = see_pitches(pitches)
pitches_voice_one = pitches
# abjad.f(pitches_voice_one)
pitches_voice_four = pitches[7:]
# abjad.f(pitches_voice_four)




# para funcionar com a debaixo 
# conforme primeira versão
# não pode fazer o retrogrado (sort reverse)
# nem fazer as terças
# select notes
# modifiquei para num_pitches_rev para poder funcionar tanto o de cima quanto o de baixo
chord_down = []
notes_down = [8, 9, 11, 12, 13, 14]
for i, note in enumerate(num_pitches):
    if i in notes_down:
        chord_down.append(note)

chord_up = []
notes_up = [15, 16, 17, 18, 19, 20]
for i, note in enumerate(num_pitches):
    if i in notes_up:
        chord_up.append(note)

chord_up_longer = []
chord_down_longer = []

for i in range(8):
    random.seed(i+3)
    random.shuffle(chord_up)
    random.seed(i+3)
    random.shuffle(chord_down)
    for note_up in chord_up:
        chord_up_longer.append(note_up)
    for note_down in chord_down:
        chord_down_longer.append(note_down)




