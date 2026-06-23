expenses  = []
def show_menu():
    print("---Expense collection software---")
    print("1. add expense")
    print("2. view all expenses ")
    print("3. sum of all expenses ")
    print("4. save in files ")
    print("5. out")

def add_expense():
    name  = input("Enter expense name:")
    sum1 = int(input("Enter a cost:"))
    expenses.append({"name":name,"cost":sum1})
    print(f"{name} is add")

def view_expense():
    print("-------------------------------------------")
    if not expenses:
        print("There is no expenses")
        return
    print("Your expenses ")
    for i, x in enumerate(expenses,start=1):
        print(f"{x['name']} prise was {x['cost']}$")
    print("-------------------------------------------")

def count_all():
    cnt = 0
    for item in expenses:
        cnt += item['cost']
    print(f"All expenses is {cnt}")

def save_all():
    with open("expenses.txt", "a") as file:
        for item in expenses:
            file.write(f"{item['name']} {item['cost']}\n")
    print("Datas are saved")

while True:
    show_menu()
    choice = int(input("Choose options (1-5) :"))
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expense()
    elif choice == 3:
        count_all()
    elif choice == 4:
        save_all()
    elif choice == 5:
        print("Goodbye")
        break
    else :
        print("Please enter a valid number")
