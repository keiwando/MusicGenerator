\header{ title = "Title"} 

upper = \new Voice \with {
 \remove "Note_heads_engraver"
 \consists "Completion_heads_engraver"
}
{
 	\clef treble
	c d e'''' fis
}

lower = \new Voice \with {
 \remove "Note_heads_engraver"
 \consists "Completion_heads_engraver"
}
{
 	\clef bass
	<c,, e g>2 <d fis a>2
}

\score {
 \new PianoStaff <<
  \set PianoStaff.instrumentName = #"Piano  "
  \new Staff = "upper" \upper
  \new Staff = "lower" \lower
 >>
}

\version "2.18.2"