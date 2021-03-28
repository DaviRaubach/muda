import iracema
import matplotlib.pyplot as plt
import numpy as np
import abjad
import muda
import itertools

class IracemaAnalysis():
	"""
    A class used to get the frequencies of a spectrum and notate them.

    ...

    Attributes
    ----------
    audioin : str
        path to the audio file (.wav)
    nharmonics : int
        number of harmonics to be analyzed
    denominator : int
        denominator of duration (4 = quarter, 8 = eighth, etc.)
        the result is always quarter note = 60BPM

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes

	>>> import muda
	>>> analysis = muda.IracemaAnalysis(
	...     audioin="janela_cut.wav",
	...     nharmonics = 12, 
	...     denominator = 4
	...     )
	>>> analysis.plot_spectrogram()
	>>> container = analysis.abjad_container()
	>>> print(container)
	Container("<f,,, c,, f,, a,, c, dqs, f, g, a, bf, c>4 <f,,, c,, f,, a,, c, dqs, f, g, a, bf, c>4 <a''' e'''' a'''' cs''''' e''''' g''''' a''''' b''''' cs'''''' dqs'''''' e''''''>4 <a''' e'''' a'''' cs''''' e''''' g''''' a''''' b''''' cs'''''' ef'''''' e''''''>4 <f,,, c,, f,, a,, c, dqs, f, g, a, bf, c>4 <a, e a cqs' e' fs' a' b' cqs'' d'' e''>4 <a''' e'''' a'''' cs''''' e''''' g''''' a''''' b''''' cs'''''' dqs'''''' e''''''>4 <g''' d'''' g'''' b'''' d''''' f''''' g''''' a''''' b''''' cs'''''' d''''''>4 <a''' e'''' a'''' cs''''' e''''' g''''' a''''' b''''' cs'''''' dqs'''''' e''''''>4 <a, e a cqs' e' fs' a' b' cqs'' d'' e''>4 <e b e' gqs' b' cs'' e'' fs'' gqs'' a'' b''>4 <a''' e'''' a'''' cs''''' e''''' g''''' a''''' b''''' cs'''''' dqs'''''' e''''''>4 <f c' f' a' c'' dqs'' f'' g'' a'' bf'' c'''>4 <fqs''' cqs'''' fqs'''' aqs'''' cqs''''' ef''''' fqs''''' gqs''''' aqs''''' b''''' cqs''''''>4 <c g c' e' g' aqs' c'' d'' e'' f'' g''>4 <a e' a' cqs'' e'' fs'' a'' b'' cqs''' d''' e'''>4 <a''' e'''' a'''' cs''''' e''''' g''''' a''''' b''''' cs'''''' dqs'''''' e''''''>4 <f c' f' a' c'' dqs'' f'' g'' a'' bf'' c'''>4 <bf''' f'''' bf'''' d''''' f''''' af''''' bf''''' c'''''' d'''''' eqf'''''' f''''''>4 <fs cs' fs' bf' cs'' eqf'' fs'' af'' bf'' b'' cs'''>4 <fs cs' fs' bf' cs'' eqf'' fs'' af'' bf'' b'' cs'''>4 <dqs, aqs, dqs fs aqs c' dqs' eqs' fs' af' aqs'>4")
	>>> 
	"""

	def __init__(self, audioin, nharmonics, denominator):
		"""
        Parameters
        ----------
	    audioin : str
	        path to the audio file (.wav)
	    nharmonics : int
	        number of harmonics to be analyzed
	    denominator : int
        	denominator of duration (4 = quarter, 8 = eighth, etc.)
        	the result is always quarter note = 60BPM
        """
		self.audioin = audioin
		self.nharmonics = nharmonics
		self.denominator = denominator
		self.container = self.abjad_container()

	def abjad_container(self):
		"""Returns the container <code> abjad.Container() </code> with the result.
        """
		audio = iracema.Audio(self.audioin)

		# specifying window and hop sizes
		window, hop = 2048, 1024

		# calculating the FFT
		fft = iracema.spectral.fft(audio, window, hop)
		self.fft = fft

		# extract pitch
		hps_pitch = iracema.pitch.hps(fft, minf0=1, maxf0=1000)

		#extract harmonics
		harmonics = iracema.harmonics.extract(fft, hps_pitch, nharm=self.nharmonics)

		x = harmonics['frequency'].data
		y = harmonics['frequency'].time
		self.x = x
		self.y = y

		myfs = audio.fs/1000
		freq_list = []
		for n, data in enumerate(x):
		    if n != 0:
		        freq_sub_list = []
		        samples = data.shape[0]
		        measure = myfs * 4
		        division = int(measure / self.denominator)
		        for i, d in enumerate(data):
		            if i % division == 0:
		                freq_sub_list.append(d)
		        freq_list.append(freq_sub_list)


		freq_list = np.array(freq_list)

		all_pitches = []
		container = abjad.Container()
		for n in range(freq_list.shape[1]):
			pitches = []
			for i, list_ in enumerate(freq_list):
				pitches.append(abjad.NamedPitch.from_hertz(freq_list[i, n]))
			chord = abjad.Chord("<e' g' c''>4")
			chord.written_duration = abjad.Duration(1, self.denominator)
			chord.written_pitches = pitches
			container.append(chord)

		abjad.attach(abjad.MetronomeMark((1, 4), 60), container[0])
		abjad.attach(abjad.LilyPondLiteral(r'\autoBeamOff'), container[0])

		return container

	def plot_spectrogram(self):
		iracema.plot.plot_spectrogram(self.fft)
		for n, data in enumerate(self.x):
		    plt.plot(self.y, self.x[n])
		plt.show()
	
	def pitch_range_filter(self, pitch_range):
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

	def assign_to_instruments(self, inst_names, inst_noten):
		# inst_names = ["Bass Clarinet", "Piano", "Cello", "Viola", "Alto Flute", "Violino"]
		# inst_noten = [1, 1, 1, 4, 1, 1]
		result = {}
		for chord in self.container:
			chord_notes = iter(chord.written_pitches)
			print(chord.written_pitches)
			for name, number in zip(inst_names, inst_noten):
				result[name] = []
				for n in range(number):
					note = next(chord_notes)
					result[name].append(note)
		return result
	



