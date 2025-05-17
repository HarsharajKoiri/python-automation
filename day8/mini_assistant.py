import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "assistant" in command:
                command = command.replace("assistant", "")
            return command
    except:
        return ""

def run_assistant():
    command = listen()
    print(f"🗣️ You said: {command}")

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        pywhatkit.info(person, 1)
    else:
        talk("Sorry, I didn't get that.")

if __name__ == "__main__":
    talk("Hi Harsh, I am your assistant. What can I do for you?")
    run_assistant()
