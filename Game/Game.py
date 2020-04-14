import json
import shutil
import os
from Room import Room

class Game:

    roomsList = list()

    # FUNCTION COMMENT PLACEHOLDER
    def displayCredits(self):
        os.system('cls')
        print('THIS IS WHERE THE CREDITS WILL BE!')
        input('PRESS ANY KEY TO RETURN')
        return

    # FUNCTION COMMENT PLACEHOLDER
    def displayMenu(self):
        # Initialize some variables for use in menu display
        cols, rows = shutil.get_terminal_size()
        lastLine = rows // 2
        centerLeftRight = cols // 1
        centerTopBottom = (lastLine) // 3
        os.system('cls')

        print('\n' * centerTopBottom)
        print('The Spook Mansion Mystery'.center(centerLeftRight, ' '))
        print('\n')
        print('Do you dare enter the Mansion?'.center(centerLeftRight, ' '))
        print('\n')
        print('Please Make a Selection:'.center(centerLeftRight, ' '))
        print('\n')
        print('\'newgame\' - to start a new game'.center(centerLeftRight, ' '))
        print('\'loadgame\' - to load a saved game'.center(centerLeftRight, ' '))
        print('\'credits\' - to view the game credits'.center(centerLeftRight, ' '))
        print('\'exit\' - to exit the game'.center(centerLeftRight, ' '))
        print('\n' * lastLine)
        selection = input("Enter Selection: ")
        # Return the user's selection
        return selection

    # FUNCTION COMMENT PLACEHOLDER
    def start(self):

        while 1:
            selection =  self.displayMenu()
            if selection == 'newgame':
                self.playGame('datastore\\newGame.json')
            elif selection == 'loadgame':
                self.playGame('datastore\\saveGame.json')
            elif selection == 'credits':
                self.displayCredits()
            elif selection == 'exit':
                break

    # FUNCTION COMMENT PLACEHOLDER
    def initializeRooms(self, data):

        # iterate through the roomData and initialize Room objects for each item
        for x in data:
            # initialize the object
            newRoom = Room(x['name'], x['longDes'], x['shortDes'], x['visited'], x['roomId'])
            # copy the droppedItems from the roomData to the object's droppedItems
            newRoom.droppedItems = x['droppedItems'].copy()
            # copy the linkedRooms from the roomData to the object's linkedRooms
            newRoom.linkedRooms = x['linkedRooms'].copy()
            # put the room into the roomsList at the index of its id - example: parlor's id == 0
            # so the parlor room is at roomsList[0]
            self.roomsList.insert(newRoom.roomId, newRoom)

        for y in self.roomsList:
            # the linkedRooms list of each item will contain the index of the other rooms
            # it is linked to in the following order north, south, east, west, up, down
            # these values will either be the index of the room in the rooms list (if
            # a link exists, or None if there is no link in that direction
            n = self.roomsList[y.linkedRooms[0]] if y.linkedRooms[0] is not None else None
            s = self.roomsList[y.linkedRooms[1]] if y.linkedRooms[1] is not None else None
            e = self.roomsList[y.linkedRooms[2]] if y.linkedRooms[2] is not None else None
            w = self.roomsList[y.linkedRooms[3]] if y.linkedRooms[3] is not None else None
            u = self.roomsList[y.linkedRooms[4]] if y.linkedRooms[4] is not None else None
            d = self.roomsList[y.linkedRooms[5]] if y.linkedRooms[5] is not None else None
            # call to link the rooms
            y.linkRooms(n, s, e, w, u, d)

    # FUNCTION COMMENT PLACEHOLDER
    def testHarness(self, startingRoom):

        currentRoom = startingRoom
        i = 0

        while i <= 10:
            print("Current Room: {}".format(currentRoom.name))
            print(currentRoom.getDescription())
            currentRoom.setVisited()
            if currentRoom.north:
                currentRoom = currentRoom.north
            elif currentRoom.east:
                currentRoom = currentRoom.east
            elif currentRoom.west:
                currentRoom = currentRoom.west
            elif currentRoom.south:
                currentRoom = currentRoom.south
            else:
                break
            i += 1


    # FUNCTION COMMENT PLACEHOLDER
    def playGame(self, inputFile):

        gameFile = open(inputFile, 'r')
        fileData = json.loads(gameFile.read())
        roomData = fileData['rooms']

        self.initializeRooms(roomData)
        self.testHarness(self.roomsList[0])
