from view.TournamentMenuView import TournamentMenuView
import controller.MainController
from model.Round import Round



class TournamentMenuController:
    def __init__(self, tournament):
        self.tournament = tournament

    def menu(self):
        while 1:
            option = TournamentMenuView().view_menu() #renvoi à TournamentMenuView
            if option == "1":
                self.start_round()
            elif option == "2":
                self.stop_round()
            elif option == "3":
                print("vous entrez les scors")
            else:
                TournamentMenuView().display_error("commande inconnue")


    def start_round(self):

        if len(self.tournament.rounds_list) != 0 and self.tournament.rounds_list[-1].end_time == None:# l'accesseur avec une valeure négative permet de compter en remontant à partir de la fin de la liste
            print('attention: un Round est en cours')
        elif len(self.tournament.rounds_list) == 4 and self.tournament.rounds_list[-1].end_time != None: # tournament == 4 : tournoi terminé, si <4 tournoi non fini!
            print("le tournoi est terminé")
        else:
            new_round = Round()  # instance de la class Round
            #condition verifiant si Tournament.round_list est vide ou à déja un tours.
            if not self.tournament.rounds_list:
                new_round.first_pairing(self.tournament.player)
            else:
                new_round.other_pairing(self.tournament.player, self.tournament.rounds_list)
            self.tournament.rounds_list.append(new_round)
            self.tournament.update()

    def stop_round(self):
        if len(self.tournament.rounds_list) == 0 or self.tournament.rounds_list[-1].end_time != None :
            print("attention aucun round n'est en cours")
        elif len(self.tournament.rounds_list) == 4 and self.tournament.rounds_list[-1].end_time != None : # tournament == 4 : tournoi terminé, si <4 tournoi non fini!
            print("le tournoi est terminé")
        else:
            pass # stopper le round et afficher les round 1 à 1 pour rentrer les scores

