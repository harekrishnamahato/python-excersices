import random
from mod_09 import Car


# Exercise 1
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print("Floor:", self.current_floor)

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print("Floor:", self.current_floor)

    def go_to_floor(self, destination):
        if destination < self.bottom_floor or destination > self.top_floor:
            print("Invalid floor")
            return
        while self.current_floor < destination:
            self.floor_up()
        while self.current_floor > destination:
            self.floor_down()


# Exercises2-3
class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.elevators = []
        for number in range(elevator_count):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, destination):
        # Elevator numbers start at 1; list indexes start at 0.
        if 1 <= elevator_number <= len(self.elevators):
            self.elevators[elevator_number - 1].go_to_floor(destination)
        else:
            print("Invalid elevator number")

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)


# Exercise 4
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(self.name)
        print(f"{'Registration':<15}{'Max km/h':>10}{'Speed km/h':>12}{'Distance km':>14}")
        for car in self.cars:
            print(f"{car.registration_number:<15}{car.maximum_speed:>10}"
                  f"{car.current_speed:>12}{car.travelled_distance:>14.1f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


if __name__ == "__main__":
    # Exercise 1
    elevator = Elevator(0, 10)
    elevator.go_to_floor(5)
    elevator.go_to_floor(0)

    # Exercise 2
    building = Building(0, 10, 3)
    building.run_elevator(1, 5)
    building.run_elevator(2, 8)
    building.run_elevator(3, 3)

    # Exercise 3
    print("Fire alarm")
    building.fire_alarm()

    # Exercise 4
    cars = []
    for number in range(1, 11):
        cars.append(Car(f"ABC-{number}", random.randint(100, 200)))
    race = Race("Grand Demolition Derby", 8000, cars)
    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            print("Hours:", hours)
            race.print_status()
    print("Final results after", hours, "hours")
    race.print_status()
