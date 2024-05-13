import re
import math

def calculate() -> float | int | str:
    print("Enter Calculation and press Enter to calculate (Use ** for power and _/ for square root): ")
    calculation = input(">>> ")

    try:
        matches = re.findall(r'_/(\d+(?:\.\d+)?)', calculation)
        for match in matches:
            calculation = calculation.replace(f"_/{match}", str(math.sqrt(float(match))))
        result = round(eval(calculation), 3)
        return result
    except Exception as e:
        return "Error: " + str(e)
