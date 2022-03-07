from tinydb import TinyDB, Query, where
db = TinyDB('tournoi.json')


class Tournament:
    def __init__(self, name=None, place=None, dated=None, description=None, type_tournament=None):
        self.name = name # nom du tournoi
        self.place = place # lieu du tournoi
        self.dated = dated # date du tournoi
        self.description = description
        self.type_tournament = type_tournament
        self.rounds = 4 # le nombre de tours par défaut est de 4
        self.rounds_list = [] # La liste des instances rondes, ajouter en séria et déséria
        self.player = [] # joueurs

    def __str__(self): # affiche la classe en string.
        return f"{self.name}"

    def serialize(self):
        return {
            'name': self.name,
            'place': self.place,
            'dated': self.dated,
            'rounds': self.rounds,
            'player': self.player,
            'description': self.description,
            'type_tournament': self.type_tournament
        }

    def deserialize(self, t):
        self.name = t['name']
        self.place = t['place']
        self.dated = t['dated']
        self.rounds = t['rounds']
        self.player = t['player']
        self.description= t['description']
        self.type_tournament = t['type_tournament']
        return self


    def save(self): # fonction de sauvegarde
        db.insert(self.serialize()) # sauvegarde dans la db

    @staticmethod
    def get_all():
        tournament = []
        for t in db.all():
            tournament.append(Tournament().deserialize(t))
        return tournament