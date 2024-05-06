import json
import turtle

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
            
            if not user1.get("username") or reg_or_log == "r":
                print("Registering...")
                print()
                regis()
            elif reg_or_log == "l":
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
    data_admin = {
        "admin": {
            "username": "Admin",
            "password": "adpass9!"
        },
        
        "file_dat": {
            "version": "1.1.4",
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

def draw_circle(size, posx, posy):
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.pendown()
    turtle.circle(size)

    return
    # turtle.done()

def on_drag(x, y):
    turtle.speed(100)
    turtle.ondrag(None)  # Deaktiviere die ondrag-Funktion, um eine Endlosschleife zu vermeiden
    turtle.goto(x, y)
    turtle.ondrag(on_drag)  # Aktiviere die ondrag-Funktion erneut
    return

def logged_in():
    """
    Function to handle actions after successful login.
    """
    global data_user1_login
    
    print()
    print("Welcome " + us_log)
    print()
    print("-" * 14)
    print("c...Change Password\nu...Change Username\nl...Log Out\nh...Help\nw...Write File\nr...Read File\nsh...Shutdown\ndr...Draw")
    print("-" * 14)
    print()
    com = input(">>> ")
    
    if com == "c":
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
                continue
            
    elif com == "l":
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
        filedat = r"write_text.txt"
    
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
        filedat = r"write_text.txt"
        
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
    print("l...Log Out\nh...Help\nw...Write File\nr...Read File\nsh...Shutdown\ndr...Draw\npdjson...Programmer Data")        
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
        filedat = r"write_text.txt"
    
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
        filedat = r"write_text.txt"
        
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
        filepath = r"log_in_admin.json"
    
        with open(filepath, "r") as file:
            data = json.load(file)
            progr_dat = data.get("file_dat", None)
        
            if progr_dat is not None:
                print("Version: " + progr_dat["version"] + "\n" + "Copyright: " + progr_dat["copyright"] + "\n" + "Rights: " + progr_dat["rights"] + "\n" + "Information:" + progr_dat["information"])
        
        programmer_logged_in()
    
    else:
        print("Key does not exist!")
        print("Press 'r' to return to menu!")
        input(">>> ")
        programmer_logged_in()

# Run Funktion

innerPy()