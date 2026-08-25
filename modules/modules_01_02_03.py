age = int(input("entr age :  "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >= 18 or age >= 15 and weight >= 55):
    print("you are eligible to get the medicine "  +  "get well soon")
else: 
     print("Sorry you " \
     " are not  elible to get the medcicine")