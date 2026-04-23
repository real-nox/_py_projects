etudiants = dict()

def ajout_etudiant():
    print("\nEtudiants :")
    nom = str(input("Entrer le nom d'etudiant:\t"))
    prenom = str(input("Entrer le prenom d'etudiant:\t"))
    n_modules = int(input("Entrer le nombre de modules:\t"))

    #Modules
    modules_e = dict()
    print("\nModules :")
    for i in range(0,n_modules):
        nom_m = str(input(f"Entrer le nom du module {i+1}:\t"))
        note = float(input(f"Note d'etudiant dans {nom_m}:\t"))
        modules_e.update({nom_m : note})

    n_complete = nom + " " + prenom
    etudiants.update({n_complete : {"Nom" : nom, "Prenom": prenom, "Modules": modules_e}})

def affichage_etudiant():
    nom_complet = str(input("Entrer le nom complet d'etudiant:\t"))
    print("\n")
    for etudiant, elements in etudiants.items():
        print("-"*28)
        print("|", etudiant)
        for key in elements:
            if key != "Modules":
                print("|", key, ":", elements[key], end="\n")
            else:
                affichage_mod(nom_complet)

def affichage_mod(nom_complet):
    print("-"*28)
    print(f"| {'Modules':<10} | {'Notes':<10}", end="  |\n")
    print("-"*28)
    for module in etudiants[nom_complet]["Modules"]:
        print(f"| {module:<10} | {etudiants[nom_complet]["Modules"][module]:<10}", end="  |\n")
    print("-" * 28)

def moyenne_note():
    nom_complet = str(input("Entrer le nom complet d'etudiant:\t"))
    m = 0
    c = 0
    for module in etudiants[nom_complet]["Modules"]:
        m += float(etudiants[nom_complet]["Modules"][module])
        c = c + 1

    affichage_mod(nom_complet)
    print(f"| {'Moyenne G':<10} | {(m/c):<10.2f}", end="  |\n")

    rep = ""
    if m<10:
        rep = "Ajournée"
    elif m<12 and m>=10:
        rep = "Passable"
    elif m>=12 and m<14:
        rep = "A bien"
    elif m>14 and m<16:
        rep = "Bien"
    elif m<18 and m>=16:
        rep = "Tres bien"
    else:
        rep = "Excellent"

    print(f"| {' ':<10} | {rep:<10}", end="  |\n")
    print("-"*28)

def main():
    print("Bienvenue dans le logiciel de Management des etudiants")

    choix = -1

    while choix !=0:
        choix = int(input("\nVeuillez choisir d'après ces choix\n[1] + Ajout d'un etudiant\n[2] + Affichage d'etudiant\n[3] + Moyenne Generale\n\n[0] - Quiter\n\n[RESULTAT] "))

        if choix == 1:
            print(choix)
            ajout_etudiant()
        elif choix == 2:
            affichage_etudiant()
        elif choix == 3:
            moyenne_note()
        else:
            print("Au revoir cher(e) utilisateur")
            return

main()