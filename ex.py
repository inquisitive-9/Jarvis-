import speech_recognition as sr
import pyttsx3
import time

engine = pyttsx3.init('sapi5')
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

print("Done listening.")
time.sleep(1)
engine.say("yes sir")
engine.runAndWait()