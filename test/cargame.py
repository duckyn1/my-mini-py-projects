import time

car_start = "The car is started."
car_stop = "The car is stopped."
car_afk = ""
car_help = "start - to start the car\nstop - to stop the car\nexit - to exit"
started = False

while car_afk != "exit":
    command = input("")
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print(car_start)
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print(car_stop)
    elif command == "help":
        print(car_help)
    elif command == "love":
        print("uhh.. it's a car game, not real life")
        time.sleep(0.5)
        print("if u find The secret Word, u will Gain secret option..")
    elif command == "TWG":
        print("Congrats, u just unlocked new car!")
        print("choose: exit or start again?")

        if input("") == "exit":
            break

        elif input("") == "start again":
            car_afk
            
    elif command == "exit":
        print("Bye-bye")
        break
    else:
        print("Sorry, but i don't understand that")