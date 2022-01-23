from view.TournamentMenuView import tournamentMenuView
from model.Tournament import Tournament

class TournamentMenuController:

    tournament_menu = tournamentMenuView

    def Choise_controll(self):
        while 1:
            option = self.tournament_menu.view_menu(), #renvoi à TournamentMenuView
            if option == "1":
                print("lancez le tour")
            elif option == "2":
                print("terminer le tour")
            elif option == "3":
                print("vous entrez les scors")
            else:
                self.tournament_menu.display_error("commande inconnue")