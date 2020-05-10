import textwrap

class Language_Parser:

    def __init__(self):
        # Dictionaries for each of the possible directions and rooms to move to.
        self.move_words = ["go", "walk", "move", "jaunt", "run", "step", "stroll", "march", "travel", "proceed",
                           "sprint", "jog"]

        self.look_words = ["look", "glance", "eye", "peak", "view", "stare", "peer", "study", "examine"]

        self.look_objects = ["windowsill", "crystal", "corner", "east window", "south window", "west window", "toys",
                             "prybar", "pry bar", "ashes", "workbench", "shelves", "box", "padlock", "coffin",
                             "undead chef", "painting", "dog", "table", "mirror", "armor", "clock", "stone", "shears",
                             "garden", "tree", "grave tree", "fireplace", "pool", "window", "plank", "axe", "vision",
                             "bed", "glint", "chef", "knife", "drawer", "sink", "key", "piano", "book", "bookcase",
                             "north window", "pistol", "apparition", "sack", "pocketwatch", "pocket watch",
                             "poltergeist",
                             "couch", "fireplace", "table", "easel", "loom", "left gargoyle", "right gargoyle", "paint",
                             "music box", "bed", "rocking horse", "rose", "spade", "fountain", "roses", "hair",
                             "door lock", "shelf", "toilet", "sink", "mirror", "journal", "locket", "vine", "window",
                             "statue", "tile", "hollow", "grave", "girl", "lock", "paintbrush"]

        self.tw_look_objects = ["window", "sill", "east", "window", "west", "south", "pry", "bar", "pad", "lock",
                                "undead", "chef", "grave", "tree", "book", "case", "north", "pocket", "watch", "left",
                                "right", "gargoyle", "music", "box", "rocking", "horse", "door", "lock", "small", "bed"]

        self.take_words = ["grab", "seize", "lift", "take"]

        self.use_words = ["use", "apply", "put"]

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

        self.other_commands = ["map", "inventory", "exit", "help", "save"]

    def parse_args(self, rooms_list, hero):
        # Get user input. Make it lowercase and split it.
        split_args = input('            > ').lower().split()

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

        # Set the command to 'move' if it's in move_words.
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

        elif command[0] not in self.other_commands:
            self.print_output("Bad command passed.")
            return "badcommand"

        # Return the parsed command.
        return command

    def parse_move(self, command, hero, rooms_list):
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

        return command

    def parse_use(self, command):
        command[0] = "use"

        if len(command) < 3:
            self.print_output("Error. Invalid objects passed.")
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
        command[0] = "take"

        if len(command) < 2:
            print("Invalid item name.")
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

        return command

    def print_output(self, string):
        wrapped_text = textwrap.wrap(string, width=74)
        for i in wrapped_text:
            print('            ' + i)
