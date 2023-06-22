import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from tkinter import *
import numpy as np
import random
import sys
import webbrowser
from rck import rps
from tictaktoe import tictaktoe

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'spark' in command:
                command = command.replace('spark', '')
                print(command)
    except:
        pass
    return command


def run_spark():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'ttt' in command:
         print(tictaktoe())
    elif 'rock paper scissor' in command:
         print(rps())
    elif 'close' in command:
         print("Program is going to closed")
         print(sys.exit(0) )
    elif 'open google' in command:
         print(webbrowser.open('http://google.com', new=2))
    elif 'open instagram' in command:
         print(webbrowser.open('https://www.instagram.com/parsivinish/', new=2))

    else:
        talk('Please say the command again.')


while True:
    run_spark()