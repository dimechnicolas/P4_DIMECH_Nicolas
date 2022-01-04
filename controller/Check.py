import re

"""fichier qui controle les entier et les chaines de caractères 
   file that controls integers and strings"""

class Check:

    @staticmethod
    def check_str(text):
        while True:
            response = input(text)
            match = re.search('^[[:alpha:] -]{3,}$', response)# verification des lettres au minima 3
            if match:
                return response
            print("vous avez rentrez une movaise valeure, merci de recommancez")


    @staticmethod
    def check_sexe(text):
        while True:
            response = input(text)
            if response == "M" or response == "F":
                return response
            print("vous devez rentrer M pour une homme et F pour une femme")


    @staticmethod
    def check_date(text):
        while True:
            response = input(text)
            match = re.search('^[\d]{2}\/[\d]{2}\/[\d]{4}$', response) #verification des dates avec /
            if match:
                return response
            print("merci de ne rentrer que des chiffres sans virgules")

