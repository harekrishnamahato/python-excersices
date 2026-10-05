def show_menu(file_commands=False):
    print()
    print("Main menu")
    print("- katso: look around")
    print("- kartta: show the map")
    print("- laukku: show your inventory")
    print("- keraa: collect an item")
    print("- liiku: move to another room")
    print("- lepaa: rest")
    if file_commands:
        print("- tallenna: save game")
        print("- lataa: load game")
    print("- lopeta: quit")
    print()


def look_around(player):
    print("Your location:", player.location.name)
    print(player.location.description)
    if player.location.item != None:
        print("You see:", player.location.item.name)
    else:
        print("There is no item here.")
    print("You can move to:")
    for room in player.location.neighbours:
        print("-", room.name)


def show_map(rooms):
    print("Map connections:")
    for room in rooms:
        print(room.name + ":")
        for neighbour in room.neighbours:
            print("-", neighbour.name)


def show_inventory(items):
    if len(items) == 0:
        print("Your bag is empty.")
    else:
        print("Your bag contains:")
        total_weight = 0
        for item in items:
            print(item.name, "-", item.weight, "kg")
            total_weight = total_weight + item.weight
        print("Total weight:", total_weight, "kg")


def collect_item(player):
    if player.location.item != None:
        print("Item available:", player.location.item.name)
        item_name = input("Enter the item name to collect it: ")
        if item_name == player.location.item.name:
            if player.collect_item():
                print("Added to your bag:", item_name)
        else:
            print("That item is not here.")
    else:
        print("There is no item to collect here.")


def move_player(player):
    print("You can move to:")
    for room in player.location.neighbours:
        print("-", room.name)

    destination_name = input("Enter the room name: ")
    moved = False
    for room in player.location.neighbours:
        if room.name == destination_name:
            moved = player.move(room)

    if moved:
        print("You moved to", player.location.name)
    else:
        print("You cannot move to that room from here.")


def rest():
    print("You rest for a moment beside the path.")
