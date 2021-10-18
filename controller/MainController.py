from view.MainView import MainView

class MainController:

    main_view = MainView

    def start(self):
        while 1:
            option = self.main_view.display_menu()
            if option == "1":
                self.option_1()
            elif option == "2":
                pass
            elif option == "3":
                pass
            elif option == "4":
                break
            else:
                self.main_view.display_error("commande inconnue")

    def option_1(self):
        print("option 1")
        input("nom:")
