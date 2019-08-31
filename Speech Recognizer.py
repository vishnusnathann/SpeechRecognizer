# speech recogonition 

import speech_recognition as sr 

r=sr.Recognizer()
print("Speak anything : ")
while(1):
	with sr.Microphone() as source:

		audio =r.listen(source) # recording voice
		
		try:
			
			text = r.recognize_google(audio)

			print("you >{}".format(text))#printing the speech to text 

			#3 test cases in order to respond to the user command
			if format(text)=="hello":
				print("System > hello boss")
			elif format(text)=="how are you":
				print("System > I'm good")
			elif format(text)=="I love you":
				print("System > Love you 3000")
			else:
				print("System > sorry boss I didn't get that")

		except Exception as e:
			print("don't understand")
		else:
			pass
		finally:
			pass
