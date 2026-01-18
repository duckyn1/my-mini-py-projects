import random
import time

options = ("Rock", "Paper", "Scissors")

req = input("Hi, wanna play with me a Rock, Paper, and Scissors? (y/n): ").lower()
running = True

while running:
    bot = random.choice(options)
    inp = None

    if req == "n":
        print("okay, bye!")
        break
    while inp not in options:
        inp = input("Rock, Paper, or Scissors? ").capitalize()
        time.sleep(0.5)

    print(f"You: {inp}, Computer: {bot}")

    if inp == bot:
        print("It's a tie!")
    elif inp == "Rock" and bot == "Scissors":
        print('You win!')
    elif inp == "Paper" and bot == "Rock":
        print("You win!")
    elif inp == "Sccissors" and bot == "Paper":
        print("You win!")
    else:
        print('You lose :(')

    if not input("Play again? (y/n): ").lower() == "y":
        running = False
print("Thanks for playing!")
