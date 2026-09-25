import math
import random

# Exercise 1
def roll_dice():
    return random.randint(1, 6)


result = 0
while result != 6:
    result = roll_dice()
    print(result)


# Exercise2
def roll_custom_dice(sides):
    return random.randint(1, sides)


sides = int(input("Enter the number of sides: "))
if sides > 0:
    result = 0
    while result != sides:
        result = roll_custom_dice(sides)
        print(result)
else:
    print("The number of sides must be positive.")


# Exercise 3
def gallons_to_liters(gallons):
    return gallons * 3.78541


gallons = float(input("Enter US gallons (negative to quit): "))
while gallons >= 0:
    print("Liters:", gallons_to_liters(gallons))
    gallons = float(input("Enter US gallons (negative to quit): "))


# Exercise 4
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


numbers = [2, 5, 8, 11]
print("Sum:", sum_numbers(numbers))


# Exercise 5
def remove_odd_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


numbers = [1, 2, 3, 4, 5, 6]
print("Original list:", numbers)
print("Even numbers:", remove_odd_numbers(numbers))


# Exercise 6
def pizza_unit_price(diameter, price):
    radius_meters = diameter / 200
    area = math.pi * radius_meters ** 2
    return price / area


diameter1 = float(input("First pizza diameter in cm: "))
price1 = float(input("First pizza price in euros: "))
diameter2 = float(input("Second pizza diameter in cm: "))
price2 = float(input("Second pizza price in euros: "))

if diameter1 > 0 and diameter2 > 0:
    unit_price1 = pizza_unit_price(diameter1, price1)
    unit_price2 = pizza_unit_price(diameter2, price2)
    print("First pizza euros per square meter:", unit_price1)
    print("Second pizza euros per square meter:", unit_price2)
    if unit_price1 < unit_price2:
        print("The first pizza provides better value.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value.")
    else:
        print("Both pizzas provide equal value.")
else:
    print("Pizza diameters must be positive.")
