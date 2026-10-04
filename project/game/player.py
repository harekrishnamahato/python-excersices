class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.items = []
        self.location = location

    def move(self, destination):
        # Only rooms connected to the current room can be reached.
        if destination in self.location.neighbours:
            self.location = destination
            return True
        return False

    def collect_item(self):
        if self.location.item != None:
            self.items.append(self.location.item)
            # Remove the item from the room so it cannot be taken twice.
            self.location.item = None
            return True
        return False
