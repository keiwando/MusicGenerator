\header{ title = "A scale in LilyPond" } 

 upper = \new Voice \with {
    \remove "Note_heads_engraver"
    \consists "Completion_heads_engraver"
  } 
  \relative c'{
   	\clef treble 
    \key c \minor
   	<c e g>2 bes1 g4 a b c 
  } 

 lower = \new Voice \with {
    \remove "Note_heads_engraver"
    \consists "Completion_heads_engraver"
  } 
  \relative c{ \key c \minor \clef bass <d f a> gis16 g f d f1 } 

 \score {
  \new PianoStaff <<
    \set PianoStaff.instrumentName = #"Piano  "
    \new Staff = "upper" \upper
    \new Staff = "lower" \lower
  >>
  \layout { }
  \midi { }
}

 \version "2.18.2"