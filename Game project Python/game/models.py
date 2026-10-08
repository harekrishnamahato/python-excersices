class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
        self.neighbours = []

class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.items = []

    def move(self, room):
        if room in self.location.neighbours:
            self.location = room
            return True
        return False

    def collect(self):
        if self.location.item != None:
            self.items.append(self.location.item)
            self.location.item = None
            return True
        return False
