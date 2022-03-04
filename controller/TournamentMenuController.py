from view.TournamentMenuView import TournamentMenuView
import controller.MainController
from model.Round import Round


class TournamentMenuController:
    def __init__(self, tournament):
        self.tournament = tournament

    def menu(self):
        while 1:
            option = TournamentMenuView().view_menu() #renvoi à TournamentMenuView
            if option == "1":
                self.start_round()
            elif option == "2":
                self.stop_round()
            elif option == "3":
                print("vous entrez les scors")
            else:
                TournamentMenuView().display_error("commande inconnue")

    def start_round(self):
        new_round = Round()
        self.tournament.rounds_list.append(new_round)

    def stop_round(self):
        pass # roud à tirer dans la liste Tournament