# library yang harus digunakan / library that you must use
import speech_recognition as sr
import playsound
import webbrowser
import random
import time
import os
from gtts import gTTS
from time import ctime

# method speechrecogition
r = sr.Recognizer()

# function untuk merekam audio / function for recording the audio
def record_audio(ask = False):
	with sr.Microphone() as source:
		if ask:
			nopedawn_speak(ask)
		audio = r.listen(source)
		voice_data = ''
		try:
			voice_data = r.recognize_google(audio)
		except sr.UnknownValueError:
			nopedawn_speak('Sorry, I did not get that')
		except sr.RequestError:
			nopedawn_speak('Sorry, My speech service is down')
		return voice_data

# function bot / narrator
def nopedawn_speak(audio_string):
	tts = gTTS(text=audio_string, lang='en')
	r = random.randint(1, 10000000)
	audio_file = 'audio-' + str(r) + '.mp3'
	tts.save(audio_file)
	playsound.playsound(audio_file)
	print(audio_string)
	os.remove(audio_file)

# function untuk membaca audio dan merespon function record_audio
def respond(voice_data):
	if 'what is your name' in voice_data:
		nopedawn_speak('My name is dawn')
	if 'tes tes... cek satu dua tiga, masuk masuk' in voice_data:
		nopedawn_speak('sorry.. can you speak english?')
	if 'can you help me' in voice_data:
		nopedawn_speak('yeahh! of course')
	if 'what time is it' in voice_data:
		nopedawn_speak(ctime())
	if 'search' in voice_data:
		search = record_audio('What do you want to search for?')
		url = 'https://google.com/search?q=' + search
		webbrowser.get().open(url)
		nopedawn_speak('Here is what I found for ' + search)
	if 'find location' in voice_data:
		location = record_audio('What is the location?')
		url = 'https://google.nl/maps/place/' + location + '/&amp;'
		webbrowser.get().open(url)
		nopedawn_speak('Here is the location of ' + location)
	if 'exit' in voice_data:
		nopedawn_speak('have a nice day sir! good bye...')
		exit()

# method library time
time.sleep(1)
nopedawn_speak('Welcome back sir, how can I help you?')

# for while
while 1:
	voice_data = record_audio()
	respond(voice_data)