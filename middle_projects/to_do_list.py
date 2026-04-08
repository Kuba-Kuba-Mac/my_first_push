tasks = []
cnt = 0

def show_manu():
    print("---to do list functions ---")
    print("1. add task")
    print("2. View tasks")
    print("3. mark task as done ")
    print("4. delete task")
    print("5. Exit")


def add_tasks():
    task = input("Enter task: ")
    tasks.append({"task":task,"done":False})
    print(f"Task {task} added !")


def view_task() :
    if not tasks:
        print("No tasks added")
        return
    print("\nYour tasks")
    for i ,task in enumerate(tasks,start=1):
        status = "done" if task["done"] else "Not done"
        print(f"{i} {task} {status}")


def mark_down():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark done: "))-1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Marked is done")
        else :
            print("invalid number")
    except ValueError:
        print("Please enter a valid number ")


def delete_tasks():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete :")) -1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task '{removed["task"]}'")
        else : print("Invalid number")

    except ValueError:
        print("Please enter a valid number")


while True:
    show_manu()
    choice = int(input("Choose an option (1-5) :"))

    if choice == 1:
        add_tasks()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_down()
    elif choice == 4:
        delete_tasks()
    elif choice == 5:
        print("Goodbye!!!")
        break
    else :
        print("Please enter a valid number")



