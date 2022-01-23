from view.TournamentMenuView import tournamentMenuView
from model.Tour import Tour

class TournamentMenuController:

    tournament_menu = tournamentMenuView

    def Choise_controll(self):
        while 1:
            option = self.tournament_menu.view_menu() #renvoi à TournamentMenuView
            if option == "1":
                self.star_trick()
            elif option == "2":
                self.stop_ride()
            elif option == "3":
                print("vous entrez les scors")
            else:
                self.tournament_menu.display_error("commande inconnue")

    @staticmethod
    def star_trick():
        Tour.start_timer()

    @staticmethod
    def stop_ride():
        Tour.end_timer()
        Tour.timme_elapsed()