from view.MainView import MainView
from view.PlayerView import PlayerView
from model.Player import Player
from view.TournamentView import TournamentView
from model.Tournament import Tournament
from controller.TournamentMenuController import TournamentMenuController  

"""conrtoleur menue
    Controller menu"""


class MainController:

    main_view = MainView

    def start(self):
        while True:
            option = self.main_view.display_menu()
            if option == "1":
                self.create_player()
            elif option == "2":
                self.create_tournament()
            elif option == "3":
                self.load_tournament()
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
        tournament_data = TournamentView().get_tournament_data()
        tournament = Tournament(tournament_data['name'], tournament_data['place'], tournament_data['dated'], tournament_data['description'], tournament_data['type_tournament'])
        Player.get_all() # ajout des joueurs, afficher la liste des jouteurs et en selectionner 8
        tournament.save()
        TournamentMenuController(tournament).menu()

    @staticmethod
    def load_tournament(tournaments):
        TournamentView.tournament_select(tournaments)
        Tournament.get_all()#afficher la liste des tournoi et en selectionner 1
        TournamentMenuController().Choise_controll()
