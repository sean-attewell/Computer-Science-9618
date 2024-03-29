from sys import exit
from room import Room
from player import Player
from item import Item
from os import system, name

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Helmet", """An abandoned helmet, I wonder who it belonged to? """)]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Chainsaw", """this seems oddly out of place in this setting"""),
                                                         Item("MedKit", """Hopefully you wont be needing this"""), Item("BFG9000", """Seriously, was doom guy here?""")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Coins", """Gold peices that look like they were dropped in a hurry""")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("EmptyChest", """Maybe you could upcycle this into a coffee table""")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#


def clearScreen():

    if name == "nt":
        _ = system('cls')
    else:
        _ = system('clear')

    # name == "nt" means that the operating system (“os”) is a microsoft
    # operating system of the NT lineage, such as windows
    # 10 or windows 7 (or windows NT), as distinct from the
    # older dos and semi-dos windows systems such as
    # windows 3.1 or windows 95 (and also distinct from other
    # operating systems such as (old) mac and various flavors
    # of unix).

# Make a new player object that is currently in the 'outside' room.
clearScreen()
print("\n\n*****************************************************************************")
print(
    "**************** T H O R B E N ' S    D U N G E O N *************************")
print("*****************************************************************************\n")
print("\n~sPooKy MuSic plAys~\n\n")

print("""Welcome to Thorben's Dungeon!""")
new_name = input("Please enter your name > ")

p = Player(new_name, room["outside"], [
           Item("Letter", """A reminder of home""")])

input(f"If ye dare enter, {p.name} ... press enter > ")
clearScreen()

playerOptions = {
    "n": "North",
    "e": "East",
    "s": "South",
    "w": "West",
    "i": "Check inventory",
    "l": "Look for items",
    "t": "Take item",
    "d": "Drop item",
    "q": "Quit"
}
selection = ""

# While we have not selected Quit
# +1 because we added quit
while selection != "q":

    print(p.current_room, "\n\n")

    selection = input(
        "### ACTIONS ###\nMove north, south, east or west: n, s, e, w\nCheck inventory: i\nLook for items: l\nTake item: t [item]\nDrop item: d [item]\nQuit Game: q\n\n> ").split(" ")
    if len(selection) == 1:
        verb = selection[0]
    elif len(selection) == 2:
        verb = selection[0]
        item = selection[1]
        # TODO: Allow for items with space in the name
    else:
        verb = ''
    # error handler using try
    try:
        # if the user input something not in the playerOptions dict, we'll hit a KeyError immediately, which is safely handled below
        move_choice = f"\033[0;32mYou moved to the {playerOptions[verb]}.\033[0m\n"

        if verb == "n":
            p.current_room = p.current_room.n_to
            clearScreen()
            print(move_choice)

        elif verb == "e":
            p.current_room = p.current_room.e_to
            clearScreen()
            print(move_choice)

        elif verb == "s":
            p.current_room = p.current_room.s_to
            clearScreen()
            print(move_choice)

        elif verb == "w":
            p.current_room = p.current_room.w_to
            clearScreen()
            print(move_choice)

        elif verb == "i":
            clearScreen()
            p.listInventory()

        elif verb == "l":
            clearScreen()
            p.current_room.listItems()

        elif verb == "t":
            clearScreen()
            itemsFound = 0
            for i in p.current_room.items_in_room:
                if (i.name == item):
                    itemsFound += 1
                    p.current_room.removeItem(i)
                    p.addItem(i)
                    i.onTake()
            if itemsFound > 0:
                pass
            else:
                print(f"\033[31mThere is no {item} to take\033[m\n")

        elif verb == "d":
            clearScreen()
            itemsFound = 0
            for i in p.inventory:
                if (i.name == item):
                    itemsFound += 1
                    p.removeItem(i)
                    p.current_room.addItem(i)
                    i.onDrop()
            if itemsFound > 0:
                pass
            else:
                print(f"\033[31mYou do not have a {item} to drop\033[m\n")
        else:
            clearScreen()
            print("GAME OVER\n\nThank you for playing!\n")
            exit(1)
    except AttributeError:
        # For example if you try and go south but there is no south path, then
        # p.current_room will not have a '.s_to' attribute
        clearScreen()
        print(
            "\033[31mThere is no way through in that direction, please try again.\033[m\n")
    except KeyError:
        # When you try to access a key that is not in the dictionary, a KeyError is raised
        clearScreen()
        print(
            "\033[31mInvalid selection, Please choose from the options provided.\033[m\n")
