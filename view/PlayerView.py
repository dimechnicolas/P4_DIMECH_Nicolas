def player_information():
    nom = input("nom")
    prenom = input("prénom")
    DateNaissance = input("date de naissance")
    sexe = input("sexe")
    classement = input("classement")

    player = nom, prenom, DateNaissance,sexe, classement
    #serialized = {'nom': player.nom, 'prenom': player.prenom, 'date de naissance': player.DateNaissance, 'sexe': player.sexe, 'classement': player.classement}
    print(player)

