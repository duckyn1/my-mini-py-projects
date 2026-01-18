import time
import random

your_wins = 0
blud_wins = 0
random_nmb = random.randrange(67, 70)

games = 0

while True:
    print("Ur blud: Hey, wanna bet if my number bigger than urs?")
    time.sleep(1)
    print("You: Okay")
    time.sleep(1)
    print("Ur blud choosing the number..")
    time.sleep(1.5)
    a = random.randrange(1, 200)
    
    b_input = input("Write here ur number: ")
    if b_input.lower() == 'exit':
        print("Okay, see ya later! 👋")
        break

    try:
        b = float(b_input)
    except ValueError:
        print("Bro, that's not a number 😅 Try again!")
        continue

    burgers = f"dam {b} is big 🔥" if b > a else f"nah {a} is bigger, sorry bro 😔"
    print(burgers)
    
    games += 1
    if b > a:
        your_wins += 1
        print(f"You won! Score: {your_wins}:{blud_wins}. Total games played: {games}. Testing: {random_nmb}")
    else:
        blud_wins += 1
        print(f"Blud won. Score: {your_wins}:{blud_wins}. Total games played: {games}. Testing: {random_nmb}")

    time.sleep(2)
