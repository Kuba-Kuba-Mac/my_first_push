import os

notes = []
def show_menu():
    print("----Note manager menu----")
    print("1. add Note")
    print("2. edit Note")
    print("3. view Notes")
    print("4. delete Note")
    print("5. read a note")
    print("6. exit")


def add_note():
    file_path = input("Enter name of your file like (.txt) in the end :")
    note = input("Enter your text : ")
    notes.append(f"{file_path}")
    try :
        with open(file_path, "w") as file:
            file.write(note)
            print(f"txt file '{file_path}' was created ")
    except FileExistsError:
        print("That file is already exist")


def edit_note():
    note = input("Enter what do you wanna no add: ")
    file_path = input("enter a file path : ")

    if not os.path.exists(file_path):
        print("File not found")
        return

    try :
        with open(file_path,"a") as file:
            for i in note:
                file.write(i + "")
            print("File was edited")
    except FileExistsError:
        print("That file is already exist")


def delete_note():
    view_note()
    file_path = input("Enter what note i should delete :")

    if os.path.exists(file_path):
        os.remove(file_path)
        notes.remove(file_path)
        print("Notes is deleted ")
    else:
        print("Note is not found ")

def view_note():
    if not notes:
        print("Notes are  empty")
    for i in notes:
        print(i)


def read_note():
    view_note()
    file_path = input("Enter file name: ")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            print(file.read())

while True:
    show_menu()
    try:
        choice = int(input("Choose an option (1-6): "))
    except ValueError:
        print("Please enter a number !")
        continue

    if choice ==  1:
        add_note()
    elif choice == 2:
        edit_note()
    elif choice == 3:
        view_note()
    elif choice == 4:
        delete_note()
    elif choice == 5:
        read_note()
    elif choice == 6:
        break
    else : print("Enter a valid number ")











