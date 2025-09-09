import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text): 
    engine.say(text)
    engine.runAndWait()

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
            speak(f"Sorry, I couldn't find {song} in your music library.")

if __name__ == "__main__":
    speak("say jarvis to activate jarvis") 
    while True:
        r = sr.Recognizer()
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
            word = r.recognize_google(audio)
            print(f"Heard: {word}")
            if (word.lower() == "jarvis"):
                time.sleep(1)
                speak("yes sir")
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                    processcommand(command)
        except Exception as e:
            print("error: {0}".format(e))