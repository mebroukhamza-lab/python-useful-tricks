# pip install SpeechRecognition pyaudio
import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)
text = recognizer.recognize_google(audio)
print("You said:", text)
