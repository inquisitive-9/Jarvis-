import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')


def speak(text): 
    print(f"SPEAK CALLED WITH: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Speech error: {e}")

def processcommand(c):
    c = c.lower()
    if "open youtube" in c:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c:
        webbrowser.open("https://www.google.com")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")
    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")
    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")
    elif c.startswith("play"):
        song = c.replace("play", "", 1).strip()
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            engine.say(f"Sorry, I couldn't find {song} in your music library.")

if __name__ == "__main__":
    speak("say jarvis to activate jarvis") 
    while True:
        r = sr.Recognizer()
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(f"Heard: {word}")
            if (word.lower() == "jarvis"):
                engine.say("yes sir")
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                    processcommand(command)
        except Exception as e:
            print("error: {0}".format(e))