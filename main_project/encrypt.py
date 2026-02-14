import random
import string
import time

running = True
char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
keys = char.copy()

random.shuffle(keys)

def encrypt(char, keys):
        inp = input("Write a message to encrypt: ")
        out_sipher = ""

        for letter in inp:
            index = char.index(letter)
            out_sipher += keys[index]

        print(f"original: {inp}")
        print(f"encrypted: {out_sipher}")

def decrypt(char, keys):
        out_sipher = input("Write a message to decrypt: ")
        inp = ""

        for letter in out_sipher:
            index = keys.index(letter)
            inp += char[index]

        print(f"encrypted: {out_sipher}")
        print(f"original (decrypted): {inp}")

def menu():
        while running:
            print("------------------------")
            print("Hello! What do you want?")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Exit")
            print("------------------------")
            choose = input("Choose your option: ")

            if choose == "1":
                encrypt(char, keys)
                time.sleep(1)
            elif choose == "2":
                decrypt(char, keys)
                time.sleep(1)
            elif choose == "3":
                break
            else:
                print("idk what is this")
menu()


print("Thanks for using this program! ^^")