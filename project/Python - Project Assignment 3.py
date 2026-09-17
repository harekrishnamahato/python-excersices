def add_item(inventory):
    item = input("Enter an item to add: ")
    inventory.append(item)
    print(item, "was added to your inventory.")


def show_inventory(inventory):
    print("Inventory:")
    for item in inventory:
        print("-", item)


def look_around():
    print("You look around. The room is quiet.")


name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 12:
    print("You are a minor. The game will shut down.")
else:
    print("Welcome to the game,", name)

    inventory = []
    command = ""

    while command != "lopeta":
        print()
        print("Main menu")
        print("- add")
        print("- inventory")
        print("- look")
        print("- lopeta")

        command = input("Enter command: ")

        if command == "add":
            add_item(inventory)
        elif command == "inventory":
            show_inventory(inventory)
        elif command == "look":
            look_around()
        elif command == "lopeta":
            print("Game ended.")
        else:
            print("Unknown command.")
