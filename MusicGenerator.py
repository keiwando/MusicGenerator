'''
Creates Lilypond Files Based On Input or 'Randomly'.
'''

import os
import random
from collections import deque

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


	

class ExpressionDecoder:
	def __init__(self,Expression,complexity):
		self.complexity = complexity
		self.Expression = Expression
		self.dynamics = ['ppp','pp','p','mp','mf','f','ff','fff','fp','sf','sp','sfz',"<",">","!"]
		self.Expressionulation = ['(',')','staccato','portato','trill','accent','tenuto', 'turn','fermata','prall', 'mordent','expressivo']

	def nextExpression(self):
		dec = int(self.Expression.next(1),2)
		index = int(self.Expression.next(4),2)
		if dec == 0:
			index = index % len(self.dynamics)
			return self.dynamics[index]
		else:
			index = index % len(self.Expressionulation)
			return self.Expressionulation[index]

	def next(self):
		
		dec = int(self.Expression.next(2),2)
		comp = self.complexity
		if comp == 1:
			return ""
		elif comp == 2:
			if dec < 3:
				return ""
			else:
				return "\\" + self.nextExpression()
		elif comp == 3:
			if dec < 2:
				return ""
			else:
				return "\\" + self.nextExpression()


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

def generateRandomExpString():
	length = 2400
	maxDecimal = (2**length)
	resultAsDecimal = random.randint(0,maxDecimal)
	resultAsBinary = bin(resultAsDecimal)[2:].zfill(length)
	return resultAsBinary

def repeatListToSize(oldList,size):
	newList = []
	for i in range(0,size):
		newList.append(oldList[i%len(oldList)])
	return newList

def getNextMelodyOrChord(melody):
	#melody is a deque
	result = ""
	maxNotesInChord = 10
	counter = 0
	nextNote = melody.pop()
	peek = melody.peek()
	copy = nextNote
	last = nextNote[-1:]
	first = nextNote[0:1]

	if first == "<":
		if peek[0:1] == "<":
			result += ">"
		result += nextNote
		counter += 1
		while last != ">" and len(melody) > 0 and counter < maxNotesInChord:
			nextNote = melody.pop()
			result += " " + nextNote
			last = nextNote[-1:]
			counter += 1

			if (len(melody) == 0 and last != ">") or counter == maxNotesInChord:
				result += ">"
			
		return result
	else:
		return nextNote

def writeRandomLilyPondFile(rhythmCompl,melodyCompl,ExpressionCompl):
	rhythmString = generateRandomRhythmString()
	melodyString = generateRandomMelodyString()
	ExpressionString = generateRandomExpString()
	rhythm = StringQueue(rhythmString)
	melody = StringQueue(melodyString)
	Expression = StringQueue(ExpressionString)
	rDecoder = RhythmDecoder(rhythm,rhythmCompl)
	mDecoder = MelodyDecoder(melody,melodyCompl)
	aDecoder = ExpressionDecoder(Expression,ExpressionCompl)

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
		#expressions
		musicUpper += aDecoder.next()
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
		musicLower += aDecoder.next()
		musicLower += " "

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

def writeSheet(title,rhyCompl,melCompl,exprCompl,rhythmTreble,rhythmBass,melodyTreble,melodyBass,expressionTreble,expressionBass):
	#rhythm
	if rhyCompl == "0":
		#rhythm from input
		rhythmTreble = rhythmTreble.split()
		rhythmBass = rhythmBass.split()

		if len(rhythmTreble) == 0:
			rhythmTreble = ['x4']
		if len(rhythmBass) == 0:
			rhythmBass = ['x4']

		rhythmTreble = repeatListToSize(rhythmTreble,150)
		rhythmBass = repeatListToSize(rhythmBass,150)
	else: 
		rhythmTreble = generateRandomRhythmString()
		rhythmTreble = StringQueue(rhythmTreble)
		decoder = RhythmDecoder(rhythmTreble,int(rhyCompl))
		rhythmTreble = []
		for i in range(0,150):
			rhythmTreble.append(decoder.next())
		
		rhythmBass = generateRandomRhythmString()
		rhythmBass = StringQueue(rhythmBass)
		decoder = RhythmDecoder(rhythmBass,int(rhyCompl))
		rhythmBass = []
		for i in range(0,150):
			rhythmBass.append(decoder.next())

	#melody
	if melCompl == "0":
		melodyTreble = melodyTreble.split()
		melodyBass = melodyBass.split()

		if len(melodyTreble) == 0:
			melodyTreble = ['c\'']
		if len(melodyBass)  == 0:
			melodyBass = ['c']

		melodyTreble = repeatListToSize(melodyTreble,300)
		melodyBass = repeatListToSize(melodyBass,300)
	else:
		melodyTreble = generateRandomMelodyString()
		melodyTreble = StringQueue(melodyTreble)
		decoder = MelodyDecoder(melodyTreble,int(melCompl))
		melodyTreble = []
		for i in range(0,300):
			melodyTreble.append(decoder.next("treble"))

		melodyBass = generateRandomMelodyString()
		melodyBass = StringQueue(melodyBass)
		decoder = MelodyDecoder(melodyBass,int(melCompl))
		melodyBass = []
		for i in range(0,300):
			melodyBass.append(decoder.next("bass"))

	#expressions
	if exprCompl == "0":
		expressionTreble = expressionTreble.split()
		expressionBass = expressionBass.split()

		if len(expressionTreble) == 0:
			expressionTreble = ['']
		if len(expressionBass) == 0:
			expressionBass = ['']

		expressionTreble = repeatListToSize(expressionTreble,300)
		expressionBass = repeatListToSize(expressionBass,300)
	else:
		expressionTreble = generateRandomExpString()
		expressionTreble = StringQueue(expressionTreble)
		decoder = ExpressionDecoder(expressionTreble,int(exprCompl))
		expressionTreble = []
		for i in range(0,300):
			expressionTreble.append(decoder.next())

		expressionBass = generateRandomExpString()
		expressionBass = StringQueue(expressionBass)
		decoder = ExpressionDecoder(expressionBass,int(exprCompl))
		expressionBass = []
		for i in range(0,300):
			expressionBass.append(decoder.next())	


	#create upper and lower staff
	musicUpper = ""
	musicLower = ""
	melodyTreble = deque(melodyTreble)
	melodyBass = deque(melodyBass)
	expressionTreble = deque(expressionTreble)
	expressionBass = deque(expressionBass)
	melodyTreble.reverse()
	melodyBass.reverse()
	expressionTreble.reverse()
	expressionBass.reverse()

	for i in range(0,150):
		if len(melodyTreble) > 0:
			beat = rhythmTreble[i]
			#determine if note or rest
			det = beat[0:1]
			if det == "x":
				#note
				musicUpper += getNextMelodyOrChord(melodyTreble)
				musicUpper += beat[1:]
			else:
				musicUpper += beat
			#expressions
			musicUpper += expressionTreble.pop()
			musicUpper += " "

	for i in range(0,150):
		if len(melodyBass) > 0:
			beat = rhythmBass[i]
			#determine if note or rest
			det = beat[0:1]
			if det == "x":
				#note
				musicLower += getNextMelodyOrChord(melodyBass)
				musicLower += beat[1:]
			else:
				musicLower += beat
			#expressions
			musicLower += expressionBass.pop()
			musicLower += " "

	#print musicUpper
	#return "Upper: " + musicUpper + " Lower: " + musicLower
	#write lilypond file
	writeLilyPondFile(musicUpper,musicLower,"Sheet",title)


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

def testExpressionDecoder():
	testString = generateRandomExpString()
	expression = StringQueue(testString)
	decoder = ExpressionDecoder(expression,3)
	for i in range (0,400):
		print decoder.next()

def testNextMelOrChord():
	testInput = deque(['<a','c','d>','f','as','g','<a','eis','a','c','e','x','x','x','x','x','x','x','x','x','x'])
	testInput.reverse()
	while len(testInput) > 0:
		print getNextMelodyOrChord(testInput)


#testMelodyDecoder()
#writeRandomLilyPondFile(3,1,2)
#testNextMelOrChord()




