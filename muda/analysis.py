"""
Todo.

Todo.
"""

import iracema
import matplotlib.pyplot as plt
import numpy as np
import abjad
import json
import evans
from abjadext import microtones


class IracemaAnalysis():
    r"""Gets the frequencies of a spectrum and notate them.

    Atributes
        audioin: str
            path to the audio file (.wav)
        nharmonics: int
            number of harmonics to be analyzed
        denominator: int
            denominator of duration (4 = quarter, 8 = eighth, etc.)
            the result is always quarter note = 60BPM

    >>> import muda
    >>> import abjad
    >>> analysis = muda.IracemaAnalysis(
    ...     audioin="cataventos31.wav",
    ...     nharmonics=16,
    ...     denominator=4,
    ...     # minf0=55,
    ...     # maxf0=588,
    ... )
    >>> analysis.abjad_container()
    Container("<a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <gqs'' dqs''' gqs''' b''' dqs'''' f'''' gqs'''' aqs'''' b'''' cs''''' dqs''''' e''''' f''''' gqf''''' gqs'''''>4 <af'' dqs''' gqs''' bqs''' dqs'''' f'''' gqs'''' aqs'''' b'''' cs''''' dqs''''' e''''' f''''' fs''''' gqs'''''>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <g' d'' g'' b'' d''' f''' g''' a''' b''' cs'''' d'''' e'''' f'''' fs'''' g''''>4 <g' d'' g'' b'' d''' f''' g''' a''' b''' cs'''' d'''' e'''' f'''' fs'''' g''''>4 <gqs' ef'' af'' bqs'' ef''' fqs''' af''' bf''' bqs''' cs'''' ef'''' e'''' fqs'''' gqf'''' af''''>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <af'' ef''' af''' bqs''' ef'''' f'''' af'''' bf'''' bqs'''' cs''''' ef''''' e''''' fqs''''' gqf''''' af'''''>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <b'' fs''' b''' ef'''' fs'''' a'''' b'''' cs''''' ef''''' f''''' fs''''' af''''' a''''' bf''''' b'''''>4 <b'' fs''' b''' ef'''' fs'''' a'''' b'''' cs''''' ef''''' eqs''''' fs''''' gqs''''' a''''' bf''''' b'''''>4 <bqf'' f''' bf''' d'''' fqs'''' af'''' bqf'''' cqs''''' d''''' e''''' fqs''''' g''''' af''''' a''''' bqf'''''>4 <bqf'' fqs''' bqf''' d'''' fqs'''' af'''' bqf'''' cqs''''' d''''' e''''' fqs''''' g''''' af''''' a''''' bqf'''''>4 <bf'' f''' bf''' d'''' f'''' af'''' bf'''' c''''' d''''' e''''' f''''' g''''' af''''' a''''' bf'''''>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <gqs'' dqs''' gqs''' b''' dqs'''' f'''' gqs'''' aqs'''' b'''' cs''''' dqs''''' e''''' f''''' gqf''''' gqs'''''>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <bf' f'' bf'' d''' f''' af''' bf''' c'''' d'''' e'''' f'''' g'''' af'''' a'''' bf''''>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4 <bf' f'' bf'' d''' f''' af''' bf''' c'''' d'''' e'''' f'''' g'''' af'''' a'''' bf''''>4 <a,, e, a, cqs e fs a b cqs' d' e' f' fs' gqs' a'>4")
    >>> analysis.select_chords([8, 9, 23])
    >>> analysis.in_hertz()
    Saved in chords_in_hertz.txt
    [[398.3642578125, 597.54638671875, 796.728515625, 995.91064453125, 1195.0927734375, 1394.27490234375, 1593.45703125, 1792.63916015625, 1991.8212890625, 2191.00341796875, 2390.185546875, 2589.36767578125, 2788.5498046875, 2987.73193359375, 3186.9140625], [403.74755859375, 613.6962890625, 818.26171875, 1022.8271484375, 1227.392578125, 1431.9580078125, 1636.5234375, 1841.0888671875, 2045.654296875, 2250.2197265625, 2449.40185546875, 2659.3505859375, 2863.916015625, 3068.4814453125, 3273.046875], [473.73046875, 710.595703125, 947.4609375, 1184.326171875, 1415.80810546875, 1652.67333984375, 1894.921875, 2131.787109375, 2368.65234375, 2605.517578125, 2842.3828125, 3079.248046875, 3316.11328125, 3552.978515625, 3789.84375]]
    >>> abjad.show(analysis.container)

    .. lily::
        :noedge:
        :audio:

        \version "2.20.0"
        \language "english"
        \new Staff {
            <g' d'' g'' b'' d''' f''' g''' a''' b''' cs'''' d'''' e'''' f'''' fs'''' g''''>4
            ^ \markup { 8 }
            <gqs' ef'' af'' bqs'' ef''' fqs''' af''' bf''' bqs''' cs'''' ef'''' e'''' fqs'''' gqf'''' af''''>4
            ^ \markup { 9 }
            <bf' f'' bf'' d''' f''' af''' bf''' c'''' d'''' e'''' f'''' g'''' af'''' a'''' bf''''>4
            ^ \markup { 23 }
        }

    """

    def __init__(self, audioin, nharmonics, denominator, minf0=24, maxf0=4200):
        """Todo.

        Parameters
        ----------
           audioin : str
                path to the audio file (.wav)
           nharmonics : int
                number of harmonics to be analyzed
           denominator : int
            denominator of duration (4 = quarter, 8 = eighth, etc.)
            the result is always quarter note = 60BPM

        :meta public:
        """
        self.audioin = audioin
        self.nharmonics = nharmonics
        self.denominator = denominator
        self.minf0 = minf0
        self.maxf0 = maxf0
        self.container = self.abjad_container()
        self.chords_in_hertz = []

    def abjad_container(self):
        """Return the container ``abjad.Container()`` with the result."""
        def hz_to_midi(f, f_a4_in_hz=440):
            return (69 + 12 * np.log2(f / f_a4_in_hz))

        audio = iracema.Audio(self.audioin)
        # specifying window and hop sizes
        window, hop = 2048, 1024
        # calculating the FFT
        fft = iracema.spectral.fft(audio, window, hop)
        self.fft = fft
        # extract pitch
        hps_pitch = iracema.pitch.hps(fft, minf0=self.minf0, maxf0=self.maxf0)
        # extract harmonics
        harmonics = iracema.harmonics.extract(
            fft,
            hps_pitch,
            nharm=self.
            nharmonics,
            minf0=self.minf0,
            maxf0=self.maxf0)

        x = harmonics['frequency'].data
        y = harmonics['frequency'].time
        self.x = x
        self.y = y
        myfs = audio.fs / 1000
        freq_list = []
        for n, data in enumerate(x):
            if n != 0:
                freq_sub_list = []
                # samples = data.shape[0]
                measure = myfs * 4
                division = int(measure / self.denominator)
                for i, d in enumerate(data):
                    if i % division == 0:
                        freq_sub_list.append(d)
                freq_list.append(freq_sub_list)
        freq_list = np.array(freq_list)
        # all_pitches = []
        chords_in_hertz = []
        container = abjad.Container()
        for n in range(freq_list.shape[1]):
            pitches = []
            chord_in_hertz = []
            for i, list_ in enumerate(freq_list):
                chord_in_hertz.append(freq_list[i, n])
                numberedp = (hz_to_midi(freq_list[i, n], 440) - 60)
                roundedp = evans.to_nearest_twelfth_tone(numberedp)
                pitches.append(roundedp)
                # pitches.append(abjad.NamedPitch.from_hertz(freq_list[i, n]))
            chord = abjad.Chord("<e' g' c''>4")
            chord.written_duration = abjad.Duration(1, self.denominator)
            chord.written_pitches = pitches
            container.append(chord)
            chords_in_hertz.append(chord_in_hertz)
        abjad.attach(abjad.MetronomeMark((1, 4), 60), container[0])
        abjad.attach(abjad.LilyPondLiteral(r'\autoBeamOff'), container[0])
        selection = abjad.select(container).leaves()
        for i, leaf in enumerate(selection):
            abjad.attach(
                abjad.Markup(str(i), direction=abjad.Up), leaf,
            )
        self.container = container
        self.chords_in_hertz = chords_in_hertz
        return container

    def select_chords(self, chords_list):
        """Todo."""
        selection = abjad.select(self.container).leaves()
        new_container = abjad.Container()
        new_hertz_list = []
        for i in chords_list:
            new_container.append(selection[i])
            new_hertz_list.append(self.chords_in_hertz[i])
        self.container = new_container
        self.chords_in_hertz = new_hertz_list

    def plot_spectrogram(self):
        """Todo."""
        iracema.plot.plot_spectrogram(self.fft)
        for n, data in enumerate(self.x):
            plt.plot(self.y, self.x[n])
            plt.show()

    def pitch_range_filter(self, pitch_range):
        """Todo."""
        rangein = abjad.PitchRange(pitch_range)
        for chord in self.container:
            pitches = []
            for note in chord.written_pitches:
                if note in rangein:
                    pitches.append(note)
                else:
                    pass
                chord.written_pitches = pitches
        return self.container

    def in_hertz(self):
        """Get list of chords in hertz and save as .txt file."""
        f = open("chords_in_hertz.txt", "w")
        f.write(str(self.chords_in_hertz))
        f.close()
        print("Saved in chords_in_hertz.txt")
        return self.chords_in_hertz

    def assign_to_instruments(self, inst_names, inst_noten):
        """Distribute analyzed pitches to different instruments.

        inst_noten: number of pitches assigned for each specified instrument
        (inst_names), for each chord analyzed.

        Save the result in a .json file.

        """
        # inst_names = ["Bass Clarinet", "Piano"]
        # inst_noten = [4, 1]
        result = {}
        save_dict = {}
        for name in inst_names:
            result[name] = []
            save_dict[name] = []
        for chord in self.container:
            chord_ = []
            str_chord = []
            chord_notes = iter(chord.written_pitches)
            # print(chord.written_pitches)
            for name, number in zip(inst_names, inst_noten):
                for n in range(number):
                    note = next(chord_notes)
                    chord_.append(note)
                    str_chord.append(note.name)
                result[name].append(chord_)
                save_dict[name].append(str_chord)
        file_str = ""
        for item in result:
            file_str = file_str + item + "_"
        file_str = file_str + "pitches.json"
        a_file = open(file_str, "w")
        json.dump(save_dict, a_file)
        print("Saved in", file_str)
        a_file.close()
