class tournamentMenuView:
    @staticmethod
    def view_menu():
        print("1: lancer le tour")
        print("2: terminer le tour")
        print("3: voir les rapports")
        print("4: retour au menu principal")
        input("quel est votre choix?")

    @staticmethod
    def display_error(error):
        print(error)