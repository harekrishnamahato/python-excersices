import json
import os
from game import Player

def save_game(player, rooms):
    room_items = {}
    for room in rooms:
        room_items[room.name] = room.item
    data = {
        "name": player.name,
        "age": player.age,
        "location": player.location.name,
        "items": player.items,
        "room_items": room_items
    }
    with open("save.json", "w") as file:
        json.dump(data, file)
    print("Game saved.")

def load_game(rooms):
    if os.path.exists("save.json") == False:
        print("No saved game found.")
        return None
    with open("save.json", "r") as file:
        data = json.load(file)
    location = None
    for room in rooms:
        if room.name == data["location"]:
            location = room
    if location == None or data["age"] < 12:
        print("Invalid saved game.")
        return None
    player = Player(data["name"], data["age"], location)
    player.items = data["items"]
    for room in rooms:
        room.item = data["room_items"][room.name]
    print("Game loaded.")
    return player
