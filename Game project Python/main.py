from game import Room, Player
from actions import show_menu, look_around, show_map, show_inventory
from actions import collect_item, move_player, help_nature
from save_load import save_game, load_game

def create_rooms():
    village = Room("village", "A village beside a damaged forest.", "water")
    forest = Room("forest", "New trees are needed here.", "seedlings")
    river = Room("river", "There is litter along the riverbank.", "rubbish bag")
    castle = Room("castle", "The locked garden needs water.", "small key")

    village.neighbours = [forest, river]
    forest.neighbours = [village, castle]
    river.neighbours = [village, castle]
    castle.neighbours = [forest, river]
    return [village, forest, river, castle]

def read_age():
    age = int(input("Your age (whole number): "))
    return age

def main():
    print("Nature Adventure")
    print("By Harekrishna")
    name = input("Your name: ").strip()
    age = read_age()
    print("Player:", name)
    print("Age:", age)
    if age < 12:
        print("This game is for players aged 12 and above.")
        return

    rooms = create_rooms()
    player = Player(name, age, rooms[0])
    print("Welcome", name)
    print("Help nature by completing ONE of these tasks:")
    print("Plant trees in the forest, clean the river,")
    print("or restore the castle garden.")
    print("Collect supplies, then use madad at your chosen place.")
    look_around(player)

    command = ""
    won = False
    while command != "band" and won == False:
        show_menu()
        command = input("Command: ").strip().lower()
        if command == "dekho":
            look_around(player)
        elif command == "naksha":
            show_map(rooms)
        elif command == "jhola":
            show_inventory(player)
        elif command == "uthao":
            collect_item(player)
        elif command == "chalo":
            move_player(player)
        elif command == "madad":
            won = help_nature(player)
        elif command == "sambhalo":
            save_game(player, rooms)
        elif command == "kholo":
            loaded_player = load_game(rooms)
            if loaded_player != None:
                player = loaded_player
                look_around(player)
        elif command == "band":
            print("Thanks for playing.")
        else:
            print("Unknown command.")
    if won:
        print("You completed your mission. Well done", player.name + "!")

if __name__ == "__main__":
    main()
