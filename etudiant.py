'''etudiants = dict()
filieres = dict()

def ajout_filiere():
    print("\nAjout Filière :\n")
    nom = str(input("Entrer le nom de la filière"))
    n_place = int(input(f"Entrer le nombre de place de {nom}"))
    filieres.update({nom: {"nombre_place": n_place, "etudiants": None}})


def ajout_etudiant():
    print("\nEtudiants :")
    nom = str(input("Entrer le nom d'etudiant:\t")) or "Sirri"
    prenom = str(input("Entrer le prenom d'etudiant:\t")) or "Sirri"
    n_modules = int(input("Entrer le nombre de modules:\t"))  or 1

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
        elif choix == 4:
            ajout_filiere()
            print(filieres)
        else :
            print("Au revoir cher(e) utilisateur")
            return

main()'''

# Fichier (info + moyenne + mention + classement)

note_moyenne = []

class Etudiant:#Self pointeur
    def __init__(self):
        self.filename = "files/Etudiants.txt"
        self.nom = ''
        self.prenom = ''
        self.age = 0
        self.cni = ''
        self.filiere = ''
        self.etudiants = dict()
        self.modules = dict()
        self.moyenne = 0
        self.mention = ''
        self.classement = 1

    def ajouter_Etudiant(self):
        self.nom = str(input("Entrer le nom d'etudiant:\t")).upper() or ''
        self.prenom = str(input("Entrer le prenom d'etudiant:\t")).capitalize() or ''
        self.age = int(input("Entrer l'age d'etudiant:\t")) or 0
        self.cni = str(input("Entrer la cni d'etudiant:\t"))
        self.filiere = str(input("Entrer la filière d'etudiant:\t"))

        self.ajouter_modules(int(input("Entrer le nombre de modules d'etudiant:\t")))

        self.etudiants.update({
            self.nom.upper() + " " + self.prenom.capitalize() : {
                "Nom": self.nom.upper(),
                "Prenom": self.prenom.capitalize(),
                "Age": str(self.age),
                "CNI": self.cni,
                "Filiere": self.filiere,
                "Modules": self.modules
            }
        })

        string = ''
        for etudiant, elements in self.etudiants.items():
            string += "-"*26
            string += "\n|" + etudiant + "\n"
            for key in elements:
                if key != "Modules":
                    string += "| -" + key + ":" + elements[key] + "\n"
                else:
                    string += f"| {'Modules':<10} | {'Notes':<10}" + "|\n"
                    string += "-"*26
                    for module in elements[key]:
                        string += f"\n| {module:<10} | {elements[key][module]:<10}" + "|\n"
                        string += "-" * 26

        self.calculer_moyenne_mention()

        string += f"\n| {'Moyenne':<10} | {self.moyenne:<10} |\n"
        string += f"\n| {'Mention':<10} | {self.mention:<10} |\n"
        string += "-" * 26
        string += f"\n| {'Classement':<10} | {self.classement:<10} |\n"

        file = open(self.filename, "a", encoding="utf-8")
        file.write(string)
        file.close()

    def ajouter_modules(self, nombre):
        for i in range(1, nombre+1):
            nom_m = str(input(f"Entrer le nom du {i} module:\t"))
            note_m = float(input(f"Entrer la nom de {nom_m}:\t"))
            self.modules.update({
                nom_m: note_m
            })
        return

    def calculer_moyenne_mention(self):
        c = 0
        for module, note in self.modules.items():
            c+=1
            self.moyenne+= note

        self.moyenne/=c
        note_moyenne.append(self.moyenne)

        print("notemoyenne ", note_moyenne)
        if self.moyenne<10:
            self.mention = "Ajournée"
        elif self.moyenne<12 and self.moyenne>=10:
            self.mention = "Passable"
        elif self.moyenne>=12 and self.moyenne<14:
            self.mention = "A bien"
        elif self.moyenne>14 and self.moyenne<16:
            self.mention = "Bien"
        elif self.moyenne<18 and self.moyenne>=16:
            self.mention = "Tres bien"
        else:
            self.mention = "Excellent"

        self.calculer_classement()
    
    def calculer_classement(self):
        n = sorted(note_moyenne, reverse=True)
        self.classement = n.index(self.moyenne) + 1
        return self.classement
    
    def afficher_Eleves(self):
        print("\n")
        for etudiant, elements in self.etudiants.items():
            print("-"*28)
            print("|", etudiant)
            for key in elements:
                #if key != "Modules":
                print("|", key, ":", elements[key], end="\n")

def main():
    print("Bienvenue dans le logiciel de Management des etudiants")

    choix = -1

    while choix !=0:
        etu = Etudiant()
        choix = int(input("\nVeuillez choisir d'après ces choix\n[1] + Ajout d'un etudiant\n[2] + Affichage des etudiants\n[3] + Affichage de Moyenne Generale\n\n[0] - Quiter\n\n[RESULTAT] "))
        if choix == 1:
            print(choix)
            etu.ajouter_Etudiant()
        elif choix == 2:
            etu.afficher_Eleves()
        elif choix == 3:
            print(note_moyenne)
        else :
            print("Au revoir cher(e) utilisateur")
            
main()