import json
from tkinter import messagebox

def delete_user():
    username = input("Username: ")
    password = input("Password: ")

    response = messagebox.askyesno("Delete User", "Are you sure you want to delete this user?")
    if response:
        while True:
            with open("log_in_data.json", "r") as file:
                user_data = json.load(file)

            if username in user_data.keys():
                if password == user_data[username]:
                    response = messagebox.askyesno("Delete User", "Do you want to delete this user?")
                    if response:
                        del user_data[username]
                        print("User deleted")

                        with open("log_in_data.json", "w") as file:
                            json.dump(user_data, file, indent=4)
                        return
                    else:
                        return
                else:
                    print("Wrong password.")

    else:
        return
