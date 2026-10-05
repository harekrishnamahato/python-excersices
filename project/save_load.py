import json
from game import Item, Player


def save_game(player, rooms, filename):
    items = []
    for item in player.items:
        items.append({"name": item.name, "weight": item.weight})

    room_data = []
    for room in rooms:
        item_data = None
        if room.item != None:
            item_data = {"name": room.item.name, "weight": room.item.weight}
        room_data.append({"name": room.name, "item": item_data})

    data = {
        "name": player.name,
        "age": player.age,
        "location": player.location.name,
        "items": items,
        "rooms": room_data
    }

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError:
        print("The game could not be saved.")
        return False

    print("Game saved.")
    return True


def load_game(rooms, filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        location = None
        for room in rooms:
            if room.name == data["location"]:
                location = room

        if location == None or int(data["age"]) < 12:
            raise ValueError

        player = Player(data["name"], int(data["age"]), location)
        for item in data["items"]:
            player.items.append(Item(item["name"], float(item["weight"])))

        if len(data["rooms"]) != len(rooms):
            raise ValueError

        room_items = []
        for index in range(len(rooms)):
            saved_room = data["rooms"][index]
            if saved_room["name"] != rooms[index].name:
                raise ValueError
            item = None
            if saved_room["item"] != None:
                item = Item(saved_room["item"]["name"],
                            float(saved_room["item"]["weight"]))
            room_items.append(item)

    except FileNotFoundError:
        print("No saved game was found.")
        return None
    except (ValueError, KeyError, TypeError, IndexError, UnicodeError):
        print("The saved game is not valid.")
        return None
    except OSError:
        print("The saved game could not be read.")
        return None

    for index in range(len(rooms)):
        rooms[index].item = room_items[index]

    print("Game loaded.")
    return player
