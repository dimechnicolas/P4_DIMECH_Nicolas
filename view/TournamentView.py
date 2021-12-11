from controller.Check import Check

"""vue pour la récupération des infos d'un tournoi
    view for retrieving tournament info """

class tournament_information:

    @staticmethod
    def way():
        nom = Check.check_str('nom:')
        lieu = Check.check_str('lieu:')
        date = Check.check_str('Date:')
        joueurs = Check.check_str('joueurs:')
        return {'nom': nom, 'lieu': lieu, 'date': date, 'joueurs': joueurs}

