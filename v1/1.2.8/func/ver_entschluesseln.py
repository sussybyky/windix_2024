def ver_entschluessel():
    table = {"A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V",
             "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q",
             "K": "P", "L": "O", "M": "N", "N": "M", "O": "L",
             "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G",
             "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B", "Z": "A"}
    table2 = {"Z": "A", "Y": "B", "X": "C", "W": "D", "V": "E",
              "U": "F", "T": "G", "S": "H", "R": "I", "Q": "J",
              "P": "K", "O": "L", "N": "M", "M": "N", "L": "O",
              "K": "P", "J": "Q", "I": "R", "H": "S", "G": "T",
              "F": "U", "E": "V", "D": "W", "C": "X", "B": "Y", "A": "Z"}
    print("d...decipher")
    print("e...encrypt")
    print()
    auswahl = input(">>> ")
    print("-" * 14)
    if auswahl == "d":
        nachricht = input("Crypted message: ")
        print()
        neu_nachricht = nachricht.upper()
        print("Encrypted message: ")
        for zeichen in neu_nachricht:
            entziefert = ""
            if zeichen.isalpha():
                entziefert += table[zeichen]
                print(entziefert, end="")

            else:
                entziefert += zeichen
                print(entziefert, end="")
        print("-" * 14, end="\n")
        return

    elif auswahl == "e":
        nachricht = input("Encrypted message: ")
        print()
        neu_nachricht = nachricht.upper()
        print("Crypted message: ")
        for zeichen in neu_nachricht:
            verziefert = ""
            if zeichen.isalpha():
                verziefert += table2[zeichen]
                print(verziefert, end="")

            else:
                verziefert += zeichen
                print(verziefert, end="")
        print("-" * 14, end="\n")
        return