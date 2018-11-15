import speech_recognition as sr
AUDIO_FILE=("example2.wav")
#use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
#reads the audio file.here we use record intead of listen
	audio = r.record(source)
try:
	print("the audio file contains:"+r.recogonize_google(audio))
except sr.UnknownValueError:
	print("google speech recogonition could not understand audio")
except sr.RequestError as e:
	print("could not request results from google speech recogonition service:{0}".format(e))
