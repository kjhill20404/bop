from gtts import gTTS
import playsound
import os
import random
import time

def os_speak(audio_string):
	tts = gTTS(text=audio_string, lang='en')
	r = random.randint(1, 1000000)
	audio_file = 'audio-' + str(r) + '.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	os.remove(audio_file)
	
def ohno():
	path = '/home/kevin/Documents/bop/dep/'
	playsound.playsound(path + 'battle003.mp3')
