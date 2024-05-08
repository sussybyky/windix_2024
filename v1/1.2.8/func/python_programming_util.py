def run_code(code: str):
    try:
        if isinstance(code, str):
            exec(code)
        else:
            raise TypeError("Invalid code")
    except Exception as e:
        return e


def main():
    import os
    print(os.get_exec_path())
    print("Python 3.11 -> ")

    send_code = ""
    code = ""
    while code.strip() != "run/code":
        send_code += code + "\n"
        code = input(">>> ")


    run_code(send_code)
