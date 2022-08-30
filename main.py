from vosk import Model, KaldiRecognizer
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

import pyaudio

def speak(text):
    tts = gTTS(text=text)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

model = Model(r"C:\Users\loges\PycharmProjects\FirstAssistant\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)

    if recognizer.AcceptWaveform(data):

        text = recognizer.Result()

        if "hello" in text:
            speak("hi log welcome back")
        if "what is your name" in text:
            speak("my name is rosy")
        if "what is my name" in text:
            speak("Your name is log")
        if "Hey you" in text:
            speak("Hi log")
        if "who are my friends" in text:
            speak("Gokul and Aravind")
        if "Good Night":
            speak("Good night log")

