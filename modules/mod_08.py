# Exercise 1
seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Enter the month number: "))
if 1 <= month <= 12:
    print(seasons[(month % 12) // 3])
else:
    print("Invalid month")

# Exercise 2
names = set()
name = input("Enter a name (empty to quit): ")
while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    name = input("Enter a name (empty to quit): ")
for name in names:
    print(name)

# Exercise 3
airports = {}
command = ""
while command != "quit":
    command = input("Enter new, fetch or quit: ").lower()
    if command == "new":
        code = input("ICAO code: ").upper()
        name = input("Airport name: ")
        airports[code] = name
    elif command == "fetch":
        code = input("ICAO code: ").upper()
        if code in airports:
            print(airports[code])
        else:
            print("Airport not found.")
    elif command != "quit":
        print("Invalid command")
