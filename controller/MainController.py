from view.MainView import MainView
from view.PlayerView import player_information
from model.player import Player
from view.TournamentView import tournament_information
from model.tournament import Tournament


class MainController:

    main_view = MainView

    def start(self):
        while 1:
            option = self.main_view.display_menu()
            if option == "1":
                self.joueurs()
            elif option == "2":
                self.tournoi()
            elif option == "3":
                pass
            elif option == "4":
                break
            else:
                self.main_view.display_error("commande inconnue")

    def joueurs(self):
        player_data = player_information().way()
        player = Player(player_data['first_name'], player_data['name'], player_data['birthday'], player_data['sex'], player_data['ranking'])
        player.sauve()

    def tournoi(self):
        tournament_data = tournament_information().way()
        tournament = Tournament(tournament_data['name'], tournament_data['place'], tournament_data['dated'])
        tournament.save()