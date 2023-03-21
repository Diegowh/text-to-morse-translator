import sqlite3
from morse_db import MorseDB
from constants import *

class MorseTranslator:
    def __init__(self, db_path) -> None:
        self._db = MorseDB(db_path)
        self._db.connect()
        try:
            self._db.create_table()
        except sqlite3.OperationalError:
            pass
        self._db.insert_alphabet(MORSE_CODE_ALPHABET)
        
    def __del__(self):
        self._db.close()
    
    
    def translate(self, input_phrase):
        try: 
            morse_phrase_list = [self._db.search(character) for character in input_phrase]
        except IndexError:
            return "You have entered invalid characters."
        else:
            morse_phrase = ""
            for i, character in enumerate(morse_phrase_list):
                morse_phrase += character
                if i != len(morse_phrase_list) - 1:
                    morse_phrase += "   "
            return morse_phrase