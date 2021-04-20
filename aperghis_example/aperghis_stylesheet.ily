\version "2.20"
\language "english"
% #(set-default-paper-size "a4portrait")
% #(set-default-paper-size "11x17landscape")
#(set-global-staff-size 8)


\header {
  tagline = ##f
  breakbefore = ##t
  % dedication = \markup \override #'(font-name . "STIXGeneral") \fontsize #4.5 \center-column {" "}
  title =  "Recitación 9"
  subtitle = \markup \override #'(font-name . "STIXGeneral") \fontsize #2.5 \center-column {" "}
  % subsubtitle = \markup \override #'(font-name . "STIXGeneral") \fontsize #3.5 \center-column {" c "}
  composer = \markup  \override #'(font-name . "STIXGeneral") \pad-around #5 \fontsize #3 {"Davi Raubach (*1992)"}
}

\layout {
  %{ \accidentalStyle forget %}
  %{ \accidentalStyle modern %}
  %{ \accidentalStyle modern-cautionary %}
  \accidentalStyle dodecaphonic
  % indent = #15
  ragged-last = ##t
  %     ragged-right = ##t
  %left-margin = #15
  \context {
    \name TimeSignatureContext
    \type Engraver_group
    \numericTimeSignature
    % \consists Axis_group_engraver
    % \consists Bar_number_engraver
    % \consists Time_signature_engraver
    % \consists Mark_engraver
    % \consists Metronome_mark_engraver
    % \consists Text_engraver
    % 		\override BarNumber.Y-extent = #'(0 . 0)
    % 		\override BarNumber.Y-offset = 0
    % 		\override BarNumber.extra-offset = #'(-4 . 0)
    % 		\override BarNumber.font-name = "STIXGeneral"
    %{ \override BarNumber.stencil = #(make-stencil-boxer 0.1 0.7 ly:text-interface::print) %}
    %{ \override BarNumber.stencil = #(make-stencil-circler 0.1 0.7 ly:text-interface::print) %}
    % 		\override BarNumber.font-size = 5
    % 		\override BarNumber.padding = 4
    %\override BarNumber.stencil = ##f
    \override MetronomeMark.X-extent = #'(0 . 0)
    \override MetronomeMark.Y-extent = #'(0 . 0)
    \override MetronomeMark.break-align-symbols = #'(left-edge)
    \override MetronomeMark.extra-offset = #'(0 . 1)
    \override MetronomeMark.font-size = 3
    %\override RehearsalMark.stencil = #(make-stencil-circler 0.1 0.7 ly:text-interface::print)
    \override RehearsalMark.X-extent = #'(0 . 0)
    \override RehearsalMark.X-offset = 6
    \override RehearsalMark.Y-offset = -2.5
    \override RehearsalMark.break-align-symbols = #'(time-signature)
    \override RehearsalMark.break-visibility = #end-of-line-invisible
    \override RehearsalMark.font-name = "STIXGeneral"
    \override RehearsalMark.font-size = 9.5
    \override RehearsalMark.outside-staff-priority = 500
    \override RehearsalMark.self-alignment-X = #center
    \override TimeSignature.X-offset = #ly:self-alignment-interface::x-aligned-on-self
    \override TimeSignature.Y-extent = #'(0 . 0)
    \override TimeSignature.break-visibility = #end-of-line-invisible
    % \override TimeSignature.font-name = "STIXGeneral"
    % \override TimeSignature.font-size = #2
    \override TimeSignature.self-alignment-X = #center
    \override TimeSignature.whiteout-style = #'outline
    \override TimeSignature.whiteout = ##t
    \override VerticalAxisGroup.default-staff-staff-spacing = #'((basic-distance . 12) (minimum-distance . 10) (padding . 4) (stretchability . 0))

    %{ \override TimeSignature.X-extent = ##f
        \override TimeSignature.break-align-symbol = #'left-edge
        \override TimeSignature.break-visibility = #end-of-line-invisible
		\override TimeSignature.font-name = "STIXGeneral"
        \override TimeSignature.font-size = 3
        \override TimeSignature.space-alist.clef = #'(extra-space . 0.5)
        \override TimeSignature.style = #'numbered %}
  }
  \context {
    \Score
    \numericTimeSignature
    \remove Metronome_mark_engraver
    \remove Bar_number_engraver
    \remove Mark_engraver
    \accepts TimeSignatureContext
    % \override BarLine.X-extent = #'(0 . 0)
    % \override BarLine.bar-extent = #'(-2 . 2)
    \override BarLine.hair-thickness = #0.9
    \override BarLine.thick-thickness = #8
    %\override BarLine.stencil = ##f
    % \override Beam.breakable = ##t
    % \override Beam.concaveness = #10000
    % \override Beam.beam-thickness = #0.6
    % \override Beam.length-fraction = #1.3
    \override Clef.layer = -1
    \override Clef.whiteout-style = #'outline
    \override Clef.whiteout = 1
    %{ \override Clef.X-extent = #'(0 . 0) %}
    \override DynamicText.font-size = #-1
    % \override DynamicLineSpanner.staff-padding = 4.5
    %{ \override DynamicLineSpanner.Y-extent = #'(-1.5 . 1.5) %}
    %{ \override Hairpin.bound-padding = #1.5 %is this necessary? %}
    \override Glissando.breakable = ##t
    %{ \override Glissando.thickness = #2 %}
    \override Glissando.thickness = #1.8
    \override Stem.thickness = #0.5
    \override Staff.thickness = #0.5
    \override MetronomeMark.font-size = 2
    % \override SpacingSpanner.strict-grace-spacing = ##t
    % \override SpacingSpanner.strict-note-spacing = ##t
    % \override SpacingSpanner.uniform-stretching = ##t
    %         \override StaffGrouper.staff-staff-spacing = #'((basic-distance . 23) (minimum-distance . 23) (padding . 8))
    \override Stem.stemlet-length = #1.15
    \override StemTremolo.slope = #0.3
    %{ \override StemTremolo.shape = #'rectangle %}
    \override StemTremolo.shape = #'beam-like
    %{ \override StemTremolo.flag-count = #3 %}
    \override StemTremolo.beam-thickness = #0.3
    \override TupletBracket.bracket-visibility = ##t
    \override TupletBracket.minimum-length = #3
    % \override TupletBracket.padding = #2
    %{ \override TupletBracket.staff-padding = #1.5 %}
    \override TupletBracket.staff-padding = #2
    \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
    \override TupletBracket.direction = #down
    \override TupletNumber.font-size = #1.2
    \override TupletNumber.text = #tuplet-number::calc-fraction-text
    % autoBeaming = ##f
    %{ subdivideBeams = ##t %}
    % \override SpacingSpanner.strict-note-spacing = ##t
    proportionalNotationDuration = #(ly:make-moment 1 12)
    % tupletFullLength = ##t
  }
  \context {
    \Staff

    %
    %         \remove Forbid_line_break_engraver
  }
  \context {
    \Staff
    \remove Time_signature_engraver
    % 		fontSize = #-1
    explicitClefVisibility = #end-of-line-invisible
  }
  \context {
    \RhythmicStaff
    \remove Time_signature_engraver
  }
  % \context{
  %   \PianoStaff
  %   \override StaffGrouper.staff-staff-spacing =
  %   #'((basic-distance . 10)
  %      (minimum-distance . 2)
  %      (padding . 1)
  %      (stretchability . 9))

  %   \override StaffGrouper.staffgroup-staff-spacing =
  %   #'((basic-distance . 10)
  %      (minimum-distance . 2)
  %      (padding . 1)
  %      (stretchability . 9))
  % }
}

\paper {
  system-separator-markup = \markup { \slashSeparator }
  system-system-spacing = #'((basic-distance . 16) (minimum-distance . 16) (padding . 4))

  indent = 20\mm
  short-indent = 15\mm
  bottom-margin = 10\mm
  left-margin = 10\mm
  right-margin = 10\mm
  top-margin = 10\mm

  %{ top-margin = 1\cm
	bottom-margin = 1\cm
	left-margin = 2\cm
	right-margin = 1\cm %}

  oddHeaderMarkup = \markup ""
  evenHeaderMarkup = \markup ""
  oddFooterMarkup = \markup
  \fill-line {
    \override #'(font-name . "STIXGeneral")
    \bold \fontsize #3 "no "
    \concat {
      \override #'(font-name . "STIXGeneral")
      \bold \fontsize #3
      %{ \on-the-fly #print-page-number-check-first %}
      \fromproperty #'page:page-number-string
    }
  }
  evenFooterMarkup = \markup
  \fill-line {
    \concat {
      \override #'(font-name . "STIXGeneral")
      \bold \fontsize #3
      %{ \on-the-fly #print-page-number-check-first %}
      \fromproperty #'page:page-number-string
    }
    \override #'(font-name . "STIXGeneral")
    \bold \fontsize #3 "nothing"
  }
}


