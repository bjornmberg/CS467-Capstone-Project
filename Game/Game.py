import json
import platform
from Credits import credits
from Hero import Hero
from Intro import intro
from Inventory import Inventory
from Menu import menu
from Room import Room


class Game:

    rooms_list = list()
    inventory = Inventory()
    hero = Hero()

    # This function handles loop control for the menu and game
    def start(self):
        # Determine the system type running the game
        plat = platform.system()

        while 1:
            selection =  menu.display()
            if selection == 'newgame':
                if plat == 'Windows':
                    # self.play_game('datastore\\newGame.json')
                    intro.display()
                    self.play_game('dataStore\\newGame\\load_file.json', 'dataStore\\newGame\\RoomState\\')
                else:
                    intro.display()
                    self.play_game('dataStore/newGame/load_file.json', 'dataStore/newGame/RoomState/')
            elif selection == 'loadgame':
                if plat == 'Windows':
                    self.play_game('datastore\\savedGame\\load_file.json', 'dataStore\\savedGame\\RoomState\\')
                else:
                    self.play_game('dataStore/saveGame/load_file.json', 'dataStore/newGame/RoomState/')
            elif selection == 'credits':
                credits.display()
            elif selection == 'exit':
                break

    # This function is used to initialize the Room objects.
    # Parameters:
    #   data - a list of the room files
    #   file_path - a string that shows the full path to these room files
    def initialize_rooms(self, data, file_path):

        for x in data:
            room_file = open(file_path + x, 'r', encoding='utf-8')
            room_data = json.loads(room_file.read())
            new_room = Room(
                room_data['name'],
                room_data['longDes'],
                room_data['shortDes'],
                room_data['visited'],
                room_data['roomId'])
            new_room.directions = room_data['directions'].copy()
            new_room.items = room_data['items'].copy()
            self.rooms_list.insert(new_room.room_id, new_room)

    # This function is used to set the state of the hero
    # Parameters:
    #   data - a dictionary representing the hero
    def initialize_hero(self, data):

        self.hero.name = data['name']
        self.hero.location = data['location']

    # This function is used to set the state of the inventory
    # Parameters:
    #   data - a dictionary representing the inventory
    def initialize_inventory(self, data):
        self.inventory.used_slots = data['usedSlots']
        self.inventory.items = data['items'].copy()

    # This function is used to move the hero through the rooms
    # Parameters:
    # direction - a string representing the direction to move
    def move(self, direction):
        # set the current room to where the hero is located
        current_room = self.rooms_list[self.hero.location]

        # check to see if the direction to move possible within that room
        if direction in current_room.directions:
            # change the hero's location to the new room
            self.hero.location = current_room.directions[direction]
            # set the room being left to visited
            current_room.set_visited()
        # if the hero cannot move in that direction print and return
        else:
            print('You cannot move in that direction.')

    # FUNCTION COMMENT PLACEHOLDER
    def take(self, item):

        current_room = self.rooms_list[self.hero.location]
        if item in current_room.items:
            self.inventory.add_item(item ,current_room.items[item])
            del current_room.items[item]
        else:
            print('That is not an item you can take.')


    # FUNCTION COMMENT PLACEHOLDER
    def get_command(self):

        current_room = self.rooms_list[self.hero.location]
        current_room.get_description()
        command = self.parseArgs()

        if command[0] == 'move':
            self.move(command[1])
        elif command[0] == 'take':
            self.take(command[1])
        elif command[0] == 'inventory':
            self.inventory.show_inventory()
        elif command[0] == 'drop':
            status, item = self.inventory.drop_item((command[1]))
            if status == True:
                current_room.items[command[1]] = item

    # This function is the main game driver function
    def play_game(self, input_file, file_path):

        game_file = open(input_file, 'r', encoding='utf-8')
        file_data = json.loads(game_file.read())

        room_data = file_data['rooms']
        hero_data = file_data['hero']
        inventory_data = file_data['inventory']

        self.initialize_rooms(room_data, file_path)
        self.initialize_hero(hero_data)
        self.initialize_inventory(inventory_data)

        print('{}'.format(file_data['intro']))

        while 1:
            self.get_command()

    # Parse the arguments
    def parseArgs(self):
        # Dictionaries for each of the possible directions and rooms to move to.
        moveWords = ["go", "walk", "move", "jaunt", "run", "step", "stroll", "march", "travel", "proceed",
                     "sprint", "jog"]

        moveDirections = ["north", "south", "east", "west", "up", "down"]

        moveRooms = ["solarium", "game room", "kitchen", "dining room", "bathroom", "library",
                     "foyer", "parlor", "porch", "cellar", "servant's quarters", "crypt",
                     "servant's bathroom", "dark tunnel", "red room", "child's room", "pink room",
                     "art studio", "green room", "master's quarters", "landing", "linen closet",
                     "upstairs", "downstairs", "attic", "hidden room", "gardens", "gazebo"]

        twoWordRooms = ["game", "room", "dining", "servant's", "quarters", "bathroom", "dark",
                        "tunnel", "red", "green", "master's", "linen", "closet", "hidden"]

        testWords = ["take", "inventory", "drop"]

        # Get user input.
        userIn = input('> ')

        # Make the argument lowercase
        parsedArgs = userIn.lower()

        # Split the arguments into a separate list
        splitArgs = parsedArgs.split()
        command = []

        # Pick out only the valid words
        for i in splitArgs:
            if i in moveDirections or i in moveRooms or i in twoWordRooms or i in moveWords or i in testWords:
                command.append(i)

        # Print an error if no words were valid.
        if len(command) == 0:
            print("Error. Invalid command passed.")

        # Set the command to 'move' if it's in movewords.
        elif command[0] in moveWords:
            command[0] = "move"

            # Print an error if no room was provided.
            if len(command) <= 1:
                print("Error. Invalid room name or direction given.")
            else:
                # Check to see if it's a one-word named room
                if command[1] in moveRooms:
                    print("TODO: Argument is in moveRooms. Need to parse direction from game class")
                    # move(command[1])
                # Check to see if it's a cardinal direction
                elif command[1] in moveDirections:
                    # move(command[1])
                    print("moving " + command[1] + " ...")

                # Check to see if it's a two-word room
                # and both are in the two-word room dictionary
                elif len(command) == 3 and command[1] in twoWordRooms and command[2] in twoWordRooms:
                    twoWords = command[1] + ' ' + command[2]
                    if twoWords in moveRooms:
                        print("TODO: Argument is in moveRooms. Need to parse direction from game class")
                        # move(twoWords)
                    else:
                        print("Invalid room name or direction given.")
                # Display error if a bad room name/direction were given.
                else:
                    print("Invalid room name or direction given.")
        elif command[0] not in testWords:
            print("Invalid command \'" + splitArgs[0] + "\' passed.")

        # Append bad commands to not crash the game in the function calls above.
        while len(command) < 2:
            command.append("badCommand")

        return command
