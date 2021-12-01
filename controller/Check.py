class Check:
    def check_nom(text):
        reponse = ''
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

    def check_sexe(sexe):
        reponse = ''
        while True:
            reponse = input(sexe)
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
        return reponse