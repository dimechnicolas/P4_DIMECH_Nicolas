from tinydb import TinyDB, Query, where

class Player:

    def __init__(self, first_name=None, name=None, birthday=None, sex=None, ranking=None):
        self.id = -1
        self.first_name = first_name
        self.name = name
        self.birthday = birthday
        self.sex = sex
        self.ranking = ranking
        self.score = 0
        self.matchs = []
        self.table = TinyDB('player.json').table('Player')

    def __str__(self):
        return f'{self.first_name} {self.name}'

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'name': self.name,
            'birthday': self.birthday,
            'sex': self.sex,
            'ranking': self.ranking,
            'score': self.score
        }

    def deserialize (self, p):
        self.id = p['id']
        self.first_name = p['first_name']
        self.name = p['name']
        self.birthday = p['birthday']
        self.sex = p['sex']
        self.ranking = p['ranking']
        self.score = p['score']
        return self

    def save(self):
        self.table.insert(self.serialize())

    def get_all(self):
        players = []
        for p in self.table.all():
            players.append(Player().deserialize(p))
        return players

