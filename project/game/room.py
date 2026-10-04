class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
        self.neighbours = []
