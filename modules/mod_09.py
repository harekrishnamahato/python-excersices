import random


# Exercises 1-3:the Car class is extended with accelerate and drive.
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


if __name__ == "__main__":
    # Exercise 1
    car = Car("ABC-123", 142)
    print("Registration number:", car.registration_number)
    print("Maximum speed:", car.maximum_speed)
    print("Current speed:", car.current_speed)
    print("Travelled distance:", car.travelled_distance)

    # Exercise 2
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print("Speed after acceleration:", car.current_speed)
    car.accelerate(-200)
    print("Speed after emergency brake:", car.current_speed)

    # Exercise 3
    car.travelled_distance = 2000
    car.accelerate(60)
    car.drive(1.5)
    print("Distance after driving:", car.travelled_distance)

    # Exercise 4
    cars = []
    for number in range(1, 11):
        cars.append(Car(f"ABC-{number}", random.randint(100, 200)))

    finished = False
    while not finished:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.travelled_distance >= 10000:
                finished = True

    print(f"{'Registration':<15}{'Max km/h':>10}{'Speed km/h':>12}{'Distance km':>14}")
    for car in cars:
        print(f"{car.registration_number:<15}{car.maximum_speed:>10}"
              f"{car.current_speed:>12}{car.travelled_distance:>14.1f}")
