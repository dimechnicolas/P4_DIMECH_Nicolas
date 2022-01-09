from view.TournamentMenueView import tournamentMenue

class TournamentMenue:

    tournament_menue = tournamentMenue

    def tournament_menue(self):
        while 1:
            option = self.tournament_menue.tournamentMenue()
            if option == "1":
                print("voius créez un tour")
            elif option == "2":
                print("vous lancez le tour")
            elif option == "3":
                print("vous entrez les scors")
            else:
                self.tournament_menue.display_error("commande inconnue")