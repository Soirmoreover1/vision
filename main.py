import speech_recognition as sr 
import sys
rec = sr.Recognizer()

with sr.Microphone() as src:  # Initialize an instance of Microphone
    while True :
        print("Say something........")
        audio = rec.listen(src)
        text = rec.recognize_google(audio_data=audio, language="ar")

        print(text)
        if text in "اغلاق":
            sys.exit(0)