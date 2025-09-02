import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text): 
    engine.say("text")
    engine.runAndwait()

    def processcommand(c):
        if "open YouTube" in c.lower:
            webbrowser.open("https://www.youtube.com")
        elif "open Google" in c.lower:
            webbrowser.open("https://www.google.com")
        elif "open LinkedIn" in c.lower:
            webbrowser.open("https://www.linkedin.com")
        elif "open Instagram" in c.lower:
            webbrowser.open("https://www.instagram.com")
        elif "open facebook" in c.lower:
            webbrowser.open("https://www.facebook.com")

        elif c.lower().startswith("play") :
            song = c.lower().split("")[1]         #c.lower = "song name here"
            link = musiclibrary.music[song]   
            webbrowser.open(link)                
        else:
            speak("Sorry, I didn't understand that command.")

    if __name__ == "__main__":
        speak("Hello, how can I assist you today?") 

    r = sr.Recognizer()

    print("recoznizing")
    try:
        with sr.Microphone() as source:
         print("Listening...")
         audio = r.listen(source,timeout=2,phrase_time_limit=2)        # Use microphone as source
      
        word = r.recognize_google(audio)          # Convert speech to text
        if(word.lower()=="jarvis"):
         speak("yes sir")                             # Respond to wake word
            
        with sr.Microphone() as source:
         print("Listening...")
         audio = r.listen(source )   
         command = r.recognize_google(audio) 

         processcommand(command)
    except Exception as e:
        print("error; {0}".format(e))