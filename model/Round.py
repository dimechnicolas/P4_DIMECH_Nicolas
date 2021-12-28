from datetime import datetime

class Round:
    def __init__(self):
        self.name = name
        self.start_time = datetime.now().strftime('%d-%m%y %H%M%S')
        self.end_time = ''
        self.matches = []

    def __repr__ (self): # renvoi une représentation lisible par l'interpreteur/returns a representation readable by the interpreter
        return f'{self.name} ({self.start_time} - {self.end_time})'

    def __str__(self): # renvoi une representation lisible par l'Homme/returns a human-readable representation
        return f'{self.name} ({self.start_time} - {self.end_time})'

