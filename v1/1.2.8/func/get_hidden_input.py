import getpass


def get_hidden_input(prompt="Enter Password: "):
    return getpass.getpass(prompt)
