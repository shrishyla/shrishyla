import speach_recogonition as sr
r = sr.Recogonizer()
with sr.Microphone() as source
	r.adjust_for_ambient_noise(source, duration=5)
	print("say something")
	while True:
		audio=r.listen(source)
		print("you said"+r.recogonise_google(audio))