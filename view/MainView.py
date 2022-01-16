"""vie entrée et sortie du menue avec gestion
   menu entry and exit life with management"""

class MainView:
    @staticmethod
    def display_menu():
        print("chess program")
        print("1: création d'un joueur")
        print("2: création d'un tournoi")
        print("3: charger un tournoi")
        print("4: mise à jours des classements")
        print("5: éditer les rapports")
        print("6: quitter le programme")
        option = input("Votre choix ?")
        return option

    @staticmethod
    def display_error(error):
        print(error)