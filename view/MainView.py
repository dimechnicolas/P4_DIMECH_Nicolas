class MainView:
    @staticmethod
    def display_menu():
        print("chess program")
        print("1: création d'un joueur")
        print("2: création d'un tournoi")
        print("3: création de tours")
        print("4: generer les pairs")
        print("5: mise à jours des classements")
        print("6: éditer les rapports")
        print("7: quitter le programme")
        option = input("Votre choix ?")
        return option

    @staticmethod
    def display_error(error):
        print(error)