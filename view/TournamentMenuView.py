class TournamentMenuView:
    @staticmethod
    def view_menu():
        print("1: lancer le tour")
        print("2: terminer le tour")
        print("3: voir les rapports")
        option = input("Votre choix ?")
        return option

    @staticmethod
    def display_error(error):
        print(error)