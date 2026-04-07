def chat():
    print("Simple Chat (type 'exit' to stop)")

    while True:
        user1 = input("User1: ")
        if user1 == "exit":
            break

        user2 = input("User2: ")
        if user2 == "exit":
            break

chat()