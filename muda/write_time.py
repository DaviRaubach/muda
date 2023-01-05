for time_sig1, time_sig2, (i, selection) in zip(in_time_signatures[0::2], in_time_signatures[1:][0::2], enumerate(result)):
    if i == 0:
        abjad.attach(
            abjad.TimeSignature(time_sig1),
            abjad.select.leaf(selection, 0),
            tag=tag,
        )
    if time_sig1 != time_sig2
    abjad.attach(
        abjad.TimeSignature(time_sig1),
        abjad.select.leaf(selection, 0),
        tag=tag,
    )

for (i, time_sig), selection in zip(enumerate(in_time_signatures), result):
    j = i
    if i != 0:
        j = i - 1
    if in_time_signatures[j] == time_sig:
        pass
    else:
        abjad.attach(
            abjad.TimeSignature(time_sig),
            abjad.select.leaf(selection, 0),
            tag=tag,
        )
