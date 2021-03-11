#!/usr/local/bin/python3
import os
import abjad
import organi


class SegmentMaker(abjad.SegmentMaker):
    """
    Segment-maker.
    """

    # INITIALIZER #

    def __init__(
        self,
        time_signatures=None,
        post_process_staffgroup=None,
        durations_voice_one=None,
        rhythm_maker_voice_one=None,
        pitches_voice_one=None,
        initial_rest_voice_one=None,
        legato_voice_one=False,
        chords_voice_one=None,
        make_those_chords_voice_one=False,
        rest_interval_voice_one=None,
        post_process_voice_one=None,
        durations_voice_two=None,
        rhythm_maker_voice_two=None,
        pitches_voice_two=None,
        initial_rest_voice_two=None,
        legato_voice_two=False,
        chords_voice_two=None,
        make_those_chords_voice_two=False,
        rest_interval_voice_two=None,
        post_process_voice_two=None,
        durations_voice_three=None,
        rhythm_maker_voice_three=None,
        pitches_voice_three=None,
        initial_rest_voice_three=None,
        legato_voice_three=False,
        chords_voice_three=None,
        make_those_chords_voice_three=False,
        rest_interval_voice_three=None,
        post_process_voice_three=None,
        durations_voice_four=None,
        rhythm_maker_voice_four=None,
        pitches_voice_four=None,
        initial_rest_voice_four=None,
        legato_voice_four=False,
        chords_voice_four=None,
        make_those_chords_voice_four=False,
        rest_interval_voice_four=None,
        post_process_voice_four=None,
        durations_voice_five=None,
        rhythm_maker_voice_five=None,
        pitches_voice_five=None,
        initial_rest_voice_five=None,
        legato_voice_five=False,
        chords_voice_five=None,
        make_those_chords_voice_five=False,
        rest_interval_voice_five=None,
        post_process_voice_five=None,
        chords_voice_one_elec=None,
        post_process_electronics=None,
        make_measures_pitched=True,
        indicators=None,
        includes=None,
        collect=True,
    ):
        assert len(time_signatures)
        self.time_signatures = time_signatures

        self.score_template = organi.ScoreTemplate()

        self.post_process_staffgroup = post_process_staffgroup

        self.durations_voice_one = durations_voice_one
        self.rhythm_maker_voice_one = rhythm_maker_voice_one
        self.pitches_voice_one = pitches_voice_one
        self.initial_rest_voice_one = initial_rest_voice_one
        self.legato_voice_one = legato_voice_one
        self.chords_voice_one = chords_voice_one
        self.make_those_chords_voice_one = make_those_chords_voice_one
        self.rest_interval_voice_one = rest_interval_voice_one
        self.post_process_voice_one = post_process_voice_one

        self.rhythm_maker_voice_two = rhythm_maker_voice_two
        self.durations_voice_two = durations_voice_two
        self.pitches_voice_two = pitches_voice_two
        self.initial_rest_voice_two = initial_rest_voice_two
        self.legato_voice_two = legato_voice_two
        self.chords_voice_two = chords_voice_two
        self.make_those_chords_voice_two = make_those_chords_voice_two
        self.rest_interval_voice_two = rest_interval_voice_two
        self.post_process_voice_two = post_process_voice_two

        self.rhythm_maker_voice_three = rhythm_maker_voice_three
        self.durations_voice_three = durations_voice_three
        self.pitches_voice_three = pitches_voice_three
        self.initial_rest_voice_three = initial_rest_voice_three
        self.legato_voice_three = legato_voice_three
        self.chords_voice_three = chords_voice_three
        self.make_those_chords_voice_three = make_those_chords_voice_three
        self.rest_interval_voice_three = rest_interval_voice_three
        self.post_process_voice_three = post_process_voice_three

        self.rhythm_maker_voice_four = rhythm_maker_voice_four
        self.durations_voice_four = durations_voice_four
        self.pitches_voice_four = pitches_voice_four
        self.initial_rest_voice_four = initial_rest_voice_four
        self.legato_voice_four = legato_voice_four
        self.chords_voice_four = chords_voice_four
        self.make_those_chords_voice_four = make_those_chords_voice_four
        self.rest_interval_voice_four = rest_interval_voice_four
        self.post_process_voice_four = post_process_voice_four

        self.rhythm_maker_voice_five = rhythm_maker_voice_five
        self.durations_voice_five = durations_voice_five
        self.pitches_voice_five = pitches_voice_five
        self.initial_rest_voice_five = initial_rest_voice_five
        self.legato_voice_five = legato_voice_five
        self.chords_voice_five = chords_voice_five
        self.make_those_chords_voice_five = make_those_chords_voice_five
        self.rest_interval_voice_five = rest_interval_voice_five
        self.post_process_voice_five = post_process_voice_five

        self.chords_voice_one_elec = chords_voice_one_elec
        self.post_process_electronics = post_process_electronics

        self.make_measures_pitched = make_measures_pitched
        self.includes = includes
        self.collect = collect

    # PUBLIC METHODS #

    def run(
        self, metadata=None, midi=None, previous_metadata=None,
    ) -> abjad.LilyPondFile:
        """
        Runs segment-maker.
        """
        self._metadata = metadata
        self.midi = midi
        self.previous_metadata = previous_metadata

        score = self.score_template()

        # SKIPS #######################################################################

        assert len(self.time_signatures)
        time_signatures_abjad = [abjad.TimeSignature(_) for _ in self.time_signatures]
        for time_sig in time_signatures_abjad:
            skip = abjad.Skip(1, multiplier=(time_sig))
            # print(skip)
            score["Global_Context"].append(skip)
        global_context = score["Global_Context"]
        for time_sig in time_signatures_abjad:
            skip = abjad.Skip(1, multiplier=(time_sig))
            # print(skip)
            score["Global_Context_II"].append(skip)
            # score["Global_Context_III"].append(skip)
        print("making skips")

        # select skips to attach TIME SIGNATURES

        mylist = self.time_signatures
        for i, element in enumerate(mylist):
            previous_element = mylist[i - 1] if i > 0 else None
            current_element = element
            # next_element = mylist[i+1] if i < len(mylist)-1 else None
            if current_element != previous_element:
                i = mylist.index(current_element)
                abjad.attach(
                    time_signatures_abjad[i],
                    global_context[i],
                    tag=abjad.Tag("scaling time signatures"),
                )

        # VOICE ONE ###################################################################

        voice_one = score["RH_Voice_One"]

        # initial rest
        if self.initial_rest_voice_one is not None:
            rh_voice_one_initial_rest = self._make_initial_rest(
                self.initial_rest_voice_one
            )
            voice_one.extend(rh_voice_one_initial_rest)
            print("making initial rest voice one")

        # make measures

        if (
            self.durations_voice_one is not None
            and self.make_those_chords_voice_one is False
        ):
            rh_voice_one_measures = self._make_measures(
                self.durations_voice_one,
                self.rhythm_maker_voice_one,
                self.pitches_voice_one,
                self.legato_voice_one,
            )
            voice_one.extend(rh_voice_one_measures)
            print("making measures voice one")

        # make chords

        if self.chords_voice_one is not None:
            rh_voice_one_chords = self._make_chords(self.chords_voice_one)
            voice_one.extend(rh_voice_one_chords)
            print("making chords voice one")

        # make those chords

        if self.make_those_chords_voice_one is True:
            measures = self._make_those_chords(
                self.time_signatures,
                self.durations_voice_one,
                self.rhythm_maker_voice_one,
                self.pitches_voice_one,
                self.rest_interval_voice_one,
            )
            voice_one.extend(measures)

            self._rewrite_meter_and_tie(voice_one, self.time_signatures)
            print("making those chords voice one, rewriting meter, and attaching ties")

        # rewrite meter

        if self.durations_voice_one or self.chords_voice_one is not None:
            if self.make_those_chords_voice_one is False:
                voice_one = voice_one
                self._rewrite_meter(voice_one, self.time_signatures)
                print("rewriting meter voice one")

        # attach indicators
        if self.post_process_voice_one is not None:
            self.post_process_voice_one(voice_one, score)

        # VOICE TWO ###################################################################

        voice_two = score["RH_Voice_Two"]

        # initial rest
        if self.initial_rest_voice_two is not None:
            rh_voice_two_initial_rest = self._make_initial_rest(
                self.initial_rest_voice_two
            )
            voice_two.extend(rh_voice_two_initial_rest)
            print("making initial rest voice two")

        # make measures

        if (
            self.durations_voice_two is not None
            and self.make_those_chords_voice_two is False
        ):
            rh_voice_two_measures = self._make_measures(
                self.durations_voice_two,
                self.rhythm_maker_voice_two,
                self.pitches_voice_two,
                self.legato_voice_two,
            )
            voice_two.extend(rh_voice_two_measures)
            print("making measures voice two")

        # make chords

        if self.chords_voice_two is not None:
            rh_voice_two_chords = self._make_chords(self.chords_voice_two)
            voice_two.extend(rh_voice_two_chords)
            print("making chords voice two")

        # make those chords

        if self.make_those_chords_voice_two is True:
            measures = self._make_those_chords(
                self.time_signatures,
                self.durations_voice_two,
                self.rhythm_maker_voice_two,
                self.pitches_voice_two,
                self.rest_interval_voice_two,
            )
            voice_two.extend(measures)

            self._rewrite_meter_and_tie(voice_two, self.time_signatures)
            print("making those chords voice two, rewriting meter, and attaching ties")

        # rewrite meter

        if self.durations_voice_two or self.chords_voice_two is not None:
            if self.make_those_chords_voice_two is False:
                voice_two = voice_two
                self._rewrite_meter(voice_two, self.time_signatures)
                print("rewriting meter voice two")

        # attach indicators
        if self.post_process_voice_two is not None:
            self.post_process_voice_two(voice_two, score)

        # VOICE THREE #################################################################

        voice_three = score["RH_Voice_Three"]

        # initial rest
        if self.initial_rest_voice_three is not None:
            rh_voice_three_initial_rest = self._make_initial_rest(
                self.initial_rest_voice_three
            )
            voice_three.extend(rh_voice_three_initial_rest)
            print("making initial rest voice three")

        # make measures

        if (
            self.durations_voice_three is not None
            and self.make_those_chords_voice_three is False
        ):
            rh_voice_three_measures = self._make_measures(
                self.durations_voice_three,
                self.rhythm_maker_voice_three,
                self.pitches_voice_three,
                self.legato_voice_three,
            )
            voice_three.extend(rh_voice_three_measures)
            print("making measures voice three")

        # make chords

        if self.chords_voice_three is not None:
            rh_voice_three_chords = self._make_chords(self.chords_voice_three)
            voice_three.extend(rh_voice_three_chords)
            print("making chords voice three")

        # make those chords

        if self.make_those_chords_voice_three is True:
            measures = self._make_those_chords(
                self.time_signatures,
                self.durations_voice_three,
                self.rhythm_maker_voice_three,
                self.pitches_voice_three,
                self.rest_interval_voice_three,
            )
            voice_three.extend(measures)

            self._rewrite_meter_and_tie(voice_three, self.time_signatures)
            print(
                "making those chords voice three, rewriting meter, and attaching ties"
            )

        # rewrite meter

        if self.durations_voice_three or self.chords_voice_three is not None:
            if self.make_those_chords_voice_three is False:
                voice_three = voice_three
                self._rewrite_meter(voice_three, self.time_signatures)
                print("rewriting meter voice three")

        # attach indicators
        if self.post_process_voice_three is not None:
            self.post_process_voice_three(voice_three)
            self._rewrite_meter(voice_three, self.time_signatures)

        # VOICE FOUR (LEFT HAND) ######################################################

        voice_four = score["LH_Voice_Four"]
        # initial rest

        if self.initial_rest_voice_four is not None:
            lh_voice_four_initial_rest = self.initial_rest_voice_four
            voice_four.extend(lh_voice_four_initial_rest)
            print("making initial rest voice four")

        # make measures

        if (
            self.durations_voice_four is not None
            and self.make_those_chords_voice_four is False
        ):
            lh_voice_four_measures = self._make_measures(
                self.durations_voice_four,
                self.rhythm_maker_voice_four,
                self.pitches_voice_four,
                self.legato_voice_four,
            )
            voice_four.extend(lh_voice_four_measures)
            print("making measures voice four")

        # make chords

        if self.chords_voice_four is not None:
            lh_voice_four_chords = self._make_chords(self.chords_voice_four)
            voice_four.extend(lh_voice_four_chords)
            print("making chords voice four")

        # make those chords

        if self.make_those_chords_voice_four is True:
            measures = self._make_those_chords(
                self.time_signatures,
                self.durations_voice_four,
                self.rhythm_maker_voice_four,
                self.pitches_voice_four,
                self.rest_interval_voice_four,
            )
            voice_four.extend(measures)
            self._rewrite_meter_and_tie(voice_four, self.time_signatures)
            print("making those chords voice four, rewriting meter, and attaching ties")

        # rewrite meter

        if self.durations_voice_four or self.chords_voice_four is not None:
            if self.make_those_chords_voice_four is False:
                voice_four = voice_four
                self._rewrite_meter(voice_four, self.time_signatures)
                print("rewriting meter voice four")

        # attach indicators
        if self.post_process_voice_four is not None:
            self.post_process_voice_four(voice_four, score)

        # VOICE FIVE (LEFT HAND) ######################################################

        voice_five = score["LH_Voice_Five"]

        # initial rest
        if self.initial_rest_voice_five is not None:
            rh_voice_five_initial_rest = self._make_initial_rest(
                self.initial_rest_voice_five
            )
            voice_five.extend(rh_voice_five_initial_rest)
            print("making initial rest voice five")

        # make measures

        if (
            self.durations_voice_five is not None
            and self.make_those_chords_voice_five is False
        ):
            rh_voice_five_measures = self._make_measures(
                self.durations_voice_five,
                self.rhythm_maker_voice_five,
                self.pitches_voice_five,
                self.legato_voice_five,
            )
            voice_five.extend(rh_voice_five_measures)
            print("making measures voice five")

        # make chords

        if self.chords_voice_five is not None:
            rh_voice_five_chords = self._make_chords(self.chords_voice_five)
            voice_five.extend(rh_voice_five_chords)
            print("making chords voice five")

        # make those chords

        if self.make_those_chords_voice_five is True:
            measures = self._make_those_chords(
                self.time_signatures,
                self.durations_voice_five,
                self.rhythm_maker_voice_five,
                self.pitches_voice_five,
                self.rest_interval_voice_five,
            )
            voice_five.extend(measures)

            self._rewrite_meter_and_tie(voice_five, self.time_signatures)
            print("making those chords voice five, rewriting meter, and attaching ties")

        # rewrite meter

        if self.durations_voice_five or self.chords_voice_five is not None:
            if self.make_those_chords_voice_five is False:
                voice_five = voice_five
                self._rewrite_meter(voice_five, self.time_signatures)
                print("rewriting meter voice five")

        # attach indicators
        if self.post_process_voice_five is not None:
            self.post_process_voice_five(voice_five)

        # STAFF GROUP #################################################################
        # attach indicators
        if self.post_process_staffgroup is not None:
            self.post_process_staffgroup(score)

        # ELECTRONICS #################################################################
        electronics = score["RH_Voice_One_Electronics"]
        # make chords

        if self.chords_voice_one_elec is not None:
            electronics_chords = self._make_chords(self.chords_voice_one_elec)
            electronics.extend(electronics_chords)

        if self.post_process_electronics is not None:
            self.post_process_electronics(electronics, score)

        # SCORE #######################################################################

        if self.collect is False:
            organ_group = score["Piano_Staff"]
            abjad.setting(organ_group).midi_instrument = abjad.scheme.Scheme(
                "Flute", force_quotes=True
            )
            abjad.attach(abjad.instruments.Flute(), organ_group[0][0][0])
            lilypond_file = abjad.LilyPondFile.new(score, includes=self.includes,)
            midi_block = abjad.Block(name="midi")
            layout_block = abjad.Block(name="layout")
            lilypond_file["score"].items.append(layout_block)
            lilypond_file["score"].items.append(midi_block)
        else:
            self._add_midi_instruments(score)
            lilypond_file = abjad.LilyPondFile.new(score, includes=self.includes,)
        return lilypond_file

    def compile(self, score, includes):
        lilypond_file = abjad.LilyPondFile.new(score, includes=includes,)
        return lilypond_file

    # FUNCTIONS ###################################################################

    def _make_initial_rest(self, initial_rest):
        if initial_rest is not None:
            rest = abjad.Rest(initial_rest)
        return [rest]

    # make measures

    def _make_measures(
        self, durations, rhythm_maker, pitches, legato=False,
    ):

        if rhythm_maker is not None:
            measures = rhythm_maker(durations)
            measures = abjad.Container(measures)

        if pitches is not None:
            logical_ties = (
                abjad.select(measures)
                .leaves()
                .logical_ties(pitched=self.make_measures_pitched)
            )
            for i, logical_tie in enumerate(logical_ties):
                index = i % len(pitches)
                pitch = pitches[index]
                for note in logical_tie:
                    if isinstance(note, abjad.Rest):
                        pass
                    else:
                        note.written_pitch = pitch
        if legato is True:
            leaves = abjad.select(measures).leaves()
            for leaf1, leaf2 in zip(leaves[0::2], leaves[1:][0::2]):
                if not isinstance(leaf1, abjad.Rest) and not isinstance(
                    leaf2, abjad.Rest
                ):
                    abjad.attach(abjad.StartPhrasingSlur(), leaf1)
                    abjad.attach(abjad.StopPhrasingSlur(), leaf2)

        return measures

    # make measures segment 5

    def _make_measures_seg_5(
        self, durations, rhythm_maker, pitches,
    ):

        if rhythm_maker is not None:
            measures = rhythm_maker(durations)
            measures = abjad.Container(measures)

        if pitches is not None:
            logical_ties = abjad.select(measures).leaves().logical_ties()
            for i, logical_tie in enumerate(logical_ties):
                index = i % len(pitches)
                pitch = pitches[index]

                for note in logical_tie:
                    if isinstance(note, abjad.Rest):
                        pass
                    else:
                        note = abjad.Chord()
        return measures

    # make those chords

    def _make_those_chords_old(
        self, time_signatures, durations, rhythm_maker, pitches, rest_interval,
    ):
        measures = rhythm_maker(durations)
        leaves = abjad.select(measures).leaves()
        chords = []
        for x, y, z in zip(pitches, pitches[1:], pitches[2:]):
            for pitch in pitches[0::3]:
                if x == pitch:
                    for i, leave in zip(range(6), leaves):
                        i = i + 1
                        if i == 1:
                            note = abjad.Note(x, (1, 4))
                            note.written_duration = leave.written_duration
                            chords.append(note)
                        if i == 2:
                            chord = abjad.Chord((x, y), (1, 4))
                            chord.written_duration = leave.written_duration
                            chords.append(chord)
                        if i == 3:
                            chord = abjad.Chord((x, y, z), (1, 4))
                            chord.written_duration = leave.written_duration
                            chords.append(chord)
                        if i == 4:
                            chord = abjad.Chord((y, z), (1, 4))
                            chord.written_duration = leave.written_duration
                            chords.append(chord)
                        if i == 5:
                            note = abjad.Note(z, (1, 4))
                            note.written_duration = leave.written_duration
                            chords.append(note)
                        if rest_interval is not None:
                            if i == 6:
                                rest = rest_interval
                                chords.append(rest)
        return chords

    def _make_those_chords(
        self, time_signatures, durations, rhythm_maker, pitches, rest_interval,
    ):
        measures = rhythm_maker(durations)

        leaves = abjad.select(measures).leaves()
        chords = []
        for x, y, z in zip(pitches[0::3], pitches[1:][0::3], pitches[2:][0::3]):
            for i in range(6):
                if i == 0:
                    note = abjad.Note(x, (1, 4))
                    # note.written_duration = leaf.written_duration
                    chords.append(note)
                if i == 1:
                    chord = abjad.Chord((x, y), (1, 4))
                    # chord.written_duration = leaf.written_duration
                    chords.append(chord)
                if i == 2:
                    chord = abjad.Chord((x, y, z), (1, 4))
                    # chord.written_duration = leaf.written_duration
                    chords.append(chord)
                if i == 3:
                    chord = abjad.Chord((y, z), (1, 4))
                    # chord.written_duration = leaf.written_duration
                    chords.append(chord)
                if i == 4:
                    note = abjad.Note(z, (1, 4))
                    # note.written_duration = leaf.written_duration
                    chords.append(note)
                if i == 5:
                    if rest_interval is not None:
                        chords.append(rest_interval)

        for chord, leaf in zip(chords, leaves):
            if not isinstance(chord, (abjad.Note, abjad.Chord)):
                pass
            else:
                chord.written_duration = leaf.written_duration
        return chords

    # make chords
    def _make_chords(self, chords):
        if chords is not None:
            chords = abjad.Chord(chords)
        return [chords]

    # rewrite meter
    def _rewrite_meter(self, music, time_signature_pairs):
        time_signatures = []
        for item in time_signature_pairs:
            time_signatures.append(abjad.TimeSignature(item))
        abjad.mutate(music[:]).split(time_signature_pairs, cyclic=True)
        selector = abjad.select(music).leaves()
        measures = selector.group_by_measure()
        for time, measure in zip(time_signatures, measures):
            abjad.mutate(measure).rewrite_meter(time)
        return measures

    def _rewrite_meter_and_tie(self, music, time_signature_pairs):
        # I made this separate function because I needed
        # to rewrite meter before to attach ties :/
        time_signatures = []
        for item in time_signature_pairs:
            time_signatures.append(abjad.TimeSignature(item))
        abjad.mutate(music[:]).split(time_signature_pairs, cyclic=True)
        selector = abjad.select(music).leaves()
        measures = selector.group_by_measure()
        for time, measure in zip(time_signatures, measures):
            abjad.mutate(measure).rewrite_meter(time)

        # TIES
        selection = abjad.select(music).leaves().logical_ties()
        # verify next leave to apply ties correctly
        for leave, next_leave in zip(selection, selection[1:]):
            if isinstance(leave[-1], abjad.Note) and isinstance(
                next_leave[0], abjad.Chord
            ):
                # verify if there are same pitches in both leaves
                for item in next_leave[0].written_pitches:
                    if item == leave[-1].written_pitch:
                        # print("note-chord tie:" + str(leave[-1]))
                        abjad.attach(abjad.Tie(), leave[-1])
            if isinstance(leave[-1], abjad.Note) and isinstance(
                next_leave[0], abjad.Note
            ):
                if leave[-1].written_pitch == next_leave[0].written_pitch:
                    # print("note-note tie:" + str(leave[-1]))
                    abjad.attach(abjad.Tie(), leave[-1])
            # if leave is chord
            if isinstance(leave[-1], abjad.Chord) and isinstance(
                next_leave[0], abjad.Chord
            ):
                # verify if there are same pitches in both leaves
                if set(leave[-1].written_pitches) & set(next_leave[0].written_pitches):
                    # print("chord-chord tie:" + str(leave[-1]))
                    abjad.attach(abjad.Tie(), leave[-1])
            if isinstance(leave[-1], abjad.Chord) and isinstance(
                next_leave[0], abjad.Note
            ):
                for item in leave[-1].written_pitches:
                    # print("chord-note tie:" + str(leave[-1]))
                    if item == next_leave[0].written_pitch:
                        abjad.attach(abjad.Tie(), leave[-1])
        return measures

    def _add_midi_instruments(self, score):
        organ_group = score["Piano_Staff"]
        abjad.setting(organ_group).midi_instrument = abjad.scheme.Scheme(
            "Flute", force_quotes=True
        )
        abjad.attach(abjad.instruments.Flute(), organ_group[0][0][0])

    # INDICATORS
    def _attach_indicators(indicators, music, indexes):
        for indicator, index in zip(indicators, indexes):
            abjad.attach(indicator, music[index])
        return music
