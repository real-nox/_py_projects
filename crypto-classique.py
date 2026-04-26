# Chiffrage/Déchiffrage (Methode de Jules César)

alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
k = 3 #Decalage

def chiffrement_par_cle(msg, cle):
    msg_chiffré = ""
    for char in msg.upper():
        if char != " ":
            msg_chiffré += alphabets[(alphabets.index(char) + k) % len(alphabets)]
        else:
            msg_chiffré += " "

    return msg_chiffré

def déchiffrement_par_cle(msg_chiffré, cle):
    msg_déchiffré = ""
    for char in msg_chiffré.upper():
        if char != " ":
            msg_déchiffré += alphabets[(alphabets.index(char) - k) % len(alphabets)]
        else:
            msg_déchiffré += " "

    return msg_déchiffré

msg = str(input("Entrer une phrase a chiffré:\t"))

msg_chiffré = chiffrement_par_cle(msg, k)
print("\n[+] Message chiffré:\t", msg_chiffré, end="\n")

msg_déchiffré = déchiffrement_par_cle(msg_chiffré, k)
print("[+] Message déchiffré:\t", msg_déchiffré)