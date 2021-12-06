from controller.Check import Check

"""vue pour la récupération des infos d'un jouer
    view for retrieving player info """

class player_information:


    @staticmethod
    def way():
        #nom =input("nom:")
        nom = Check.check_str('nom:')
        #prenom = input("prenom:")
        check_prenom = Check.check_str('prenom:')
        # DateDeNaissance = input("date de naissance:")
        check_DateDeNaissance = Check.check_str('Date De Naissance:')
        sexe = input("sexe:")
        check_sexe = Check.check_sexe(sexe)
        classement = input("classement:")
        check_classement = Check.check_classement(classement)
        #print(check_nom, check_prenom, check_DateDeNaissance, check_sexe, check_classement)
        return {'nom': nom, 'prenom': prenom, 'date de naissance': DateDeNaissance, 'sexe': sexe, 'classement': classement}

