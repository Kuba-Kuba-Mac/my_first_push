import json

players = []


def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number")


def show_menu():
    print("\n===== Basketball Statistics Manager =====")
    print("1. Add player")
    print("2. Show all players")
    print("3. Best scorer")
    print("4. Top 3 scorers")
    print("5. Edit player")
    print("6. Delete player")
    print("7. Save to file")
    print("8. Load from file")
    print("9. Average statistics")
    print("10. Best assister")
    print("11. Best rebounder")
    print("12. Search player")
    print("13. Exit")


def add_player():
    name = input("Player name: ")

    point = get_number("Points: ")
    assists = get_number("Assists: ")
    rebounds = get_number("Rebounds: ")

    players.append({
        "name": name,
        "point": point,
        "assists": assists,
        "rebounds": rebounds
    })

    print("Player added successfully!")


def view_all_players():
    if not players:
        print("No players found.")
        return

    print("\n----- PLAYERS -----")

    for i, player in enumerate(players, start=1):
        print(
            f"{i}. {player['name']} | "
            f"PTS: {player['point']} | "
            f"AST: {player['assists']} | "
            f"REB: {player['rebounds']}"
        )


def best_scorer():
    if not players:
        print("No players found.")
        return

    best = max(players, key=lambda p: p["point"])

    print("\nBest Scorer")
    print(f"{best['name']} - {best['point']} points")


def top_scorers():
    if not players:
        print("No players found.")
        return

    sorted_players = sorted(
        players,
        key=lambda p: p["point"],
        reverse=True
    )

    print("\nTop Scorers")

    for i, player in enumerate(sorted_players[:3], start=1):
        print(f"{i}. {player['name']} - {player['point']} pts")


def edit_player():
    if not players:
        print("No players found.")
        return

    name = input("Enter player name: ")

    for player in players:
        if player["name"].lower() == name.lower():

            print("Enter new stats")

            player["point"] = get_number("Points: ")
            player["assists"] = get_number("Assists: ")
            player["rebounds"] = get_number("Rebounds: ")

            print("Player updated successfully.")
            return

    print("Player not found.")


def delete_player():
    if not players:
        print("No players found.")
        return

    view_all_players()

    index = get_number("Enter player number: ") - 1

    if 0 <= index < len(players):
        removed = players.pop(index)
        print(f"{removed['name']} deleted.")
    else:
        print("Invalid number.")


def save_players():
    with open("players.json", "w") as file:
        json.dump(players, file, indent=4)

    print("Players saved.")


def load_players():
    global players

    try:
        with open("players.json", "r") as file:
            players = json.load(file)

        print("Players loaded.")

    except FileNotFoundError:
        print("players.json not found.")


def average_stats():
    if not players:
        print("No players found.")
        return

    total_points = sum(player["point"] for player in players)
    total_assists = sum(player["assists"] for player in players)
    total_rebounds = sum(player["rebounds"] for player in players)

    count = len(players)

    print("\nAverage Statistics")
    print(f"Points: {total_points / count:.2f}")
    print(f"Assists: {total_assists / count:.2f}")
    print(f"Rebounds: {total_rebounds / count:.2f}")


def best_assister():
    if not players:
        print("No players found.")
        return

    best = max(players, key=lambda p: p["assists"])

    print(
        f"Best Assister: "
        f"{best['name']} ({best['assists']} assists)"
    )


def best_rebounder():
    if not players:
        print("No players found.")
        return

    best = max(players, key=lambda p: p["rebounds"])

    print(
        f"Best Rebounder: "
        f"{best['name']} ({best['rebounds']} rebounds)"
    )


def search_player():
    if not players:
        print("No players found.")
        return

    name = input("Enter player name: ")

    for player in players:
        if player["name"].lower() == name.lower():

            print("\nPlayer Found")
            print(
                f"{player['name']} | "
                f"PTS: {player['point']} | "
                f"AST: {player['assists']} | "
                f"REB: {player['rebounds']}"
            )
            return

    print("Player not found.")


while True:

    show_menu()

    choice = get_number("Choose option: ")

    if choice == 1:
        add_player()

    elif choice == 2:
        view_all_players()

    elif choice == 3:
        best_scorer()

    elif choice == 4:
        top_scorers()

    elif choice == 5:
        edit_player()

    elif choice == 6:
        delete_player()

    elif choice == 7:
        save_players()

    elif choice == 8:
        load_players()

    elif choice == 9:
        average_stats()

    elif choice == 10:
        best_assister()

    elif choice == 11:
        best_rebounder()

    elif choice == 12:
        search_player()

    elif choice == 13:
        print("Goodbye!")
        break

    else:
        print("Invalid option.")