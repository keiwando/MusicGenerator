\header{ title = "Random Music"} 

upper = \new Voice \with {
 \remove "Note_heads_engraver"
 \consists "Completion_heads_engraver"
}
{
 	\clef treble
	b'8. e'1. r2. r1 d'1. r2 r8 a'8 r8 e''1 r2 g'16. c'1. r16. r1. b''8 r8. c''2 r8. c''16 r8 r1. r8. r16 r8 b'16 r8 r8 a'16 r8 r16 r8 r8 d'8 r8 r4 r8 r8 r8. r8 c'1 r1 r8 r8. r8. r16. r4. b'1. r2. r8. r1 e'8. r8. g'4. r8 r1. c'2 r2. r16. r2 c''16. r8. r8 r8. r1 a'8. r16 r8 r8 c'2 a'1. r1 d'2 d''8 c'8. f''16 e'8 e'16 r1. a'8 c''8 d'4 r16 r16 c'4 a'8 a'8 r8. f''8 b'1 r8. b'1 g'8 c'2. r4. r8 b''8 r8. r8. r16 r8 c''4 r16 d'8. r1 c'8. g'8 f'16. r1 r16. f'8 r8. f'8. a'8. r8. e''8. r2 a'1 d'2 b'8. r8 r16. r1. e'16. f'1. r8. a'4 r8 r2. c'8 r2. d'8. r8 d'1. b'4. a''16. d'8 b'16 e'1 g''1 r8 r16 c'4 f'8. r2. r8 f'4. g'16. r8. r8 
}

lower = \new Voice \with {
 \remove "Note_heads_engraver"
 \consists "Completion_heads_engraver"
}
{
 	\clef bass
	r8. a1. g8 r8. r8 g8. r4. r8. b8. d,16 r4 r1 f,2. f,1 f8. a8 r16. c,16 r16. c16 b8 r8 r8. d4 r2. a8. r8. r4. g2. c16 g1. r8 c2. g,2 c2 a2. r4. r8. b,8 r4. r8 g,8 g8 c8. r8 r16 r8 r8. f4. r8. c16. f,2 r8 d8. r2 a8. r8. f8. r8. r16. r4 r16 r8 c8. a2 r8 e8 b8. r8 r16 c2 d,2 e16 r1. r8 g16 d16 r16 e,2. c,8. r16. r1 g8 r2. r2. c,1. r8. a8 r8 r4. c2. c1 c8. r8 c8 r8. g,2 g8 f1 c8 r16 d,8. c8. c,8. r8. f8. r1. a8. a4. r8. c8 b8. r8 e1. r8 a16 r8 r8. r8. a,2. c8 r16. r16. r16. f8 e2 r2. c4 d8 r1. a8. r8. r8 r8. b1. r8 c,8. r8 a1 r8. a2 a1. r2 g4. g2 c,8. r8 r16. a16 e1. 
}

\score {
 \new PianoStaff <<
  %\set PianoStaff.instrumentName = #"Piano  "
  \new Staff = "upper" \upper
  \new Staff = "lower" \lower
 >>
}

\version "2.18.2"