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
Timespans will be filled with different materials later. Each column in the list below refers to a material. The number represents the material presence (duration).

>>> alternations = [
...     # matA, matB, matC, ..., matL
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
...     "matA", "matB", "matC", "matD", "matE", "matF", "matG",
...     "matH", "matI", "matJ", "matK", "matL"]

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
...     "matL": rmakers.stack(
...         rmakers.talea([2, 1, -1], 16),
...         rmakers.extract_trivial()),
...     "matK": rmakers.stack(
...         rmakers.talea([1, 1, 1, 1, 1], 32, extra_counts=[1]),
...         rmakers.extract_trivial()),
...     "matJ": rmakers.stack(
...         rmakers.talea([-1, 1, -1], 8, extra_counts=[1]),
...         rmakers.extract_trivial()),
...     "matI": rmakers.stack(
...         rmakers.talea([1, 1, 1], 4, extra_counts=[1]),
...         rmakers.extract_trivial()),
...     "matH": rmakers.stack(
...         rmakers.talea([-3, -2, 1, -3, -3], 16, extra_counts=[4]),
...         rmakers.extract_trivial()),
...     "matG": rmakers.stack(
...         rmakers.talea([-2, 1, 1, 1, 1, 1, 1], 32),
...         rmakers.extract_trivial()),
...     "matF": rmakers.stack(
...         rmakers.talea([1, 4, 2], 8),
...         rmakers.extract_trivial()),
...     "matE": rmakers.stack(
...         rmakers.talea([-4, 2, 1, 1, -1, 1, 1, -1, 2, 1, 1], 32),
...         rmakers.extract_trivial()),
...     "matD": rmakers.stack(
...         rmakers.talea([2, -1, 2, 2, 2, -2, 2, -2], 16, extra_counts=[5]),
...         rmakers.extract_trivial()),
...     "matC": rmakers.stack(
...         rmakers.talea([-1, 1, 1, -1], 32),
...         rmakers.extract_trivial()),
...     "matB": rmakers.stack(
...         rmakers.talea([2, -1], 16, extra_counts=[1]),
...         rmakers.extract_trivial()),
...     "matA": rmakers.stack(
...         rmakers.talea([-8, -2, 2, 1, -3], 32),
...         rmakers.extract_trivial())
... }

Pitches
-------

Pitch is also different for each material and are also expressed in a python dictionary.

>>> annotated_pitches = {
...     "matL": abjad.PitchSegment("a' b'"),
...     "matK": abjad.PitchSegment("e''' ef'' b'' a' d'"),
...     "matJ": abjad.PitchSegment("b'"),
...     "matI": abjad.PitchSegment("f'' e'' ef''"),
...     "matH": abjad.PitchSegment("b'"),
...     "matG": abjad.PitchSegment("e'' c'' e'' c'' g' b'"),
...     "matF": abjad.PitchSegment("e' e'' g''"),
...     "matE": abjad.PitchSegment("b' b' b' a' b' b' b'"),
...     "matD": abjad.PitchSegment("b'"),
...     "matC": abjad.PitchSegment("b'"),
...     "matB": abjad.PitchSegment("b'"),
...     "matA": abjad.PitchSegment("b'"),
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

It will generate containers whose names will be the material names (annotated in durations) 
plus an index number.

>>> containers = abjad.select.components(mats.container, abjad.Container)
>>> for container in containers:
...     if container.name is not None:  # ignore subcontainers
...         print(container.name, container)
matL_0 Container("c'8", name='mat11_0')
matL_1 Container("c'8 c'16 r16", name='mat11_1')
matK_0 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
matL_2 Container("c'8 c'16 r16", name='mat11_2')
matJ_0 Tuplet('3:2', "r8 c'8 r8")
matK_1 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
matL_3 Container("c'8 c'16 r16", name='mat11_3')
matI_0 Tuplet('3:2', "c'4 c'4 c'4")
matJ_1 Tuplet('3:2', "r8 c'8 r8")
matK_2 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
matL_4 Container("c'8 c'16 r16", name='mat11_4')
matH_0 Tuplet('3:2', "r8. r8 c'16 r8. r8.")
matI_1 Tuplet('3:2', "c'4 c'4 c'4")
matJ_2 Tuplet('3:2', "r8 c'8 r8")
matK_3 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
matL_5 Container("c'8 c'16 r16", name='mat11_5')
matG_0 Container("r16 c'32 c'32 c'32 c'32 c'32 c'32", name='mat06_0')
matH_1 Tuplet('3:2', "r8. r8 c'16 r8. r8.")
matI_2 Tuplet('3:2', "c'4 c'4 c'4")
matJ_3 Tuplet('3:2', "r8 c'8 r8")
matK_4 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
matL_6 Container("c'8 c'16 r16", name='mat11_6')
matF_0 Container("c'8 c'2 c'4", name='mat05_0')
matG_1 Container("r16 c'32 c'32 c'32 c'32 c'32 c'32", name='mat06_1')
matH_2 Tuplet('3:2', "r8. r8 c'16 r8. r8.")
matI_3 Tuplet('3:2', "c'4 c'4 c'4")
matJ_4 Tuplet('3:2', "r8 c'8 r8")
matK_5 Tuplet('5:4', "c'32 c'32 c'32 c'32 c'32")
matL_7 Container("c'8 c'16 r16", name='mat11_7')
matE_0 Container("r8 c'16 c'32 c'32", name='mat04_0')
etc...

I had to write the retrograde of some rhythms because abjad
would write the material in a given duration from left to right.
However, Aperghis' piece expands from right to left. Below,
I use the ``muda.Material.retrograde()`` method to get it right.

>>> mats.retrograde("matL")
>>> mats.retrograde("matE")
>>> mats.retrograde("matD")
>>> mats.retrograde("matC")
>>> mats.retrograde("matB")
>>> mats.retrograde("matA")

Write Pitches
-------------

The ``muda.Material.write_pitches_by_name()`` method writes pitches according to materials.

>>> mats.write_pitches_by_name(annotated_pitches)

Changing Leaves
---------------

To change leaves and attach indicators on them I use their index in a specific material.
Therefore, is important to vizualize materials and indices. For that I use the ``muda.Material.annotate_material_names()`` method. The only argument is a list of material names I want to annotate (here it is in the ``annotations`` variable.
In this case, I also need to add time signatures to ``mats.container`` and I will also rewrite meter according to that time signatures.

>>> time_signatures = []
>>> for item in durations:
...     if isinstance(item, list):
...         for i in item:
...             time_signatures.append(abjad.TimeSignature(i))
...     else:
...         time_signatures.append(abjad.TimeSignature(item))
>>> mats.rewrite_meter(time_signatures)
>>> mats.write_time_signatures(time_signatures)
>>> mats.annotate_material_names(annotations)

The illustration is saved in muda's directory. Once I had the illustration, I can comment the last two lines.

Illustration:

:pdfembed:`src:_static/illustration.pdf, height:580, width:700, align:middle`



Delete Leaves
^^^^^^^^^^^^^

Below, I use the ``delete()`` method. It is possible to remove leaves or to
transform them into rests or skips.

To delete a leaf inside a material, use the ``material_name`` argument.

>>> mats.delete(
...     muda.leaf_0,
...     material_name="matE_2",
...     replace_with_rests=True,
... )
>>> mats.delete(
...     muda.leaf_1,
...     material_name="matE_2",
...     replace_with_rests=True,
... )
>>> mats.delete(
...     muda.leaf_0,
...     material_name="matE_3",
...     replace_with_rests=True,
... )
>>> mats.delete(
...     muda.leaf_5,
...     material_name="matD_1",
...     replace_with_rests=True,
... )
>>> mats.delete(
...     lambda _: muda.leaves(_)[:4],
...     material_name="matD_1",
...     replace_with_skips=True,
... )
>>> mats.delete(
...     lambda _: muda.leaves(_)[:4],
...     material_name="matD_2",
...     replace_with_skips=True,
... )

Modify all the "matF" containers:

>>> mats.delete(
...     muda.leaf_1,
...     material_name="matF",
...     replace_with_skips=True,
... )

Attach
^^^^^^

I can attach things in a specific material like this:

>>> mats.attach(
...     argument=abjad.BeforeGraceContainer("b'8"),
...     select=muda.leaf_2,
...     material_name="matH",
... )

In this case, all the containers which name starts with "matH" will receive a
grace note before the second leaf.

It is possible to attach literals:

>>> literal00 = [
...     r"\override Score.BarLine.stencil = ##f",
...     r"\override Staff.NoteHead.no-ledgers = ##t",
...     r"\override Staff.StaffSymbol.line-count = 1",
...     r"\omit Clef"]

When ``material_name`` is ``None``, it attaches to ``mats.container`` leaves, pitched
or not. Muda has also some predefined abjad selections. Here ``muda.leaf_0`` is actually ``lambda _: abjad.select.leaf(_, 0)``.

>>> mats.attach(
...     literal00,  # literal
...     muda.leaf_0)  # leaf

>>> mats.attach(r"\break", muda.leaf_1)

I will attach breaks after every "matL" containers:

>>> for leaf, (i, leaf2) in zip(mats.container, enumerate(mats.container[1:])):
...     if leaf.name is not None:
...         leaftest = leaf.name.startswith("matL")
...         leaf2test = leaf2.name.startswith("matL")
...         if leaftest is True and leaf2test is False:
...             abjad.attach(abjad.LilyPondLiteral(r"\break"), leaf2)

I also need to change the line count in materials I, J, K, and L.

>>> five_lines = r"\stopStaff \startStaff \revert Staff.StaffSymbol.line-count"
>>> one_line = r'\stopStaff \startStaff \override Staff.StaffSymbol.line-count = 1'
>>> mats.attach(five_lines, muda.leaf_0, ["matI", "matK"])
>>> mats.attach(one_line, 0, ["matJ", "matL"])

Change Noteheads
^^^^^^^^^^^^^^^^

It is easy to change the noteheads of a particular material:

>>> mats.note_heads("matG", "#'cross")

To get arrows, I will need some more lilypond overrides.

>>> arrowdown_head = (
...     r"\stemUp"
...     + r"\once \override Staff.Stem.X-offset  = #-0.07"
...     + r"\once \override Staff.Stem.Y-offset  = #0.3"
...     + r"\once \override Staff.Flag.Y-offset  = #1.5"
...     + r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
...     + r"\once \override Staff.NoteHead #'text = \markup{" 
...     + r" \arrow-head #Y #DOWN ##f}")
>>> arrowup_head = (
...     + r" \stemNeutral"
...     + r" \once \override Staff.Stem.Y-offset  = #-1.3"
...     + r" \once \override Staff.Stem.X-offset  = #-0.1"
...     + r" \once \override Staff.NoteHead.stencil = #ly:text-interface::print"
...     + r" \once \override Staff.NoteHead #'text = \markup{" 
...     + r"  \arrow-head #Y #UP ##f}")

>>> mats.attach(arrowdown_head, muda.leaf_0, "matF")
>>> mats.attach(arrowup_head, muda.leaf_r1, "matF")

Cross note heads in "matG":

>>> matG = muda.select_material(mats.container, "matG")
>>> matG = muda.pitched_leaves(matG)
>>> for leaf in matG:
...     abjad.override(leaf).NoteHead.style = "#'cross"

Attach Texts
^^^^^^^^^^^^
>>> mats.attach(
...     abjad.Markup('\markup "expirar"', direction=abjad.Up),
...     muda.leaf_0,
...     "matF_0",
... )
>>> mats.attach(
...     abjad.Markup('\markup "inspirar"', direction=abjad.Up),
...     muda.leaf_r1,
...     "matF_0",
... )
>>> mats.attach(
...     abjad.Markup('\markup "(potrinaire)"', direction=abjad.Up), muda.leaf_0, "matI_0"
... )
>>> mats.attach(
...     abjad.Markup('\markup "(souffle)"', direction=abjad.Up), muda.leaf_0, "matG_0"
... )

Write indicators
^^^^^^^^^^^^^^^^

With ``write_indicators`` is easy to write slurs (I need to rewrite this method).

>>> mats.write_indicators(material_name="matF", slur_down=[(0, 1)])
>>> mats.write_indicators(material_name="matI", slur_up=[(0, 2)])
>>> mats.write_indicators(material_name="matK", slur_up=[(0, 4)])

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

Obs.: It would be necessary some adjusts to have a score nearer to the original (delete some rests, implement a different signatures, etc.). However, the objective here was only illustrate the possibilities of muda library.

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

Notice that the name "Soprano_Voice_1" I predicted when wrote the
``muda.Material`` and ``muda.Lyrics`` is defined automatically. I just needed
to put the name "Soprano".

In this case, when creating the instrument is also necessary to add the
``lyrics_target``.

Append the instrument in the score:

>>> score.append([inst])
muda.Score.append() Soprano

Make Skips
----------

I use ``muda.Material()`` also to create a global context to time signatures:

>>> global_context = muda.Material("Global_Context")
>>> global_context.make_skips(time_signatures)
>>> global_context.write_time_signatures(time_signatures)

Write Materials
---------------

``write_materials()`` will write the materials and lyrics to the score. What
is behind the scenes is that ``mats.container`` is appended to
``score.score["Soprano_Voice_1"]``.

>>> score.write_materials([mats, lyrics, global_context])

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

:pdfembed:`src:_static/aperghis_example.pdf, height:580, width:700, align:middle`


    """
import abjad
import muda
import os
from abjadext import rmakers

print("composing example")


# COMPONENTS

# Timespans
"""Create timespans using ``muda.timespan.alternating_timespans``.
Each column refers to in the list below refers to a material.
It represents the material presence (duration).
"""

alternations = [
    # matA, matB, matC, ..., matL
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
    [4, 1, 1, 5, 4, 7, 2, 4, 4, 2, 1, 2],
]

# names for the materials in the list above:
annotations = [
    "matA",
    "matB",
    "matC",
    "matD",
    "matE",
    "matF",
    "matG",
    "matH",
    "matI",
    "matJ",
    "matK",
    "matL",
]

timespans = muda.timespan.alternating_timespans(
    alternations=alternations, denominator=8, annotations=annotations
)

# Transform it to a list of ``muda.AnnotatedDuration``
durations = timespans.annotated_durations(subdivision=(2, 4))

time_signatures = []
for item in durations:
    if isinstance(item, list):
        for i in item:
            time_signatures.append(abjad.TimeSignature(i))
    else:
        time_signatures.append(abjad.TimeSignature(item))

# time_signatures = timespans.time_signatures()

# It is a list of durations where each one is annotated with
# the material name.

# Rhythms of each material
makers = {
    "matL": rmakers.stack(rmakers.talea([2, 1, -1], 16), rmakers.extract_trivial()),
    "matK": rmakers.stack(
        rmakers.talea([1, 1, 1, 1, 1], 32, extra_counts=[1]),
        rmakers.extract_trivial(),
    ),
    "matJ": rmakers.stack(
        rmakers.talea([-1, 1, -1], 8, extra_counts=[1]), rmakers.extract_trivial()
    ),
    "matI": rmakers.stack(
        rmakers.talea([1, 1, 1], 4, extra_counts=[1]), rmakers.extract_trivial()
    ),
    "matH": rmakers.stack(
        rmakers.talea([-3, -2, 1, -3, -3], 16, extra_counts=[4]),
        rmakers.extract_trivial(),
    ),
    "matG": rmakers.stack(
        rmakers.talea([-2, 1, 1, 1, 1, 1, 1], 32), rmakers.extract_trivial()
    ),
    "matF": rmakers.stack(rmakers.talea([1, 4, 2], 8), rmakers.extract_trivial()),
    "matE": rmakers.stack(
        rmakers.talea([-4, 2, 1, 1, -1, 1, 1, -1, 2, 1, 1], 32),
        rmakers.extract_trivial(),
    ),
    "matD": rmakers.stack(
        rmakers.talea([2, -1, 2, 2, 2, -2, 2, -2], 16, extra_counts=[5]),
        rmakers.extract_trivial(),
    ),
    "matC": rmakers.stack(rmakers.talea([-1, 1, 1, -1], 32), rmakers.extract_trivial()),
    "matB": rmakers.stack(
        rmakers.talea([2, -1], 16, extra_counts=[1]), rmakers.extract_trivial()
    ),
    "matA": rmakers.stack(
        rmakers.talea([-8, -2, 2, 1, -3], 32), rmakers.extract_trivial()
    ),
}

# MATERIALS
mats = muda.Material("Soprano_Voice_1")
mats.alternating_materials(
    durations,
    makers,
)

mats.retrograde("matL")
mats.retrograde("matE")
mats.retrograde("matD")
mats.retrograde("matC")
mats.retrograde("matB")
mats.retrograde("matA")

# mats.rewrite_meter(time_signatures)


# Pitches for each material
annotated_pitches = {
    "matL": abjad.PitchSegment("a' b'"),
    "matK": abjad.PitchSegment("e''' ef'' b'' a' d'"),
    "matJ": abjad.PitchSegment("b'"),
    "matI": abjad.PitchSegment("f'' e'' ef''"),
    "matH": abjad.PitchSegment("b'"),
    "matG": abjad.PitchSegment("e'' c'' e'' c'' g' b'"),
    "matF": abjad.PitchSegment("e' e'' g''"),
    "matE": abjad.PitchSegment("b' b' b' a' b' b' b'"),
    "matD": abjad.PitchSegment("b'"),
    "matC": abjad.PitchSegment("b'"),
    "matB": abjad.PitchSegment("b'"),
    "matA": abjad.PitchSegment("b'"),
}

mats.write_pitches_by_name(annotated_pitches)

# Para vizualizar materiais e indices precisamos ajustar as fórmulas de compasso.

# Incluímos um "material" apenas para adicionar as fórmulas de compasso chamado Global Context.


# rewrite our Soprano material
mats.rewrite_meter(time_signatures)

# now we can illustrate it to see where the pitches are.

# you can comment these lines later
# mats.write_time_signatures(time_signatures)

# mats.annotate_material_names(annotations)


mats.delete(
    muda.leaf_0,
    material_name="matE_2",
    replace_with_rests=True,
)
mats.delete(
    muda.leaf_1,
    material_name="matE_2",
    replace_with_rests=True,
)
mats.delete(
    muda.leaf_0,
    material_name="matE_3",
    replace_with_rests=True,
)
mats.delete(
    muda.leaf_5,
    material_name="matD_1",
    replace_with_rests=True,
)
mats.delete(
    lambda _: muda.leaves(_)[:4],
    material_name="matD_1",
    replace_with_skips=True,
)
mats.delete(
    lambda _: muda.leaves(_)[:4],
    material_name="matD_2",
    replace_with_skips=True,
)
mats.delete(
    muda.leaf_1,
    material_name="matF",
    replace_with_skips=True,
)

# print(abjad.lilypond(mats.container))
# ATTACH

mats.attach(
    argument=abjad.BeforeGraceContainer("b'8"),
    select=muda.leaf_2,
    material_name="matH",
)

# LITERALS
literal00 = [
    r"\override Score.BarLine.stencil = ##f",
    r"\override Staff.NoteHead.no-ledgers = ##t",
    r"\override Staff.StaffSymbol.line-count = 1",
    r"\omit Clef",
]

# # when material_name is None, it attaches to ``mats.container`` leaves,
# # pitched or not.
mats.attach(literal00, muda.leaf_0)  # literal  # leaf

mats.attach(r"\break", muda.leaf_1)

# # breaks
for leaf, (i, leaf2) in zip(mats.container, enumerate(mats.container[1:])):
    if leaf.name is not None:
        leaftest = leaf.name.startswith("matL")
        leaf2test = leaf2.name.startswith("matL")
        if leaftest is True and leaf2test is False:
            abjad.attach(abjad.LilyPondLiteral(r"\break"), leaf2)

# stop and start staff
five_lines = r"\stopStaff \startStaff \revert Staff.StaffSymbol.line-count"
one_line = r"\stopStaff \startStaff \override Staff.StaffSymbol.line-count = 1"
mats.attach(five_lines, muda.leaf_0, ["matI", "matK"])
mats.attach(one_line, muda.leaf_0, ["matJ", "matL"])

# # noteheads
arrowdown_head = (
    r"\stemUp \once \override Staff.Stem.X-offset = #-0.07 \once \override Staff.Stem.Y-offset  = #0.3 \once \override Staff.Flag.Y-offset  = #1.5 \once \override Staff.NoteHead.stencil = #ly:text-interface::print \once \override Staff.NoteHead #'text = \markup{"
    + r" \arrow-head #Y #DOWN ##f}"
)
# arrowdown_head = [
#     r"\stemUp",
#     r"\once \override Staff.Stem.X-offset  = #-0.07",
#     r"\once \override Staff.Stem.Y-offset  = #0.3",
#     r"\once \override Staff.Flag.Y-offset  = #1.5",
#     r"\once \override Staff.NoteHead.stencil = #ly:text-interface::print",
#     r"\once \override Staff.NoteHead #'text = \markup{" + r" \arrow-head #Y #DOWN ##f}",
# ]
arrowup_head = (
    r" \stemNeutral"
    + r" \once \override Staff.Stem.Y-offset  = #-1.3"
    + r" \once \override Staff.Stem.X-offset  = #-0.1"
    + r" \once \override Staff.NoteHead.stencil = #ly:text-interface::print"
    + r" \once \override Staff.NoteHead #'text = \markup{" + r" \arrow-head #Y #UP ##f}"
)

mats.attach(arrowdown_head, muda.leaf_0, "matF")
mats.attach(arrowup_head, muda.leaf_r1, "matF")


matG = muda.select_material(mats.container, "matG")
matG = muda.pitched_leaves(matG)
for leaf in matG:
    abjad.override(leaf).NoteHead.style = "#'cross"
# texts

mats.attach(
    abjad.Markup('\markup "expirar"', direction=abjad.Up),
    muda.leaf_0,
    "matF_0",
)
mats.attach(
    abjad.Markup('\markup "inspirar"', direction=abjad.Up),
    muda.leaf_r1,
    "matF_0",
)
mats.attach(
    abjad.Markup('\markup "(potrinaire)"', direction=abjad.Up), muda.leaf_0, "matI_0"
)
mats.attach(
    abjad.Markup('\markup "(souffle)"', direction=abjad.Up), muda.leaf_0, "matG_0"
)
# slurs
mats.write_indicators(material_name="matF", slur_down=[(0, 1)])
mats.write_indicators(material_name="matI", slur_up=[(0, 2)])
mats.write_indicators(material_name="matK", slur_up=[(0, 4)])


# mats.annotate_material_names(annotations)

# Lyrics
lyrics = muda.Lyrics("Soprano_Voice_1")

lyrics.write_lyrics(
    r"""
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
    """
)

global_context = muda.Material("Global_Context")
# add skips
global_context.make_skips(time_signatures)
# add time s
global_context.write_time_signatures(time_signatures)


# mats.material_name_markups()
# SCORE
score = muda.Score()
inst = muda.Instrument(
    abjad_instrument=abjad.SopranoVoice(),
    name="Soprano",
    staff_count=1,
    voice_count=[1],
    lyrics_target="Soprano_Voice_1",
)
score.append([inst])
score.write_materials([mats, lyrics, global_context])
# print(abjad.lilypond(score.score))
# score.make_skips(time_signatures)
# score.rewrite_meter(time_signatures)
lilypond_file = abjad.LilyPondFile(
    items=[score.score],
)
# print(abjad.lilypond(score.score))
os.chdir(os.path.dirname(__file__))
abjad.persist.as_ly(lilypond_file, "aperghis_score.ly")
os.system("pwd")
os.system("lilypond aperghis_example.ly")


# if __name__ == '__main__':
# aperghis_example()
