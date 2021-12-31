from datetime import datetime
from model.Player import Player

class Round:
    def __init__(self, name=None):
        self.name = name
        self.start_time = datetime.now().strftime('%d%m%y %H%M%S')#%d day of month on two digits, %m two-digit month number, %y year in twodigits
        self.end_time = ''
        self.matches = []

    def __repr__ (self): # renvoi une représentation lisible par l'interpreteur/returns a representation readable by the interpreter
        return f'{self.name} ({self.start_time} - {self.end_time})'

    def __str__(self): # renvoi une representation lisible par l'Homme/returns a human-readable representation
        return f'{self.name} ({self.start_time} - {self.end_time})'

    def serialize(self):
        return {
        'name': self.name,
        'start_time': self.start_time,
        'end_time': self.end_time
        }

    def deserialize(self, r):
        self.name = r['name']
        self.start_time = r['start_time']
        self.end_time = r['end_time']
        return self

        