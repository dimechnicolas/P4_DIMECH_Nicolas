class Check:

    @staticmethod
    def check_str(text):
        while True:
            reponse = input(text)
            if reponse != "False":
                break
            print("vous avez rentrez une movaise valeure, merci de recommancez")
        return reponse





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