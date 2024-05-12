# -*- coding: utf-8 -*-

from func.browser import *
from func.calendar import *
from func.colortx import *
from func.draw_circle import *
from func.draw_line import *
from func.notizen import *
from func.on_drag import *
from func.ver_entschluesseln import *
from func.russiches_roulette import *
from func.python_programming_util import *
from func.get_hidden_input import *
from func.delete_user import *

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
    pas = get_hidden_input("Password: ")

    data_user1 = {
        us: pas
    }

    data_admin = {
        "admin": {
            "username": "Admin",
            "password": "adpass9!"
        },

        "file_dat": {
            "version": "Windix 1(2.8)",
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

    print()
    print("Welcome " + us_log)
    print()
    print("-" * 14)
    print("s...Settings\nl...Log Out\nh...Help\nw...Write File\nr...Read File\nsh...Shutdown\ndr...Draw\ncal...Calender\ndec...Deciphering\nbr...Browser\nno...Notes\nco...Text Color\nrus...Russian roulette\ndel...Delte this User\ncode...Write python code")
    print("-" * 14)
    print()
    com = input(">>> ")

    if com.lower() == "c":
        while True:
            print("-" * 14)
            new_pas = input("New Password: ")
            new_pas_check = input("New Password again: ")
            print("-" * 14)

            if new_pas == new_pas_check:
                login_data_basic["password"] = new_pas
                with open(filename, "w") as file:
                    json.dump({"user1": login_data_basic}, file, indent=4)
                print("Password changed!", new_pas)
                print("-" * 14)
                logged_in()
                break
            else:
                print()
                print("Passwords do not match!")
                continue

    elif com.lower() == "u":
        while True:
            print("-" * 14)
            new_us = input("New Username: ")
            new_us_check = input("New Username again: ")
            print("-" * 14)

            if new_us == new_us_check:
                login_data_basic["username"] = new_us
                with open(filename, "w") as file:
                    json.dump({"user1": login_data_basic}, file, indent=4)
                print("Username changed!", new_us)
                print("-" * 14)
                logged_in()
                break
            else:
                print()
                print("Usernames do not match!")
                continue

    elif com.lower() == "l":
        print("Good Bye " + us_log)
        print("-" * 14)
        innerPy()

    elif com.lower() == "h":
        print()
        print("Help".center(50))
        print("-" * 50)
        print()
        print("Draw".center(50))
        print("-" * 50)
        print(
            "To Draw enter: \n - line(size=100,facing=(up,down,left,right),color=(red,gree,purple,...)) or \n - circle(size=100,posx=0,posy=0) or \n - manual to draw manually")
        print()
        input(">>> ")
        logged_in()

    elif com.lower() == "w":
        print("-" * 14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\write_text.txt"

        with open(filedat, "w") as file:
            while True:
                inp = input(">>> ")

                if inp.lower() == "exitfile":
                    break
                else:
                    file.write(inp + "\n")

        logged_in()

    elif com.lower() == "r":
        print("-" * 14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\write_text.txtt"

        with open(filedat, "r") as file:
            print(f"Text Written: " + file.read())
        print("-" * 14)
        logged_in()

    elif com.lower() == "sh":
        print("See you soon!")
        exit()

    elif com.lower() == "dr":
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

                draw_circle(size, posx, posy)

            elif command.lower() == "exit":
                programmer_logged_in()

            elif command.lower() == "manual":
                turtle.ondrag(on_drag)
                # turtle.mainloop()

    elif com.lower() == "cal":
        print("-" * 14)
        print()
        calendar()
        logged_in()

    elif com.lower() == "dec":
        ver_entschluessel()
        logged_in()

    elif com.lower() == "br":
        browser()
        logged_in()

    elif com.lower() == "s":
        while True:
            print("-" * 14)
            print("Change Password(pw) or Username(un)? Type 'exit' to exit the Settings.")

            sett = input(">>> ")

            if sett.lower() == "pw":
                while True:
                    print("-" * 14)
                    new_pas = input("New Password: ")
                    new_pas_check = input("New Password again: ")
                    print("-" * 14)

                    if new_pas == new_pas_check:
                        with open(filename, "w") as file:
                            json.dump({us_log: new_pas}, file, indent=4)
                        print("Password changed!", new_pas)
                        print("-" * 14)
                        break
                    else:
                        print()
                        print("Passwords do not match!")
                        continue
            elif sett.lower() == "un":
                while True:
                    print("-" * 14)
                    new_us = input("New Username: ")
                    new_us_check = input("New Username again: ")
                    print("-" * 14)

                    if new_us == new_us_check:
                        with open(filename, "w") as file:
                            json.dump({new_us: pas_log}, file, indent=4)
                        print("Username changed!", new_us)
                        print("-" * 14)
                        break
                    else:
                        print()
                        print("Usernames do not match!")
                        continue

            elif sett.lower() == "exit":
                break

            else:
                print("Wrong input! Try again!")
                continue

        logged_in()

    elif com.lower() == "no":
        notizen_app()
        logged_in()

    elif com.lower() == "co":
        colortx()
        logged_in()

    elif com.lower() == "del":
        delete_user()
        innerPy()

    elif com.lower() == "rus":
        russian_roulette()
        logged_in()

    elif com.lower() == "code":
        main()
        logged_in()

    else:
        print("Key does not exist!")
        print("Press 'r' to return to menu!")
        input(">>> ")
        logged_in()


def programmer_logged_in():
    global login_data_basic

    print()
    print("Welcome " + us_log)
    print()
    print("-" * 14)
    print("l...Log Out\nh...Help\nw...Write File\nr...Read File\nsh...Shutdown\ndr...Draw\ncal...Calender\ndec...Decipher\nping...Ping Pong(in developement)\nbr...Browser\nno...Notes\nco...Text Color\nrus...Russian roulette\ncode...Write python code\npdjson...Programmer Data")
    print("-" * 14)
    print()
    com = input(">>> ")

    if com.lower() == "l":
        print("Good Bye " + us_log)
        print("-" * 14)
        innerPy()

    elif com.lower() == "h":
        print()
        print("Help".center(50))
        print("-" * 50)
        print()
        print("Draw".center(50))
        print("-" * 50)
        print(
            "To Draw enter: \n - line(size=100,facing=(up,down,left,right),color=(red,gree,purple,...)) or \n - "
            "circle(size=100,posx=0,posy=0) or \n - manual to draw manually")
        print()
        print("Write".center(50))
        print("-" * 50)
        print("Functions in WinWrite: \n - exitfile (to exit)")
        print("")
        print("")
        input(">>> ")
        programmer_logged_in()

    elif com.lower() == "w":
        print("-" * 14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\write_text.txt"

        with open(filedat, "w") as file:
            while True:
                inp = input(">>> ")

                if inp.lower() == "exitfile":
                    break
                else:
                    file.write(inp + "\n")

        programmer_logged_in()

    elif com.lower() == "r":
        print("-" * 14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\write_text.txt"

        with open(filedat, "r") as file:
            print(f"Text Written: " + file.read())
        print("-" * 14)
        programmer_logged_in()

    elif com.lower() == "sh":
        print("See you soon!")
        exit()

    elif com.lower() == "dr":
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

                draw_circle(size, posx, posy)

            elif command.lower() == "exit":
                programmer_logged_in()

            elif command.lower() == "manual":
                turtle.ondrag(on_drag)
                # turtle.mainloop()

    elif com.lower() == "pdjson":
        filepath = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\programm_files\log_in_admin.json"

        with open(filepath, "r") as file:
            data = json.load(file)
            progr_dat = data.get("file_dat", None)

            if progr_dat is not None:
                print("Version: " + progr_dat["version"] + "\n" + "Copyright: " + progr_dat[
                    "copyright"] + "\n" + "Rights: " + progr_dat["rights"] + "\n" + "Information:" + progr_dat[
                          "information"])

        programmer_logged_in()

    elif com.lower() == "cal":
        print("-" * 14)
        print()
        calendar()
        programmer_logged_in()

    elif com.lower() == "dec":
        ver_entschluessel()
        programmer_logged_in()

    elif com.lower() == "br":
        browser()
        programmer_logged_in()

    elif com.lower() == "no":
        notizen_app()
        programmer_logged_in()

    elif com.lower() == "co":
        colortx()
        programmer_logged_in()

    elif com.lower() == "rus":
        russian_roulette()
        programmer_logged_in()

    elif com.lower() == "code":
        main()
        programmer_logged_in()

    else:
        print("Key does not exist!")
        print("Press 'r' to return to menu!")
        input(">>> ")
        programmer_logged_in()


# Run Funktion

innerPy()
