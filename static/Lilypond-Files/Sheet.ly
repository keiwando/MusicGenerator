\header{ title = "Random"} 

upper = \new Voice \with {
 \remove "Note_heads_engraver"
 \consists "Completion_heads_engraver"
}
{
 	\clef treble
	ees'8 r8 fis'8 aes''1 r8. r8 ges'8. r16. r1 cis'8 r8 dis'2 ais'8. r8. gis'8. ges'8. r2. r1. r2 r8 fes'8 r8 a'8. r8. r16. gis'8. r2. r2 des'4. a'8. bis'8. eis'8. cis'2 r2. a'2. g'4. e'1. r8 fis'8 r8 r8 f''8. fes'2 r4 e'8 ees'8 r1 r8 ces''8 g'8 cis'2 r1. r8. ces'1. r2 r1. des'8 r2. ces'2 bes'8. ces'8 bes'8 r16. r4 bes'4 r4 r8 c'2 r4. gis''2. ces'8 r8 r16. r4 r1 dis'4. r8. r8. e''1 eis''4 r8. bis''8. r16 r8 r8. eis'8. r2 ges'4 r8. eis'8 fes'8. r8. dis''8 ces'1 r8 r4. r16 ees'2 r4. ais'8 r8 r4 r8 r4 r8 r8 r4 r2 r16 r16 ges'8. r8. r4 b''2. r8. fes''8. r2. r8 aes'8 r2 r8. r4 ees''8. fes'8. r2 gis''8. bis'8 fis'2. dis'8. g'16. r8 r2 r8. r8. fes''2. r8 r8 r8 ces'1. r2 r8 ces'16 r16 r8. fis'2 gis'2. r4. r8. r8 r4. 
}

lower = \new Voice \with {
 \remove "Note_heads_engraver"
 \consists "Completion_heads_engraver"
}
{
 	\clef bass
	fis8. r2. bis,4. bes2. cis8 d8 r4. r1. ces8. r8 r16. gis8 ges4. c4. gis,4 r8. r8. r8 r4. r1 cis2 ces8. r8. r8 r8. gis,4. r8. bis4. d8 aes1 f8 r8 r8. r8 b,8 r4 ges8. fes8 r8. r8. d8. d8. r8 gis8. r8. eis,8 r2. r8. e8. r8 r1. aes8. gis1. fis1. r8 r8. ais2 r2 aes1 r8 r8. r8 r1. cis8 gis,8 d2 r8 r8. cis4 ges,8. ais8. r8. r4 r16 gis16 r16. r16. r8 r1. ais8 ces16. r2 r8. des1. gis16. r8 r8 ces2. r8. bis16. d16. des1 dis4 eis8 a,8. gis8. f2 r4. ees8. r1. aes8. r8 r8 r4. r8 des8 des8 ces8 r4 r8 fis4 r8. des,8 a8. b2 ees8. cis4. fes,8. aes,8 cis1 fes,1. ees,2. r1 r4. r4. r1. bes8. r4 r2 r2 r16 gis16 r8 fes4 r2 r8. ees8. r8. r8. r1. dis16 ees,8. r1 a,4 r1. r2. r8. r1 r8. r2. 
}

\score {
 \new PianoStaff <<
  %\set PianoStaff.instrumentName = #"Piano  "
  \new Staff = "upper" \upper
  \new Staff = "lower" \lower
 >>
}

\version "2.18.2"