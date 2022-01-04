"""vie entrée et sortie du menue avec gestion
   menu entry and exit life with management"""

class MainView:
    @staticmethod
    def display_menu():
        print("chess program")
        print("1: création d'un joueur")
        print("2: création d'un tournoi")
        print("3: création de tours")
        print("4: générer les pairs")
        print("5: mise à jours des classements")
        print("6: éditer les rapports")
        print("7: quitter le programme")
        option = input("Votre choix ?")
        return option

    @staticmethod
    def display_error(error):
        print(error)