#!/usr/bin/env python

import os
import traceback
from pydub import AudioSegment


def debugSay():
	print("Saving Wav file to 42.wav...")
	print(sayToWavFile('test', "this is a test Waveform Audio File Format"))
	print("Done.")
	print("Saving Ogg file at 42.ogg...")
	print(sayToOggFile('test', "this is a test Ogg Vorbis Audio File"))
	print("Done.")
	#open("phrase.txt", "r").read().rstrip())

def sayToWavFile(filePath, phrase):
	sanitizePhrase(phrase)
	command = 'wine say.exe -w '+filePath+'.wav "'+phrase+'"'
	os.system(command)
	return command

def sayToOggFile(filePath, phrase):
	tempFilePath = '/tmp/temp.wav'
	sanitizePhrase(phrase)
	command = 'wine say.exe -w '+tempFilePath+' "'+phrase+'"'
	os.system(command)
	
	sound = AudioSegment.from_file(tempFilePath, format="wav")
	sound.export(filePath+".ogg", bitrate='32k', format="ogg")
	os.remove(tempFilePath)
	return filePath+".ogg"

def sanitizePhrase(phrase):
	phrase.replace('"','')
	phrase.replace(';','')
	phrase.replace('&','')
	phrase.replace('|','')
	return phrase

#debugSay()
