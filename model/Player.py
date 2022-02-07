from tinydb import TinyDB, Query, where
db = TinyDB('player.json')

class Player:

    def __init__(self, first_name=None, name=None, birthday=None, sex=None, ranking=None):
        self.id = 0
        self.first_name = first_name
        self.name = name
        self.birthday = birthday
        self.sex = sex
        self.ranking = ranking
        self.matchs = []

    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'name': self.name,
            'birthday': self.birthday,
            'sex': self.sex,
            'ranking': self.ranking
        }

    def deserialize (self, p):
        self.id = p['id']
        self.name = p['first_name']
        self.name = p['name']
        self.birthday = p['birthday']
        self.sex = p['sex']
        self.ranking = p['ranking']
        return self

    def save(self):
        db.insert(self.serialize())

    @staticmethod
    def get_all():
        players = []
        for p in db.all():
            players.append(Player().deserialize(p))
        return players

