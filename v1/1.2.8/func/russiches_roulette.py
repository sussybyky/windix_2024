import random
import time


def russian_roulette():
    print("Welcome to the Russian roulette!")
    print("...")
    print("Choose how many bullets to load.")
    print("The Possible count is 1-3, but be aware, the gun is getting shot three times.")
    print("You have a Pisol with 6 Ammunition slots. The bullets get loadet in ramdom slots.")
    wiederhole = True
    while wiederhole:
        try:
            bull = input("Amount of bullets: ")
            bull = int(bull)
        except ValueError:
            print(f"No number: {bull}")
        else:
            if bull in range(1, 4):
                wiederhole = False
    print("...")
    print("You load the Pisol...")
    time.sleep(1)
    print("and you put it on your sleeve and pull the trigger...")
    time.sleep(3)

    # Kugel werden hier "geladen"
    chambers = [0] * 6
    if bull == 1:
        chambers[random.randint(1, 5)] = 1
    elif bull == 2:
        chambers[random.randint(0, 5)] = 1
        chambers[random.randint(0, 5)] = 1
    else:
        chambers[random.randint(0, 5)] = 1
        chambers[random.randint(0, 5)] = 1
        chambers[random.randint(0, 5)] = 1

    for i in range(1, 4):
        print("...")
        print(f"Shot {i}...")
        time.sleep(2)

        if chambers[i] == 1:
            print("The pistol Shot! You died!")
            return

        else:
            print("The slot is emtpy. You lived!")

    print("...")
    print("You did all your shots and survived! Lucky you!")
