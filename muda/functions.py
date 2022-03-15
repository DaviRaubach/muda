import abjad


def make_measures(
    durations, rhythm_maker, pitches,
):

    if rhythm_maker is not None:
        measures = rhythm_maker(durations)
        measures = abjad.Container(measures)

    if pitches is not None:
        logical_ties = abjad.select(measures).leaves().logical_ties(pitched=True)
        for i, logical_tie in enumerate(logical_ties):
            index = i % len(pitches)
            pitch = pitches[index]
            for note in logical_tie:
                if isinstance(note, abjad.Rest):
                    pass
                else:
                    note.written_pitch = pitch

    return measures

def make_skips(score, time_signatures):
    site = "muda.functions.MakeSkips()"
    tag = abjad.Tag(site)
    print(str(tag))

    if isinstance(time_signatures[0], abjad.TimeSignature):
        time_signatures_abjad = time_signatures
        in_time_signatures = [_.pair for _ in time_signatures]
    else:
        in_time_signatures = time_signatures
        time_signatures_abjad = [abjad.TimeSignature(_) for _ in in_time_signatures]

    for time_sig in time_signatures_abjad:
        skip = abjad.Skip(1, multiplier=(time_sig.pair))
        score["Global_Context"].append(skip)

    # select skips to attach TIME SIGNATURES
    for i, element in enumerate(in_time_signatures):
        previous_element = time_signatures[i - 1] if i > 0 else None
        current_element = element

        # if current_element != previous_element:
        a = in_time_signatures.index(current_element)
        abjad.attach(time_signatures_abjad[a], score["Global_Context"][i], tag=tag)

# rewrite meter
def rewrite_meter(score, time_signatures):
    # global_skips = [_ for _ in abjad.select(score["Global_Context"]).leaves()]
    # sigs = []
    # for skip in global_skips:
    #     for indicator in abjad.get.indicators(skip):
    #         if isinstance(indicator, abjad.TimeSignature):
    #             sigs.append(indicator)
    durations = [_.duration for _ in time_signatures]
    for voice in abjad.select(score).components(abjad.Voice):
        # voice_dur = abjad.get.duration(voice)
        if voice:
            print("rewriting meter:", voice.name)
            # sig_dur = sum(durations)
            # assert voice_dur == sig_dur, (voice_dur, sig_dur)
            shards = abjad.mutate.split(voice[:], durations)
            for shard, time_signature in zip(shards, time_signatures):
                # leaf = abjad.get.leaf(shard, 0)
                # time_signature = abjad.get.indicator(leaf, abjad.TimeSignature)
                # print(time_s)
                # print(time_signature)
                abjad.Meter.rewrite_meter(
                    shard[:],
                    time_signature,
                    boundary_depth=1,
                    rewrite_tuplets=False,
                    maximum_dot_count=1,
                )

            # for time_signature, shard in zip(time_signatures, shards):
            #     abjad.Meter.rewrite_meter(shard, time_signature, boundary_depth=1)

            # inventories = [
            #     x
            #     for x in enumerate(
            #         abjad.Meter(time_signature.pair).depthwise_offset_inventory
            #     )
            # ]
            # if time_signature.denominator == 4:
            #     abjad.Meter.rewrite_meter(
            #         shard,
            #         time_signature,
            #         boundary_depth=inventories[-1][0],
            #         rewrite_tuplets=False,
            #     )
            # else:
            #     abjad.Meter.rewrite_meter(
            #         shard,
            #         time_signature,
            #         boundary_depth=inventories[-2][0],
            #         rewrite_tuplets=False,
            #     )

        # abjad.mutate().split(voice, in_time_signature, cyclic=True)

    # time_signatures = []
    # for item in in_time_signatures:
    #     time_signatures.append(abjad.Meter(item))
    # abjad.mutate().split(music, in_time_signature, cyclic=True)
    # # selection
    # abjad.Meter.rewrite_meter(music[:], time_signatures)
    # selector = abjad.select(music).leaves()
    # measures = selector.group_by_measure()
    # for time, measure in zip(time_signatures, measures):
    #     abjad.mutate(measure).rewrite_meter(time)
    # return measures


def separate_timespans_by_annotation(timespan_list):
    voices = []
    for item in timespan_list:
        if item.annotation not in voices:
            voices.append(item.annotation)
    general_list = []
    for i, voice in enumerate(voices):
        ts_list = abjad.TimespanList()
        for span in timespan_list:
            if span.annotation == voice:
                ts_list.append(span)
        general_list.append(ts_list)
    return general_list


def opposite_timespans(one_voice_timespan_list):
    for span1, span2 in zip(one_voice_timespan_list, one_voice_timespan_list[1:]):
        i = one_voice_timespan_list.index(span1)
        if i == 0:
            if span1.start_offset == 0:
                print("it is at the beginning")
                pass
            else:
                new_initial_span = abjad.AnnotatedTimespan(
                    start_offset=(0, 1),
                    stop_offset=span1.start_offset,
                    annotation="Silence " + one_voice_timespan_list[0].annotation,
                )
                one_voice_timespan_list.append(new_initial_span)

        timespans = abjad.TimespanList([span1, span2])
        if timespans.all_are_contiguous is False:
            new_span = abjad.AnnotatedTimespan(
                start_offset=span1.stop_offset,
                stop_offset=span2.start_offset,
                annotation="Silence " + one_voice_timespan_list[i + 1].annotation,
            )
            one_voice_timespan_list.append(new_span)

def select_material(container, material_name):
        """Select container by name."""
        selection = abjad.select.components(container, abjad.Container)
        indices = [
            i
            for i, container in enumerate(selection)
            if (
                (isinstance(container, abjad.Tuplet or abjad.Voice or abjad.BeforeGraceContainer))
                or (container.name is None)
                or (material_name not in container.name)
            )
        ]

        selection = abjad.select.exclude(selection, indices)

        return selection
