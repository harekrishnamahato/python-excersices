import random

# Exercise 1
dice_count = int(input("How many dice? "))
total = 0
for die in range(dice_count):
    total += random.randint(1, 6)
print("Sum of dice:", total)

# Exercise 2
numbers = []
text = input("Enter a number (empty to quit): ")
while text != "":
    numbers.append(float(text))
    text = input("Enter a number (empty to quit): ")
numbers.sort(reverse=True)
print("Five greatest numbers:")
for number in numbers[:5]:
    print(number)

# Exercise 3
number = int(input("Enter an integer: "))
is_prime = number >= 2
for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

# Exercise 4
cities = []
for count in range(5):
    city = input("Enter a city: ")
    cities.append(city)
for city in cities:
    print(city)
