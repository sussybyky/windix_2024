
import json
from math import e
from os import access
import turtle
import tkinter as tk
import random
from typing import Any
import webbrowser as web

filename = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\log_in_data.json"
adfilename = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\log_in_admin.json"

class Farben:
    ROT = '\033[91m'
    GRUEN = '\033[92m'
    GELB = '\033[93m'
    BLAU = '\033[94m'
    LILA = '\033[95m'
    ENDE = '\033[0m'


def innerPy():
    """
    Main function to handle user registration, login, and menu navigation.
    """
    global filename
    global rep
    global adfilename
    
    rep = True
    
    while rep:
        reg_or_log = input("Register or Login: ")
        print("-" * 14)
        
        with open(filename, "r") as file:
            data = json.load(file)
            user1 = data.get("user1", {})
            
            if reg_or_log.lower() == "r":
                print("Registering...")
                print()
                regis()
            elif reg_or_log.lower() == "l":
                print("Log In...")
                print()
                login()
            else:
                print("Wrong input!\nPlease Enter 'r'(Register) or 'l'(Login)!")
                continue
            
def regis():
    """
    Function to handle user registration.
    """
    us = input("Username: ")
    pas = input("Password: ")
    
    data_user1 = {
        "user1": {
            "username": us,
            "password": pas
        }
    }
    data_admin =  { 
        "admin": {
            "username": "Admin",
            "password": "adpass9!"
        },

        "file_dat": {
            "version": "1.2.1",
            "copyright": "\u00a9Daniel Naderer/Levente Racz 2024",
            "rights": "Legally supported by \u00a9Windix 2024",
            "information": "This is a copy of the original file made by the Owner \u00a9Daniel Naderer/Levente Racz! Do not ignore the copyright!"
        }
    }
    

    with open(filename, "r") as file:
        datas = json.load(file)


    with open(adfilename, "r") as file:
        datadm = json.load(file)


    datas.update(data_user1)
    datadm.update(data_admin)


    with open(filename, 'w') as datei:
        json.dump(datas, datei, indent=4)


    with open(adfilename, 'w') as datei:
        json.dump(datadm, datei, indent=4)

def login():
    """
    Function to handle user login.
    """
    global data_user1_login
    global data_admin
    global pas_log
    global us_log
    global rep
    
    us_log = input("Username: ")
    pas_log = input("Password: ")    
    
    with open(filename, "r") as file:
        datas = json.load(file)
    
    with open(adfilename, 'r') as file:
        datadm = json.load(file)
        
    data_user1_login = datas.get("user1", {})
    admin_login = datadm.get("admin", {})
    
    if data_user1_login.get("password") == pas_log and data_user1_login.get("username") == us_log:
        logged_in()
        rep = False
        
    elif admin_login.get("password") == pas_log and admin_login.get("username") == us_log:
        programmer_logged_in()
        rep = False
        
    else:
        print("-" * 14)
        print("Invalid username or password.")
        print("-" * 14)
        login()
        
def draw_line(size, facing, color):
    turtle.penup()
    turtle.color(color)
    turtle.goto(0, 0)
    turtle.pendown()

    if facing == "up":
        turtle.goto(0, size)
    elif facing == "down":
        turtle.goto(0, -size)
    elif facing == "right":
        turtle.goto(size, 0)
    elif facing == "left":
        turtle.goto(-size, 0)
    else:
        print("Wrong input! Try again.")
        return
    
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


def draw_circle(size, posx, posy):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.circle(size)

    return
    # turtle.done()

def on_drag(x, y):
    turtle.speed(100)
    turtle.ondrag(None)
    turtle.goto(x, y)
    turtle.ondrag(on_drag)
    return

def ver_entschluessel():
    table={"A" : "Z", "B" : "Y", "C" : "X", "D" : "W", "E" : "V",	
            "F" : "U", "G" : "T", "H": "S", "I" : "R", "J" : "Q",	
            "K" : "P", "L" : "O", "M" : "N", "N" : "M", "O" : "L",
            "P" : "K", "Q" : "J", "R" : "I", "S" : "H", "T" : "G",
            "U" : "F", "V" : "E", "W" : "D", "X" : "C", "Y" : "B", "Z" : "A"}
    table2={"Z" : "A", "Y" : "B", "X" : "C", "W" : "D", "V" : "E",	
            "U" : "F", "T" : "G", "S": "H", "R" : "I", "Q" : "J",	
            "P" : "K", "O" : "L", "N" : "M", "M" : "N", "L" : "O",
            "K" : "P", "J" : "Q", "I" : "R", "H" : "S", "G" : "T",
            "F" : "U", "E" : "V", "D" : "W", "C" : "X", "B" : "Y", "A" : "Z"}
    print("d...decipher")
    print("e...encrypt")
    print()
    auswahl = input(">>> ")
    print("-"*14)
    if auswahl == "d":
        nachricht=input("Crypted message: ")
        print()
        neu_nachricht=nachricht.upper()
        print("Encrypted message: ")
        for zeichen in neu_nachricht:
            entziefert = ""
            if zeichen.isalpha():									
                entziefert += table[zeichen]	
                print(entziefert, end="")
                
            else:
                entziefert += zeichen		
                print(entziefert, end="")
        print("-"*14, end="\n")
        return
    
    elif auswahl == "e":
        nachricht=input("Encrypted message: ")
        print()
        neu_nachricht=nachricht.upper()
        print("Crypted message: ")
        for zeichen in neu_nachricht:
            verziefert = ""
            if zeichen.isalpha():	
                verziefert += table2[zeichen]
                print(verziefert, end="")
                
            else:
                verziefert += zeichen		
                print(verziefert, end="")
        print("-"*14, end="\n")
        return
    
def calendar():
    path = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\calendar.json"
    print("Add Event(ae) or read Event(re) or show all Events(sa) or exit(exit)?")
    typ = input(">>> ")

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
            print("-"*14)

    elif typ == "exit":
        return

    else:
        print("Invalid Syntax! Try again!")
        calendar()

def ping_pong():
    def start_game():
        global ball_speed_x, ball_speed_y, paddle_speed, left_score, right_score

        ball_speed_x = 4 * random.choice((1, -1))
        ball_speed_y = 4 * random.choice((1, -1))
        paddle_speed = 0
        left_score = 0
        right_score = 0

        canvas.delete("all")
        draw_game()

        root.after(1000, move_ball)

    def draw_game():
        canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="black")

        canvas.create_line(WIDTH // 2, 0, WIDTH // 2, HEIGHT, fill="white", dash=(15, 5))

        canvas.create_rectangle(left_paddle["x"] - PADDLE_WIDTH // 2, left_paddle["y"] - PADDLE_HEIGHT // 2,
                                left_paddle["x"] + PADDLE_WIDTH // 2, left_paddle["y"] + PADDLE_HEIGHT // 2, fill="white")

        canvas.create_rectangle(right_paddle["x"] - PADDLE_WIDTH // 2, right_paddle["y"] - PADDLE_HEIGHT // 2,
                                right_paddle["x"] + PADDLE_WIDTH // 2, right_paddle["y"] + PADDLE_HEIGHT // 2, fill="white")

        canvas.create_oval(ball["x"] - BALL_SIZE // 2, ball["y"] - BALL_SIZE // 2,
                            ball["x"] + BALL_SIZE // 2, ball["y"] + BALL_SIZE // 2, fill="white")

        canvas.create_text(WIDTH // 4, 50, text=str(left_score), font=("Helvetica", 36), fill="white")
        canvas.create_text(3 * WIDTH // 4, 50, text=str(right_score), font=("Helvetica", 36), fill="white")

    def move_ball():
        global ball_speed_x, ball_speed_y, left_score, right_score

        ball["x"] += ball_speed_x
        ball["y"] += ball_speed_y

        # Kollision mit den Paddles
        if (ball["x"] - BALL_SIZE // 2 < left_paddle["x"] + PADDLE_WIDTH // 2 and
                ball["y"] - BALL_SIZE // 2 < left_paddle["y"] + PADDLE_HEIGHT // 2 and
                ball["y"] + BALL_SIZE // 2 > left_paddle["y"] - PADDLE_HEIGHT // 2):
            ball_speed_x *= -1

        if (ball["x"] + BALL_SIZE // 2 > right_paddle["x"] - PADDLE_WIDTH // 2 and
                ball["y"] - BALL_SIZE // 2 < right_paddle["y"] + PADDLE_HEIGHT // 2 and
                ball["y"] + BALL_SIZE // 2 > right_paddle["y"] - PADDLE_HEIGHT // 2):
            ball_speed_x *= -1

        # Kollision mit den Wxnden
        if ball["y"] - BALL_SIZE // 2 < 0 or ball["y"] + BALL_SIZE // 2 > HEIGHT:
            ball_speed_y *= -1

        # Punkt fuer rechte Seite
        if ball["x"] - BALL_SIZE // 2 < 0:
            right_score += 1
            start_game()

        # Punkt fuer linke Seite
        if ball["x"] + BALL_SIZE // 2 > WIDTH:
            left_score += 1
            start_game()

        draw_game()

        root.after(20, move_ball)

    def move_paddle(event):
        if event.keysym == "Up":
            right_paddle["y"] -= paddle_speed
        elif event.keysym == "Down":
            right_paddle["y"] += paddle_speed

        if right_paddle["y"] - PADDLE_HEIGHT // 2 < 0:
            right_paddle["y"] = PADDLE_HEIGHT // 2
        elif right_paddle["y"] + PADDLE_HEIGHT // 2 > HEIGHT:
            right_paddle["y"] = HEIGHT - PADDLE_HEIGHT // 2

        draw_game()

    # Hauptprogramm
    WIDTH = 800
    HEIGHT = 600
    PADDLE_WIDTH = 15
    PADDLE_HEIGHT = 100
    BALL_SIZE = 20

    root = tk.Tk()
    root.title("Ping Pong Game")

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
    canvas.pack()

    left_paddle = {"x": PADDLE_WIDTH // 2 + 10, "y": HEIGHT // 2}
    right_paddle = {"x": WIDTH - PADDLE_WIDTH // 2 - 10, "y": HEIGHT // 2}
    ball = {"x": WIDTH // 2, "y": HEIGHT // 2}

    ball_speed_x = 0
    ball_speed_y = 0
    paddle_speed = 0

    root.bind("<Up>", move_paddle)
    root.bind("<Down>", move_paddle)

    start_game()

    root.mainloop()
    
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
                web.open(links[int(lopen)-1])
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
        
def logged_in():
    """
    Function to handle actions after successful login.
    """
    global data_user1_login
    
    print()
    print("Welcome " + us_log)
    print()
    print("-" * 14)
    print("s...Settings\nl...Log Out\nh...Help\nw...Write File\nr...Read File\nsh...Shutdown\ndr...Draw\ncal...Calender\ndec...Deciphering\nbr...Browser\nno...Notes\nco...Text Color")
    print("-" * 14)
    print()
    com = input(">>> ")
    
    """if com == "c":
        while True:
            print("-"*14)
            new_pas = input("New Password: ")
            new_pas_check = input("New Password again: ")
            print("-"*14)
                        
            if new_pas == new_pas_check:
                data_user1_login["password"] = new_pas
                with open(filename, "w") as file:
                    json.dump({"user1": data_user1_login}, file, indent=4)
                print("Password changed!", new_pas)
                print("-"*14)
                logged_in()
                break
            else:
                print()
                print("Passwords do not match!")
                continue
            
    elif com == "u":
        while True:   
            print("-"*14)
            new_us = input("New Username: ")
            new_us_check = input("New Username again: ")
            print("-"*14)
            
            if new_us == new_us_check:
                data_user1_login["username"] = new_us
                with open(filename, "w") as file:
                    json.dump({"user1": data_user1_login}, file, indent=4)
                print("Username changed!", new_us)
                print("-"*14)
                logged_in()
                break
            else:
                print()
                print("Usernames do not match!")
                continue"""
            
    if com == "l":
        print("Good Bye " + us_log)
        print("-" * 14)
        innerPy()
    
    elif com == "h":
        print()
        print("Help".center(50))
        print("-" * 50)
        print()
        print("Draw".center(50))
        print("-" * 50)
        print("To Draw enter: \n - line(size=100,facing=(up,down,left,right),color=(red,gree,purple,...)) or \n - circle(size=100,posx=0,posy=0) or \n - manual to draw manually")
        print()
        input(">>> ")
        logged_in()
        
    elif com == "w":
        print("-"*14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\write_text.txt"
    
        with open(filedat, "w") as file:
            while True:
                inp = input(">>> ")
            
                if inp.lower() == "exitfile":
                    break 
                else:
                    file.write(inp + "\n")

        logged_in()
                   
    elif com == "r":
        print("-"*14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\write_text.txtt"
        
        with open(filedat, "r") as file:
            print(f"Text Written: " + file.read())
        print("-"*14)
        logged_in()
     
    elif com == "sh":
        print("See you soon!")
        exit()
        
    elif com == "dr":
        # print("-"*14)
        # print("Not finished yet!!\nPlease be patient!")
        # print("Press 'Enter' to continue.")
        # print("-"*14)
        # input(">>> ")
        # logged_in()

        while True:
            command = input("What to draw (controls in Help, to exit write: eixt): ")

            if "line" in command:
                size = int(command[command.find("size=") + 5:command.find("facing=") - 1])
                facing = command[command.find("facing=") + 7:command.find("color=") - 1]
                color = command[command.find("color=") + 6:command.find(")")]

                draw_line(size, facing, color)
            
            elif "circle" in command:
                size = int(command[command.find("size=") + 5:command.find(",posx")])
                posx = int(command[command.find("posx=") + 5:command.find(",posy")])
                posy = int(command[command.find("posy=") + 5:command.find(")")])

                draw_circle(size,posx,posy)

            elif command == "exit":
                programmer_logged_in()    

            elif command == "manual":
                turtle.ondrag(on_drag)
                # turtle.mainloop()  

    elif com == "cal":
        print("-"*14)
        print()
        calendar()
        logged_in()
        
    elif com == "dec":
        ver_entschluessel()
        logged_in()
        
    elif com == "br":
        browser()
        logged_in()
        
    elif com == "s":
        while True:
            print("-" * 14)
            print("Change Password(pw) or Username(un)? Type 'exit' to exit the Settings.")
        
            sett = input(">>> ")
        
            if sett == "pw":
                while True:
                    print("-"*14)
                    new_pas = input("New Password: ")
                    new_pas_check = input("New Password again: ")
                    print("-"*14)
                        
                    if new_pas == new_pas_check:
                        data_user1_login["password"] = new_pas
                        with open(filename, "w") as file:
                            json.dump({"user1": data_user1_login}, file, indent=4)
                        print("Password changed!", new_pas)
                        print("-"*14)
                        break
                    else:
                        print()
                        print("Passwords do not match!")
                        continue
                    
            elif sett == "un":
                while True:   
                    print("-"*14)
                    new_us = input("New Username: ")
                    new_us_check = input("New Username again: ")
                    print("-"*14)
            
                    if new_us == new_us_check:
                        data_user1_login["username"] = new_us
                        with open(filename, "w") as file:
                            json.dump({"user1": data_user1_login}, file, indent=4)
                        print("Username changed!", new_us)
                        print("-"*14)
                        break
                    else:
                        print()
                        print("Usernames do not match!")
                        continue
            
            elif sett == "exit":
                break
                
            else:
                print("Wrong input! Try again!")
                continue
            
        logged_in()
        
    elif com == "no":
        notizen_app()
        logged_in()

    elif com == "co":
        colortx()
        logged_in()
    
    else:
        print("Key does not exist!")
        print("Press 'r' to return to menu!")
        input(">>> ")
        logged_in()

def programmer_logged_in():
    global data_user1_login
    
    print()
    print("Welcome " + us_log)
    print()
    print("-" * 14)
    print("l...Log Out\nh...Help\nw...Write File\nr...Read File\nsh...Shutdown\ndr...Draw\ncal...Calender\ndec...Decipher\nping...Ping Pong(in developement)\nbr...Browser\nno...Notes\nco...Text Color\npdjson...Programmer Data")        
    print("-" * 14)
    print()
    com = input(">>> ")
    
    """if com == "c":
        while True:
            print("-"*14)
            new_pas = input("New Password: ")
            new_pas_check = input("New Password again: ")
            print("-"*14)
                        
            if new_pas == new_pas_check:
                data_user1_login["password"] = new_pas
                with open(filename, "w") as file:
                    json.dump({"user1": data_user1_login}, file, indent=4)
                print("Password changed!", new_pas)
                print("-"*14)
                programmer_logged_in()
                break
            else:
                print()
                print("Passwords do not match!")
                continue
            
    elif com == "u":
        while True:   
            print("-"*14)
            new_us = input("New Username: ")
            new_us_check = input("New Username again: ")
            print("-"*14)
            
            if new_us == new_us_check:
                data_user1_login["username"] = new_us
                with open(filename, "w") as file:
                    json.dump({"user1": data_user1_login}, file, indent=4)
                print("Username changed!", new_us)
                print("-"*14)
                programmer_logged_in()
                break
            else:
                print()
                print("Usernames do not match!")
                continue"""
            
    if com == "l":
        print("Good Bye " + us_log)
        print("-" * 14)
        innerPy()
    
    elif com == "h":
        print()
        print("Help".center(50))
        print("-" * 50)
        print()
        print("Draw".center(50))
        print("-" * 50)
        print("To Draw enter: \n - line(size=100,facing=(up,down,left,right),color=(red,gree,purple,...)) or \n - circle(size=100,posx=0,posy=0) or \n - manual to draw manually")
        print()
        print("Write".center(50))
        print("-"*50)
        print("Functions in WinWrite: \n - exitfile (to exit)")
        print("")
        print("pr")
        input(">>> ")
        programmer_logged_in()
        
    elif com == "w":
        print("-"*14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\write_text.txt"
    
        with open(filedat, "w") as file:
            while True:
                inp = input(">>> ")
            
                if inp.lower() == "exitfile":
                    break 
                else:
                    file.write(inp + "\n")

        programmer_logged_in()
                   
    elif com == "r":
        print("-"*14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\write_text.txt"
        
        with open(filedat, "r") as file:
            print(f"Text Written: " + file.read())
        print("-"*14)
        programmer_logged_in()
     
    elif com == "sh":
        print("See you soon!")
        exit()
        
    elif com == "dr":
        # print("-"*14)
        # print("Not finished yet!!\nPlease be patient!")
        # print("Press 'Enter' to continue.")
        # print("-"*14)
        # input(">>> ")
        # logged_in()

        while True:
            command = input("What to draw (controls in Help, to exit write: eixt): ")

            if "line" in command:
                size = int(command[command.find("size=") + 5:command.find("facing=") - 1])
                facing = command[command.find("facing=") + 7:command.find("color=") - 1]
                color = command[command.find("color=") + 6:command.find(")")]

                draw_line(size, facing, color)
            
            elif "circle" in command:
                size = int(command[command.find("size=") + 5:command.find(",posx")])
                posx = int(command[command.find("posx=") + 5:command.find(",posy")])
                posy = int(command[command.find("posy=") + 5:command.find(")")])

                draw_circle(size,posx,posy)

            elif command == "exit":
                programmer_logged_in()
                
            elif command == "manual":
                turtle.ondrag(on_drag)
                # turtle.mainloop() 
    
    elif com == "pdjson":
        filepath = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\log_in_admin.json"
    
        with open(filepath, "r") as file:
            data = json.load(file)
            progr_dat = data.get("file_dat", None)
        
            if progr_dat is not None:
                print("Version: " + progr_dat["version"] + "\n" + "Copyright: " + progr_dat["copyright"] + "\n" + "Rights: " + progr_dat["rights"] + "\n" + "Information:" + progr_dat["information"])
        
        programmer_logged_in()
        
    elif com == "cal":
        print("-"*14)
        print()
        calendar()
        programmer_logged_in()
        
    elif com == "dec":
        ver_entschluessel()
        programmer_logged_in()
        
    elif com == "ping":
        ping_pong()
        programmer_logged_in()
        
    elif com == "br":
        browser()
        programmer_logged_in()     
    
    elif com == "no":
        notizen_app()
        programmer_logged_in()

    elif com == "co":
        colortx()
        programmer_logged_in()
    
    else:
        print("Key does not exist!")
        print("Press 'r' to return to menu!")
        input(">>> ")
        programmer_logged_in()

# Run Funktion

innerPy() 