"""
Timespans.

Class and function to operate timespans.
"""

from itertools import cycle
import abjad
import muda
from copy import copy


class TimespanList(abjad.TimespanList):
    r"""Add fuctions to abjad original TimespanList."""

    def separate_timespans_by_annotation(self):
        """Todo."""
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

    def opposite_timespan_list(self):
        """Todo."""
        for span1, span2 in zip(self, self[1:]):
            i = self.index(span1)
            if i == 0:
                if span1.start_offset == 0:
                    pass
                else:
                    new_initial_span = abjad.Timespan(
                        start_offset=(0, 1),
                        stop_offset=span1.start_offset,
                        annotation="Rests " + self[0].annotation,
                    )
                    self.append(new_initial_span)

            timespans = abjad.TimespanList([span1, span2])
            if timespans.all_are_contiguous is False:
                new_span = abjad.Timespan(
                    start_offset=span1.stop_offset,
                    stop_offset=span2.start_offset,
                    annotation="Rests " + self[i + 1].annotation,
                )
                self.append(new_span)
        return self

    def subdivide(self, subdivisions: dict = None):
        """Method for subdivide spans according to divisions."""
        new_ts_list = []

        for span in self:
            sub_ts_list = []
            # print(annotation)
            print(span)
            if hasattr(span, "annotation") and span.annotation is not None:
                print(subdivisions[span.annotation])
                splitted = span.divide_by_ratio(subdivisions[span.annotation])
                # for ts in splitted:
                # new_ts_list.append(ts)
                self.remove(span)
                for ts in splitted:
                    newts = abjad.Timespan(
                        start_offset=ts.start_offset,
                        stop_offset=ts.stop_offset,
                        annotation=span.annotation,
                    )
                    sub_ts_list.append(newts)
            new_ts_list.append(sub_ts_list)
            # ts.annotation = annotation
            # self.append(ts)
        print(new_ts_list)
        return new_ts_list

    def pure_annotated_durations(self):
        dur_list = []
        for span in self:
            if isinstance(span, list):
                # print("is list")
                dur_sub_list = []
                for sp in span:
                    dur = muda.rhythm.AnnotatedDuration(
                        sp.duration, annotation=sp.annotation
                    )
                    dur_sub_list.append(dur)
                if dur_sub_list:
                    dur_list.append(dur_sub_list)
            else:
                # print("is not a list")
                dur = muda.rhythm.AnnotatedDuration(
                    span.duration, annotation=span.annotation
                )
                # print("mudadur:", dur)
                # dur.annotation = span.annotation
                dur_list.append(dur)
            # print(span.annotation)
        print(dur_list)
        return dur_list

    def annotated_durations(self, subdivision: tuple = None):
        """Todo."""

        if subdivision == None:
            subdivision = (2, 4)
        subdur = abjad.Duration(subdivision)

        new_ts_list = []
        for span in self:
            sub_ts_list = []
            append_lower = True
            append_higher = True
            for a in range(2, 16):
                if span.duration < subdur * 2 and append_lower is True:
                    sub_ts_list.append(span)
                    # print("menor:", span.duration)
                    append_lower = False
                elif (
                    span.duration >= subdur * (a - 1)
                    and span.duration < subdur * a
                ) and append_higher is True:
                    # print("maior:", span.duration)
                    rest = span.duration % subdur
                    # print("rest", rest)
                    if rest == 0:
                        splited1 = span.divide_by_ratio(a - 1)
                        for ts in splited1:
                            newts = abjad.Timespan(
                                start_offset=ts.start_offset,
                                stop_offset=ts.stop_offset,
                                annotation=span.annotation,
                            )
                            sub_ts_list.append(newts)
                            # print("rest = 0, span annotation:",
                            #       newts.annotation)
                    else:
                        newspan = copy(span)
                        # print("rest =!0, span duration: ", span.duration)
                        dim = span.duration - rest
                        # print("dur dim", dim)
                        newspan = newspan.set_duration(dim)
                        # print("newspan dur:", newspan.duration)
                        splited2 = newspan.divide_by_ratio(a - 1)
                        # print("splited:", splited2)
                        for o, ts2 in enumerate(splited2):
                            # print("o", o)
                            if o == (len(splited2) - 1):
                                nts2 = splited2[-1].set_duration(
                                    splited2[-1].duration + rest
                                )
                                nts2.annotation = span.annotation
                                sub_ts_list.append(nts2)
                                # print("aquiiii", nts2.duration)
                            else:
                                ts2.annotation = span.annotation
                                sub_ts_list.append(ts2)
                            # print("rest =! 0:", ts2.duration)
                    append_higher = False
            new_ts_list.append(sub_ts_list)

        dur_list = []
        for span in new_ts_list:
            if isinstance(span, list):
                # print("is list")
                dur_sub_list = []
                for sp in span:
                    # print(sp.annotation)
                    dur = muda.rhythm.AnnotatedDuration(
                        sp.duration, annotation=sp.annotation
                    )
                    dur_sub_list.append(dur)
                if dur_sub_list:
                    dur_list.append(dur_sub_list)
            else:
                # print("is not a list")
                dur = muda.rhythm.AnnotatedDuration(
                    span.duration, annotation=span.annotation
                )
                # print("mudadur:", dur)
                # dur.annotation = span.annotation
                dur_list.append(dur)
            # print(span.annotation)
        return dur_list

    def nannotated_durations(
        self, subdivision: tuple | None = None, subdivisions: dict | None = None
    ):
        """Todo."""

        if subdivisions == None:
            subdivisions = {}
            for name in self.annotations:
                subdivisions[name] = abjad.Duration(subdivision)

        else:
            for k, v in subdivisions.items():
                subdivisions[k] = abjad.Duration(v)
        # subdur = abjad.Duration(subdivision)

        new_ts_list = []
        for span in self:
            sub_ts_list = []
            append_lower = True
            append_higher = True
            for a in range(2, 56):
                if (
                    span.duration < subdivisions[span.annotation] * 2
                    and append_lower is True
                ):
                    sub_ts_list.append(span)
                    # print("menor:", span.duration)
                    append_lower = False
                elif (
                    span.duration >= subdivisions[span.annotation] * (a - 1)
                    and span.duration < subdivisions[span.annotation] * a
                ) and append_higher is True:
                    # print("maior:", span.duration)
                    rest = span.duration % subdivisions[span.annotation]
                    # print("rest", rest)
                    if rest == 0:
                        splited1 = span.divide_by_ratio(a - 1)
                        for ts in splited1:
                            newts = abjad.Timespan(
                                start_offset=ts.start_offset,
                                stop_offset=ts.stop_offset,
                                annotation=span.annotation,
                            )
                            sub_ts_list.append(newts)
                            # print("rest = 0, span annotation:",
                            # newts.annotation)
                    else:
                        newspan = copy(span)
                        # print("rest =!0, span duration: ", span.duration)
                        dim = span.duration - rest
                        # print("dur dim", dim)
                        newspan = newspan.set_duration(dim)
                        # print("newspan dur:", newspan.duration)
                        splited2 = newspan.divide_by_ratio(a - 1)
                        # print("splited:", splited2)
                        for o, ts2 in enumerate(splited2):
                            # print("o", o)
                            if o == (len(splited2) - 1):
                                nts2 = splited2[-1].set_duration(
                                    splited2[-1].duration + rest
                                )
                                nts2.annotation = span.annotation
                                sub_ts_list.append(nts2)
                                # print("aquiiii", nts2.duration)
                            else:
                                ts2.annotation = span.annotation
                                sub_ts_list.append(ts2)
                            # print("rest =! 0:", ts2.duration)
                    append_higher = False
            new_ts_list.append(sub_ts_list)

        dur_list = []
        for span in new_ts_list:
            if isinstance(span, list):
                # print("is list")
                dur_sub_list = []
                for sp in span:
                    # print(sp.annotation)
                    dur = muda.rhythm.AnnotatedDuration(
                        sp.duration, annotation=sp.annotation
                    )
                    dur_sub_list.append(dur)
                if dur_sub_list:
                    dur_list.append(dur_sub_list)
            else:
                # print("is not a list")
                dur = muda.rhythm.AnnotatedDuration(
                    span.duration, annotation=span.annotation
                )
                # print("mudadur:", dur)
                # dur.annotation = span.annotation
                dur_list.append(dur)
            # print(span.annotation)
        return dur_list

    from abjadext import rmakers

    def rests(self):
        divisions = self.annotated_durations()
        nested_music = rmakers.note(divisions)
        container = abjad.Container(nested_music)
        logical_ties = abjad.select.logical_ties(container)
        rmakers.force_rest(logical_ties)
        _rests = abjad.mutate.eject_contents(container)
        return _rests

    def time_signatures(self, permitted_meters: list | None):
        """It returns time signatures based on timespan list."""
        if permitted_meters is None:
            permitted_meters = [
                (5, 4),
                (9, 8),
                (4, 4),
                (7, 8),
                (3, 4),
                (5, 8),
                (2, 4),
                (3, 8),
                # (5, 16),
                # (1, 4),
                # (3, 16),
                # (1, 8),
            ]
        permitted_meters = [abjad.Meter(_) for _ in permitted_meters]
        fitted_meters = abjad.Meter.fit_meters(
            argument=self,
            meters=permitted_meters,  # maximum_run_length=1
        )
        time_signatures = [_.implied_time_signature for _ in fitted_meters]
        return time_signatures

    # def durations_dict(self, subdivision=(2, 4)):
    #         """Todo."""
    #         subdur = abjad.Duration(subdivision)
    #         new_ts_list = []
    #         for span in self:
    #             append_lower = True
    #             append_higher = True
    #             for a in range(2, 16):
    #                 if span.duration < subdur * 2 and append_lower is True:
    #                     new_ts_list.append(span)
    #                     # print("menor:", span.duration)
    #                     append_lower = False
    #                 elif (span.duration >= subdur * (a - 1) and
    #                       span.duration < subdur * a) and append_higher is True:
    #                     # print("maior:", span.duration)
    #                     rest = span.duration % subdur
    #                     # print("rest", rest)
    #                     if rest == 0:
    #                         splited1 = span.divide_by_ratio(a - 1)
    #                         for ts in splited1:
    #                             newts = abjad.Timespan(
    #                                 start_offset=ts.start_offset,
    #                                 stop_offset=ts.stop_offset,
    #                                 annotation=span.annotation)
    #                             new_ts_list.append(newts)
    #                             # print("rest = 0, span annotation:",
    #                             #       newts.annotation)
    #                     else:
    #                         newspan = copy(span)
    #                         # print("rest =!0, span duration: ", span.duration)
    #                         dim = span.duration - rest
    #                         # print("dur dim", dim)
    #                         newspan = newspan.set_duration(dim)
    #                         # print("newspan dur:", newspan.duration)
    #                         splited2 = newspan.divide_by_ratio(a - 1)
    #                         # print("splited:", splited2)
    #                         for o, ts2 in enumerate(splited2):
    #                             # print("o", o)
    #                             if o == (len(splited2) - 1):
    #                                 nts2 = splited2[-1].set_duration(
    #                                     splited2[-1].duration + rest)
    #                                 nts2.annotation = span.annotation
    #                                 new_ts_list.append(nts2)
    #                                 # print("aquiiii", nts2.duration)
    #                             else:
    #                                 ts2.annotation = span.annotation
    #                                 new_ts_list.append(ts2)
    #                             # print("rest =! 0:", ts2.duration)
    #                     append_higher = False

    #         dur_list = []
    #         for span in new_ts_list:
    #             dur = {span.annotation: span.duration}
    #             dur_list.append(dur)
    #         print(dur_list)
    #         return dur_list


def alternating_timespans(
    alternations: list[list],
    denominator: int,
    annotations: list[str],
):
    """Make timespans to use with alternating materials."""
    n_annotations = len(annotations)
    timespans = TimespanList()
    counter_1 = []
    assert len(annotations) == len(alternations[0])
    # if len(annotations) != len(alternations[0]):
    #     raise Exception("Annotations counts != alternations counts")
    for a, alt in enumerate(alternations):
        for i in range(n_annotations):
            # print(annotations[i])
            if alt[i] == 0:
                pass
            else:
                if a == 0 and i == 0:
                    timespans.append(
                        abjad.Timespan(
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
                    ts = abjad.Timespan(
                        annotation=annotations[i],
                        start_offset=start_offset_,
                        stop_offset=stop_offset_,
                    )

                    timespans.append(ts)
                    counter_1.append(alt[i])
                    # print(alt[i], ts)
    timespans.annotations = annotations
    return timespans

    # print(timespans)
    # abjad.show(timespans, scale=0.8, key="annotation")

    # is_tangent_to_timespan


# t_list = abjad.TimespanList()
# span1 =
#     abjad.Timespan(
#         start_offset=(1, 4), stop_offset=(7, 8), annotation="Voice 1"
#     )

# t_list.append(span1)

# print(t_list)
# list_with_voices = t_list.SeparateTimespansByAnnotation()
# print(list_with_voices)


def make_alternations(
    total_duration: abjad.Duration,
    numerator_lists: list[list],
    denominator: int,
):
    current_duration = 0
    remaining_duration = 0
    alternations = []
    durations = []
    while current_duration < total_duration:
        numerator_lists = [cycle(_) for _ in numerator_lists]
        sublist = []
        for i in range(len(numerator_lists)):
            if current_duration == total_duration:
                break
            # print("i", i)
            n = next(numerator_lists[i])

            n_dur = abjad.Duration(n, denominator)
            if remaining_duration > 0:
                # print("remaining > 0")
                if remaining_duration < n_dur:
                    r_dur = abjad.duration.with_denominator(
                        remaining_duration, denominator
                    )
                    r_dur = abjad.Duration(r_dur)
                    # OLD r_dur = remaining_duration.with_denominator(denominator)
                    # print("aqui", r_dur)
                    n = r_dur.numerator
                    # print("adjusting final duration")
            # print("n =", n)
            sublist.append(n)
            if n != 0:
                durations.append(abjad.Duration(n, denominator))
            # print(sublist)
            # print(i, len(numerator_lists))
            # durations = [abjad.Duration(_, denominator) for _ in durations if _ != 0]
            current_duration = sum(durations)
            # print("current =", current_duration)
            remaining_duration = total_duration - current_duration
            j = i + 1
            # if remaining_duration == 0 and remaining_duration < n_dur and i < len(numerator_lists):
            if remaining_duration == 0:
                while len(sublist) < len(numerator_lists):
                    # for a in numerator_lists[i:]:
                    sublist.append(0)
        assert len(sublist) == len(numerator_lists)
        alternations.append(sublist)
        # print("denominator =", denominator)
        # print("durations =", durations)
        # print("current =", current_duration)
        # print("remaining =", remaining_duration)
        # if total_duration == current_duration:
        # print("END")
    # print(alternations)
    return alternations


def illustrate_timespans(
    timespans: abjad.TimespanList, title: str = "Timespans"
):
    m_a = timespans._make_markup(key="annotation")
    ly_file = abjad.LilyPondFile(
        items=[
            r' #(set-default-paper-size "a4landscape") ',
            rf" \markup {{\vspace #4 \bold \fontsize #2 {{ {title} }} }}",
            m_a,
        ],
    )
    abjad.persist.as_pdf(ly_file, "timespans_illustration.pdf")
