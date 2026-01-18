weight_a = int(input("Enter your weight: "))

text_units = input("Is that kg or lbs (enter k or l): ")

if text_units.lower() or text_units.upper() == "K":
    convert = weight_a / 0.45
    print(f"Your weight is {convert} lbs")
elif text_units.lower() or text_units.upper() == "L":
    convert = weight_a * 0.45
    print(f"Your weight is {convert} kgs")
else:
    print("nah bro, try again")
