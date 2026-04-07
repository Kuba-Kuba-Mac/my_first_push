contacts =[]
def show_manu():
     print("---Contacts manu---")
     print("1. add contact")
     print("2. delete contact")
     print("3. search contact")
     print("4. view contacts")
     print("5. Exit")


def contact_add():
    name = input("Enter your contact: ")
    number = int(input("Enter contacts number :"))
    contacts.append({"contact": name,"number":number})
    print(f"Contact {name} is added")

def contact_delete():
    contact_view()
    if not contacts:
        print("No contact added")
        return
    try:
        index = int(input("Enter contact index to delete :"))-1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Contact {removed['contact']} is deleted ")
        else : print("invalid number ")
    except ValueError:
        print("please enter a valid number")

def contact_view():
    if not contacts:
        print("No contact added")
        return
    for i , name ,in enumerate(contacts,start=1):
        print(f"{i} {name}")



def contact_search():
    if not contacts:
        print("No contact added")
        return

    keyword = input("Enter a contact's name: ")
    found = False

    for i, contact in enumerate(contacts, start=1):
        if keyword.lower() in contact["contact"].lower():
            print(f"Your contact is found  {contact['contact']} - {contact['number']}")
            found = True

    if not found:
        print("Your contact is not found!!!")


while True:
    show_manu()
    choice = int(input("Choose an option (1-5) :"))

    if choice == 1:
        contact_add()
    elif choice == 2:
        contact_delete()
    elif choice == 3:
        contact_search()
    elif choice == 4:
        contact_view()
    elif choice == 5:
        print("Goodbye!!!")
        break
    else :
        print("Please enter a valid number")


