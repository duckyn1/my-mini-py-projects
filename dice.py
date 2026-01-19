import random

dices_art = {
1: ("┌───────┐", 
    "│   ●   │", 
    "│       │",
    "└───────┘"), 
2: ("┌───────┐", 
    "│   ●   │", 
    "│   ●   │",
    "└───────┘"),
3: ("┌───────┐", 
    "│ ●   ● │", 
    "│   ●   │",
    "└───────┘"),
4: ("┌───────┐", 
    "│ ●   ● │", 
    "│ ●   ● │",
    "└───────┘")
}

dice = []
total = 0
nmb_dices = int(input("How many dices? "))

for die in range(nmb_dices):
    dice.append(random.randint(1, 4))

for die in range(nmb_dices):
    for line in dices_art.get(dice[die]):
        print(line)

for die in dice:
    total += die
print(f"Total: {total}")