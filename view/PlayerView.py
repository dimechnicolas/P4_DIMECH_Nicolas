from controller.Check import Check

"""vue pour la récupération des infos d'un jouer
    view for retrieving player info """


class PlayerView:

    @staticmethod
    def get_player_data():
        first_name = Check.check_str('nom:')
        name = Check.check_str('prenom:')
        birthday = Check.check_str('Date De Naissance:')
        sex = Check.check_sexe('sexe:')
        ranking = Check.check_str('classement:')
        return {'first_name': first_name, 'name': name, 'birthday': birthday, 'sex': sex, 'ranking': ranking}

