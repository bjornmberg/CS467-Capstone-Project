'''
    Implementation of the Game class. The Game class is the base class of the game.
    The Game is responsible for initializing the state of the game and allowing the
    user to interact with the Rooms, Features, Items, and Inventory. The Game has a
    list() of Rooms, a Hero, and an Inventory.
'''

import json
import os
import sys
from pathlib import Path
from Credits import credits
from Hero import Hero
from Intro import intro
from Inventory import Inventory
from inventoryMapScreen import inventoryMapScreen
from Menu import menu
from Room import Room
from Task import Task
from Language_Parser import Language_Parser
import textwrap


class Game:

    # member variables
    rooms_list = list()         # a list of Rooms
    hero = None
    inventory = None
    tasks = Task()
    parser = Language_Parser.Language_Parser()

    # This function handles loop control for the menu and game
    # Parameters:
    #   NONE
    def start(self):

        while 1:
            item_list = []
            selection = menu.display()
            if selection == 'newgame':
                intro.display()
                self.play_game('dataStore/newGame/load_file.json', 'dataStore/newGame/RoomState/', 0, item_list)
            elif selection == 'loadgame':
                # Check if saved game exists to load
                load_file = Path('dataStore/savedGame/load_file.json')
                if load_file.is_file():
                    self.play_game(load_file, 'dataStore/savedGame/RoomState/', 0, item_list)
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
            # Check if a task is necessary on move into next room and get the status. Currently nothing done with the status.
            self.tasks.perform_task_on_move(self.inventory, self.rooms_list, self.hero.location)
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
            parser.print_output("That is not an item you can take.")

    def use(self, str_item, str_feature):

        current_room = self.rooms_list[self.hero.location]

        # check to see if the feature is in the room and get it
        feat_status, feat = current_room.get_feature(str_feature)

        # False Feature status - feature is not in the Room
        if not feat_status:
            print('There is no {} in the room.'.format(str_feature))
        else:
            # check that the item is in the inventory and get it
            item_status, item = self.inventory.in_inventory(str_item)

            # if the item is in the inventory and the feature is in the room
            if feat_status and item_status:
                # attempt to perform the task and get the status
                status = self.tasks.perform_task(item, feat, self.rooms_list)

                # True, means this is a valid Item/Feature combination
                if status:
                    # Remove the item from the inventory
                    self.inventory.remove_item(item)
                else:
                    # Else this is not a valid combination
                    parser.print_output(' ...you cannot do that now.')

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
            parser.print_output("That item is not in your inventory.")


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
            parser.print_output(thing_room_des)
            # Check to see if a task is associated with look operation
            self.tasks.perform_task_on_look(thing_room_des, self.rooms_list, self.hero.time)
        # not in the Room, but in the Inventory, print description
        elif thing_in_inven:
            'INVENTORY ITEM: '
            parser.print_output(thing_inven_des)
            # Check to see if a task is associated with look operation
            self.tasks.perform_task_on_look(thing_inven_des, self.rooms_list, self.hero.time)
        # not in the Room or the Inventory
        else:
            print('You do not see a {}'.format(thing))


    # FUNCTION COMMENT PLACEHOLDER
    def save_game(self):

        room_names = open('dataStore/savedGame/Seed.json', 'r', encoding='utf-8')
        load_data = json.loads(room_names.read())
        room_names.close()

        load_file = open('dataStore/savedGame/load_file.json', 'w', encoding='utf-8')
        load_data['inventory'] = self.inventory.save_inventory()
        load_data['hero'] = self.hero.save_hero()

        output_data = json.dumps(load_data, indent=2)
        load_file.write(output_data)
        load_file.close()

        for room in self.rooms_list:
            room_file = open('dataStore/savedGame/RoomState/{}.json'.format(room.name), 'w', encoding='utf-8' )
            room_data = json.dumps(room.save_room(), indent=2)
            room_file.write(room_data)


    # FUNCTION COMMENT PLACEHOLDER
    def get_command(self, renderCounter):
        parser = Language_Parser.Language_Parser()
        current_room = self.rooms_list[self.hero.location]
        current_room.get_description()

        command = parser.parse_args(self.rooms_list, self.hero)

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
                parser.print_output(current_room.long_des)
            else:
                self.look_at_something(command[1])
        elif command[0] == 'use':
            self.use(command[1], command[2])
        elif command[0] == 'map':
            inventoryMapScreen.display(self.inventory, current_room.name, self.hero.location)
        elif command[0] == 'save':
            self.save_game()

        # Simple hero time increment operation, as well as debugging output
        self.hero.time = self.hero.set_time(self.hero.time)

    # This function is the main game driver function
    def play_game(self, input_file, file_path, roomIdx, item_list):

        game_file = open(input_file, 'r', encoding='utf-8')
        file_data = json.loads(game_file.read())

        room_data = file_data['rooms']
        hero_data = file_data['hero']
        inventory_data = file_data['inventory']

        self.initialize_rooms(room_data, file_path)

        self.hero = Hero(hero_data['name'], hero_data['location'], hero_data['time'])
        self.inventory = Inventory(inventory_data)

        roomIterator = 0
        current_room = self.rooms_list[0]

        while roomIterator < 22:
            for i in item_list:
                status, taken_item = current_room.take_item(i)
                if status:
                    self.inventory.add_item(taken_item)
            roomIterator += 1
            current_room = self.rooms_list[roomIterator]

        renderCounter = -1

        while 1:
            renderCounter += 1
            if renderCounter == 4:
                renderCounter = 1
            self.get_command(renderCounter)

    def print_output(self, string):
        wrappedText = textwrap.wrap(string, width=74)
        for i in wrappedText:
            print('            ' + i)