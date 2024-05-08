def notizen_app():
    # Laden der vorhandenen Notizen aus der JSON-Datei
    try:
        with open(r'notizen.json', 'r') as file:
            notizen = json.load(file)
    except FileNotFoundError:
        notizen = []

    while True:
        print("\n--- Notes App ---")
        print("1. Show all Notes")
        print("2. Create new Note")
        print("3. Delete Note")
        print("4. Close app")
        print("Choose an option (1/2/3/4)")

        auswahl = input(">>> ")

        if auswahl == '1':
            # Alle Notizen anzeigen
            print("\n--- All Notes ---")
            for index, notiz in enumerate(notizen, start=1):
                print(f"{index}. {notiz}")
        elif auswahl == '2':
            # Neue Notiz hinzufügen
            print("Enter new Note")
            neue_notiz = input(">>> ")
            notizen.append(neue_notiz)
            print("Added Note!")
        elif auswahl == '3':
            # Notiz löschen
            if not notizen:
                print("No Notes found.")
            else:
                print("\n--- All Notes ---")
                for index, notiz in enumerate(notizen, start=1):
                    print(f"{index}. {notiz}")
                try:
                    index_to_delete = int(input("Enter the number of the Note to delete: "))
                    if 1 <= index_to_delete <= len(notizen):
                        del notizen[index_to_delete - 1]
                        print("Deleted note!")
                    else:
                        print("Invalid Number.")
                except ValueError:
                    print("Invalid Input. Please Enter a valid Number.")
        elif auswahl == '4':
            # App beenden und Notizen in JSON-Datei speichern
            with open(r'notizen.json', 'w') as file:
                json.dump(notizen, file)
            print("Notes Saved. App gets closed.")
            break
        else:
            print("Invalid Input. Please choose 1, 2, 3 or 4.")

