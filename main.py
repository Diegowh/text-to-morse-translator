# This is a text-based (command line) program that takes any String input and converts it into Morse Code.
# This program will be upgraded with a UI using tkinter 

from constants import *
from morse_translator import MorseTranslator
from translator_app import TranslatorApp



if __name__ == "__main__":
    app = TranslatorApp()
    app.run()
