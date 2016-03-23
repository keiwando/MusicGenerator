from subprocess import call
import os
import re

def compile():
	pathToScript = os.path.dirname(__file__)
	#pathToScript = os.path.dirname(pathToScript)

	#pathToScript = os.path.join(pathToScript,"Contents")
	pathToScript = os.path.join(pathToScript,"static/scripts")
	pathToScript = os.path.join(pathToScript,"CompileFile.sh")

	print pathToScript

	pathToScript = re.sub(" ","\ ",pathToScript)

	print "New Path: ", pathToScript

	call(pathToScript, shell=True)

def test():
	return "Test"