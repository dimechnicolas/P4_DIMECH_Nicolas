from view.TournamentMenuView import tournamentMenu

class TournamentMenu:

    tournament_menu = tournamentMenu

    def tournament_menu(self):
        while 1:
            option = self.tournament_menu.tournamentMenu()
            if option == "1":
                print("voius créez un tour")
            elif option == "2":
                print("vous lancez le tour")
            elif option == "3":
                print("vous entrez les scors")
            else:
                self.tournament_menu.display_error("commande inconnue")