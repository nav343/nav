"""
Nav Module. Version 0.0.1. Unmodified.

The module is made to simplify the things related to voice in python.
The Module class is kind of a wrapper for all the other functions of this module.
Use <from nav import Module> code to get access to all the functions of this module.
You can use <Module.Voice.speak()> for using the text-to-speech (aka tts). The speak() functions takes to parameters, one, the original/main text and the second, gender, use "male" for male voice and "female" for female voice.

You can use <Module.Voice.listen.said_text()> to use speech recognition in python, using the google speech_recognition api. For doing further stuff with the audio, make a variable and call it anything you like, set its value to <Module.Voice.listen.said_text()> and then try printing the variable. The output will be the text that you just spoke.

Author : Navaneeth K (aka Snm_Logic)
Doc written Date : 19/12/2021
Project Started on : 10/12/2021
Version : 0.0.1 (v1)
Source_Code : ___???____ ( Github )

Please visit the official github page for contributing to this project.
"""

'''
Importing all the required modules.
'''

import pyttsx3
import speech_recognition as sr
import winsound
r = sr.Recognizer()
source = sr.Microphone()


class Module():
    class Voice:
        def speak(txt, gender):
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            rate = engine.getProperty('rate')
            engine.setProperty('rate', 170)
            if gender == 'male':
                engine.setProperty('voice', voices[1].id)
            elif gender == 'female':
                engine.setProperty('voice', voices[0].id)
            else:
                print("Invalid name")
            engine.say(txt)
            engine.runAndWait()

        class listen():
            def said_text():
                with sr.Microphone(sample_rate=48000) as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    return text

    class Music():
        def play_music(path):
            filename = path
            winsound.PlaySound(filename, winsound.SND_FILENAME)

        def beep(hz, ms):
            winsound.Beep(hz, ms)


Module()
