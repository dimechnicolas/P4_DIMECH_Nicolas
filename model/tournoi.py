from tinydb import TinyDB, Query, where
db = TinyDB('tournoi.json')


class Tournoi:
    def __init__(self, nom, lieu, date, tournees, joueurs):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.tours = 4 # le nombre de tours par défaut est de 4
        self.tournees = tournees
        self.joueurs = joueurs

    def show(self):
        print("nom:" + self.nom)
        print("lieu:" + self.lieu)
        print("date:" + self.date)
        print("tours:" + self.tours)
        print("joueurs:" + self.joueurs)

    def serialize(self):
        return {
            'nom': self.nom,
            'lieu': self.lieu,
            'date ': self.date,
            'tours': self.tours,
            'joueurs': self.joueurs
        }

    def sauve(self):
        db.insert(self.serialize())
