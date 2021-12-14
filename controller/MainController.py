from view.MainView import MainView
from view.PlayerView import player_information
from model.joueurs import Player
from view.TournamentView import tournament_information
from model.tournoi import Tournoi


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
        player = Player(player_data['nom'], player_data['prenom'], player_data['date de naissance'], player_data['sexe'], player_data['classement'])
        player.sauve()

    def tournoi(self):
        tournoi_data = tournament_information().way()
        tournament = Tournoi(tournoi_data['name'], tournoi_data['place'], tournoi_data['dated'])
        tournament.save()