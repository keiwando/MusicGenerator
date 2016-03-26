'''
Creates Lilypond Files Based On Input or 'Randomly'.
'''

import os
import random

FILEPATH = os.path.dirname(__file__)
FILEPATH = os.path.join(FILEPATH,"static","Lilypond-Files")

class StringQueue:

	def __init__(self,str):
		self.str = str
		self.fr = 0		#fr = from
		self.to = 0

	def next(self,length):
		self.to += length
		result = self.str[self.fr:self.to]
		self.fr = self.to
		return result

class RhythmDecoder:

	def __init__(self,rhythm,complexity):
		self.rhythm = rhythm
		self.complexity = complexity

	def next(self):
		beat = self.rhythm.next(5)
		nor = beat[:1]
		length = beat[1:4]
		dot = beat[-1:]
		
		result = ""
		if nor == "1":
			result += "x"
		else:
			result += "r"

		length = int(length,2)
		if self.complexity <= 2:
			if length > 3:
				length = 3
		elif self.complexity == 3:
			if length > 4:
				length = 3
		result += str(2**length)

		if self.complexity > 1:
			if dot == "1":
				result += "."

		return result

	

class MelodyDecoder:
	def __init__(self,melody,complexity):
		self.melody = melody
		self.complexity = complexity
		self.inChord = False
		self.NiC = 0	#notes in chord

	def nextNote(self,clef):
		notes = ['c','d','e','f','g','a','b','c']
		accidentals = ['','is','es','isis','eses']
		octavesTreble = ['\'','\'',"\'","\'\'","\'\'","","\'\'\'","\'\'\'\'"]	#(0,0,+1,+1,+2,-1,+3,+4)
		octavesBass = ['','','',",",",",'',",,","\'"]	#(0,0,0,-1,-1,0,-2,+1)
		noteIndex = int(self.melody.next(3),2)
		note = notes[noteIndex]
		accIntex = int(self.melody.next(3))
		comp = self.complexity
		
		if comp == 1:
			accIntex = 0
		elif comp >= 2 and comp < 5:
			accIntex = accIntex % 3
		else:
			accIntex = accIntex % 5

		note += accidentals[accIntex]

		octave = int(self.melody.next(3),2) 
		if comp == 1:
			octave = octave % 4
		elif comp <= 3:
			octave = octave % 5
		elif comp == 4:
			octave = octave % 6
		elif comp == 5:
			octave = octave % 7

		if clef == "treble":
			note += octavesTreble[octave]
		elif clef == "bass":
			note += octavesBass[octave]
		else:
			print "Clef not known Error"

		return note


	def next(self,clef):
		comp = self.complexity
		if not self.inChord:
			if comp > 2:
				choN = self.melody.next(2)
				numberOfNotesInChord = int(self.melody.next(3),2)
				if comp == 3:
					numberOfNotesInChord = numberOfNotesInChord % 3
				elif comp == 4:
					numberOfNotesInChord = numberOfNotesInChord % 4
				else:
					numberOfNotesInChord = numberOfNotesInChord % 6

				self.NiC = numberOfNotesInChord
				self.inChord = True

		result = ""
		if self.NiC != 0:
			result += "<"
			while self.NiC > 0:
				result += " " + self.nextNote(clef)
				self.NiC -= 1
			result += ">"
			self.inChord = False
		else:
			result = self.nextNote(clef)

		return result


	

class ArticDecoder:
	def __init__(self,artic,complexity):
		self.complexity = complexity
		self.artic = artic

	def next(self):
		choice = ['accent','tenuto','expressivo', 'staccato', 'portato', 'turn', 'trill', 'prall', 'mordent', 'fermata']
		pass	

def generateLilyPondHeader(title):
	return "\\header{ title = \"" + title + "\"} \n\n"

def generateLilyPondUpper(notes):
	return "upper = \\new Voice \\with {" + "\n \\remove \"Note_heads_engraver\"" + \
			"\n \\consists \"Completion_heads_engraver\"\n}" + "\n{" + \
			"\n \t\\clef treble\n\t" + notes + "\n}\n\n"	#not  \\relative c\'

def generateLilyPondLower(notes):
	return "lower = \\new Voice \\with {" + "\n \\remove \"Note_heads_engraver\"" + \
			"\n \\consists \"Completion_heads_engraver\"\n}" + "\n{" + \
			"\n \t\\clef bass\n\t" + notes + "\n}\n\n"	#not  \\relative c

def generateLilyPondPianoScore():
	return "\\score {\n" + " \\new PianoStaff <<\n" + "  %\\set PianoStaff.instrumentName = #\"Piano  \"\n" + \
			"  \\new Staff = \"upper\" \\upper\n" + "  \\new Staff = \"lower\" \\lower\n >>\n}\n\n"

def generateLilyPondVersionNumber():
	return "\\version \"2.18.2\""

def generateRandomRhythmString():
	length = 1500
	maxRythmDecimal = (2**length)
	rhythmAsDecimal = random.randint(0,maxRythmDecimal)
	rhythmAsBinary = bin(rhythmAsDecimal)[2:].zfill(length)
	return rhythmAsBinary

def generateRandomMelodyString():
	length = 15000
	maxMelodyDecimal = (2**length)
	melodyAsDecimal = random.randint(0,maxMelodyDecimal)
	melodyAsBinary = bin(melodyAsDecimal)[2:].zfill(length)
	return melodyAsBinary

def generateRandomArtOrnDynString():
	length = 2400
	maxDecimal = (2**length)
	resultAsDecimal = random.randint(0,maxDecimal)
	resultAsBinary = bin(maxDecimal)[2:].zfill(length)
	return resultAsBinary

def writeRandomLilyPondFile(rhythmCompl,melodyCompl):
	rhythmString = generateRandomRhythmString()
	melodyString = generateRandomMelodyString()
	articString = generateRandomArtOrnDynString()
	rhythm = StringQueue(rhythmString)
	melody = StringQueue(melodyString)
	artic = StringQueue(articString)
	rDecoder = RhythmDecoder(rhythm,rhythmCompl)
	mDecoder = MelodyDecoder(melody,melodyCompl)

	musicUpper = ""
	for i in range(0,150):
		beat = rDecoder.next()
		#determine if note or rest
		det = beat[0:1]
		if det == "x":
			#note
			musicUpper += mDecoder.next("treble")
			musicUpper += beat[1:]
		else:
			musicUpper += beat
		musicUpper += " "

	musicLower = ""
	for i in range(0,150):
		beat = rDecoder.next()
		#determine if note or rest
		det = beat[0:1]
		if det == "x":
			#note
			musicLower += mDecoder.next("bass")
			musicLower += beat[1:]
		else:
			musicLower += beat
		musicLower += " "


	#missing art..

	#save to file
	writeLilyPondFile(musicUpper,musicLower,"Sheet","Random")


def writeLilyPondFile(upper,lower,filename,title):
	file = open(os.path.join(FILEPATH,filename + ".ly"),"w")

	text = generateLilyPondHeader(title)
	text += generateLilyPondUpper(upper)
	text += generateLilyPondLower(lower)
	text += generateLilyPondPianoScore()
	text += generateLilyPondVersionNumber()

	file.write(text)

	file.close()



def writeTestFile():
	file = open(os.path.join(FILEPATH,"Test2.ly"),"w")

	text = generateLilyPondHeader("Title")
	text += generateLilyPondUpper("c d e'''' fis")
	text += generateLilyPondLower("<c,, e g>2 <d fis a>2")
	text += generateLilyPondPianoScore()
	text += generateLilyPondVersionNumber()

	file.write(text)

	file.close()

#writeTestFile()

def testRhythmDecoder():
	testString = generateRandomRhythmString()
	rhythm = StringQueue(testString)
	decoder = RhythmDecoder(rhythm,3)
	for i in range(0,300):
		print decoder.next()

def testMelodyDecoder():
	testString = generateRandomMelodyString()
	melody = StringQueue(testString)
	decoder = MelodyDecoder(melody,3)
	for i in range(0,400):
		print decoder.next("treble")


#testMelodyDecoder()
#writeRandomLilyPondFile(3,1)







