# Exercise 1
length = float(input("Enter the length of the zander in cm: "))
if length < 42:
    print("Release the fish back into the lake.")
    print("Centimeters below the size limit:", 42 - length)
else:
    print("The fish meets the size limit.")

# Exercise 2
cabin = input("Enter the cabin class: ").upper()
if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

# Exercise 3: ranges given in the assignment.
gender = input("Enter biological gender (female/male): ").lower()
hemoglobin = float(input("Enter hemoglobin in g/l: "))
if gender == "female":
    if hemoglobin < 117:
        print("Low")
    elif hemoglobin <= 155:
        print("Normal")
    else:
        print("High")
elif gender == "male":
    if hemoglobin < 134:
        print("Low")
    elif hemoglobin <= 167:
        print("Normal")
    else:
        print("High")
else:
    print("Invalid gender")

# Exercise 4
year = int(input("Enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
