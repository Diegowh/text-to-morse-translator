import sqlite3

class MorseDB:
    def __init__(self, db_path) -> None:
        self._db_path = db_path
        self._connection = None
        self._cursor = None
        
    def connect(self):
        self._connection = sqlite3.connect(self._db_path)
        self._cursor = self._connection.cursor()
        
    def create_table(self):
        self._cursor.execute("CREATE TABLE text_to_morse (text text, morse text)")
        
    def insert_alphabet(self, alphabet):
        self._cursor.executemany("INSERT INTO text_to_morse VALUES (?,?)", alphabet)
        
    def search(self, letter):
        self._cursor.execute("SELECT * FROM text_to_morse WHERE text=:t", {"t": letter})
        letter_search = self._cursor.fetchall()
        return letter_search[0][1]
    
    def close(self):
        self._connection.close()