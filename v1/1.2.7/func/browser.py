import json
import webbrowser as web


def browser():
    while True:
        print("-" * 14)
        print("Enter a Link or Type 'exit' to quit. To open a presaved Link enter 1.\nTo add a presaved Link enter 2.\nTo delete a presaved Link enter 3.")

        link = input(">>> ")

        if link != "2" and link != "1" and link != "3" and link != "exit":
            web.open(link)

        elif link == "1":
            try:
                with open("browser.json", "r") as file:
                    links = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                print("No presaved links.")
            else:
                num = 1
                for saved_link in links:
                    print(num, saved_link)
                    num += 1

            lopen = input("Link to open >>> ")

            try:
                web.open(links[int(lopen) - 1])
            except Exception as e:
                print(e)

        elif link == "2":
            save_link = input("Link to Save >>> ")

            try:
                with open("browser.json", "r") as file:
                    links = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                links = []

            links.append(save_link)

            with open("browser.json", "w") as file:
                json.dump(links, file, indent=4)

        elif link == "3":
            try:
                with open("browser.json", "r") as file:
                    links = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                print("No presaved links.")
            else:
                num = 1
                for saved_link in links:
                    print(num, saved_link)
                    num += 1

            dele = int(input("Link to delete (enter the number) >>> "))

            if dele > 0 and dele <= len(links):
                del links[dele - 1]
                with open("browser.json", "w") as file:
                    json.dump(links, file, indent=4)
            else:
                print("Invalid input. No link deleted.")

        elif link == "exit":
            return
