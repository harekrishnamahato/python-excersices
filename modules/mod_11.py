from mod_09 import Car


# Exercise 1
class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print("Name:", self.name)
        print("Author:", self.author)
        print("Page count:", self.page_count)


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Name:", self.name)
        print("Chief editor:", self.chief_editor)


# Exercise 2
class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume


if __name__ == "__main__":
    # Exercise 1
    magazine = Magazine("Donald Duck", "Aki Hyypp\u00e4")
    book = Book("Compartment No. 6", "Rosa Liksom", 192)
    magazine.print_information()
    book.print_information()

    # Exercise 2
    electric = ElectricCar("ABC-15", 180, 52.5)
    gasoline = GasolineCar("ACD-123", 165, 32.3)
    electric.accelerate(100)
    gasoline.accelerate(80)
    electric.drive(3)
    gasoline.drive(3)
    print(electric.registration_number, "distance:", electric.travelled_distance, "km")
    print(gasoline.registration_number, "distance:", gasoline.travelled_distance, "km")
