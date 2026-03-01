import time
import datetime

def menu():
    print("Welcome to Ducky's Alarm Clock!")
    print("\n 1. Set alarm clock \n 2. Check current time \n 3. Exit")

def set_alarm(alarm_time):
    print(f"Alarm set for: {alarm_time}")
    running = True
    while running:
        current = datetime.datetime.now().strftime("%H:%M:%S")
        print(current)
        
        if current == alarm_time:
            print("Wake up!")
            running = False
            
        time.sleep(1)

def check_current():
    now = datetime.datetime.now()
    current = now.strftime("%H:%M:%S")
    print(f"Current time: {current}")

def main():
    running = True
    while running:
        menu()
        inp = input("Choose your option: ")
        if inp == "1":
            alarm_time = input("Enter the alarm time (HH:MM:SS): ")
            set_alarm(alarm_time)
        elif inp == "2":
            check_current()
        elif inp == "3":
            break
        else:
            print("\n")

if __name__ == "__main__":
    main()
