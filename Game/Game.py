import json
import os
from Room import Room
from Hero import Hero

class Game:

    roomsList = list()

    # This function will display the credits for the Game
    # Needs formatting
    def displayCredits(self):
        # os.system('cls')
        print('THIS IS WHERE THE CREDITS WILL BE!')
        input('PRESS ANY KEY AND ENTER TO RETURN')
        return

    # This function displays the menu and asks the user for input
    # The input (string) is returned to the calling function
    # Needs formatting
    def displayMenu(self):

        # os.system('cls')

        print('The Spook Mansion Mystery')
        print('\n')
        print('Do you dare enter the Mansion?')
        print('\n')
        print('Please Make a Selection:')
        print('\n')
        print('\'newgame\' - to start a new game')
        print('\'loadgame\' - to load a saved game')
        print('\'credits\' - to view the game credits')
        print('\'exit\' - to exit the game')

        selection = input("Enter Selection: ")
        # Return the user's selection
        return selection

    # This function handles loop control for the menu and game
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

    # This function is used to initialize the Room objects to a state from either
    # a save file or a start file.
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

        # go through the rooms and link them
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

    # This function is just a test harness to use w/o having a hero
    # all this does is walk through the Rooms making sure that the
    # state is changed when entered
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


    # This function is the main game driver function
    def playGame(self, inputFile):

        gameFile = open(inputFile, 'r')
        fileData = json.loads(gameFile.read())
        roomData = fileData['rooms']

        self.initializeRooms(roomData)
        # self.testHarness(self.roomsList[0])

        heroData = fileData['hero']
        hero = Hero(heroData['name'], heroData['location'])

        while 1:
            print('--------------------------------------')
            currentRoom = self.roomsList[hero.location]
            print('{}\'s Current Location: {}'.format(hero.name, currentRoom.name))
            print('Description: {}'.format(currentRoom.getDescription()))
            print('Linked Room Indices: {}'.format(currentRoom.linkedRooms))
            direction = input('Enter n, s, e, w, u, d: ')

            if direction == 'n':
                if currentRoom.north is not None:
                    hero.location = currentRoom.north.roomId
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 's':
                if currentRoom.south is not None:
                    hero.location = currentRoom.south.roomId
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 'e':
                if currentRoom.east is not None:
                    hero.location = currentRoom.east.roomId
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 'w':
                if currentRoom.west is not None:
                    hero.location = currentRoom.west.roomId
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 'u':
                if currentRoom.up is not None:
                    hero.location = currentRoom.up.roomId
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 'd':
                if currentRoom.down is not None:
                    hero.location = currentRoom.down.roomId
                else:
                    print('No Room in that direction')
                    continue

            currentRoom.setVisited()

