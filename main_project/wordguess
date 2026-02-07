import random

words = ["venom", "apple", "weee", "mini"]
secret_word2 = random.choice(words)
display = ["_" for _ in secret_word2]
used_word = []
guesses_count = 0
guesses_limit = 10

def secret_word1():
    letter1 = input("Enter ur word: ")
    if letter1 == secret_word2:
        print(f"ur right! word is: {secret_word2}")
    else:
        print("nah, try again.")

while guesses_count < guesses_limit:
    letter = input("Enter a letter of the secret word: ")

    guesses_count += 1
    if guesses_count == guesses_limit:
        print(f"Try again. the word was: {secret_word2}")
        break
    if letter in used_word:
        print("You already wrote it!")
        continue
    used_word.append(letter)
    
    if "_" not in display:
        print("You win!")
        break
    if letter in secret_word2:
            print(f"There's a {letter} in secret word!")

            for i in range(len(secret_word2)):
                if secret_word2[i] == letter:
                    display[i] = letter
            print(" ".join(display))

            choose = input('You wanna write the secret word? (y/n): ')

    else:
        print(f"Nah, in this word u don't have: {letter}.")
        choose = input('You wanna write the secret word? (y/n): ')

    if choose == "y".lower():
        secret_word1()
        break
    elif choose == "n".lower():
        print(f"Ur last wroten letter is: {letter}")
        continue
    else:
        print("idk what is this")

    if secret_word1() == secret_word2:
        break
    else:
        continue
