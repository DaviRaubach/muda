r"""
Rewriting Aperghis Recitación 9.

    .. raw:: html

       <iframe width="560" height="315" src="https://www.youtube.com/embed/85CloE5kQLg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>  

>>> import abjad
>>> import muda
>>> from abjadext import rmakers

I have conceived three definition ambits using muda:

1) **Components**: define timespans, rhythms, pitches;
2) **Materials**: generate materials with defined components and modify them;
3) **Score**: create staffs (instruments) and append generated materials;

Components
==========

Timespans
---------

First, I create timespans using ``muda.timespan.alternating_timespans()``.
The timespans will be filled with different materials.

Each column in the list below refers to a material.
The number represents the material presence (duration).

>>> alternations = [
...     # mat00, mat01, mat02, ..., mat11
...     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
...     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
...     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
...     [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2],
...     [0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 1, 2],
...     [0, 0, 0, 0, 0, 0, 0, 4, 4, 2, 1, 2],
...     [0, 0, 0, 0, 0, 0, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 0, 0, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 0, 2, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 0, 3, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 1, 4, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
...     [0, 0, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2],
...     [4, 1, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2]]

Annotations are names for each material and refer to each column in the list
above:

>>> annotations = [
...     "mat00", "mat01", "mat02", "mat03", "mat04", "mat05", "mat06",
...     "mat07", "mat08", "mat09", "mat10", "mat11"]

>>> timespans = muda.timespan.alternating_timespans(
...     n_annotations=12,
...     alternations=alternations,
...     denominator=8,
...     annotations=annotations)

The variable `timespans` is now a list of timespans that are associated with
different materials. Then, I transform it into a list of durations using the
method ``annotated_durations()``. It becomes a list of
``muda.AnnotatedDuration()`` each of which is annotated with the material
name.

>>> durations = timespans.annotated_durations(
...     subdivision=(2, 4)  # divide long durations
... )

Pitch and rhythm are associated with the same
materials through python dictionaries.

Rhythms
-------

These are the rhythms for each material:

>>> makers = {
...     "mat11": rmakers.stack(
...         rmakers.talea([2, 1, -1], 16),
...         rmakers.extract_trivial()),
...     "mat10": rmakers.stack(
...         rmakers.talea([1, 1, 1, 1, 1], 32, extra_counts=[1]),
...         rmakers.extract_trivial()),
...     "mat09": rmakers.stack(
...         rmakers.talea([-1, 1, -1], 8, extra_counts=[1]),
...         rmakers.extract_trivial()),
...     "mat08": rmakers.stack(
...         rmakers.talea([1, 1, 1], 4, extra_counts=[1]),
...         rmakers.extract_trivial()),
...     "mat07": rmakers.stack(
...         rmakers.talea([-3, -2, 1, -3, -3], 16, extra_counts=[4]),
...         rmakers.extract_trivial()),
...     "mat06": rmakers.stack(
...         rmakers.talea([-2, 1, 1, 1, 1, 1, 1], 32),
...         rmakers.extract_trivial()),
...     "mat05": rmakers.stack(
...         rmakers.talea([1, 4, 2], 8),
...         rmakers.extract_trivial()),
...     "mat04": rmakers.stack(
...         rmakers.talea([-4, 2, 1, 1, -1, 1, 1, -1, 2, 1, 1], 32),
...         rmakers.extract_trivial()),
...     "mat03": rmakers.stack(
...         rmakers.talea([2, -1, 2, 2, 2, -2, 2, -2], 16, extra_counts=[5]),
...         rmakers.extract_trivial()),
...     "mat02": rmakers.stack(
...         rmakers.talea([-1, 1, 1, -1], 32),
...         rmakers.extract_trivial()),
...     "mat01": rmakers.stack(
...         rmakers.talea([2, -1], 16, extra_counts=[1]),
...         rmakers.extract_trivial()),
...     "mat00": rmakers.stack(
...         rmakers.talea([-8, -2, 2, 1, -3], 32),
...         rmakers.extract_trivial())
... }

Pitches
-------

These are the pitches for each material:

>>> pitches = {
...     "mat11": abjad.PitchSegment("a' b'"),
...     "mat10": abjad.PitchSegment("e''' ef'' b'' a' d'"),
...     "mat09": abjad.PitchSegment("b'"),
...     "mat08": abjad.PitchSegment("f'' e'' ef''"),
...     "mat07": abjad.PitchSegment("b'"),
...     "mat06": abjad.PitchSegment("e'' c'' e'' c'' g' b'"),
...     "mat05": abjad.PitchSegment("e' e'' g''"),
...     "mat04": abjad.PitchSegment("b' b' b' a' b' b' b'"),
...     "mat03": abjad.PitchSegment("b'"),
...     "mat02": abjad.PitchSegment("b'"),
...     "mat01": abjad.PitchSegment("b'"),
...     "mat00": abjad.PitchSegment("b'"),
... }

Materials
=========

``muda.Material()`` is used to put together the declared components.
It creates an ``abjad.Container()`` that will be appended later in a voice.
The voice name must be declared when creating the ``muda.Material()`` instance.

>>> mats = muda.Material("Soprano_Voice_1")

Now, I can use ``muda.Material()`` methods to write something to the
``muda.Material.container``.

Write Rhythms
-------------

Here, I must use ``alternating_materials()`` method to manipulate that
dictionary of rhythm makers according to the annotated durations.

>>> mats.alternating_materials(
...     durations,
...     makers,
... )

It will generate containers whose names will be the durations annotations plus
an index number.

>>> containers = abjad.select(mats.container).components(abjad.Container)
>>> for container in containers:
...     if container.name is not None:  # ignore subcontainers
...         print(container.name, container)
mat11_0 Container("c'8", name='mat11_0')
mat11_1 Container("c'8 c'16 r16", name='mat11_1')
mat10_0 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
mat11_2 Container("c'8 c'16 r16", name='mat11_2')
mat09_0 Tuplet('3:2', "r8 c'8 r8")
mat10_1 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
mat11_3 Container("c'8 c'16 r16", name='mat11_3')
mat08_0 Tuplet('3:2', "c'4 c'4 c'4")
mat09_1 Tuplet('3:2', "r8 c'8 r8")
mat10_2 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
mat11_4 Container("c'8 c'16 r16", name='mat11_4')
mat07_0 Tuplet('3:2', "r8. r8 c'16 r8. r8.")
mat08_1 Tuplet('3:2', "c'4 c'4 c'4")
mat09_2 Tuplet('3:2', "r8 c'8 r8")
mat10_3 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
mat11_5 Container("c'8 c'16 r16", name='mat11_5')
mat06_0 Container("r16 c'32 c'32 c'32 c'32 c'32 c'32", name='mat06_0')
mat07_1 Tuplet('3:2', "r8. r8 c'16 r8. r8.")
mat08_2 Tuplet('3:2', "c'4 c'4 c'4")
mat09_3 Tuplet('3:2', "r8 c'8 r8")
mat10_4 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
mat11_6 Container("c'8 c'16 r16", name='mat11_6')
mat05_0 Container("c'8 c'2 c'4", name='mat05_0')
mat06_1 Container("r16 c'32 c'32 c'32 c'32 c'32 c'32", name='mat06_1')
mat07_2 Tuplet('3:2', "r8. r8 c'16 r8. r8.")
mat08_3 Tuplet('3:2', "c'4 c'4 c'4")
mat09_4 Tuplet('3:2', "r8 c'8 r8")
mat10_5 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
mat11_7 Container("c'8 c'16 r16", name='mat11_7')
mat04_0 Container("r8 c'16 c'32 c'32", name='mat04_0')
etc...

I had to write the retrograde of some rhythms because abjad
would write the material in a given duration from left to right.
However, Aperghis' piece expands from right to left. Below,
I use the ``muda.Material.retrograde()`` method to get it right.

>>> mats.retrograde("mat11")
>>> mats.retrograde("mat04")
>>> mats.retrograde("mat03")
>>> mats.retrograde("mat02")
>>> mats.retrograde("mat01")
>>> mats.retrograde("mat00")

Write Pitches
-------------

Pitches will also be written according to that annotations.

>>> mats.write_pitches_by_duration(pitches, durations)

Changing Leaves
---------------

To change any leaf then it is necessary to know the index. So, you can use
``muda.Material.see_leaves_number(pitched=False)`` to illustrate
``muda.Material.container`` and see the indices upon the leaves in the score.
Here, the process is to compile, see what leaf you want to change,
and use its index to make this alteration.

Another method is possible because the name of each material container is
completed with an index number. The first "mat11" container is actually
named as "mat11_0", the second "mat11_1". So, I can use
``muda.Material.see_materials_leaves_number()`` to see indexes inside each of
these containers. Then, I can use this material name to modify specific
leaves inside this numbered container.

Delete Leaves
^^^^^^^^^^^^^

Below, I use the ``delete()`` method. It is possible to remove leaves or to
transform them into rests or skips.

First, let's see the leaves indexes:

>>> mats.see_materials_leaves_number()

.. lilyinclude:: /Users/Davi/github/muda/muda/aperghis_example/aperghis_see_mats.ly
    :noedge:

To delete a leaf inside a material, use the ``material_name`` argument.

>>> mats.delete(
...     [0, 1],  # leaves indices
...     material_name="mat04_2",
...     replace_with_rests=True)
>>> mats.delete([0], material_name="mat04_3", replace_with_rests=True)
>>> mats.delete([3], material_name="mat03_1", replace_with_rests=True)

Modify all the "mat05" containers:

>>> mats.delete(material_name="mat05", [1], replace_with_skips=True)

It is also possible to use indexes of the whole ``mats.container`` leaves.

>>> mats.see_leaves_number()

...

>>> mats.delete([343, 344, 345, 391, 392, 393], replace_with_skips=True)

Attach
^^^^^^

You can attach things in a specific material like this:

>>> mats.attach(abjad.BeforeGraceContainer("b'8"), 2, "mat07")

In this case, all the containers which name starts with "mat07" will receive a
grace note before the second leaf.

It is possible to attach literals:

>>> literal00 = [
...     r"\override Score.BarLine.stencil = ##f",
...     r"\override Staff.NoteHead.no-ledgers = ##t",
...     r"\override Staff.StaffSymbol.line-count = 1",
...     r"\omit Clef"]

When ``material_name`` is ``None``, it attaches to ``mats.container`` leaves, pitched
or not.

>>> mats.attach(
...     literal00,  # literal
...     0)  # leaf

>>> mats.attach(r"\break", 1)

I will attach breaks after every "mat11" containers:

>>> for leaf, leaf2 in zip(mats.container, mats.container[1:]):
...     if leaf.name is not None:
...         if leaf.name == "mat11" and leaf2.name != "mat11":
...             abjad.attach(abjad.LilyPondLiteral(r"\break"), leaf2)

I also need to change the line count in materials 08, 09, 10, and 11.

>>> five_lines = r"\stopStaff \startStaff \revert Staff.StaffSymbol.line-count"
>>> one_line = r'\stopStaff \startStaff \override Staff.StaffSymbol.line-count = 1'
>>> mats.attach(five_lines, 0, ["mat08", "mat10"])
>>> mats.attach(one_line, 0, ["mat09", "mat11"])

Change Noteheads
^^^^^^^^^^^^^^^^

It is easy to change the noteheads of a particular material:

>>> mats.note_heads("mat06", "#'cross")

To get arrows, I will need some more lilypond overrides.

>>> arrowdown_head = [
...     r"\stemUp",
...     r"\once \override Staff.Stem.X-offset  = #-0.07",
...     r"\once \override Staff.Stem.Y-offset  = #0.3",
...     r"\once \override Staff.Flag.Y-offset  = #1.5",
...     r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
...     r"\once \override Staff.NoteHead #'text = \markup{" +
...     r" \arrow-head #Y #DOWN ##f}"]
>>> arrowup_head = [
...     r"\stemNeutral",
...     r"\once \override Staff.Stem.Y-offset  = #-1.3",
...     r"\once \override Staff.Stem.X-offset  = #-0.1",
...     r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
...     r"\once \override Staff.NoteHead #'text = \markup{" +
...     r" \arrow-head #Y #UP ##f}"]
>>> mats.attach("mat05", arrowdown_head, 0)
>>> mats.attach("mat05", arrowup_head, -1)

Attach Texts
^^^^^^^^^^^^

I used ``mats.see_leaves_number(pitched=True)`` to get the leaves index again.
And then I attached some text to them.

>>> mats.attach(
...     abjad.Markup("expirar", direction=abjad.Up), 59, pitched=True)
>>> mats.attach(
...     abjad.Markup("inspirar", direction=abjad.Up), 60, pitched=True)
>>> mats.attach(
...     abjad.Markup("(potrinaire)", direction=abjad.Up), 18, pitched=True)
>>> mats.attach(
...     abjad.Markup("(souffle)", direction=abjad.Up), 41, pitched=True)

Write indicators
^^^^^^^^^^^^^^^^

With ``write_indicators`` is easy to write slurs:

>>> mats.write_indicators(material_name="mat05", slur_down=[(0, 1)])
>>> mats.write_indicators(material_name="mat08", slur_up=[(0, 2)])
>>> mats.write_indicators(material_name="mat10", slur_up=[(0, 4)])

Lyrics
------

Lyrics are written in a specific class: ``muda.Lyrics``. It requires the
target to which the lyrics will be added. Later, we put this ``muda.Lyrics``
instance together with the materials in the score through the method
``muda.Score.write_mateirals``.

>>> lyrics = muda.Lyrics("Soprano_Voice_1")
>>> lyrics.write_lyrics(r'''
...     sir
...     dé -- sir
...     _ dé -- sir
...     ce _ dé -- sir
...     donc __ ce _  dé -- sir
...     porquoi  donc __ ce _ dé -- sir
...     _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
...     _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
...     je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
...     par -- fois je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
...     jé par -- fois je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
...     tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
...         porquoi donc __ ce _  dé -- sir
...     san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
...         porquoi donc __ ce _  dé -- sir
...     vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
...         porquoi donc __ ce _  dé -- sir
...     en -- vie vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
...         porquoi donc __ ce _  dé -- sir
...     mon en -- vie vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
...         porquoi donc __ ce _  dé -- sir
...     à mon en -- vie vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
...         porquoi donc __ ce _  dé -- sir
...     ré -- siste à mon en -- vie vé san tu -- jé par -- fois je lui cède
...         _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
...     par -- fois je ré -- siste à mon en -- vie vé san tu -- jé
...         par -- fois je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
...     ''')

Score
=====

>>> score = muda.Score()
muda.Score()

Append Instrument
-----------------

>>> inst = muda.Instrument(
...     abjad_instrument=abjad.SopranoVoice(),
...     name="Soprano",
...     nstaffs=1,
...     nvoices=[1],
...     lyrics_target="Soprano_Voice_1",
... )
muda.score.Instrument() Soprano
creating Staff: Soprano_Staff_1
creating Voice: Soprano_Voice_1
creating Context:  Soprano_Voice_1_Lyrics

Note that the name "Soprano_Voice_1" that I predicted when wrote the
``muda.Material`` and ``muda.Lyrics`` is defined automatically. I just needed
to put the name "Soprano".

In this case, when creating the instrument is also necessary to add the
``lyrics_target``.

Append the instrument in the score:

>>> score.append([inst])
muda.Score.append() Soprano

Make Skips
----------

I will need some time signatures based on my durations.

>>> time_signatures = [abjad.TimeSignature(_) for _ in durations]

``make_skips`` will create a "Global_Context" staff with skips and time
signatures.

>>> score.make_skips(time_signatures)
muda.Score.make_skips()

Write Materials
---------------

``write_materials()`` will write the materials and lyrics to the score. What
is behind the scenes is that ``mats.container`` is appended to
``score.score["Soprano_Voice_1"]``.

>>> score.write_materials([mats, lyrics])

LilyPond File
-------------

>>> lilypond_file = abjad.LilyPondFile(
...     items=[score.score],
... )
>>> abjad.persist.as_ly(lilypond_file, "aperghis_score.ly")
('aperghis_score.ly', 0.21055388450622559)

The generated score ("aperghis_score.ly") is included in the following
lilypond file:

.. code-block:: html

    \version "2.20.0"   %! abjad.LilyPondFile._get_format_pieces()
    \language "english" %! abjad.LilyPondFile._get_format_pieces()

    \include "aperghis_stylesheet.ily"


    \markuplist {
      \right-column {
        \pad-around #1
        \score-lines {
          \include "aperghis_score.ly"
        }
      }
    }

>>> abjad.io.run_lilypond("aperghis_example.ly")

The sylesheet content:

.. code-block:: html

    \version "2.20"
    \language "english"

    #(set-global-staff-size 9)

    \header {
      tagline = ##f
      % breakbefore = ##t
      title =  "Recitación 9"
      poet = "Georges Aperghis (*1945)"
    }

    \layout {
      ragged-right = ##t
      \context {
        \name TimeSignatureContext
        \type Engraver_group
        \numericTimeSignature
      }
      \context {
        \Score
        \numericTimeSignature
        \remove Metronome_mark_engraver
        \remove Bar_number_engraver
        \remove Mark_engraver
        \accepts TimeSignatureContext
        \override BarLine.hair-thickness = #0.9
        \override BarLine.thick-thickness = #8
        \override Stem.thickness = #0.5
        \override Staff.thickness = #0.5
        \override Stem.stemlet-length = #1.15
        \override TupletBracket.bracket-visibility = ##t
        \override TupletBracket.minimum-length = #3
        \override TupletBracket.padding = #2
        \override TupletBracket.staff-padding = #2
        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
        \override TupletBracket.direction = #down
        \override TupletNumber.font-size = #1.2
        \override TupletNumber.text = #tuplet-number::calc-fraction-text
        \override SpacingSpanner.strict-note-spacing = ##t
        proportionalNotationDuration = #(ly:make-moment 1 28)
        tupletFullLength = ##t
      }

      \context {
        \Staff
        \remove Time_signature_engraver
        \remove Clef_engraver
      }
    }

    \paper {
      #(set-paper-size "b4landscape")
      indent = 0
      bottom-margin = 10\mm
      left-margin = 50\mm
      right-margin = 20\mm
      top-margin = 10\mm

    }


The result:

:pdfembed:`src:_static/aperghis_example.pdf, height:580, width:800, align:middle`


"""
import abjad
import muda
from abjadext import rmakers

# COMPONENTS

# Timespans
"""Create timespans using ``muda.timespan.alternating_timespans``.
Each column refers to in the list below refers to a material.
It represents the material presence (duration).
"""

alternations = [
    # mat00, mat01, mat02, ..., mat11
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 2, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 0, 0, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 0, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 2, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 3, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 0, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 1, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 0, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [0, 0, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2],
    [4, 1, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2]]

# names for the materials in the list above:
annotations = [
    "mat00", "mat01", "mat02", "mat03", "mat04", "mat05", "mat06",
    "mat07", "mat08", "mat09", "mat10", "mat11"]

timespans = muda.timespan.alternating_timespans(
    n_annotations=12,
    alternations=alternations,
    denominator=8,
    annotations=annotations)

# Transform it to a list of ``muda.AnnotatedDuration``
durations = timespans.annotated_durations(subdivision=(2, 4))
# It is a list of durations where each one is annotated with 
# the material name.

# Rhythms of each material
makers = {
    "mat11": rmakers.stack(
        rmakers.talea([2, 1, -1], 16),
        rmakers.extract_trivial()),
    "mat10": rmakers.stack(
        rmakers.talea([1, 1, 1, 1, 1], 32, extra_counts=[1]),
        rmakers.extract_trivial()),
    "mat09": rmakers.stack(
        rmakers.talea([-1, 1, -1], 8, extra_counts=[1]),
        rmakers.extract_trivial()),
    "mat08": rmakers.stack(
        rmakers.talea([1, 1, 1], 4, extra_counts=[1]),
        rmakers.extract_trivial()),
    # "mat07": r"r8 \times 2/3 {r8 c16} r8 r8",)
    "mat07": rmakers.stack(
        rmakers.talea([-3, -2, 1, -3, -3], 16, extra_counts=[4]),
        rmakers.extract_trivial()),
    "mat06": rmakers.stack(
        rmakers.talea([-2, 1, 1, 1, 1, 1, 1], 32),
        rmakers.extract_trivial()),
    "mat05": rmakers.stack(
        rmakers.talea([1, 4, 2], 8),
        rmakers.extract_trivial()),
    "mat04": rmakers.stack(
        rmakers.talea([-4, 2, 1, 1, -1, 1, 1, -1, 2, 1, 1], 32),
        rmakers.extract_trivial()),
    "mat03": rmakers.stack(
        rmakers.talea([2, -1, 2, 2, 2, -2, 2, -2], 16, extra_counts=[5]),
        rmakers.extract_trivial()),
    "mat02": rmakers.stack(
        rmakers.talea([-1, 1, 1, -1], 32),
        rmakers.extract_trivial()),
    "mat01": rmakers.stack(
        rmakers.talea([2, -1], 16, extra_counts=[1]),
        rmakers.extract_trivial()),
    "mat00": rmakers.stack(
        rmakers.talea([-8, -2, 2, 1, -3], 32),
        rmakers.extract_trivial())
}

# Pitches for each material
pitches = {
    "mat11": abjad.PitchSegment("a' b'"),
    "mat10": abjad.PitchSegment("e''' ef'' b'' a' d'"),
    "mat09": abjad.PitchSegment("b'"),
    "mat08": abjad.PitchSegment("f'' e'' ef''"),
    "mat07": abjad.PitchSegment("b'"),
    "mat06": abjad.PitchSegment("e'' c'' e'' c'' g' b'"),
    "mat05": abjad.PitchSegment("e' e'' g''"),
    "mat04": abjad.PitchSegment("b' b' b' a' b' b' b'"),
    "mat03": abjad.PitchSegment("b'"),
    "mat02": abjad.PitchSegment("b'"),
    "mat01": abjad.PitchSegment("b'"),
    "mat00": abjad.PitchSegment("b'"),
}

# MATERIALS
mats = muda.Material("Soprano_Voice_1")
mats.alternating_materials(
    durations,
    makers,
)

"""I had to write the retrograde in some rhythm makers because abjad
would write the material in a given duration from left to right.
However, the Aperghis' piece expands from right to left. Below,
I use the ``muda.Material.retrograde()`` to get it right."""

# containers = abjad.select(mats.container).components(abjad.Container)
# for container in containers:
#     if container.name is not None:  # ignore subcontainers
#         print(container.name, container)


mats.retrograde("mat11")
mats.retrograde("mat04")
mats.retrograde("mat03")
mats.retrograde("mat02")
mats.retrograde("mat01")
mats.retrograde("mat00")

mats.write_pitches_by_duration(pitches, durations)

# print(abjad.show(mats.container))

# mats.see_materials_leaves_number(pitched=False)


mats.delete([0, 1], material_name="mat04_2", replace_with_rests=True)
mats.delete([0], material_name="mat04_3", replace_with_rests=True)
mats.delete([3], material_name="mat03_1", replace_with_rests=True)

# mats.see_leaves_number(pitched=False)

mats.delete([343, 344, 345, 391, 392, 393], replace_with_skips=True)
mats.delete([1], material_name="mat05", replace_with_skips=True)

mats.attach(
    argument=abjad.BeforeGraceContainer("b'8"),
    leaf=2,
    material_name="mat07")


# LITERALS

literal00 = [
    r"\override Score.BarLine.stencil = ##f",
    r"\override Staff.NoteHead.no-ledgers = ##t",
    r"\override Staff.StaffSymbol.line-count = 1",
    r"\omit Clef"]

# when material_name is None, it attaches to ``mats.container`` leaves,
# pitched or not.
mats.attach(
    literal00,  # literal
    0)  # leaf

mats.attach(r"\break", 1)

# breaks
for leaf, (i, leaf2) in zip(mats.container, enumerate(mats.container[1:])):
    if leaf.name is not None:
        leaftest = leaf.name.startswith("mat11")
        leaf2test = leaf2.name.startswith("mat11")
        if leaftest is True and leaf2test is False:
            abjad.attach(abjad.LilyPondLiteral(r"\break"), leaf2)

# stop and start staff
five_lines = r"\stopStaff \startStaff \revert Staff.StaffSymbol.line-count"
one_line = r'\stopStaff \startStaff \override Staff.StaffSymbol.line-count = 1'
mats.attach(five_lines, 0, ["mat08", "mat10"])
mats.attach(one_line, 0, ["mat09", "mat11"])

# noteheads
arrowdown_head = [
    r"\stemUp",
    r"\once \override Staff.Stem.X-offset  = #-0.07",
    r"\once \override Staff.Stem.Y-offset  = #0.3",
    r"\once \override Staff.Flag.Y-offset  = #1.5",
    r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
    r"\once \override Staff.NoteHead #'text = \markup{" +
    r" \arrow-head #Y #DOWN ##f}"]
arrowup_head = [
    r"\stemNeutral",
    r"\once \override Staff.Stem.Y-offset  = #-1.3",
    r"\once \override Staff.Stem.X-offset  = #-0.1",
    r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
    r"\once \override Staff.NoteHead #'text = \markup{" +
    r" \arrow-head #Y #UP ##f}"]

mats.note_heads("mat06", "#'cross")
mats.attach(arrowdown_head, 0, "mat05")
mats.attach(arrowup_head, -1, "mat05")

# mats.see_leaves_number(pitched=True)

# texts
mats.attach(
    abjad.Markup("expirar", direction=abjad.Up), 59, pitched=True)
mats.attach(
    abjad.Markup("inspirar", direction=abjad.Up), 60, pitched=True)
mats.attach(
    abjad.Markup("(potrinaire)", direction=abjad.Up), 18, pitched=True)
mats.attach(
    abjad.Markup("(souffle)", direction=abjad.Up), 41, pitched=True)

# slurs
mats.write_indicators(material_name="mat05", slur_down=[(0, 1)])
mats.write_indicators(material_name="mat08", slur_up=[(0, 2)])
mats.write_indicators(material_name="mat10", slur_up=[(0, 4)])
# mats.see_materials_leaves_number(pitched=False)

# Lyrics
lyrics = muda.Lyrics("Soprano_Voice_1")
lyrics.write_lyrics(r"""
    sir

    dé -- sir

    _ dé -- sir

    ce _ dé -- sir

    donc __ ce _  dé -- sir

    porquoi  donc __ ce _ dé -- sir

    _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir

    _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir

    je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir

    par -- fois je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir

    jé par -- fois je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir

    tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
    porquoi donc __ ce _  dé -- sir

    san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
    porquoi donc __ ce _  dé -- sir

    vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
    porquoi donc __ ce _  dé -- sir

    en -- vie vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
    porquoi donc __ ce _  dé -- sir

    mon en -- vie vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
    porquoi donc __ ce _  dé -- sir

    à mon en -- vie vé san tu -- jé par -- fois je lui cède _ _ _ _ _ _ _
    porquoi donc __ ce _  dé -- sir

    ré -- siste à mon en -- vie vé san tu -- jé par -- fois je lui cède
    _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir

    par -- fois je ré -- siste à mon en -- vie vé san tu -- jé
    par -- fois je lui cède _ _ _ _ _ _ _ porquoi donc __ ce _  dé -- sir
    """)

# SCORE
score = muda.Score()
inst = muda.Instrument(
    abjad_instrument=abjad.SopranoVoice(),
    name="Soprano",
    nstaffs=1,
    nvoices=[1],
    lyrics_target="Soprano_Voice_1",
)
score.append([inst])
time_signatures = [abjad.TimeSignature(_) for _ in durations]
score.make_skips(time_signatures)
score.write_materials([mats, lyrics])
score.rewrite_meter(time_signatures)

lilypond_file = abjad.LilyPondFile(
    items=[score.score],
)
abjad.persist.as_ly(lilypond_file, "aperghis_score.ly")
abjad.io.run_lilypond(
    "/Users/Davi/github/muda/muda/aperghis_example/aperghis_example.ly")
