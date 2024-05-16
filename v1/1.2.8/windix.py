# -*- coding: utf-8 -*-
import json
import turtle
from func.browser import browser
from func.calendar import calendar
from func.colortx import colortx
from func.draw_circle import draw_circle
from func.draw_line import draw_line
from func.notizen import notizen_app
from func.on_drag import on_drag
from func.ver_entschluesseln import ver_entschluessel
from func.russiches_roulette import russian_roulette
from func.python_programming_util import main
from func.get_hidden_input import get_hidden_input
from func.delete_user import delete_user
from func.calculator import calculate

filename = r"log_in_data.json"
adfilename = r"log_in_admin.json"

def innerPy():
    """
    Main function to handle user registration, login, and menu navigation.
    """
    global filename
    global rep
    global adfilename

    rep = True

    while rep:
        reg_or_log = input("Register or Login (r/l): ").lower()
        print("-" * 14)

        with open(filename, "r") as file:
            data = json.load(file)
            user1 = data.get("user1", {})

        if reg_or_log == "r":
            print("Registering...")
            regis()
        elif reg_or_log == "l":
            print("Log In...")
            login()
        else:
            print("Wrong input! Please Enter 'r'(Register) or 'l'(Login)!")
            continue

def regis():
    """
    Function to handle user registration.
    """
    us = input("Username: ")
    pas = get_hidden_input("Password: ")

    data_user1 = {
        us: pas
    }

    data_admin = {
        "admin": {
            "username": "Admin",
            "password": "adpass001/1.2.8/2024"
        },
        "file_dat": {
            "version": "Windix 1(2.8)",
            "copyright": "GNU General Public License: https://github.com/sussybyky/windix_2024/blob/master/LICENSE",
            "rights": "Read the Readme file for further information: https://github.com/sussybyky/windix_2024/blob/master/README.md",
            "information": "This is a copy of the original file!"
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
    global login_data_basic
    global data_admin
    global pas_log
    global us_log
    global rep

    us_log = input("Username: ")
    pas_log = get_hidden_input("Password: ")

    with open(filename, "r") as file:
        datas = json.load(file)

    with open(adfilename, 'r') as file:
        datadm = json.load(file)

    login_data_basic = datas
    admin_login = datadm.get("admin", {})

    if us_log in login_data_basic.keys() and pas_log == login_data_basic[us_log]:
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

def logged_in():
    """
    Function to handle actions after successful login.
    """
    global login_data_basic

    print(f"\nWelcome {us_log}\n")
    print("-" * 14)
    print("s...Settings\nl...Log Out\nh...Help\nw...Write File\nr...Read File\nsh...Shutdown\n"
          "dr...Draw\ncal...Calender\ndec...Deciphering\nbr...Browser\nno...Notes\nco...Text Color\n"
          "rus...Russian roulette\ndel...Delete this User\ncode...Write python code\ncalc...Calculator")
    print("-" * 14)
    print()

    com = input(">>> ").lower()

    commands = {
        "s": settings,
        "l": log_out,
        "h": help_menu,
        "w": write_file,
        "r": read_file,
        "sh": shutdown,
        "dr": draw,
        "cal": calendar_menu,
        "dec": decipher,
        "br": browse,
        "no": notes,
        "co": text_color,
        "del": delete_user_func,
        "rus": russian_roulette_game,
        "code": write_python_code,
        "calc": calculator
    }

    command_func = commands.get(com, invalid_command)
    command_func()

def settings():
    while True:
        print("-" * 14)
        print("Change Password(pw) or Username(un)? Type 'exit' to exit the Settings.")
        sett = input(">>> ").lower()

        if sett == "pw":
            change_password()
        elif sett == "un":
            change_username()
        elif sett == "exit":
            break
        else:
            print("Wrong input! Try again!")

def change_password():
    while True:
        print("-" * 14)
        new_pas = input("New Password: ")
        new_pas_check = input("New Password again: ")
        print("-" * 14)

        if new_pas == new_pas_check:
            login_data_basic["password"] = new_pas
            with open(filename, "w") as file:
                json.dump({us_log: login_data_basic}, file, indent=4)
            print(f"Password changed! {new_pas}")
            print("-" * 14)
            logged_in()
            break
        else:
            print("Passwords do not match!")

def change_username():
    while True:
        print("-" * 14)
        new_us = input("New Username: ")
        new_us_check = input("New Username again: ")
        print("-" * 14)

        if new_us == new_us_check:
            login_data_basic["username"] = new_us
            with open(filename, "w") as file:
                json.dump({new_us: pas_log}, file, indent=4)
            print(f"Username changed! {new_us}")
            print("-" * 14)
            logged_in()
            break
        else:
            print("Usernames do not match!")

def log_out():
    print(f"Good Bye {us_log}")
    print("-" * 14)
    innerPy()

def help_menu():
    print()
    print("Help".center(50))
    print("-" * 50)
    print("Draw".center(50))
    print("-" * 50)
    print("To Draw enter: \n - line(size=100,facing=(up,down,left,right),color=(red,gree,purple,...)) or \n - "
          "circle(size=100,posx=0,posy=0) or \n - manual to draw manually")
    print()
    input(">>> ")
    logged_in()

def write_file():
    print("-" * 14)
    filedat = r"write_text.txt"

    with open(filedat, "w") as file:
        while True:
            inp = input(">>> ")
            if inp.lower() == "exitfile":
                break
            else:
                file.write(inp + "\n")
    logged_in()

def read_file():
    print("-" * 14)
    filedat = r"write_text.txt"

    with open(filedat, "r") as file:
        print(f"Text Written: " + file.read())
    print("-" * 14)
    logged_in()

def shutdown():
    print("See you soon!")
    exit()

def draw():
    while True:
        command = input("What to draw (controls in Help, to exit write: exit): ").lower()
        if "line" in command:
            size = int(command[command.find("size=") + 5:command.find("facing=") - 1])
            facing = command[command.find("facing=") + 7:command.find("color=") - 1]
            color = command[command.find("color=") + 6:command.find(")")]
            draw_line(size, facing, color)
        elif "circle" in command:
            size = int(command[command.find("size=") + 5:command.find(",posx")])
            posx = int(command[command.find("posx=") + 5:command.find(",posy")])
            posy = int(command[command.find("posy=") + 5:command.find(")")])
            draw_circle(size, posx, posy)
        elif command == "exit":
            logged_in()
        elif command == "manual":
            turtle.ondrag(on_drag)
        else:
            print("Wrong input! Type 'exit' to exit the Draw mode.")

def calendar_menu():
    calendar()
    logged_in()

def decipher():
    ver_entschluessel()
    logged_in()

def browse():
    browser()
    logged_in()

def notes():
    notizen_app()
    logged_in()

def text_color():
    colortx()
    logged_in()

def delete_user_func():
    delete_user()
    innerPy()

def russian_roulette_game():
    russian_roulette()
    logged_in()

def write_python_code():
    main()
    logged_in()

def calculator():
    calculate()
    logged_in()

def invalid_command():
    print("Invalid command.")
    logged_in()

def programmer_logged_in():
    """
    Function to handle actions after admin login.
    """
    global rep

    print(f"\nWelcome {us_log} [Admin]\n")
    print("-" * 14)
    print("l...Log Out\nh...Help\nw...Write File\nr...Read File\nsh...Shutdown\ndr...Draw\ncal...Calendar\n"
          "dec...Decipher\nping...Ping Pong (in development)\nbr...Browser\nno...Notes\nco...Text Color\n"
          "rus...Russian roulette\ncode...Write python code\ncalc...Calculator\npdjson...Programmer Data")
    print("-" * 14)

    while True:
        com = input(">>> ").lower()

        if com == "l":
            print("Good Bye " + us_log)
            print("-" * 14)
            rep = True
            innerPy()
            break

        elif com == "h":
            help_menu()

        elif com == "w":
            write_file()

        elif com == "r":
            read_file()

        elif com == "sh":
            shutdown()

        elif com == "dr":
            draw()

        elif com == "cal":
            calendar_menu()

        elif com == "dec":
            decipher()

        elif com == "br":
            browse()

        elif com == "no":
            notes()

        elif com == "co":
            text_color()

        elif com == "del":
            delete_user_func()

        elif com == "rus":
            russian_roulette_game()

        elif com == "calc":
            calculator()

        elif com == "code":
            write_python_code()

        elif com == "pdjson":
            programmer_data()

        else:
            invalid_command()


def help_menu():
    """
    Displays the help menu.
    """
    print("\nHelp".center(50))
    print("-" * 50)
    print("\nDraw".center(50))
    print("-" * 50)
    print("To Draw enter: \n - line(size=100,facing=(up,down,left,right),color=(red,gree,purple,...)) or \n - "
          "circle(size=100,posx=0,posy=0) or \n - manual to draw manually")
    print("\nWrite".center(50))
    print("-" * 50)
    print("Functions in WinWrite: \n - exitfile (to exit)\n")
    input(">>> ")
    programmer_logged_in()


def write_file():
    """
    Allows the admin to write to a file.
    """
    print("-" * 14)
    filedat = r"write_text.txt"

    with open(filedat, "w") as file:
        while True:
            inp = input(">>> ")
            if inp.lower() == "exitfile":
                break
            else:
                file.write(inp + "\n")
    programmer_logged_in()


def read_file():
    """
    Allows the admin to read from a file.
    """
    print("-" * 14)
    filedat = r"write_text.txt"

    with open(filedat, "r") as file:
        print(f"Text Written: " + file.read())
    print("-" * 14)
    programmer_logged_in()


def shutdown():
    """
    Shuts down the application.
    """
    print("See you soon!")
    exit()


def draw():
    """
    Allows the admin to draw using commands.
    """
    while True:
        command = input("What to draw (controls in Help, to exit write: exit): ")

        if "line" in command:
            size = int(command[command.find("size=") + 5:command.find("facing=") - 1])
            facing = command[command.find("facing=") + 7:command.find("color=") - 1]
            color = command[command.find("color=") + 6:command.find(")")]

            draw_line(size, facing, color)

        elif "circle" in command:
            size = int(command[command.find("size=") + 5:command.find(",posx")])
            posx = int(command[command.find("posx=") + 5:command.find(",posy")])
            posy = int(command[command.find("posy=") + 5:command.find(")")])

            draw_circle(size, posx, posy)

        elif command.lower() == "exit":
            programmer_logged_in()

        elif command.lower() == "manual":
            turtle.ondrag(on_drag)
            turtle.mainloop()


def calendar_menu():
    """
    Displays the calendar.
    """
    print("-" * 14)
    print()
    calendar()
    programmer_logged_in()


def decipher():
    """
    Allows the admin to use the deciphering function.
    """
    ver_entschluessel()
    programmer_logged_in()


def browse():
    """
    Opens the browser functionality.
    """
    browser()
    programmer_logged_in()


def notes():
    """
    Opens the notes functionality.
    """
    notizen_app()
    programmer_logged_in()


def text_color():
    """
    Opens the text color functionality.
    """
    colortx()
    programmer_logged_in()


def delete_user_func():
    """
    Deletes the user and returns to the main menu.
    """
    delete_user()
    innerPy()


def russian_roulette_game():
    """
    Plays the Russian roulette game.
    """
    russian_roulette()
    programmer_logged_in()


def write_python_code():
    """
    Opens the function to write Python code.
    """
    main()
    programmer_logged_in()


def calculator():
    """
    Opens the calculator functionality.
    """
    while True:
        try:
            print("Press CTRL + C to exit.")
            print(calculate())
        except (KeyboardInterrupt, ValueError):
            break
    programmer_logged_in()


def programmer_data():
    """
    Displays programmer-specific data from the JSON file.
    """
    filepath = r"log_in_admin.json"

    with open(filepath, "r") as file:
        data = json.load(file)
        progr_dat = data.get("file_dat", None)

        if progr_dat is not None:
            print("Version: " + progr_dat["version"] + "\n" + "Copyright: " + progr_dat["copyright"] + "\n" +
                  "Rights: " + progr_dat["rights"] + "\n" + "Information:" + progr_dat["information"])

    programmer_logged_in()


def invalid_command():
    """
    Handles invalid commands.
    """
    print("Invalid command.")
    programmer_logged_in()


if __name__ == "__main__":
    innerPy()
