import textwrap
import sys


class LanguageParser:
    """ Class that takes and parses the natural language input by the user

    Attributes
    ----------
        move_words - Holds all the valid commands to move the player throughout the house
        look_words - Holds all the valid commands to look at objects in the house
        look_objects - Holds all the valid items a player could look at
        tw_look_objects - Holds all the two word items a player can interact with (used for building strings)
        take_words - Holds all the valid commands to take objects in the game
        use_words - Holds all the valid commands to use objects n the game
        drop_words - Holds all the valid commands to drop items in the game
        move_directions - Holds all the valid directions a player could move in the game
        move_rooms - Holds all the valid rooms a player can walk to in the game
        tw_rooms - Holds all the valid two word rooms a player can move in the game (used for building strings)
        other_commands - Holds any one-word commands that don't require items or directions

    Methods
    -------
    __init__():
        establishes the string dictionaries for the language parser
    parse_args():
        checks player's input for valid commands and handles the input command
    parse_move():
        handles the movement logic and language processing for the move command
    parse_look():
        handles the arguments for the look command
    parse_use():
        handles the arguments for the use command
    parse_drop():
        handles the arguments for the drop command
    parse_take():
        handles the arguments for the take command
    get_help():
        displays a help guide for the user
    """
    def __init__(self):
        # Dictionaries for each of the possible directions and rooms to move to.
        self.move_words = ["go", "walk", "move", "jaunt", "run", "step", "stroll", "march", "travel", "proceed",
                           "sprint", "jog"]

        self.look_words = ["look", "glance", "eye", "peak", "view", "stare", "peer", "study", "examine", "read"]

        self.look_objects = ["windowsill", "crystal", "corner", "east window", "south window", "west window", "toys",
                             "prybar", "pry bar", "ashes", "workbench", "shelves", "box", "padlock", "coffin",
                             "undead chef", "painting", "dog", "table", "mirror", "armor", "clock", "stone", "shears",
                             "garden", "tree", "grave tree", "fireplace", "pool", "window", "plank", "axe", "vision",
                             "bed", "glint", "chef", "knife", "drawer", "sink", "key", "piano", "book", "bookcase",
                             "north window", "pistol", "apparition", "sack", "pocketwatch", "pocket watch",
                             "poltergeist", "couch", "fireplace", "table", "easel", "loom", "left gargoyle", 
                             "right gargoyle", "paint", "music box", "bed", "rocking horse", "rose", "spade", 
                             "fountain", "roses", "hair", "door lock", "shelf", "toilet", "sink", "mirror", "journal", 
                             "locket", "vine", "window", "statue", "tile", "hollow", "grave", "girl", "lock", 
                             "paintbrush", "grill", "tub", "windows", "chairs", "tables", "small bed", "drawers"]

        self.tw_look_objects = ["window", "sill", "east", "window", "west", "south", "pry", "bar", "pad", "lock",
                                "undead", "chef", "grave", "tree", "book", "case", "north", "pocket", "watch", "left",
                                "right", "gargoyle", "music", "box", "rocking", "horse", "door", "lock", "small", "bed"]

        self.take_words = ["grab", "seize", "lift", "take"]

        self.use_words = ["use", "apply", "put", "pry", "unlock"]

        self.drop_words = ["drop", "remove", "dump", "release"]

        self.move_directions = ["north", "south", "east", "west", "up", "down", "southwest", "southeast",
                                "northwest", "northeast", "down hole", "door"]

        self.move_rooms = ["solarium", "game room", "kitchen", "dining room", "bathroom", "library",
                           "foyer", "parlor", "porch", "cellar", "servant quarters", "crypt",
                           "servant's bathroom", "dark tunnel", "red room", "child's room", "pink room",
                           "art studio", "green room", "master's quarters", "landing", "linen closet",
                           "upstairs", "downstairs", "attic", "hidden room", "gardens", "gazebo",
                           "rose garden", "downstairs bathroom", "landing", "front lawns",
                           "upstairs bathroom"]

        self.tw_rooms = ["game", "room", "dining", "servant", "quarters", "bathroom", "dark",
                         "tunnel", "red", "green", "master's", "linen", "closet", "hidden", "rose",
                         "garden", "down", "hole", "downstairs", "bathroom", "front", "lawns",
                         "upstairs", "pink"]

        self.other_commands = ["map", "inventory", "exit", "help", "save", "time"]

    def parse_args(self, rooms_list, hero):
        """
        This function takes and parses the user's input. The first valid word is the command, which is used to
        call the appropriate parse_command function.

        Parameters
        ----------
        rooms_list - A copy of each room in the house
        hero - a copy of the hero

        Returns
        -------
        : command, which is a dictionary with all the valid words the player typed, parsed by the appropriate
        parse_command function.
        """

        # Get user input. Make it lowercase and split it.
        print()
        split_args = input('                    > ').lower().split()

        command = []  # holds the parsed commands

        # Pick out only the valid words
        for i in split_args:
            if i in self.move_directions or i in self.move_rooms or i in self.tw_rooms or \
                    i in self.move_words or i in self.look_words or i in self.tw_look_objects or \
                    i in self.take_words or i in self.look_objects or i in self.drop_words or \
                    i in self.other_commands or i in self.use_words:
                command.append(i)

        # Print an error if no words were valid.
        if len(command) == 0:
            self.print_output("Error. Invalid command passed.")
            return "badcommand"

        elif len(command) == 1 and (command[0] in self.move_directions or command[0] in self.move_rooms):
            command.append(command[0])
            self.parse_move(command, hero, rooms_list)

        elif len(command) == 2 and command[0] in self.tw_rooms and command[1] in self.tw_rooms:
            command.insert(0, "move")
            self.parse_move(command, hero, rooms_list)

        elif command[0] in self.move_words:
            command = self.parse_move(command, hero, rooms_list)

        elif command[0] in self.look_words:
            command = self.parse_look(command, split_args)

        elif command[0] in self.use_words:
            command = self.parse_use(command)

        elif command[0] in self.drop_words:
            command = self.parse_drop(command)

        elif command[0] in self.take_words:
            command = self.parse_take(command)

        elif command[0] == "exit":
            sys.exit(0)

        elif command[0] == "help":
            self.get_help(command)

        elif command[0] == "time":
            command[0] = "look"
            command.append("pocketwatch")
            self.parse_look(command, split_args)

        elif command[0] not in self.other_commands:
            self.print_output("Bad command passed.")
            return "badcommand"

        # Return the parsed command.
        return command

    def parse_move(self, command, hero, rooms_list):
        """
        This function handles the movement logic based on the input string parameters
        ----------
        command - the valid words the user entered
        hero - a copy of the hero (for getting the room location)
        rooms_list - a copy of each room in the game (for getting the valid rooms a player can move to)

        Returns
        -------
        command - the parsed argument with either a valid direction or a bad command, which throws an error.
        """
        command[0] = "move"
        dir_name = []  # holds valid directions and the corresponding room names

        # Get the room list for matching strings
        current_room = rooms_list[hero.location]

        # Add the direction and room name to the direction_name list
        for i in self.move_directions:
            if i in current_room.directions:
                dir_name.append(i)
                dir_name.append(rooms_list[current_room.directions[i]].name.lower())

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
                    command[1] = dir_name[idx - 1]

            # Check to see if it's a two-word room
            # and both are in the two-word room dictionary
            elif len(command) == 3 and command[1] in self.tw_rooms and command[2] in self.tw_rooms:

                # Concatenate the strings for further parsing
                two_words = command[1] + ' ' + command[2]

                # Set the command if the concatenated words are valid.
                if two_words in dir_name:
                    command[1] = two_words

                    # Get the index of the valid room or direction.
                    idx = dir_name.index(two_words)

                    # If it's even, it's already a direction.
                    if idx % 2 != 0:
                        # Otherwise grab the index of the correct direction.
                        command[1] = dir_name[idx - 1]

            # Print an error if an invalid room name was passed.
            else:
                self.print_output("Invalid room name or direction given.")
                return "badcommand"

        return command

    def parse_look(self, command, split_args):
        """
        This function handles the logic for the look command
        ----------
        command - the valid words the user entered
        split_args - all the words the player entered. Used for checking the number of items the player entered.

        Returns
        -------
        command - the parsed argument with the item or feature the player will look at. Returns badcommand if the item
        is invalid or cannot be looked at.
        """

        if len(command) == 1:
            command[0] = "look"

            if len(split_args) > 1:
                self.print_output("Error. Cannot look at invalid object.")
                return "badcommand"

        elif len(command) == 2:
            if command[1] not in self.look_objects:
                self.print_output("Error. Cannot look at invalid object.")
                return "badcommand"

        elif len(command) >= 3:
            temp_word = command[1] + " " + command[2]
            if temp_word not in self.look_objects:
                self.print_output("Error. Cannot look at invalid object.")
            else:
                command[1] = temp_word
                while len(command) > 2:
                    command.pop()

        if command[1] == "drawers":
            command[1] = "drawer"

        return command

    def parse_use(self, command):
        """
        This function parses the valid words for the use command.

        Parameters
        ----------
        command - The valid words that the player entered.

        Returns
        -------
        command - the parsed, valid arguments for the use command. Returns a badcommand if invalid items are passed with
        the use command.
        """
        command[0] = "use"

        if len(command) < 3:
            self.print_output("Too few arguments passed with use command.")
            return "badcommand"

        elif len(command) == 3:
            if command[1] not in self.look_objects or command[2] not in self.look_objects:
                self.print_output("Error. Invalid objects passed.")
                return "badcommand"

        elif len(command) == 4:
            if command[1] + " " + command[2] in self.look_objects:
                command[1] = command[1] + " " + command[2]
            elif command[2] + " " + command[3] in self.look_objects:
                command[2] = command[2] + " " + command[3]
            else:
                self.print_output("Invalid object passed with use command")
                return "badcommand"
            while command > 3:
                command.pop()

        elif len(command) == 5:
            if command[1] + " " + command[2] not in self.look_objects:
                self.print_output("Invalid object passed with use command")
                return "badcommand"
            else:
                command[1] += " " + command[2]

            if command[3] + " " + command[4] not in self.look_objects:
                self.print_output("Invalid object passed with use command")
                return "badcommand"
            else:
                command[2] = command[3] + " " + command[4]

        else:
            self.print_output("Error. Too many arguments with use command.")
            return "badcommand"

        return command

    def parse_drop(self, command):
        """
        This function parses the items for the drop command.
        Parameters
        ----------
        command - All the valid words the player entered.

        Returns
        -------
        command - the parsed result of the items for the drop command. badcommand is returned if the item cannot be
        dropped.
        """
        command[0] = "drop"

        if len(command) == 1:
            self.print_output("Error. Invalid or no item to drop.")
            return "badcommand"

        if len(command) == 2:
            if command[1] not in self.look_objects:
                self.print_output("Error. Cannot drop " + command[1])
                return "badcommand"

        elif len(command) > 2:
            temp_word = command[1] + " " + command[2]
            if temp_word not in self.look_objects:
                self.print_output("Error. Invalid item cannot be dropped.")
                return "badcommand"
            else:
                command[1] = temp_word
                while len(command) > 2:
                    command.pop()

        return command

    def parse_take(self, command):
        """
        This function parses the arguments for the take command.
        Parameters
        ----------
        command - All the valid words the player entered.

        Returns
        -------
        command - the parsed, valid items the player can take. Returns badcommand if the item cannot be taken.
        """
        command[0] = "take"

        if len(command) < 2:
            self.print_output("Invalid item name.")
            return "badcommand"

        elif len(command) == 2:
            if command[1] not in self.look_objects:
                self.print_output("Invalid object cannot be taken.")
                return "badcommand"

        elif len(command) == 3:
            if command[1] + " " + command[2] not in self.look_objects:
                self.print_output("Invalid object cannot be taken.")
                return "badcommand"
            else:
                command[1] += " " + command[2]

        if len(command) > 3:
            self.print_output("Error. Too many arguments passed.")

        if command[1] == "box":
            command[1] = "ashes"

        return command

    def get_help(self, helpList):
        """
        This function prints help for the player on the screen. Displays general help instructions or detailed
        instructions for each action a player can take based on their input.

        Parameters
        ----------
        helpList - Modifiers that will determine which help screen is shown

        Returns
        -------
        Nothing
        """
        if len(helpList) == 1:
            print()
            self.print_output("The goal of the game is to explore the mansion. Through interacting with various objects and features, the player will learn the deep history that surrounds the haunted mansion. Not all clues are helpful! There are many ways to win and lose this game. Can you solve the mystery, or will you meet your demise?")
            print()

            self.print_output("For more detailed instructions regarding a specific command, enter \"help [Your_Command_Here]\"")
            print()

            self.print_output("Valid commands are: take, drop, map, inventory, look, move, and use.")

        else:
            if helpList[1] == 'take':
                print()
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
                self.print_output(
                    "The drop command allows the player to drop an item from their inventory to the room they are currently standing in. To call the drop function, a player enters a valid drop command followed by a valid object in their inventory.")
                print()

                self.print_output(
                    "Valid words that could be used for the \"drop\" command are: drop remove, dump, and release.")
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

    def print_output(self, string):
        wrappedText = textwrap.wrap(string, width=83)
        for i in wrappedText:
            print("                    " + i)
