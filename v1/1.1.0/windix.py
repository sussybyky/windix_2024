import json
import turtle

filename = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\windix\log_in_data.json"

def innerPy():
    """
    Main function to handle user registration, login, and menu navigation.
    """
    global filename
    global rep
    
    rep = True
    
    while rep:
        reg_or_log = input("Register or Login: ")
        print("-" * 14)
        
        with open(filename, "r") as file:
            data = json.load(file)
            user1 = data.get("user1", {})
            
            if not user1.get("username") or reg_or_log == "Register":
                print("Registering...")
                print()
                regis()
            elif reg_or_log == "Login":
                print("Log In...")
                print()
                login()
            else:
                print("Wrong input!\nPlease Enter 'Register' or 'Login'!")
                continue

def regis():
    """
    Function to handle user registration.
    """
    us = input("Username: ")
    pas = input("Password: ")
    
    data_user1 = {
        "username": us,
        "password": pas
    }
    
    with open(filename, "r") as file:
        datas = json.load(file)
            
    datas["user1"] = data_user1
    
    with open(filename, 'w') as datei:
        json.dump(datas, datei, indent=4)

def login():
    """
    Function to handle user login.
    """
    global data_user1_login
    global pas_log
    global us_log
    global rep
    
    us_log = input("Username: ")
    pas_log = input("Password: ")    
    
    with open(filename, "r") as file:
        datas = json.load(file)
        
    data_user1_login = datas.get("user1", {})
    admin_login = datas.get("admin", {})
    
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
        return False

    # turtle.done()

def logged_in():
    """
    Function to handle actions after successful login.
    """
    global data_user1_login
    
    print()
    print("Welcome " + us_log)
    print()
    print("-" * 14)
    print("c...Change Password\nu...Change Username\nl...Log Out\ns...Settings\nw...Write File\nr...Read File\nsh...Shutdown\ndr...Draw")        
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
    
    elif com == "s":
        print()
        print("Settings".center(50))
        print("-" * 50)
        print()
        print("No Settings Yet!!\nPress 'r' to return to Menu!")
        print()
        input(">>> ")
        logged_in()
        
    elif com == "w":
        print("-"*14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\windix\write_text.txt"
    
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
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\windix\write_text.txt"
        
        with open(filedat, "r") as file:
            print(f"Text Written: " + file.read())
        print("-"*14)
        logged_in()
     
    elif com == "sh":
        print("See you soon!")
        exit()
        
    elif com == "dr":
        print("-"*14)
        print("Not finished yet!!\nPlease be patient!")
        print("Press 'Enter' to continue.")
        print("-"*14)
        input(">>> ")
        logged_in()

        while True:
            command = input("What to draw (f.e.: line(size=2,facing=up,color=red)): ")

            if "line" in command:
                size = int(command[command.find("size=") + 5:command.find("facing=") - 1])
                facing = command[command.find("facing=") + 7:command.find("color=") - 1]
                color = command[command.find("color=") + 6:command.find(")")]

                draw_line(size, facing, color)       
    
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
    print("c...Change Password\nu...Change Username\nl...Log Out\ns...Settings\nw...Write File\nr...Read File\nsh...Shutdown\ndr...Draw\npdjson...Programmer Data")        
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
    
    elif com == "s":
        print()
        print("Settings".center(50))
        print("-" * 50)
        print()
        print("No Settings Yet!!\nPress 'r' to return to Menu!")
        print()
        input(">>> ")
        logged_in()
        
    elif com == "w":
        print("-"*14)
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\windix\write_text.txt"
    
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
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\windix\write_text.txt"
        
        with open(filedat, "r") as file:
            print(f"Text Written: " + file.read())
        print("-"*14)
        logged_in()
     
    elif com == "sh":
        print("See you soon!")
        exit()
        
    elif com == "dr":
        print("-"*14)
        print("Not finished yet!!\nPlease be patient!")
        print("Press 'Enter' to continue.")
        print("-"*14)
        input(">>> ")
        logged_in()

        while True:
            command = input("What to draw (f.e.: line(size=2,facing=up,color=red)): ")

            if "line" in command:
                size = int(command[command.find("size=") + 5:command.find("facing=") - 1])
                facing = command[command.find("facing=") + 7:command.find("color=") - 1]
                color = command[command.find("color=") + 6:command.find(")")]

                draw_line(size, facing, color)
    
    elif com == "pdjson":
        filepath = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\windix\log_in_data.json"
    
        with open(filepath, "r") as file:
            data = json.load(file)
            progr_dat = data.get("file_dat", None)
        
            if progr_dat is not None:
                print("Version: " + progr_dat["version"] + "\n" + "Copyright: " + progr_dat["copyright"] + "\n" + "Rights: " + progr_dat["rights"] + "\n" + "Information:" + progr_dat["information"])
            
    
    else:
        print("Key does not exist!")
        print("Press 'r' to return to menu!")
        input(">>> ")
        logged_in()
# Run Funktion

innerPy()
