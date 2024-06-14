import abjad
import abjadext.rmakers as rmakers


class AnnotatedDuration(abjad.Duration):
    def __new__(cls, *arguments, **kwargs):
        return super().__new__(cls, arguments[0])

    def __init__(self, *arguments, **kwargs):
        self.arguments = arguments
        self.annotation = kwargs.get("annotation")

    #     self.annotation = kwargs.get('annotation')
    #     self.arguments = arguments[0]
    #     self.dur = abjad.Duration(self.arguments)

    # def __call__(self):
    #     return self.dur.__call__()

    # def __str__(self):
    #     return self.dur.__str__()

    def __repr__(self):
        abdur = abjad.Duration(self.arguments)
        return abdur.__repr__()


def silence_and_rhythm_maker(maker, annotated_divisions, *commands):
    rest_maker = rmakers.stack(
        rmakers.note(), rmakers.force_rest(abjad.select())
    )

    my_stack_voice = abjad.Container()

    for dur in annotated_divisions:
        if dur.annotation.startswith("Rests ") is True:
            rests = rest_maker([dur])
            my_stack_voice.extend(rests)
        else:
            selection = maker([dur], *commands)
            my_stack_voice.extend(selection)
    return my_stack_voice


def rest_maker(divisions):
    nested_music = rmakers.note(divisions)
    container = abjad.Container(nested_music)
    logical_ties = abjad.select.logical_ties(container)
    rmakers.force_rest(logical_ties)
    # rmakers.rewrite_rest_filled(container)
    music = abjad.mutate.eject_contents(container)
    return music


def note_maker(divisions):
    nested_music = rmakers.note(divisions)
    container = abjad.Container(nested_music)
    # rmakers.rewrite_rest_filled(container)
    # rmakers.rewrite_sustained(container)
    music = abjad.mutate.eject_contents(container)
    return music


def rmaker(
    rmaker,
    extract_trivial=True,
    beam=False,
    rewrite_rest_filled=False,
    rewrite_meter=False,
):
    music = rmaker
    container = abjad.Voice(music)
    if rewrite_rest_filled:
        rmakers.rewrite_rest_filled(container)
    # if rewrite_meter:
    #     rmakers.rewrite_meter(container)
    if beam is True:
        rmakers.beam(container)
    if extract_trivial is True:
        rmakers.extract_trivial(container)
    music = abjad.mutate.eject_contents(container)
    return music


def make_sync_alternations(
    a_total: int, c_total: int, b_on_it: list, a_sound: list, c_sound: list
):
    """Makes alternations based on total duration of two parts (a and c) and sync b"""
    a_silence = a_total - a_sound
    c_silence = c_total - c_sound
    sync_alternations = [a_silence, a_sound] + b_on_it + [c_sound, c_silence]
    return sync_alternations


def make_in_out_alternations(
    a_total: int, b_total: int, a_sound: list, b_sound: list, tie=True
):
    """Makes alternations based on total duration of two parts (a and b). If tie argument is True, outputs 3 alternations, else, 4"""
    a_silence = a_total - a_sound
    b_silence = b_total - b_sound
    if tie is True:
        sync_alternations = [a_silence, (a_sound + b_sound), b_silence]
    else:
        sync_alternations = [a_silence, a_sound] + [b_sound, b_silence]
    return sync_alternations


def delete(
    leaves,
    replace_with_rests=False,
    replace_with_skips=False,
):
    """Delete leaves by index.

    Use ``material_name`` to delete a leaf in a
    specific material. Use ``replace_with_rests`` or
    ``replace_with_skips`` to replace leaves by rests or skips.
    """

    for leaf in leaves:
        if replace_with_skips is True:
            abjad.mutate.replace(
                leaf,
                abjad.Skip(leaf.written_duration),
            )
        elif replace_with_rests is True:
            abjad.mutate.replace(
                leaf,
                abjad.Rest(leaf.written_duration),
            )
        else:
            del leaf


def fit_in_duration(container, duration: abjad.Duration, final=False):
    shards = abjad.mutate.split(container, [duration])
    n = 0
    if final is True:
        n = -1
    copy = abjad.mutate.copy(shards[n])
    del container[:]
    container.append(copy[0])
