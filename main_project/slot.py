import random

def s_balance(balance):
    print(f"Current balance is: ${balance:.2f}")

def slot(numbers, balance):
    print("Welcome to the Ducky's Slots!")
    print(f"Your numbers is: {numbers}")
    s_balance(balance)

def bet(balance):
    bet1 = int(input("Place ur bet amount: "))
    if bet1 > balance:
        print("Not enough money to bet")
        return 0
    if bet1 == '':
        print("Write a number")
        return 0
    else:
        print('Spinning...')
        return bet1
    
def spinnin(numbers, bet1):
    spin = random.choice(numbers)
    spin1 = random.choice(numbers)
    spin2 = random.choice(numbers)
    print(f"{spin} | {spin1} | {spin2}")
    if spin == spin1 == spin2 == 7:
        win = bet1 * 10
        print(f"Jackpot! You won: ${win}!")
        return win
        
    elif spin == spin1 == spin2:
        win1 = bet1 * 3
        print(f"Mini! You won: ${win1}!")
        return win1
        
    else:

        return 0

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    balance = 100
    running = True

    while running:
        slot(numbers, balance)
        

        if balance <= 0:
            print(f"Ur broke. Balance: ${balance:.2f}")
            break
        else:
            bet1 = bet(balance)
            if bet1 > 0: 
                balance -= bet1
            else:
                continue
                return 0
            
            win = spinnin(numbers, bet1)
            balance += win
            s_balance(balance)
        if win == 0:
            inp = input("You lost! Want to try again? (y/n) ")
            if inp == "y".lower():
                continue
            elif inp == "n".lower():
                running = False
            else:
                print("idk")
        elif win > 0:
            inp = input("Congrats! Wanna try again? (y/n) ")
            if inp == "y".lower():
                continue
            elif inp == "n".lower():
                running = False
            else:
                print("idk")

        
if __name__ == "__main__":

    main()
