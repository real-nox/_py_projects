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
        nom_m = str(input(f"Entrer le nom du module {i+1} \t"))
        note = float(input(f"Note d'etudiant dans {nom_m} \t"))
        modules_e.update({nom_m : note})

    n_complete = nom + " " + prenom
    etudiants.update({n_complete : {"Nom" : nom, "Prenom": prenom, "Modules": modules_e}})

    affichage_etudiants()

def affichage_etudiants():
    print("\n")
    for etudiant, elements in etudiants.items():
        print(etudiant)
        for key in elements:
            if key != "Modules":
                print(key, ":", elements[key])
            else:
                print("-"*28)
                print(f"| {'Modules':<10} | {'Notes':<10}", end="  |\n")
                print("-"*28)
                for module in elements[key]:
                    print(f"| {module:<10} | {elements[key][module]:<10}", end="  |\n")
                print("-" * 28)
ajout_etudiant()