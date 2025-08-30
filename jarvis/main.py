import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text): 
    engine.say("helloooo")
    engine.runAndwait()

    if __name__ == "__main__":
        speak("Hello, how can I assist you today?") 

    recognizer = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

try:
    # Convert speech to text
    command = r.recognize_google(audio)
    print(command)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")