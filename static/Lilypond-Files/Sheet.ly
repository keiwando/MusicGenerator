\header{ title = "Random"} 

upper = \new Voice \with {
 \remove "Note_heads_engraver"
 \consists "Completion_heads_engraver"
}
{
 	\clef treble
	c'1. r4\fp g'8. r8. a'8. r4.\ff a'2.\portato e'8 a'1.\fff r8 r8 a'8. d'4. e'8. e'8 f'1 r8 r8 r4. d''16.\staccato r8. a'1 r8.\trill r8 b'4 r8 r1\sf f'4.\portato a''8 r2 r4. r4\turn a'2\portato r8. r2 r8 f'8.\! c'8.\p c'16. r8. r1 c''8\accent r8 b'16\expressivo b'8 r8 r16\) r2 c''8.\fermata g'8. r1 r8. r8. r4. r4 r8. r8 r8.\ppp c'8\portato d''8\pp c'1 r4 r8.\tenuto c'2. r8. c''4. r8\staccato r8 r8. c'16 r8.\< r16. g'2 r1. r16. a'8.\< c'8. r8. r8. g'8 e'4. r8 r1. r8 d'8. d''8\ff c'8. r4.\) r2 r4 b'8. f'8. e'1.\tenuto r8 r8. r1 r8 a''1 e'1. a'2.\! r8 r8. d'8. b''8. c'8 e'2. r4 c'8. c'1. g'2. r4\mordent r2 f''8. r16\accent c''8. b'8. r1 c''8. d'2. r1 r1 r16\tenuto a''8\accent b''8 a'8. r2 b'8. f'8 e''8 f'16.\accent g'8.\pp r2 r8. e''2.\( r2.\accent d'8.\staccato c''8. r8. r2 r1 r2 b'8. r16 r2. r1. r8. r1. e'4 c'1 d'8. 
}

lower = \new Voice \with {
 \remove "Note_heads_engraver"
 \consists "Completion_heads_engraver"
}
{
 	\clef bass
	a,8. e8\fp r8. r8 c8 r8 g,8\prall r8 e,4.\ppp r8. g2 f8\sfz c2 r1. r8. r8 g8. e1. r8. c1. e,1. f2. c8\> a,8. r8. e,2. r8. f2.\mordent r8. r1 e2. r8 r1. r1. r4. r16 r16.\prall b8\mp f16.\staccato r8 a,16. a8 e1\staccato e8 r16. r16. r8 c8 d1.\trill e,1. r8 c2. r2\sp b2 c1. c,8 r8 d8.\portato c8 r4 r4.\fff r8. r2.\fp g8 r8. c16 e1\tenuto r8 e,16. a8.\sp d8 r2 r16 c16. a8 r8 e8. r1. b8\sfz f8. f1 d,8. b2 r8.\mp r1 f8. r8 c,8. r2 r8 r8. r8 e8 r4 e2. f8. g,4 b,1\sf r1. r8. r16. d8 f8.\sp r8. d,2. g8. f,8. b2. r8.\accent r8 b,1\expressivo c2 d8\portato b8 e,8 d8.\trill r1 a4. r8. r1 r16 g1. r8 c,8 r16. r8 r16. c8 c,8 d16\expressivo r16 a8 r8.\p a,8\) e4. g,4. r1 r8.\sf a4 r8. e,8. c1 b8 r4. c8.\staccato e16. r4 e2\accent g8 r4 
}

\score {
 \new PianoStaff <<
  %\set PianoStaff.instrumentName = #"Piano  "
  \new Staff = "upper" \upper
  \new Staff = "lower" \lower
 >>
}

\version "2.18.2"