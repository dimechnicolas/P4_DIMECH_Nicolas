from view.TournamentMenuView import tournamentMenuView

class TournamentMenuController:

    tournament_menu = tournamentMenuView

    def Choise_controll(self):
        while 1:
            option = self.tournament_menu.view_menu(), #faire renvoi à TournamentMenuView
            if option == "1":
                print("voius créez un tour")
            elif option == "2":
                print("vous lancez le tour")
            elif option == "3":
                print("vous entrez les scors")
            else:
                self.tournament_menu.display_error("commande inconnue")