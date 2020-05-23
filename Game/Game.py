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
import textwrap
from languageParser import languageParser
from Wrapper import wrapper
import random


class Game:
    """Class used to represent the Game

    Attributes
    ----------
    rooms_list: list
        list of Room objects representing the structure of the Mansion
    hero: Hero
        the Game character/iterator of the rooms_list
    inventory: Inventory
        the Game Inventory that provides carrying/dropping abilities
    tasks: Task
        the interactions within the Game that can/must be completed

    Methods
    -------
    start()
        displays menu allows user to start the Game
    initializes_rooms()
        loads file data and initializes the Room objects
    move()
        manages Hero movement within the Game
    take()
        removes an Item from a Room and adds it to Inventory
    use()
        performs and action, with an Item
    drop()
        removes an Item from Inventory and adds it to a Room
    look_at_something()
        gets the description of an Item or a Feature
    save_game()
        saves the game data to load files for continuation
    get_command()
        retrieves user input for actions to be carried out
    play_game()
        main Game driver function

    """
    rooms_list = list()
    hero = None
    inventory = None
    tasks = Task()
    parser = languageParser.LanguageParser()

    def start(self):
        """Displays the menu in a loop and allows user to start the Game

        :return: VOID
        """
        while 1:
            item_list = []
            selection = menu.display()
            if selection == 'newgame':
                intro.display()
                self.play_game('dataStore/newGame/load_file.json', 'dataStore/newGame/RoomState/', item_list)
            elif selection == 'loadgame':
                # Check if saved game exists to load
                load_file = Path('dataStore/savedGame/load_file.json')
                if load_file.is_file():
                    self.play_game(load_file, 'dataStore/savedGame/RoomState/', item_list)
            elif selection == 'credits':
                credits.display()
            elif selection == 'exit':
                break

    def initialize_rooms(self, data, file_path):
        """Creates Room objects based on the data passed to the function

        :param dict data: a list of the Room files
        :param str file_path: the path to the newGame or savedGame directory
        :return: VOID
        """
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

    def move(self, direction):
        """Manages movement of the Hero within the Game

        :param str direction: user input direction to move
        :return: VOID
        """
        # set the current room to where the hero is located
        current_room = self.rooms_list[self.hero.location]
        current_room.set_visited()

        # check to see if the direction to move possible within that room
        if direction in current_room.directions:
            # change the hero's location to the new room
            self.hero.location = current_room.directions[direction]
            # Check if a task is necessary on move into next room and get the status. Currently nothing done with the status.
            self.tasks.perform_task_on_move(self.inventory, self.rooms_list, self.hero.location)
            # Hero time increment operation
            self.hero.time = self.hero.set_time()
            self.rooms_list[self.hero.location].get_description()



    def take(self, str_input):
        """Removes an Item from a Room and places it in the Inventory

        :param str str_input: user input of Item to be taken
        :return: VOID
        """
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
            self.print_output("That is not an item you can take.")

    def use(self, str_item, str_feature):
        """Attempts to perform an action with an Item and/or a Feature

        :param str str_item: user input of Item wished to be used
        :param str str_feature: user input of Feature to be used
        :return: VOID
        """
        current_room = self.rooms_list[self.hero.location]

        # check to see if the feature is in the room and get it
        feat_status, feat = current_room.get_feature(str_feature)

        # False Feature status - feature is not in the Room
        if not feat_status:
            print('There is no {} in the room.'.format(str_feature))
        else:
            # Key counter variable to check if user has both keys in posession
            key_counter = 0
            for x in self.inventory.items:
                if x.name == 'key':
                    key_counter += 1
            # If user has both keys, get the appropriate one for the room (kitchen or servant's quarters)
            if key_counter == 2:
                if current_room.room_id == 7:
                    str_item = 'A small ornate key.'
                    item_status, item = self.inventory.key_in_inventory(str_item)
                elif current_room.room_id == 15:
                    str_item = 'A simple key.'
                    item_status, item = self.inventory.key_in_inventory(str_item)
                else:
                    item_status = False
            # If the key_counter is 2 but item_status is False it means that user was not in the kitchen or servant's quarters
            # when attempting to use the key. Get the first key item and move on
            if key_counter == 2:
                if item_status == False:
                    # check that the item is in the inventory and get it
                    item_status, item = self.inventory.in_inventory(str_item)
            # Else user doesn't have 2 keys - attempt to get the item
            elif key_counter != 2:
                    # check that the item is in the inventory and get it
                    item_status, item = self.inventory.in_inventory(str_item)

            # if the item is in the inventory and the feature is in the room
            if feat_status and item_status:
                # attempt to perform the task and get the status
                status = self.tasks.perform_task(item, feat, self.rooms_list)

                # True, means this is a valid Item/Feature combination
                if status:
                    # Hero time increment operation
                    self.hero.time = self.hero.set_time()
                    # Remove the item from the inventory
                    self.inventory.remove_item(item)
                else:
                    # Else this is not a valid combination
                    self.print_output(' ...you cannot do that now.')

            # False Item status - item is not in the Inventory
            elif not item_status:
                print((' ' * 20) + 'There is no {} in the inventory.'.format(str_item))

    def drop(self, item_name):
        """Removes an Item from the Inventory and leaves it in a Room

        :param str item_name: user input of Item to be dropped
        :return: VOID
        """

        # set the current room to where the hero is located
        current_room = self.rooms_list[self.hero.location]

        # this will return True and the Item if the object is
        # in the Inventory. If not it will return False and None
        # it will also remove the Item from the Inventory
        status, dropped_item = self.inventory.drop_item(item_name)

        # if the Item was in the Inventory, add it to the dropped_items
        if status:
            current_room.leave_item(dropped_item)
            self.print_output('You have dropped the {}'.format(item_name))
        else:
            self.print_output('That item is not in your inventory.')

    def look_at_something(self, thing):
        """Gets the description of an Item or Feature in a Room or Inventory

        :param str thing: user input of Item/Feature to be looked at
        :return: VOID
        """
        # set the current room to where the hero is located
        current_room = self.rooms_list[self.hero.location]

        # check to see if the 'thing' is in the Room - this will look in
        # the starting_items, dropped_items, and features
        thing_in_room, thing_room_des = current_room.look_in_room(thing)
        # check to see if the 'thing' is in the Inventory
        thing_in_inven, thing_inven_des = self.inventory.look_in_inventory(thing)

        # the thing is in the Room so print the description
        if thing_in_room:
            print()
            # Print the feature description via the wrap processor to preserve colors
            processed = wrapper.wrap_processor(thing_room_des)
            for i in processed:
                print(i)
            # Check to see if a task is associated with look operation
            self.tasks.perform_task_on_look(thing_room_des, self.rooms_list, self.hero.time)
            # Hero time increment operation
            self.hero.time = self.hero.set_time()
        # not in the Room, but in the Inventory, print description
        elif thing_in_inven:
            'INVENTORY ITEM: '
            self.print_output(thing_inven_des)
            # Check to see if a task is associated with look operation
            self.tasks.perform_task_on_look(thing_inven_des, self.rooms_list, self.hero.time)
            # Hero time increment operation
            self.hero.time = self.hero.set_time()
        # not in the Room or the Inventory
        else:
            self.print_output('You do not see a {} in this room.'.format(thing))

    def save_game(self):
        """Saves the state of the Game to save files

        :return: VOID
        """
        # Get the names of the Rooms from the Seed file copy to load_data
        room_names = open('dataStore/savedGame/Seed.json', 'r', encoding='utf-8')
        load_data = json.loads(room_names.read())
        room_names.close()

        # add the Hero state and Inventory state to the load_data
        load_file = open('dataStore/savedGame/load_file.json', 'w', encoding='utf-8')
        load_data['inventory'] = self.inventory.save_inventory()
        load_data['hero'] = self.hero.save_hero()

        # write the load_data to the save file
        output_data = json.dumps(load_data, indent=2)
        load_file.write(output_data)
        load_file.close()

        # Go through the rooms_list and save each of the rooms to a separate save file
        for room in self.rooms_list:
            room_file = open('dataStore/savedGame/RoomState/{}.json'.format(room.name), 'w', encoding='utf-8' )
            room_data = json.dumps(room.save_room(), indent=2)
            room_file.write(room_data)

    def get_command(self):
        """Get user input for interactions within the Game

        :return: VOID
        """
        current_room = self.rooms_list[self.hero.location]

        command = self.parser.parse_args(self.rooms_list, self.hero)

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
                # If room has not been visited, output long description. Else, short.
                if current_room.visited == False:
                    processed = wrapper.wrap_processor(current_room.long_des)
                else:
                    processed = wrapper.wrap_processor(current_room.short_des)
                for i in processed:
                    print(i)
                # Hero time increment operation
                self.hero.time = self.hero.set_time()
            else:
                self.look_at_something(command[1])
        elif command[0] == 'use':
            self.use(command[1], command[2])
        elif command[0] == 'map':
            inventoryMapScreen.display(self.inventory, current_room.name, self.hero.location, self.rooms_list)
            current_room.get_description()
        elif command[0] == 'save':
            self.save_game()

        elif command[0] == 'play' and command[1] == 'pool':
            if current_room.name == 'Game Room':
                self.play_pool()
            else:
                print(' ' * 20 + "You can't do that here.")

        # Check day status on each iteration of the game loop
        self.check_day()

    def play_game(self, input_file, file_path, item_list):
        """Initializes the Game variables and starts the game-play

        :param str input_file: main load file
        :param str file_path: path to the appropriate Rooms directory
        :param list item_list: list of starting Items
        :return: Void
        """
        game_file = open(input_file, 'r', encoding='utf-8')
        file_data = json.loads(game_file.read())

        room_data = file_data['rooms']
        hero_data = file_data['hero']
        inventory_data = file_data['inventory']

        self.initialize_rooms(room_data, file_path)
        self.hero = Hero(hero_data['name'], hero_data['location'], hero_data['time'], hero_data['day'])
        self.inventory = Inventory(inventory_data)

        room_iterator = 0
        current_room = self.rooms_list[0]

        while room_iterator < 22:
            for i in item_list:
                status, taken_item = current_room.take_item(i)
                if status:
                    self.inventory.add_item(taken_item)
            room_iterator += 1
            current_room = self.rooms_list[room_iterator]

        # Get the description of the starting Room and print it
        starting_room = self.rooms_list[self.hero.location]
        starting_room.get_description()

        while 1:
            self.get_command()

    def print_output(self, string):
        print()
        wrappedText = textwrap.wrap(string, width=83)
        for i in wrappedText:
            print((' ' * 20) + i)

    def check_day(self):
        # Check to see if new day. If not, a Null is returned. Else an integer corresponding to the day
        day = self.hero.check_time()
        if day:
            self.tasks.perform_task_on_day(day)

    def play_pool(self):
        rand_number = random.randint(0, 100) % 2
        if rand_number == 0:
            print(' ' * 20 + "You size up the Poltergeist. You know you can take down this clown.\n")
            print(' ' * 20 + "In a flurry of quick strikes, he promptly and decidedly beats you.\n")
            print(' ' * 20 + "I don't lose. Better luck next try.")
        else:
            print(' ' * 20 + "You're not sure if you can beat the Poltergeist at his own game.\n")
            print(' ' * 20 + "Taking careful aim, you sink all of your balls without giving him a turn.")
            print(' ' * 20 + "You sink the 8-ball! You've won!\n")
            print(' ' * 20 + "The Polgergist is very unhappy. He breaks his cue against the pool table.")
            print(' ' * 20 + "Perhaps you should consider leaving this room and let him cool off for a bit.")
