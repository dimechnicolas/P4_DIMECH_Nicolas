from view.MainView import MainView
from view.PlayerView import player_information
from model.joueurs import joueurs

class MainController:

    main_view = MainView
    player = player_information

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
        while 1:
            player_information()
            serialized_player_information = {player_information}

    def tournoi(self):
        print("vous créer un tournoi")





