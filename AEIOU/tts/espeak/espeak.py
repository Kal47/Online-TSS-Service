import pyttsx3

def espeakToWav(filePath, phrase):
	engine = pyttsx3.init()
	engine.save_to_file(phrase, 'test.wav')
	engine.runAndWait()

def espeakToOGG(filePath, phrase):
	engine = pyttsx3.init()
	engine.save_to_file(phrase, 'test.ogg')
	engine.runAndWait()
