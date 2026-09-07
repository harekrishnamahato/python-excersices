name = input("Brave human, what is your name? ")
age = int(input("And how many years have you survived so far? "))
if age < 12:
    print("Sorry tiny legend, you are a minor. The game is shutting down.")
else:
    print("Welcome to the game,", name)
    print("Try not to press buttons like a confused potato.")
    command = ""
    while command != "lopeta":
        print()
        print("Main menu of questionable life choices")
        print("Commands:")
        print("snoop")
        print("snacks")
        print("door")
        print("lopeta")
        print()
        command = input("What now, genius? ")
        if command == "snoop":
            print("You look around dramatically. Nothing looks impressed.")
        elif command == "snacks":
            print("You check your bag. Emergency snacks are safe.")
        elif command == "door":
            print("You open the door. It was unlocked the whole time.")
        elif command == "lopeta":
            print("Game ended. Humanity survives another day.")
        else:
            print("Unknown command. The game judges you silently.")