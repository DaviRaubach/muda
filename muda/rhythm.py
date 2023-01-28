import abjad
import abjadext.rmakers as rmakers


class AnnotatedDuration(abjad.Duration):

    def __new__(cls, *arguments, **kwargs):
        return super().__new__(cls, arguments[0])

    def __init__(self, *arguments, **kwargs):
        self.arguments = arguments
        self.annotation = kwargs.get('annotation')

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
        rmakers.note(), rmakers.force_rest(abjad.select()))

    my_stack_voice = abjad.Container()

    for dur in annotated_divisions:
        if dur.annotation.startswith("Rests ") is True:
            rests = rest_maker([dur])
            my_stack_voice.extend(rests)
        else:
            selection = maker([dur], *commands)
            my_stack_voice.extend(selection)
    return my_stack_voice
