import random

# Exercise 1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

# Exercise 2
inches = float(input("Enter inches (negative to quit): "))
while inches >= 0:
    print("Centimeters:", inches * 2.54)
    inches = float(input("Enter inches (negative to quit): "))

# Exercise 3
smallest = None
largest = None
text = input("Enter a number (empty to quit): ")
while text != "":
    number = float(text)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
    text = input("Enter a number (empty to quit): ")

if smallest is None:
    print("No numbers entered.")
else:
    print("Smallest:", smallest)
    print("Largest:", largest)

# Exercise 4
secret = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))
while guess != secret:
    if guess > secret:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess again: "))
print("Correct")

# Exercise 5
attempts = 0
logged_in = False
while attempts < 5 and not logged_in:
    username = input("Username: ")
    password = input("Password: ")
    if username == "python" and password == "rules":
        logged_in = True
    else:
        attempts += 1

if logged_in:
    print("Welcome")
else:
    print("Access denied")
# Exercise 6
total_points = int(input("How many random points? "))
if total_points > 0:
    inside = 0
    generated = 0
    while generated < total_points:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 < 1:
            inside += 1
        generated += 1
    print("Approximation of pi:", 4 * inside / total_points)
else:
    print("The number of points must be positive.")
