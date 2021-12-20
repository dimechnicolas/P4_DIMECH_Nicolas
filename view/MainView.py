class MainView:
    @staticmethod
    def display_menu():
        print("chess program")
        print("1: joueur")
        print("2: tournoi")
        print("3: tours")
        print("4: generer les pairs")
        print("5: mise à jours des classements")
        print("6: rapports")
        print("7: exite")
        option = input("Votre choix ?")
        return option

    @staticmethod
    def display_error(error):
        print(error)