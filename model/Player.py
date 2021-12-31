from tinydb import TinyDB, Query, where
db = TinyDB('player.json')

class Player:

    def __init__(self, first_name, name, birthday, sex, ranking):
        self.id = 0
        self.first_name = first_name
        self.name = name
        self.birthday = birthday
        self.sex = sex
        self.ranking = ranking
        self.matchs = []

    def show(self):
        print("id" + str(self.id))
        print("first_name:" + self.first_name)
        print("name:" + self.name)
        print("birthday:" + self.birthday)
        print("sex:" + self.sex)
        print("ranking:" + self.ranking)

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

    def save(self):
        db.insert(self.serialize())
