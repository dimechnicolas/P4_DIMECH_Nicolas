class MainView:
    @staticmethod
    def display_menu():
        print("chess program")
        print("1: option 1")
        print("2: option 2")
        print("3: option 3")
        print("4: exit")
        option = input("Votre choix ?")
        return option

    @staticmethod
    def display_error(error):
        print(error)