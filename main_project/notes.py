import time

txt_path = "notes.txt"
txt = ''

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def menu():
    print("\n Welcome to Ducky's Notes!")
    print("\n 1. Write down notes \n 2. Show all your notes \n 3. Delete all your notes \n 4. Exit")

def write():
    inp = input("What thing can i write for you? ")
    try:
        with open(txt_path, "a") as file:
            file.write(f"\n {current_time}: {inp} \n")
            print("Your note is successfully added!")
    except FileNotFoundError:
        print("Your file is not found :(")

def delete_all():
    inp = input("Delete all notes? (y/n) ")
    if inp == 'y':
        with open(txt_path, "r+") as file:
            file.seek(0)
            file.truncate()
            print("All notes was deleted!")
    else:
        print("\n")

def show_notes():
    inp2 = input("You want to see all your notes? (y/n) ")
    if inp2 == 'y':
        with open(txt_path, "r") as file:
            note = file.read()
            print(note)
    else:
        print("\n")

def main():
    running = True

    while running:
        menu()
        inp = input("Choose your option: ")
        
        if inp == '1':
            write()
        elif inp == '2':
            show_notes()
        elif inp == '3':
            delete_all()
        elif inp == '4':
            running = False
        else:
            print("idk")
    print("Thanks for using my program!")


if __name__ == "__main__":
    main()
