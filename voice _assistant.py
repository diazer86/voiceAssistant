# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 06:09:34 2021

@author: ediaz
"""

import pyttsx3 as p
import speech_recognition as sr
import PySimpleGUI as sg


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)


def ToDoItem(num):
        return [sg.Text(f'{num}. '), sg.CBox(''), sg.In()]

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
r = sr.Recognizer()

speak("Hello sir I'm your voice assistant. How are you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I am having a good day sir, thanks for asking.")
speak("What can I do for you??")

#=============================================================================
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    
if "make me a to do list":
    speak("Here's your to do list.")
    layout = [ToDoItem(x) for x in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]
    window = sg.Window('To Do List Example', layout)
    event, values = window.read()
    
if "need" and "anything":
    speak('Can you give me some more game ')

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if"you know what Im saying" or "you feel me":
    speak("Facts, u aint never lie.")
#=============================================================================
    
    
    