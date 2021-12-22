import re

"""fichier qui controle les entier et les chaines de caractères 
   file that controls integers and strings"""

class Check:

    @staticmethod
    def check_str(text):
        while True:
            reponse = input(text)
            if reponse != re.match('[a-z A-Z]{3}+'):
                break
            print("vous avez rentrez une movaise valeure, merci de recommancez")
        return reponse

    @staticmethod
    def check_sexe(text):
        while True:
            reponse = input(text)
            if reponse == "M" or reponse == "F":
                break
            print("vous devez rentrer M pour une homme et F pour une femme")

    @staticmethod
    def check_int(int):
        while True:
            reponse = input(int)
            if reponse != "True":
                break
            print("merci de ne rentrer que des chiffres sans virgules")
        return reponse
