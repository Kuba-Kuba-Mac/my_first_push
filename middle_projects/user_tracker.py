import datetime
tasks = []
tracker = []
cnt = 0
tracker.append(f"{datetime.datetime.now()} — Пользователь: запустил программу")
def show_manu():
    tracker.append("Пользователь: открыл меню ")
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
    tracker.append(f"{datetime.datetime.now()} — Пользователь добавил задачу: {task}")


def view_task() :
    if not tasks:
        print("No tasks added")
        return
    print("\nYour tasks")
    for i ,task in enumerate(tasks,start=1):
        status = "done" if task["done"] else "Not done"
        print(f"{i} {task} {status}")
    tracker.append(f"{datetime.datetime.now()} —  Пользователь:  посмотрел задачи")


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
    tracker.append(f"{datetime.datetime.now()} —  Пользователь:  отметил задачу")



def delete_tasks():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete :")) -1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task '{removed['task']}'")
        else : print("Invalid number")

    except ValueError:
        print("Please enter a valid number")
    tracker.append(f"{datetime.datetime.now()} —  Пользователь:  удалил  задачу")


while True:
    show_manu()
    try:
        choice = int(input("Choose an option (1-5): "))
    except ValueError:
        print("Введите число!")
        continue

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
        tracker.append(f"{datetime.datetime.now()} —  Пользователь: завершил  программу ")
        break
    else :
        print("Please enter a valid number")

for item in tracker:
    print(item)


with open("log.txt", "w") as f:
    for item in tracker:
        f.write(item + "\n")





