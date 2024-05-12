import json
import os


def calendar():
    path = r"calendar.json"
    print("Add Event(ae) or read Event(re) or show all Events(sa) or exit(exit)?")
    typ = input(">>> ")

    try:
        with open(path, "r") as file:
            load_data = json.load(file)
    except IOError as e:
        with open(path, "w") as file:
            json.dump("", file, indent=4)

    if typ.lower() == "ae":
        date = input("Date >>> ")
        cont = input("Content >>> ")

        file_dat = {
            "date": date,
            "content": cont
        }

        with open(path, "r") as file:
            try:
                events = json.load(file)
            except json.decoder.JSONDecodeError:
                events = []

        events.append(file_dat)

        with open(path, "w") as file:
            json.dump(events, file, indent=4)

        calendar()

    elif typ.lower() == "re":

        print("What date?")
        datum = input(">>> ")

        with open(path, "r") as file:
            events = json.load(file)

        found_event = None
        for event in events:
            if datum == event["date"]:
                found_event = event
                break

        if found_event:
            print("Date: " + found_event["date"], "\n" + "Content: " + found_event["content"])
        else:
            print("Date not found!")

        calendar()

    elif typ.lower() == "sa":
        with open(path, "r") as file:
            try:
                events = json.load(file)
            except json.decoder.JSONDecodeError:
                events = []

        print()
        for event in events:
            time = event["date"]
            cont = event["content"]

            print("Time:", time, "\nContent:", cont)
            print("-" * 14)

    elif typ == "exit":
        return

    else:
        print("Invalid Syntax! Try again!")
        calendar()