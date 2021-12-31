from view.MainView import MainView
from view.PlayerView import PlayerView
from model.Player import Player
from view.TournamentView import tournament_information
from model.tournament import Tournament
from model.Round import Round

"""conrtoleur menue
    Controller menu"""


class MainController:

    main_view = MainView

    def start(self):
        while 1:
            option = self.main_view.display_menu()
            if option == "1":
                self.create_player()
            elif option == "2":
                self.create_tournament()
            elif option == "3":
                self.create_round()
            elif option == "4":
                print("vous générez des pairs")
            elif option == "5":
                print("mise à jours des classements")
            elif option == "6":
                print("vous générez les rapports")
            elif option == "7":
                break
            else:
                self.main_view.display_error("commande inconnue")

    @staticmethod
    def create_player():
        player_data = PlayerView().get_player_data()
        player = Player(player_data['first_name'], player_data['name'], player_data['birthday'], player_data['sex'], player_data['ranking'])
        player.save()

    @staticmethod
    def create_tournament():
        tournament_data = tournament_information().way()
        tournament = Tournament(tournament_data['name'], tournament_data['place'], tournament_data['dated'])
        tournament.save()

    @staticmethod
    def create_round():
        pass
