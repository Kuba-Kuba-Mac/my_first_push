players = []


def show_menu():
    print("1. Add a player ")
    print("2. Show all players")
    print("3. Find best bambardir ")
    print("4. Show top 3 scorers")
    print("5. Edit player stats")
    print("6. Delete player")
    print("7. Save to file")
    print("8. all avarage status ")
    print("9. quiet ")


def add_player():
    name = input("Enter a player name: ")
    try:
        point = int(input("Number of points: "))
    except ValueError:
        print("Please enter a number")

    try:
        assists = int(input("Number of assists :"))
    except ValueError:
        print("Please enter a number")

    try:
        rebounds = int(input("Number of rebounds :"))
    except ValueError:
        print("Please enter a number")

    players.append({"name": name, "point": point, "assists": assists, "rebounds": rebounds})
    print("Player added successfully!")


def view_all_players():
    print("-------------------------------------------")
    if not players:
        print("There is no players")
        return
    print("Your players ")
    for i, people in enumerate(players, start=1):
        print(f"{i}  {people['name']} {people['point']} {people['assists']} {people['rebounds']} ")
    print("-------------------------------------------")


def find_best():
    best_player = max(players, key=lambda player: player["point"])
    print("-------------------------------------------")
    print(f"Best scorer: {best_player['name']}")
    print("-------------------------------------------")


def show_tops():
    sorted_players = sorted(
        players,
        key=lambda player: player["point"],
        reverse=True
    )
    print("-------------------------------------------")
    for player in sorted_players[:3]:
        print(player["name"], player["point"])
    print("-------------------------------------------")


def edit():
    if not players:
        print("There is no players")
        return
    names = input("Enter who's stats do u wont to edit :")
    for i , player in enumerate(players,start=1):
        if names in  player['name']:
            p = int(input("Enter new stats :"))
            a = int(input("Enter new stats :"))
            r = int(input("Enter new stats :"))
            player['point'] = p
            player['assists'] = a
            player['rebounds'] = r
            print("-------------------------------------------")
            print(f"{names} stats successfully edited")
            print("-------------------------------------------")
            break


def delete():
    view_all_players()

    if not players:
        return

    try:
        index = int(input("Enter player index to delete: ")) - 1
        if 0 <= index < len(players):
            deleted_player = players.pop(index)
            print(f"{deleted_player['name']} was successfully deleted")
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter a valid number")

def save_all():
    with open("all_players.txt", "w") as file:
        for player in players:
            file.write(f"{player['name']} {player['point']} {player['assists']} {player['rebounds']}\n")
    print("Datas are saved")

def all_stats():
    p = 0
    a = 0
    r = 0
    for player in players:
        p += player['point']
        a += player['assists']
        r += player['rebounds']

    print(f"Players avarage point {p/len(players)}")
    print(f"Players avarage assists  {a / len(players)}")
    print(f"Players avarage rebounds {r / len(players)}")

while True:
    show_menu()
    choice = int(input("Choose options (1-9) :"))
    if choice == 1:
        add_player()
    elif choice == 2:
        view_all_players()
    elif choice == 3:
        find_best()
    elif choice == 4:
        show_tops()
    elif choice == 5:
        edit()
    elif choice == 6:
        delete()
    elif choice == 7:
        save_all()
    elif choice == 8:
        all_stats()
    elif choice == 9:
        print("Goodbye")
        break
    else:
        print("Please enter a valid number")
