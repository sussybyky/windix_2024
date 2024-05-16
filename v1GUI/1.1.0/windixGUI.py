import tkinter as tk
import json
import turtle

filename = r"log_in_data.json"

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

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login System")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Register or Login:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Submit", command=self.handle_input)
        self.button.pack()

    def handle_input(self):
        reg_or_log = self.entry.get()

        with open(filename, "r") as file:
            data = json.load(file)
            user1 = data.get("user1", {})

            if not user1.get("username") or reg_or_log == "Register":
                self.register_window()
            elif reg_or_log == "Login":
                self.login()
            else:
                print("Wrong input!\nPlease Enter 'Register' or 'Login'!")

    def register_window(self):
        self.destroy()
        root = tk.Tk()

        label_username = tk.Label(root, text="Enter Username:")
        label_username.pack()

        entry_username = tk.Entry(root)
        entry_username.pack()

        label_password = tk.Label(root, text="Enter Password:")
        label_password.pack()

        entry_password = tk.Entry(root, show="*")
        entry_password.pack()

        button_register = tk.Button(root, text="Register", command=lambda: self.register(entry_username.get(), entry_password.get()))
        button_register.pack()

        root.mainloop()

    def register(self, username, password):
        data_user1 = {
            "username": username,
            "password": password
        }

        with open(filename, "r") as file:
            datas = json.load(file)

        datas["user1"] = data_user1

        with open(filename, 'w') as datei:
            json.dump(datas, datei, indent=4)

    def login(self):
        global entry_username, entry_password

        self.destroy()
        root = tk.Tk()

        label_username = tk.Label(root, text="Username:")
        label_username.pack()

        entry_username = tk.Entry(root)
        entry_username.pack()

        label_password = tk.Label(root, text="Password:")
        label_password.pack()

        entry_password = tk.Entry(root, show="*")
        entry_password.pack()

        button_login = tk.Button(root, text="Login", command=lambda: self.check_credentials(entry_username.get(), entry_password.get()))
        button_login.pack()

        root.mainloop()

    def check_credentials(self, username, password):

        with open(filename, "r") as file:
            datas = json.load(file)

        data_user1_login = datas.get("user1", {})

        if data_user1_login.get("password") == password and data_user1_login.get("username") == username:
            self.logged_in()
        else:
            print("-" * 14)
            print("Invalid username or password.")
            print("-" * 14)

    def logged_in(self):
        self.destroy()
        root = tk.Tk()

        label = tk.Label(root, text=f"Welcome {entry_username}")
        label.pack()

        button_draw = tk.Button(root, text="Draw", command=self.draw_window)
        button_draw.pack()

        button_write = tk.Button(root, text="Write File", command=self.write_file)
        button_write.pack()

        root.mainloop()

    def draw_window(self):
        root = tk.Tk()

        label = tk.Label(root, text="Enter draw command:")
        label.pack()

        entry = tk.Entry(root)
        entry.pack()

        button = tk.Button(root, text="Submit", command=lambda: self.execute_draw(entry.get()))
        button.pack()

        root.mainloop()

    def execute_draw(self, command):
        if "line" in command:
            size = int(command[command.find("size=") + 5:command.find("facing=") - 1])
            facing = command[command.find("facing=") + 7:command.find("color=") - 1]
            color = command[command.find("color=") + 6:command.find(")")]

            draw_line(size, facing, color)

    def write_file(self):
        root = tk.Tk()

        label = tk.Label(root, text="Write to file (type 'exitfile' to exit):")
        label.pack()

        text = tk.Text(root)
        text.pack()

        button = tk.Button(root, text="Submit", command=lambda: self.execute_write(text.get("1.0", tk.END)))
        button.pack()

        root.mainloop()

    def execute_write(self, content):
        filedat = r"F:\Daniel\sonstiges\Anderes\Schule\python\.windix\windix\write_text.txt"

        with open(filedat, "w") as file:
            file.write(content)

        print("Content written to file.")

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
