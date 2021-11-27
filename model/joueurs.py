class player:

    def __init__(self, nom, prenom, DateNaissance, sexe, classement):
        self.id = 0
        self.nom = nom
        self.prenom = prenom
        self.DateNaissance = DateNaissance
        self.sexe = sexe
        self.classement = classement
        self.matchs = []

    def show(self):
        print("id" + str(self.id))
        print("nom:" + self.nom)
        print("prenom:" + self.prenom)
        print("date de naissance:" + self.DateNaissance)
        print("sexe:" + self.sexe)
        print("classement:" + self.classement)

    #def sauve(self):
        #db.insert({'id':self.id, 'nom': self.nom, 'prenom': self.prenom, 'date de naissance':self.DateNaissance, 'sexe': self.sexe, 'classement': self.classement})

    def serialize(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'date de naissance': self.DateNaissance,
            'sexe': self.sexe,
            'classement': self.classement
        }

    def sauve(self):
        db.insert(self.serialize())
