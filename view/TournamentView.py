from controller.Check import Check

"""vue pour la récupération des infos d'un tournoi
    view for retrieving tournament info """


class TournamentView:
    check = Check

    @staticmethod
    def get_tournament_data():
        name = Check.check_str('nom:') #récup et controle le nom
        place = Check.check_str('lieu:') # récup et controle le lieu
        dated = Check.check_date('Date:') # récup et controle la date
        description = Check.check_str('description')
        type_tournament = Check.check_str('type de tournoi')
        return {'name': name, 'place': place, 'dated': dated, 'description': description, 'type_tournament': type_tournament } # retourne un dico avec les dif info entrée

    def players_select(self, players):
        selected_players = []
        for kay, players in enumerate(players):
            print(f'{kay}:{players}')
        user_input = self.check.check_str("choix du joueur:", range(0, len(players)))
        selected_players.append(players[user_input])
        players.remove(players[user_input])

        if len(selected_players) == 8:
            break