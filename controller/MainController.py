from view.MainView import MainView
from view.PlayerView import player_information
from model.joueurs import player
from tinydb import TinyDB, Query, where

db = TinyDB('db.json')


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
        while 1:
            player_information().way()




    def tournoi(self):
        print("vous créer un tournoi")