import random

dice1 = dice2 = dice3 = roll = 0

while dice1 != 6 or dice2 != 6:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print (dice1 , dice2)

    roll = roll + 1

print("Rolled", roll, "times.")