
team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def repr_players(players: list[dict], sorted: bool, key="number") -> None:
    print("TEAM:")
    if sorted:
        players_list = __builtins__.sorted(players, key=lambda x: x[key])
    else:
        players_list = players
    for player in players_list:
        print(f"\t{player['number']} " f"Name: {player['name']}, Age: {player['age']}")
    print("\n")


def log(message: str) -> None:
    print(f"{message}")


def add_player(num: int, name: str, age: int) -> None:
    if not any(player["number"] == num for player in team):
        player = {"name": name, "age": age, "number": num}
        team.append(player)
        log(message=f"Adding {player['name']}")
    else:
        print(f"\nThere is already a player with {num} number. "
              f"Duplicate numbers are not allowed.\n")


def remove_player(players: list[dict], num: int) -> None:
    for index, player in enumerate(players):
        if player["number"] == num:
            player_name = player["name"]
            del players[index]
            log(message=f"Deleting {player_name}")


def player_update(num: int, name: str, age: int):
    data = {"name": name, "age": age, "number": num}
    for index, player in enumerate(team):
        if player["number"] == num:
            team.insert(index, data)
            team.pop(index + 1)


def main():
    # repr_players(team, sorted=True)
    add_player(num=8, name="Cris", age=31)
    add_player(num=8, name="Bob", age=39)
    player_update(num=8, name="Hary", age=2)
    repr_players(team, sorted=True)


if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")
