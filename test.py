"""
This is the test suite for the game.

Current switch options for the game:
    "-r [roomname]" allows the player to specify the starting room

For example, to start in the solarium, type:

"python3 test.py -r solarium"

Features still to be implemented:
    - Adding items to Rooms
    - Adding items to Inventory
    - Changing Item 'action' status
"""

from Game import Game
import sys

rooms = ["solarium", "game room", "kitchen", "dining room", "bathroom", "library",
                     "foyer", "parlor", "porch", "cellar", "servant quarters", "crypt",
                     "servant's bathroom", "dark tunnel", "red room", "child's room", "pink room",
                     "art studio", "green room", "master's quarters", "landing", "linen closet",
                     "upstairs", "downstairs", "attic", "hidden room", "gardens", "gazebo",
                     "rose garden", "downstairs bathroom", "landing", "front lawns",
                     "upstairs bathroom"]

newGame = Game()
indexCount = 0
roomIdx = 0
startRoom = None
itemList = []


def getRoomIndex(inputRoom):
    if(inputRoom == "attic"):
        return 13
    if(inputRoom == "cellar"):
        return 14
    if(inputRoom == "crypt"):
        return 17
    if(inputRoom == "dining room"):
        return 6
    if(inputRoom == "downstairs bathroom"):
        return 5
    if(inputRoom == "foyer"):
        return 1
    if(inputRoom == "front lawns"):
        return 21
    if(inputRoom == "game room"):
        return 4
    if(inputRoom == "gazebo"):
        return 18
    if(inputRoom == "green room"):
        return 12
    if(inputRoom == "kitchen"):
        return 7
    if(inputRoom == "landing"):
        return 11
    if(inputRoom == "library"):
        return 2
    if(inputRoom == "linen closet"):
        return 8
    if(inputRoom == "parlor"):
        return 0
    if(inputRoom == "pink room"):
        return 10
    if(inputRoom == "porch"):
        return 20
    if(inputRoom == "red room"):
        return 9
    if(inputRoom == "rose garden"):
        return 19
    if(inputRoom == "servant bathroom"):
        return 16
    if(inputRoom == "servant quarters"):
        return 15
    if(inputRoom == "solarium"):
        return 3
    if(inputRoom == "upstairs bathroom"):
        return 22

# Loop through each argument, looking for the correct switch.
for i in sys.argv:
    stringBuilder = ""

    "-r switch allows user to specify the starting room"
    if(i == "-r"):
        while (sys.argv[indexCount] != "-i") and (indexCount + 1 < len(sys.argv)):
            indexCount += 1
            stringBuilder += sys.argv[indexCount] + " "
        if stringBuilder.strip() in rooms:
            print("Setting start room to: " + stringBuilder)
            startRoom = stringBuilder.strip()
            roomIdx = getRoomIndex(startRoom)

        else:
            print("Invalid room selection: " + stringBuilder)
            sys.exit(1)

    if i == "-i":
        while (sys.argv[indexCount] != "-r") and (indexCount + 1 < len(sys.argv)):
            indexCount += 1
            itemList.append(sys.argv[indexCount])

newGame.play_game('dataStore/newGame/load_file.json', 'dataStore/newGame/RoomState/', roomIdx, itemList)
