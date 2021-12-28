import re

"""fichier qui controle les entier et les chaines de caractères 
   file that controls integers and strings"""

class Check:

    @staticmethod
    def check_str(text):
        while True:
            reponse = input(text)
            reg_check_text = re.search('[[:alpha:]]', reponse)
            if reg_check_text != 'True':
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
            reg_check_int = re.search('\d', reponse)
            if reponse != "True":
                break
            print("merci de ne rentrer que des chiffres sans virgules")
        return reponse
