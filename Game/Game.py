import json
import platform
from Credits import credits
from Hero import Hero
from Intro import intro
from Inventory import Inventory
from Item import Item
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
                    self.play_game('dataStore/newGame/load_file_test.json', 'dataStore/newGame/RoomState/')
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
            new_room.set_up(room_data)
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
        else:
            print('There is no door in that direction.')

    # FUNCTION COMMENT PLACEHOLDER
    def take(self, item):

        current_room = self.rooms_list[self.hero.location]

        status, taken_item = current_room.take_item(item)

        if status == True:
            self.inventory.add_item(taken_item)

        # if current_room.in_starting_items(item):
        #     self.inventory.add_item(item, current_room.starting_items[item])
        #     del current_room.starting_items[item]
        # elif current_room.in_dropped_items(item):
        #     self.inventory.add_item(item, current_room.dropped_items[item])
        #     del current_room.dropped_items[item]
        # else:
        #     print('Thats not an item you can take.')

    # FUNCTION COMMENT PLACEHOLDER
    def get_command(self):

        current_room = self.rooms_list[self.hero.location]
        current_room.get_description()

        # COMMENT OUT LINE 113 and UNCOMMENT LINE 115 to OVERRIDE THE PARSER
        # command = self.parseArgs()
        command = input('> ').split(' ')

        if command[0] == 'move':
            self.move(command[1])
        elif command[0] == 'take':
            self.take(command[1])
        elif command[0] == 'inventory':
            self.inventory.show_inventory()
        elif command[0] == 'drop':
            status, item = self.inventory.drop_item((command[1]))
            if status == True:
                current_room.dropped_items[command[1]] = item
        elif command[0] == 'look':
            if len(command) == 1:
                current_room.get_description()
            else:
                current_room.look_at_feature(command[1])
        elif command[0] == 'action':
            current_room.action_feature(command[1])

    # This function is the main game driver function
    def play_game(self, input_file, file_path):

        game_file = open(input_file, 'r', encoding='utf-8')
        file_data = json.loads(game_file.read())

        room_data = file_data['rooms']
        hero_data = file_data['hero']
        inventory_data = file_data['inventory']

        self.initialize_rooms(room_data, file_path)
        self.initialize_hero(hero_data)
        # self.initialize_inventory(inventory_data)

        while 1:
            self.get_command()

    # Parses the arguments passed
    def parseArgs(self):
        # Dictionaries for each of the possible directions and rooms to move to.
        moveWords = ["go", "walk", "move", "jaunt", "run", "step", "stroll", "march", "travel", "proceed",
                     "sprint", "jog"]

        moveDirections = ["north", "south", "east", "west", "up", "down", "southwest", "southeast",
                          "northwest", "northeast", "down hole"]

        moveRooms = ["solarium", "game room", "kitchen", "dining room", "bathroom", "library",
                     "foyer", "parlor", "porch", "cellar", "servant quarters", "crypt",
                     "servant's bathroom", "dark tunnel", "red room", "child's room", "pink room",
                     "art studio", "green room", "master's quarters", "landing", "linen closet",
                     "upstairs", "downstairs", "attic", "hidden room", "gardens", "gazebo",
                     "rose garden", "downstairs bathroom", "landing", "front lawns",
                     "upstairs bathroom"]

        twoWordRooms = ["game", "room", "dining", "servant", "quarters", "bathroom", "dark",
                        "tunnel", "red", "green", "master's", "linen", "closet", "hidden", "rose",
                        "garden", "down", "hole", "downstairs", "bathroom", "front", "lawns",
                        "upstairs", "pink"]

        # Future function calls.
        testWords = ["take", "inventory", "drop"]

        # Get user input. Make it lowercase and split it.
        splitArgs = input('> ').lower().split()

        command = [] # holds the parsed commands
        dir_name = [] # holds valid directions and the corresponding room names

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

            # Get the room list for matching strings
            current_room = self.rooms_list[self.hero.location]

            # Add the direction and room name to the direction_name list
            for i in moveDirections:
                if i in current_room.directions:
                    dir_name.append(i)
                    dir_name.append(self.rooms_list[current_room.directions[i]].name.lower())

            # Print an error if no room was provided.
            if len(command) <= 1:
                print("Error. Invalid room name or direction given.")

            else:
                # Check to see if it's a one-word named room
                if command[1] in dir_name:
                    # Get the index of the correct room
                    idx = dir_name.index(command[1])

                    # If the index is even, it's already a direction
                    if idx % 2 != 0:
                        # Otherwise get the index of the direction.
                        command[1] = dir_name[idx-1]

                # Check to see if it's a two-word room
                # and both are in the two-word room dictionary
                elif len(command) == 3 and command[1] in twoWordRooms and command[2] in twoWordRooms:

                    # Concatenate the strings for further parsing
                    twoWords = command[1] + ' ' + command[2]

                    # Set the command if the concatenated words are valid.
                    if twoWords in dir_name:
                        command[1] = twoWords

                        # Get the index of the valid room or direction.
                        idx = dir_name.index(twoWords)

                        # If it's even, it's already a direction.
                        if idx % 2 != 0:
                            # Otherwise grab the index of the correct direction.
                            command[1] = dir_name[idx-1]

                # Print an error if an invalid room name was passed.
                else:
                    print("Invalid room name or direction given.")

        # Throw an error if an invalid command was passed.
        elif command[0] not in testWords:
            print("Invalid command \'" + splitArgs[0] + "\' passed.")

        # Append bad commands to not crash the game in the function calls above.
        while len(command) < 2:
            command.append("badCommand")

        # Return the parsed command.
        return command
