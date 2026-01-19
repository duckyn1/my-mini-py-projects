stand = {"Sprite": 1,
         "Lays": 2, 
         "Popcorn": 0.75,
         "Hotdog": 1.5,
         "Water": 0.5}
cartp = []
total = 0

print("------- MENU -------")
for key, value in stand.items():
    print(f"{key}: ${value:.2f}")
print("---------------------")

while True:
    item = input("Enter ur food you gonna buy (e to exit): ").capitalize()
    if item.lower() == "e":
        break
        
    if stand.get(item) is not None:
        cartp.append(item)
        print(f"{item} added to ur cart!")
    elif item.lower() == "pay":
        print("its testing.")
    else:
        print(f"{item} is not exist.")
        print("------- MENU -------")
    for key, value in stand.items():
        print(f"{key}: ${value:.2f}")
    print("---------------------")


print("----- ORDER DETAILS -----")
print()

for item in cartp:
    total += stand.get(item)
    print(item, end = ' ')

print()
print(f"Total price: ${total:.2f}")
