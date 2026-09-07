


def average(numbers):
    return sum(numbers) / len(numbers)

numbers = []

amount = int(input("How many numbers? "))
for i in range(amount):
    number = float(input("Enter a number: "))
    numbers.append(number)

result = average(numbers)
print(result)