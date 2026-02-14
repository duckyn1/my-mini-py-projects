nm = input("Enter ur name: ")
ln = input("Enter ur last name: ")

def displ_name(*names):
    for name in names:
        print(name, end=" ")

displ_name(nm, ln)