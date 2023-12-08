import speech_recognition as sr # You have to install SpeechRecognition
import pyttsx3 as tts           # You have to install pyttsx3 and pyaudio

r = sr.Recognizer()
engine = tts.init()
engine.setProperty("rate", 140)

def mow(text):
    engine.say(text)
    engine.runAndWait()

def getText():
    with sr.Microphone() as source:
        try:
            print("I'm listening...")
            audio = r.listen(source)
            text = r.recognize_google(audio, language="pl-PL")
            if text !="":
                return text
            return 0
        except:
            return 0
            
while True:
    txt = getText()
    if not txt == 0:
        print(txt)
        mow(txt)
        break
    else:
        print("I couldn't recognized..")
        continue