class Farben:
    ROT = '\033[91m'
    GRUEN = '\033[92m'
    GELB = '\033[93m'
    BLAU = '\033[94m'
    LILA = '\033[95m'
    ENDE = '\033[0m'


def colortx():
    print("What color do you want?(red, green, yellow, blue, purple, gray)")
    auswahl = input(">>> ")

    if auswahl.lower() == "red":
        print(Farben.ROT + 'Red')
    elif auswahl.lower() == "green":
        print(Farben.GRUEN + 'Green')
    elif auswahl.lower() == "yellow":
        print(Farben.GELB + 'Yellow')
    elif auswahl.lower() == "blue":
        print(Farben.BLAU + 'Blue')
    elif auswahl.lower() == "purple":
        print(Farben.LILA + 'Purple')
    elif auswahl.lower() == "gray":
        print(Farben.ENDE + "Gray")
    else:
        print("Ungültige Farbauswahl.")