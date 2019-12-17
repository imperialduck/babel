#  Premier traitement
def validate_display(fullname):
    """
    Validation et affichage du nom complet
    """
    l = len(fullname)
    names = fullname.split(" ")

    if l == 2:
        print("Prénom : {}, Nom : {}".format(names[0], names[1]))
    elif l == 3:
        print("Prénom : {}, Particule : {}, Nom : {}".format(names[0], names[1], names[2]))
    elif l == 1:
        print("Nom seul : {}".format(names[0]))
    else:
        print("Format : Prénom, particule, nom")
        print("Que faire de : " + " ".join(names[3:]))


in_fullname = input("Entrez votre nom et votre prénom\n")
validate_display(in_fullname)
