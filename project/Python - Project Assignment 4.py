from game import Item, Player, Room
from actions import show_menu, look_around, show_map, show_inventory
from actions import collect_item, move_player, rest


def create_rooms():
    # Each room contains one item at most.
    village = Room("village", "A quiet village beside a damaged forest.",
                   Item("water", 1.0))
    forest = Room("forest", "A forest path where new trees are needed.",
                  Item("seedlings", 0.5))
    river = Room("river", "A river with litter along its banks.",
                 Item("rubbish bag", 0.1))
    castle = Room("castle", "An old castle with a forgotten garden.",
                  Item("small key", 0.1))

    # Neighbours are Room objects, stored in lists.
    village.neighbours = [forest, river]
    forest.neighbours = [village, castle]
    river.neighbours = [village, castle]
    castle.neighbours = [forest, river]

    return [village, forest, river, castle]


def main():
    player_name = input("Enter your name: ")
    player_age = int(input("Enter your age: "))
    print("Player name:", player_name)
    print("Player age:", player_age)

    if player_age < 12:
        print("You are a minor. The game will shut down.")
    else:
        rooms = create_rooms()
        player = Player(player_name, player_age, rooms[0])

        print("Welcome", player.name + "!")
        print("Your adventure begins now.")
        print("Prepare to restore the forest and clean the river.")
        print("Explore the rooms and collect useful supplies.")

        command = ""
        while command != "lopeta":
            show_menu()
            command = input("Enter command: ")

            if command == "katso":
                look_around(player)
            elif command == "kartta":
                show_map(rooms)
            elif command == "laukku":
                show_inventory(player.items)
            elif command == "keraa":
                collect_item(player)
            elif command == "liiku":
                move_player(player)
            elif command == "lepaa":
                rest()
            elif command == "lopeta":
                print("Thanks for playing.")
            else:
                print("Unknown command.")

if __name__ == "__main__":
    main()
