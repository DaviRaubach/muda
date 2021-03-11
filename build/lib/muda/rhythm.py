import abjad
import abjadext.rmakers as rmakers


class AnnotatedDuration(abjad.Duration):
    def __init__(self, annotation=None):
        self.annotation = annotation


def SilenceAndRythmMaker(maker, annotated_divisions, *commands):
    rest_maker = rmakers.stack(rmakers.note(), rmakers.force_rest(abjad.select()))

    my_stack_voice = abjad.Container()

    for dur in annotated_divisions:
        if dur.annotation.startswith("Rests ") is True:
            rests = rest_maker([dur])
            my_stack_voice.extend(rests)
        else:
            selection = maker([dur], *commands)
            my_stack_voice.extend(selection)
    return my_stack_voice

