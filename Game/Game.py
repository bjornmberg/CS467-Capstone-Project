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
                print('There is no {} in the inventory.'.format(str_item))

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
        else:
            self.print_output("That item is not in your inventory.")

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
            self.print_output(thing_room_des)
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
            print('You do not see a {}'.format(thing))

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
        current_room.set_visited()

        command = self.parseArgs()

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
                self.print_output(current_room.long_des)
                # Hero time increment operation
                self.hero.time = self.hero.set_time()
            else:
                self.look_at_something(command[1])
        elif command[0] == 'use':
            self.use(command[1], command[2])
        elif command[0] == 'map':
            inventoryMapScreen.display(self.inventory, current_room.name, self.hero.location, self.rooms_list)
        elif command[0] == 'help':
            self.getHelp(command)
        elif command[0] == 'save':
            self.save_game()

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

    # Parses the arguments passed
    def parseArgs(self):
        # Dictionaries for each of the possible directions and rooms to move to.
        moveWords = ["go", "walk", "move", "jaunt", "run", "step", "stroll", "march", "travel", "proceed",
                     "sprint", "jog"]
        
        lookWords = ["look", "glance", "eye", "peak", "view", "stare", "peer", "study", "examine"]

        lookObjects = ["windowsill", "crystal", "corner", "east window", "south window", "west window", "toys",
                       "prybar", "pry bar", "ashes", "workbench", "shelves", "box", "padlock", "coffin",
                       "undead chef", "painting", "dog", "table", "mirror", "armor", "clock", "stone", "shears",
                       "garden", "tree", "grave tree", "fireplace", "pool", "window", "plank", "axe", "vision",
                       "bed", "glint", "chef", "knife", "drawer", "sink", "key", "piano", "book", "bookcase",
                       "north window", "pistol", "apparition", "sack", "pocketwatch", "pocket watch", "poltergeist",
                       "couch", "fireplace", "table", "easel", "loom", "left gargoyle", "right gargoyle", "paint",
                       "music box", "bed", "rocking horse", "rose", "spade", "fountain", "roses", "hair",
                       "door lock", "shelf", "toilet", "sink", "mirror", "journal", "locket", "vine", "window",
                       "statue", "tile", "hollow", "grave", "girl", "lock", "paintbrush"]

        twLookObjects = ["window", "sill", "east", "window", "west", "south", "pry", "bar", "pad", "lock",
                         "undead", "chef", "grave", "tree", "book", "case", "north", "pocket", "watch", "left",
                         "right", "gargoyle", "music", "box", "rocking", "horse", "door", "lock", "small", "bed"]

        takeWords = ["grab", "seize", "lift", "take"]

        useWords = ["use", "apply", "put"]

        dropWords = ["drop", "remove", "dump", "release"]

        moveDirections = ["north", "south", "east", "west", "up", "down", "southwest", "southeast",
                          "northwest", "northeast", "down hole", "door"]

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

        otherCommands = ["map", "inventory", "exit", "help", "save"]

        # Get user input. Make it lowercase and split it.
        splitArgs = input((' ' * 20) + '> ').lower().split()

        command = [] # holds the parsed commands
        dir_name = [] # holds valid directions and the corresponding room names

        # Pick out only the valid words
        for i in splitArgs:
            if i in moveDirections or i in moveRooms or i in twoWordRooms or\
                    i in moveWords or i in lookWords or i in twLookObjects or\
                    i in takeWords or i in lookObjects or i in dropWords or\
                    i in otherCommands or i in useWords:

                command.append(i)

        # Print an error if no words were valid.
        if len(command) == 0:
            self.print_output("Error. Invalid command passed.")
            return "badcommand"

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
                self.print_output("Error. Invalid room name or direction given.")
                return "badcommand"

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
                    self.print_output("Invalid room name or direction given.")
                    return "badcommand"

        # TODO: I Need to find a better solution for bad objects
        elif command[0] in lookWords:
            if len(command) == 1:
                command[0] = "look"

                if len(splitArgs) > 1:
                    self.print_output("Error. Cannot look at invalid object.")
                    return "badcommand"

            elif len(command) == 2:
                if command[1] not in lookObjects:
                    self.print_output("Error. Cannot look at invalid object.")
                    return "badcommand"

            elif len(command) >= 3:
                tempWord = command[1] + " " + command[2]
                if tempWord not in lookObjects:
                    self.print_output("Error. Cannot look at invalid object.")
                else:
                    command[1] = tempWord
                    while len(command) > 2:
                        command.pop()

        elif command[0] in useWords:
            command[0] = "use"

            if len(command) < 3:
                self.print_output("Error. Invalid objects passed.")
                return "badcommand"

            elif len(command) == 3:
                if command[1] not in lookObjects or command[2] not in lookObjects:
                    self.print_output("Error. Invalid objects passed.")
                    return "badcommand"

            elif len(command) ==  4:
                if command[1] + " " + command[2] in lookObjects:
                    command[1] = command[1] + " " + command[2]
                elif command[2] + " " + command[3] in lookObjects:
                    command[2] = command[2] + " " + command[3]
                else:
                    self.print_output("Invalid object passed with use command")
                    return "badcommand"
                while command > 3:
                    command.pop()

            elif len(command) == 5:
                if command[1] + " " + command[2] not in lookObjects:
                    self.print_output("Invalid object passed with use command")
                    return "badcommand"
                else:
                    command[1] += " " + command[2]

                if command[3] + " " + command[4] not in lookObjects:
                    self.print_output("Invalid object passed with use command")
                    return "badcommand"
                else:
                    command[2] = command[3] + " " + command[4]

            else:
                self.print_output("Error. Too many arguments with use command.")
                return "badcommand"


        elif command[0] in dropWords:
            command[0] = "drop"

            if len(command) == 1:
                self.print_output("Error. Invalid or no item to drop.")
                return "badcommand"

            if len(command) == 2:
                if command[1] not in lookObjects:
                    self.print_output("Error. Cannot drop " + command[1])
                    return "badcommand"

            elif len(command) > 2:
                tempWord = command[1] + " " + command[2]
                if tempWord not in lookObjects:
                    self.print_output("Error. Invalid item cannot be dropped.")
                    return "badcommand"
                else:
                    command[1] = tempWord
                    while len(command) > 2:
                        command.pop()

        elif command[0] in takeWords:
            command[0] = "take"

            if len(command) < 2:
                print("Invalid item name.")
                return "badcommand"

            elif len(command) == 2:
                if command[1] not in lookObjects:
                    self.print_output("Invalid object cannot be taken.")
                    return "badcommand"

            elif len(command) == 3:
                if command[1] + " " + command[2] not in lookObjects:
                    self.print_output("Invalid object cannot be taken.")
                    return "badcommand"
                else:
                    command[1] += " " + command[2]

            if len(command) > 3:
                self.print_output("Error. Too many arguments passed.")

        elif command[0] == "exit":
            sys.exit(0)

        elif command[0] not in otherCommands:
            self.print_output("Bad command passed.")
            return "badcommand"

        # Return the parsed command.
        return command

    def print_output(self, string):
        print()
        wrappedText = textwrap.wrap(string, width=83)
        for i in wrappedText:
            print((' ' * 20) + i)

    def getHelp(self, helpList):
        if len(helpList) == 1:
            print()
            self.print_output("The goal of the game is to explore the mansion. Through interacting with various objects and features, the player will learn the deep history that surrounds the haunted mansion. Not all clues are helpful! There are many ways to win and lose this game. Can you solve the mystery, or will you meet your demise?")
            print()
            self.print_output("For more detailed instructions regarding a specific command, enter \"help [Your_Command_Here]\"")
            print()
            self.print_output("Valid commands are: take, drop, map, inventory, look, move, and use.")
            
        else:
            if helpList[1] == 'take':
                self.print_output("The take command allows the player to add an item from their environment to their inventory. To call the take function, a player enters a valid take command followed by a valid object in the room.")
                print()
                self.print_output("Valid words that could be used for the \"take\" command are: take, grab, seize, lift, and pick.")
                print()
                self.print_output("For example, to grab a stone off the floor, a player could enter \"Grab stone\"")
                print()
                self.print_output("Or, if the player prefers a more natural language approach, they could enter \"Take the stone off the floor.\"")
                print()
                self.print_output("If the player cannot take the object, there will be a corresponding error message for why they can't take an object.")
                print()

            elif helpList[1] == 'drop':
                print()
                self.print_output("The drop command allows the player to drop an item from their inventory to the room they are currently standing in. To call the drop function, a player enters a valid drop command followed by a valid object in their inventory.")
                print()
                self.print_output("Valid words that could be used for the \"drop\" command are: drop remove, dump, and release.")
                print()
                self.print_output("For example, to drop a stone from a player's inventory, a player could enter \"Drop stone\"")
                print()
                self.print_output("Or, if the player prefers a more natural language approach, they could enter \"Remove the stone from my inventory.\"")
                print()
                self.print_output("If the player cannot drop the object, there will be a corresponding error message for why they can't drop the object.")
                print()

            elif helpList[1] == 'map':
                print()
                self.print_output("The map command allows a player to print the map for the current floor they're standing on.")
                print()
                self.print_output("To call the command, a player simply enters \"map\".")
                print()
                self.print_output("For example, if a player were standing on the first floor, they would enter \"Map\", and the current floor's map would print.")
                print()

            elif helpList[1] == 'inventory':
                print()
                self.print_output("The inventory command allows a player to display all the items in the player's inventory.")
                print()
                self.print_output("To call the command, a player simply enters \"inventory\".")
                print()
                self.print_output("For example, a player would enter \"inventory\", and the contents of the inventory would print to the console.")
                print()

            elif helpList[1] == 'look':
                print()
                self.print_output("The look command allows the player to examine things in their environment to get useful clues about the mansion's history. To call the look function, a player enters a valid look command followed by a valid object in the room or their inventory.")
                print()
                self.print_output("Valid words that could be used for the \"look\" command are: look glance, eye, peak, view, stare, peer, study, and examine.")
                print()
                self.print_output("For example, to look at a painting, a player could enter \"Examine Painting\"")
                print()
                self.print_output("Or, if the player prefers a more natural language approach, they could enter \"Look at the painting.\"")
                print()
                self.print_output("If the player cannot examine the object for some reason, there will be a corresponding error message.")
                print()

            elif helpList[1] == 'move':
                print()
                self.print_output("The move command allows the player to move from room to room. To call the move function, a player enters a valid move command followed by a valid room or direction of an adjoining room.")
                print()
                self.print_output("Valid words that could be used for the \"move\" command are: go, walk, move, jaunt, run, step, stroll, march, travel, proceed, sprint, and jog")
                print()
                self.print_output("For example, to go into the dining room from the parlor, a player could enter \"Go North\"")
                print()
                self.print_output("Or, if the player prefers a more natural language approach, they could enter \"Step into the Dining Room.\"")
                print()
                self.print_output("If the player cannot move for any reason, there will be a corresponding error message.")
                print()

            elif helpList[1] == 'use':
                print()
                self.print_output("The use command allows the player to use an item to interact with another item or feature. To call the use function, a player enters a valid use command followed by two valid objects or features.")
                print()
                self.print_output("Valid words that could be used for the \"use\" command are: use, apply, and put.")
                print()
                self.print_output("For example, to open a locked door, a player could enter \"use key door\"")
                print()
                self.print_output("Or, if the player prefers a more natural language approach, they could enter \"Put the key into the locked door.\"")
                print()
                self.print_output("If the player cannot use the items together for any reason, there will be a corresponding error message.")
                print()
            else:
                self.print_output("Invalid command given to help function. Valid commands are: take, drop, map, inventory, look, move, and use.")
