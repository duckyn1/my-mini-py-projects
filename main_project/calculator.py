import math
import time

operator = input("Write operator (+, -, /, *, **): ")

if operator == "":
        print("ummm..")
        time.sleep(0.5)  # when u wanna use this loop, place it after operator, not after if conditions :)

nmb1 = float(input("Write 1st number: ")) # first and second numbers btw
nmb2 = float(input("Write 2nd number: "))

if operator == "+":
    plus = nmb1 + nmb2
    print(f"{round(nmb1)} + {round(nmb2)} = {round(plus)}") # we're gonna round numbers, for ex: 2.0 = 2
elif operator == "-":
    minus = nmb1 - nmb2
    print(f"{round(nmb1)} - {round(nmb2)} = {round(minus)}")
elif operator == "/":
    if nmb2 == 0:
        print("Sorry, but u can't divide by zero")
    else:
        division = nmb1 / nmb2
        print(f"{round(nmb1)} / {round(nmb2)} = {round(division)}")
elif operator == "*":
    idk = nmb1 * nmb2
    print(f"{round(nmb1)} * {round(nmb2)} = {round(idk)}")
elif operator == "**":
    grk = nmb1 ** nmb2
    print(f"{round(nmb1)} ** {round(nmb2)} = {round(grk)}")
else:
    print("idk what is this")
