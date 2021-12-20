# Nav Module

## _The solution for voice related stuff in Python_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Nav is a Python module which simplifies voice related stuff in Python.

- Just import the Module class from the nav module
- Use only one line of code to use the Text-To-Speech and speech_recognition.
- ✨Magic ✨

## Usage

- Make a `.py` file.
- Import Module class from the nav module. `from nav import Module`
- Use `Module.Voice.speak("Your text here", "voice_gender")` to use the Text-To-Speech (TTS)
- Use `Module.Voice.listen.said_text()` to use the speech_recognition.
- You can use `Module.Music.play_music(path)` to play a music and `Module.Music.beep(hz, ms)` to make a beep sound.

## Example (TTS)

```
from nav import Module

my_text = "Your text here"
Module.Voice.speak(my_text, "male")
```

The Nav module makes the life of programmers using voice related stuff in Python.
