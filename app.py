import pyttsx3
talk = pyttsx3.init()
speech = input("write:")
rate = talk.getProperty('rate')
print(rate)
talk.setProperty('rate', 140)
voices = talk.getProperty('voices')
talk.setProperty('voice', voices[0].id)
talk.say(speech)
talk.runAndWait()


