#!$HOME/github/my_venv/bin/python

import abjad
import muda


class TimespanList(abjad.TimespanList):
    r"""Add fuctions to abjad original TimespanList"""

    def SeparateTimespansByAnnotation(self):
        voices = []
        for item in self:
            if item.annotation not in voices:
                voices.append(item.annotation)
        general_list = []
        for i, voice in enumerate(voices):
            ts_list = TimespanList()
            for span in self:
                if span.annotation == voice:
                    ts_list.append(span)
            general_list.append(ts_list)
        return general_list

    def OppositeTimespanList(self):
        for span1, span2 in zip(self, self[1:]):
            i = self.index(span1)
            if i == 0:
                if span1.start_offset == 0:
                    pass
                else:
                    new_initial_span = abjad.AnnotatedTimespan(
                        start_offset=(0, 1),
                        stop_offset=span1.start_offset,
                        annotation="Rests " + self[0].annotation,
                    )
                    self.append(new_initial_span)

            timespans = abjad.TimespanList([span1, span2])
            if timespans.all_are_contiguous is False:
                new_span = abjad.AnnotatedTimespan(
                    start_offset=span1.stop_offset,
                    stop_offset=span2.start_offset,
                    annotation="Rests " + self[i + 1].annotation,
                )
                self.append(new_span)
        return self

    def AnnotatedDurations(self):
        dur_list = []
        for span in self:
            dur = muda.rhythm.AnnotatedDuration(span.duration)
            dur.annotation = span.annotation
            dur_list.append(dur)
        return dur_list


def AlternatingTimespans(
    n_annotations=3,  # different materials
    alternations=[
        [13, 5, 3],
        [8, 5, 3],
        [5, 5, 1],
        [3, 8, 1],
        [3, 13, 2],
        [2, 13, 8],
        [2, 8, 8],
        [1, 3, 13],
    ],
    denominator=4,
    annotations=["Mat_1", "Mat_2", "Rests "],
):
    """Makes timespans to use with alternating materials"""
    timespans = TimespanList()
    counter_1 = []
    for a, alt in enumerate(alternations):
        for i in range(n_annotations):
            if a == 0 and i == 0:
                timespans.append(
                    abjad.AnnotatedTimespan(
                        annotation=annotations[i],
                        start_offset=(0, denominator),
                        stop_offset=(alt[0], denominator),
                    )
                )
                counter_1.append(alt[0])
                # print(0, alt[0])
            else:
                start_offset_ = (sum(counter_1), denominator)
                stop_offset_ = (sum(counter_1) + alt[i], denominator)
                # print(start_offset_, stop_offset_)
                timespans.append(
                    abjad.AnnotatedTimespan(
                        annotation=annotations[i],
                        start_offset=start_offset_,
                        stop_offset=stop_offset_,
                    )
                )
                counter_1.append(alt[i])
    return timespans

    # print(timespans)
    # abjad.show(timespans, scale=0.8, key="annotation")

    # is_tangent_to_timespan


# t_list = abjad.TimespanList()
# span1 =
#     abjad.AnnotatedTimespan(
#         start_offset=(1, 4), stop_offset=(7, 8), annotation="Voice 1"
#     )

# t_list.append(span1)

# print(t_list)
# list_with_voices = t_list.SeparateTimespansByAnnotation()
# print(list_with_voices)
