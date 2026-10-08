def show_menu():
    print("\nMain menu")
    print("dekho - Look around")
    print("naksha - Show map")
    print("jhola - Show bag")
    print("uthao - Collect item")
    print("chalo - Move")
    print("madad - Help nature")
    print("sambhalo - Save")
    print("kholo - Load")
    print("band - Quit")

def look_around(player):
    room = player.location
    print("\nLocation:", room.name)
    print(room.description)
    if room.item != None:
        print("Item:", room.item)
    print("You can move to:")
    for neighbour in room.neighbours:
        print("-", neighbour.name)

def show_map(rooms):
    for room in rooms:
        print(room.name + ":")
        for neighbour in room.neighbours:
            print("-", neighbour.name)

def show_inventory(player):
    if len(player.items) == 0:
        print("Your bag is empty.")
    else:
        for item in player.items:
            print("-", item)

def collect_item(player):
    item = player.location.item
    if item == None:
        print("There is no item here.")
        return
    print("Available item:", item)
    name = input("Item to collect: ").strip().lower()
    if name == item:
        if player.collect():
            print("Collected:", item)
    else:
        print("That item is not here.")

def move_player(player):
    for room in player.location.neighbours:
        print("-", room.name)
    name = input("Go to: ").strip().lower()
    for room in player.location.neighbours:
        if room.name == name:
            if player.move(room):
                look_around(player)
            return
    print("You cannot go there from here.")

def help_nature(player):
    place = player.location.name
    if place == "forest":
        if "seedlings" in player.items and "water" in player.items:
            print("You plant and water new trees. The forest can grow again!")
            return True
        print("You need seedlings and water.")
    elif place == "river":
        if "rubbish bag" in player.items:
            print("You collect the litter. The riverbank is clean again!")
            return True
        print("You need a rubbish bag.")
    elif place == "castle":
        if "small key" in player.items and "water" in player.items:
            print("You unlock the garden and water the plants. They can grow!")
            return True
        print("You need a small key and water.")
    else:
        print("Visit the forest, river or castle to help nature.")
    return False
