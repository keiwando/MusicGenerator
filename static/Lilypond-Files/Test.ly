\header{ title = "A scale in LilyPond" } 

 upper = \new Voice \with {
    \remove "Note_heads_engraver"
    \consists "Completion_heads_engraver"
  } \relative c''{
   \clef treble <c e g>2 bes1 g4 a b c } 

 lower = \relative c{ \clef bass <d f a> gis16 g f d f2 } 

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