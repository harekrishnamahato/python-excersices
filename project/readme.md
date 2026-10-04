# The World's Most Serious Game

Harekrishna Mahato

## Game idea

Explore a village, forest, river, and old castle. Your current objective is to
collect useful supplies to prepare for restoring the forest and cleaning the
river. The theme relates to Sustainable Development Goals 6 (Clean Water and
Sanitation) and 15 (Life on Land). The story is suitable for players aged 12
and above.

This version completes Project tasks 1-4. It is an early version of the game:
restoration actions, winning endings, and saving/loading are not implemented yet.

## Running the game

Open `Python - Project Assignment 4.py` in this folder and run it with Python, or run:

```text
python "project/Python - Project Assignment 4.py"
```

The command above assumes your terminal is in the parent folder. If the
terminal is already in `project`, use `python "Python - Project Assignment 4.py"`.
No extra libraries are needed. Enter your age as a whole number.
Players under 12 see a message and the program ends.

## Commands

Type commands, room names, and item names exactly as displayed in lowercase.

| Command | Action |
| --- | --- |
| `katso` | Show the current room, its item, and connected rooms. |
| `kartta` | Show all rooms and their connections. |
| `laukku` | Print the inventory and total item weight. |
| `keraa` | Ask for an item name and add that room's item to the inventory. |
| `liiku` | Ask for a connected room name and move there. |
| `lepaa` | Print a resting message. |
| `lopeta` | End the game. |

An item can be collected only once. Each room has at most one item.
The main menu is displayed again after each action until the player quits.

## File structure

```text
project/
    Python - Project Assignment 4.py
    actions.py
    readme.md
    game/
        __init__.py
        item.py
        player.py
        room.py
```

- `Python - Project Assignment 4.py`: asks for name and age, creates the game objects, and runs the menu loop.
- `actions.py`: contains separate functions for menu actions.
- `game/__init__.py`: makes `game` a package and exports the three classes.
- `game/item.py`: defines Item with a name and weight.
- `game/player.py`: defines Player with name, age, inventory, and current room;
  its methods move the player and collect the current room's item.
- `game/room.py`: defines Room with a name, description, optional item, and
  a list of connected rooms.

## Project tasks and course concepts

1. **Project 1:** project folder, game heading and author, name and age inputs,
   variables, and printing both values (module 3).
2. **Project 2:** age check, `if/elif/else`, a `while` menu loop, different commands,
   and quitting with `lopeta` (modules 4-5).
3. **Project 3:** separate action functions, asking for an item to add to a list,
   and printing the list with a `for` loop (modules 6-7).
4. **Project 4:** classes, initializers, methods, objects referring to other objects,
   and dividing the program into modules and a package (modules 9-10 and 12).

The code uses the course's list, function, class, and package patterns.
There are no external libraries or advanced Python features.

