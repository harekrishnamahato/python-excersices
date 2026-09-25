import random

# Exercise 6: combination lock codes (strings preserve leading zeroes).
code_three = ""
for digit in range(3):
    code_three += str(random.randint(0, 9))

code_four = ""
for digit in range(4):
    code_four += str(random.randint(1, 6))

print("Three-digit code:", code_three)
print("Four-digit code:", code_four)
