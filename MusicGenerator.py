'''
Creates Lilypond Files Based On Input or 'Randomly'.
'''

import os

FILEPATH = os.path.dirname(__file__)
FILEPATH = os.path.join(FILEPATH,"static","Lilypond-Files")

def generateRandomRythm():
	pass

def generateRandomMelodie():
	pass

def writeLilyPondFile(rhythm,melodie):
	pass

def writeTestFile():
	file = open(os.path.join(FILEPATH,"Test.ly"),"w")

	text = "\\header{ title = \"A scale in LilyPond\" } \n\n \\relative c\'\'{ c d e f g a b c } \n\n \\version \"2.18.2\""

	file.write(text)

	file.close()

#writeTestFile()