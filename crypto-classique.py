# Chiffrage/Déchiffrage (Methode de Jules César)
import string

alphabets = string.ascii_uppercase


def chiffrement_par_cle(k):
    msg = str(input("Entrer une phrase a chiffré:\t"))
    msg_chiffré = ""
    for char in msg.upper():
        if char in alphabets:
            msg_chiffré += alphabets[(alphabets.index(char) + k) % len(alphabets)]
        else:
            msg_déchiffré += char

    print("\n[+] Message chiffré:\t", msg_chiffré, end="\n")

def déchiffrement_par_cle(k):
    msg_chiffré = str(input("Entrer une phrase a dechiffré:\t"))
    msg_déchiffré = ""
    for char in msg_chiffré.upper():
        if char in alphabets:
            msg_déchiffré += alphabets[(alphabets.index(char) - k) % len(alphabets)]
        else:
            msg_déchiffré += char

    print("[+] Message déchiffré:\t", msg_déchiffré)

ongoing = True
while ongoing:
    choix = int(input("Voulez vous :\n[1] Chiffrer\n[2] Dechiffrer\n\n[0] Quitter: \t"))

    if choix == 0:
        print("Bye")
        ongoing = False
        break
        
    if choix == 1:
        decalage = int(input("\n- Decalage :\t"))
        chiffrement_par_cle(decalage)
    elif choix == 2:
        decalage = int(input("\n- Decalage :\t"))
        déchiffrement_par_cle(decalage)

'''msg = str(input("Entrer une phrase a chiffré:\t"))

msg_chiffré = chiffrement_par_cle(msg, k)
print("\n[+] Message chiffré:\t", msg_chiffré, end="\n")

msg_déchiffré = déchiffrement_par_cle(msg_chiffré, k)
print("[+] Message déchiffré:\t", msg_déchiffré)'''