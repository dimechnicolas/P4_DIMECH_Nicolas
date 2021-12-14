from controller.Check import Check

"""vue pour la récupération des infos d'un tournoi
    view for retrieving tournament info """

class tournament_information:

    @staticmethod
    def way():
        name = Check.check_str('nom:') #récup et controle le nom
        place = Check.check_str('lieu:') # récup et controle le lieu
        dated = Check.check_str('Date:') # récup et controle la date
        return {'name': name, 'place': place, 'dated': dated} # retourne un dico avec les dif info entrée