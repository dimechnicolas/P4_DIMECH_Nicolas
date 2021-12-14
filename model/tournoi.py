from tinydb import TinyDB, Query, where
db = TinyDB('tournoi.json')


class Tournoi:
    def __init__(self, name, place, dated):
        self.name = name # nom du tournoi
        self.place = place # lieu du tournoi
        self.dated = dated # date du tournoi
        self.round = 4 # le nombre de tours par défaut est de 4
        self.tours = [] # La liste des instances rondes.
        self.player = [] # joueurs

    def show(self):
        print("name:" + self.name)
        print("place:" + self.place)
        print("dated:" + self.dated)

    def serialize(self):
        return {
            'name': self.name,
            'place': self.place,
            'dated ': self.dated,
            'round': self.round,
            'player': self.player
        }

    def save(self): # fonction de sauvegarde
        db.insert(self.serialize()) # sauvegarde dans la db