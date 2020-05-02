'''
    Implementation of the Game class. The Game class is the base class of the game.
    The Game is responsible for initializing the state of the game and allowing the
    user to interact with the Rooms, Features, Items, and Inventory. The Game has a
    list() of Rooms, a Hero, and an Inventory.
'''

import json
import os
from Credits import credits
from Hero import Hero
from Intro import intro
from Inventory import Inventory
from inventoryMapScreen import inventoryMapScreen
from Menu import menu
from Room import Room
from Task import Task

class Game:

    # member variables
    rooms_list = list()         # a list of Rooms
    inventory = Inventory()     # a Inventory object
    hero = Hero()               # a Hero object
    tasks = Task()

    # This function handles loop control for the menu and game
    # Parameters:
    #   NONE
    def start(self):

        while 1:
            selection =  menu.display()
            if selection == 'newgame':
                intro.display()
                self.play_game('dataStore/newGame/load_file.json', 'dataStore/newGame/RoomState/', 0)
            elif selection == 'loadgame':
                self.play_game('dataStore/saveGame/load_file.json', 'dataStore/newGame/RoomState/', 0)
            elif selection == 'credits':
                credits.display()
            elif selection == 'exit':
                break

    # This function is used to initialize the Room objects.
    # Parameters:
    #   data - a list of the room files
    #   file_path - a string that shows the full path to these room files
    def initialize_rooms(self, data, file_path):

        # for each item in data append it to the file path to get a full path
        # example dataStore/newGame/RoomState/Parlor.json
        # use the information in the extracted JSON to initialize Room objects
        for x in data:

            room_file = open(file_path + x, 'r', encoding='utf-8')
            room_data = json.loads(room_file.read())
            room_file.close()

            new_room = Room(
                room_data['name'],
                room_data['longDes'],
                room_data['shortDes'],
                room_data['visited'],
                room_data['roomId'],
                room_data['directions'],
                room_data['startingItems'],
                room_data['droppedItems'],
                room_data['features']
            )
            # Room objects are placed into the rooms list() at specific
            # locations according the the room_id
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
    #   direction - a string representing the direction to move
    def move(self, direction):

        # set the current room to where the hero is located
        current_room = self.rooms_list[self.hero.location]

        # check to see if the direction to move possible within that room
        if direction in current_room.directions:
            # change the hero's location to the new room
            self.hero.location = current_room.directions[direction]
            # set the room being left to visited
            current_room.set_visited()


    # This function is used to take an item from the Room and
    # place it in the inventory
    # Parameters:
    #   item_name - a string that is passed in from user input
    def take(self, str_input):

        # set the current room to where the hero is located
        current_room = self.rooms_list[self.hero.location]

        # this will return True and the Item object if the
        # object is in the Room or False and None if it is not
        # it will also remove that object from the Room
        status, taken_item = current_room.take_item(str_input)

        # if the Item was there put it in the Inventory
        if status == True:
            self.inventory.add_item(taken_item)
            # Check to determine if acquisition is part of a task
            # attempt to perform the task and get the status. Currently nothing done with the status.
            status = self.tasks.perform_task(taken_item, None, self.rooms_list)
        else:
            print('That is not an item you can take.')

    def use(self, str_item, str_feature):

        current_room = self.rooms_list[self.hero.location]

        # check to see if the feature is in the room and get it
        feat_status, feat = current_room.get_feature(str_feature)

        # check that the item is in the inventory and get it
        item_status, item = self.inventory.in_inventory(str_item)

        # if the item is in the inventory and the feature is in the room
        if feat_status and item_status:

            # attempt to perform the taks and get the status
            status = self.tasks.perform_task(item, feat, self.rooms_list)

            # True, means this is a valid Item/Feature combination
            if status:
                # Remove the item from the inventory
                self.inventory.remove_item(item)
            else:
                # Else this is not a valid combination
                print('You cannot do that!')
        # False Feature status - feature is not in the Room
        elif not feat_status:

            print('There is no {} in the room.'.format(str_feature))

        # False Item status - item is not in the Inventory
        elif not item_status:

            print('There is no {} in the inventory.'.format(str_item))



    # This function is used to drop an Item out of Inventory and
    # leave it on the floor of a Room
    # Parameters:
    #   item_name - a string that is passed in from user input
    def drop(self, item_name):

        # set the current room to where the hero is located
        current_room = self.rooms_list[self.hero.location]

        # this will return True and the Item if the object is
        # in the Inventory. If not it will return False and None
        # it will also remove the Item from the Inventory
        status, dropped_item = self.inventory.drop_item(item_name)

        # if the Item was in the Inventory, add it to the dropped_items
        if status:
            current_room.leave_item(dropped_item)
        else:
            print('That item is not in your inventory.')


    # This function is used to look at either an Item or a Feature that
    # is either in the current Room or the Inventory
    # Parameters:
    #   thing - a str passed in from the user
    def look_at_something(self, thing):

        # set the current room to where the hero is located
        current_room = self.rooms_list[self.hero.location]

        # check to see if the 'thing' is in the Room - this will look in
        # the starting_items, dropped_items, and features
        thing_in_room, thing_room_des = current_room.look_in_room(thing)
        # check to see if the 'thing' is in the Inventory
        thing_in_inven, thing_inven_des = self.inventory.look_in_inventory(thing)

        # the thing is in the Room so print the description
        if thing_in_room:
            print(thing_room_des)
        # not in the Room, but in the Inventory, print description
        elif thing_in_inven:
            'INVENTORY ITEM: '
            print(thing_inven_des)
        # not in the Room or the Inventory
        else:
            print('You do not see a {}'.format(thing))


    # FUNCTION COMMENT PLACEHOLDER
    def get_command(self, renderCounter):
        # If the three rooms have been rendered, clear the screen
        # if renderCounter == 3:
        #     os.system('clear')
        #     renderCounter = 0

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
            self.drop(command[1])
        elif command[0] == 'look':
            if len(command) == 1:
                print(current_room.long_des)
            else:
                self.look_at_something(command[1])
        elif command[0] == 'action':
            print(current_room.action_feature(command[1]))
        elif command[0] == 'use':
            self.use(command[1], command[2])
        elif command[0] == 'map':
            inventoryMapScreen.display(self.inventory, current_room.name, self.hero.location)


    # This function is the main game driver function
    def play_game(self, input_file, file_path, roomIdx):

        game_file = open(input_file, 'r', encoding='utf-8')
        file_data = json.loads(game_file.read())

        room_data = file_data['rooms']
        hero_data = file_data['hero']
        inventory_data = file_data['inventory']

        self.initialize_rooms(room_data, file_path)

        self.initialize_hero(hero_data)

        # LINE 218 was breaking something (also removed roomIdx from func input parameters)
        # self.hero.location = roomIdx

        # print('{}'.format(file_data['intro']))

        renderCounter = -1

        while 1:
            renderCounter += 1
            if renderCounter == 4:
                renderCounter = 1
            self.get_command(renderCounter)

    # Parses the arguments passed
    def parseArgs(self):
        # Dictionaries for each of the possible directions and rooms to move to.
        moveWords = ["go", "walk", "move", "jaunt", "run", "step", "stroll", "march", "travel", "proceed",
                     "sprint", "jog"]
        
        lookWords = ["look", "glance", "eye", "peak", "view", "stare", "peer", "study"]

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

        roomFeatures = ["windowsill", "hidden door", "east window", "south window", "west window",
                        "window east", "window south", "window west", "door", "stairs"]

        twoWordFeatures = ["window", "sill", "hidden", "door", "east", "west", "south"]

        # Future function calls.
        testWords = ["take", "inventory", "drop"]

        # Get user input. Make it lowercase and split it.
        splitArgs = input('            > ').lower().split()

        command = [] # holds the parsed commands
        dir_name = [] # holds valid directions and the corresponding room names

        # Pick out only the valid words
        for i in splitArgs:
            if i in moveDirections or i in moveRooms or i in twoWordRooms or i in moveWords or i in testWords or i in lookWords or i in twoWordFeatures or i in roomFeatures:
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
                print("\t\tError. Invalid room name or direction given.")

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
                    print("\t\tInvalid room name or direction given.")

        elif command[0] in lookWords:
            print("This word is in lookWords.")

        # Throw an error if an invalid command was passed.
        elif command[0] not in testWords:
            print("\t\tInvalid command \'" + splitArgs[0] + "\' passed.")

        # Append bad commands to not crash the game in the function calls above.
        while len(command) < 2:
            command.append("badCommand")

        # Return the parsed command.
        return command
