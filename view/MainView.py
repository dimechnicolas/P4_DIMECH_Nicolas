class MainView:
    @staticmethod
    def display_menu():
        print("chess program")
        print("1: joueur")
        print("2: tournoi")
        print("3: option 3")
        print("4: exit")
        option = input("Votre choix ?")
        return option

    @staticmethod
    def display_error(error):
        print(error)