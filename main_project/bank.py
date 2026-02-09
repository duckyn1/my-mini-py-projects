def s_balance(balance):
    print(f"You have: ${balance:.2f}")

def deposit():
    depo = float(input("Enter an amount to deposit: "))
    if depo < 0:
        print("It's not a valid number")
        return 0
    else:
        print(f"${depo:.2f} was deposited to your account.")
        return depo

def withdraw(balance):
    withd = float(input("Enter an amount to be withdrawn: "))
    if withd > balance:
        print(f"The amount can't be bigger than ${balance:.2f}")
        return 0
    elif withd < 0:
        print("The amount can't be smaller than zero.")
        return 0
    else:
        print("Withdrawn success")
        return withd
        

def menu1():
    print("** BANK **")
    print("1. Balance |" \
    " 2. Deposit |" \
    " 3. Withdraw |" \
    " 4. Exit")

def main():
    balance = 100
    running = True

    while running:
        menu1()

        inp1 = input("Your choice: ")
        if inp1 == "1":
            s_balance(balance)
        elif inp1 == "2":
            balance += deposit()
        elif inp1 == "3":
            balance -= withdraw(balance)
        elif inp1 == "4":
            running = False
        else:
            print("idk what is this")
    print("Thanks! Have a good day :)")

if __name__ == "__main__":
    main()