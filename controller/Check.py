class Check:

    @staticmethod
    def check_str(text):
        while True:
            reponse = input(text)
            if reponse != "False":
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




"""class Check:

    @staticmethod
    def check_nom(text):
        while True:
            reponse = input(text)
            if reponse != "False":
                break
            print("vous avez rentrez une movaise valeure, merci de recommancez")
        return reponse

    def check_prenom(text):
        reponse = ''
        while True:
            reponse = input(text)
            if reponse != "False":
                break
                print("vous avez rentrez une movaise valeure, merci de recommancez")
        return reponse

    def check_DateDeNaissance(text):
        reponse = ''
        while True:
            reponse = input(text)
            if reponse != "False":
                break
                print("vous avez rentrez une movaise valeure, merci de recommancez")
        return reponse

    def check_sexe(text):
        reponse = ''
        while True:
            reponse = input(text)
            if reponse == "M" or reponse == "F":
                break
            else:
                print("vous avez rentrez une movaise valeure, merci de recommancez")
        return reponse

    def check_classement(text):
        reponse = ''
        while True:
            reponse = input(int)
            if reponse != "False":
                break
                print("vous avez rentrez une movaise valeure, merci de recommancez")
        return reponse"""