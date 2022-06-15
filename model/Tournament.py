from tinydb import TinyDB, Query, where

from model.Player import Player
from model.Round import Round

db = TinyDB('tournoi.json')


class Tournament:
    def __init__(self, name=None, place=None, dated=None, description=None, type_tournament=None):
        self.id = -1
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
        players = []
        for p in self.player:
            players.append(p.serialize())
        rounds_list = []
        for r in self.rounds_list:
            rounds_list.append(r.serialize())

        return {
            'id': self.id,
            'name': self.name,
            'place': self.place,
            'dated': self.dated,
            'rounds': self.rounds,
            'rounds_list': rounds_list,
            'player': players,
            'description': self.description,
            'type_tournament': self.type_tournament
        }

    def deserialize(self, t):
        players = []
        for p in t['player']:
            players.append(Player().deserialize(p))
        rounds_list = []
        for r in t['rounds_list']:
            rounds_list.append(Round().deserialize(r))
        self.id = t['id']
        self.name = t['name']
        self.place = t['place']
        self.dated = t['dated']
        self.rounds = t['rounds']
        self.rounds_list = rounds_list
        self.player = players
        self.description = t['description']
        self.type_tournament = t['type_tournament']
        return self


    def save(self): # fonction de sauvegarde
        self.id = db.insert(self.serialize()) # sauvegarde dans la db
        self.update()

    def update(self):
        db.update(self.serialize(), doc_ids=[self.id])

    @staticmethod
    def get_all():
        tournament = []
        for t in db.all():
            tournament.append(Tournament().deserialize(t))
        return tournament