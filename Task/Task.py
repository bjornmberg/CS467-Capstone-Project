import os
import math
import time
from Item import Item
from Room import Room
from Feature import Feature
import textwrap
from Wrapper import wrapper

class Task:
    """Class used to represent an action within the Game

    Attributes
    ----------
    none

    Methods
    -------
    perform_task()
        calls the appropriate Task based on Item/Feature combinations
    perform_task_on_move()
        specific Task linked to a move operation
    perform_task_on_look()
        specific Task linked to a look operation
    Multiple Item/Feature Combination Tasks
    """
    def perform_task(self, item, feature, rooms):
        """Class a function to perform an action based on Item/Feature combination

        :param Item item: the Item being used in the Task
        :param Feature feature: the Feature (if any) being used in the Task
        :param list rooms: the room_list from Game to modify the Game state
        :return: bool - True for successful action, False for unsuccessful
        """
        # Perform check to determine if this is task driven by taking an item alone
        if feature is None:
            # Part of game winning sequence A
            if item.name == 'paintbrush':
                status =  self.paintbrush_task(rooms)
            # Part of game winning sequence B
            elif item.name == 'knife':
                status =  self.knife_task(rooms)
            # Part of game winning sequence B
            elif item.name == 'book':
                status =  self.book_task(rooms)
            # Part of game winning sequence B
            elif item.name == 'locket':
                status =  self.locket_task(rooms)
            # Part of game winning sequence B
            elif item.name == 'shears':
                status =  self.shears_task(rooms)
            # Part of game losing sequence A
            elif item.name == 'journal':
                status =  self.journal_task(rooms)
            # Part of game losing sequence A
            elif item.name == 'pistol':
                status =  self.pistol_task(rooms)
            # Part of game losing sequence B
            elif item.name == 'axe':
                status =  self.axe_task(rooms)
            return False
        status = False

        # Check that the Feature is usable
        if feature.usable:

            # check it there is a valid Feature/Item combination and call that function
            # Part of game winning sequence A
            if item.name == 'paintbrush' and feature.name == 'easel':
                status = self.easel_task(feature, rooms)
            # Part of game winning sequence A
            elif item.name == 'prybar' and feature.name == 'plank':
                status = self.prybar_plank_task(feature, rooms)
            # Part of game winning sequence A
            elif item.description == 'A small ornate key.' and feature.name == 'drawer':
                status = self.key_drawer_task(feature, rooms)
            # Part of game winning sequence A
            elif item.name == 'prybar' and feature.name == 'padlock':
                status = self.prybar_padlock_task(feature, rooms)
            # Part of game winning sequence A
            elif item.name == 'knife' and feature.name == 'chef':
                self.knife_chef_task(feature, rooms)
            # Part of game winning sequence A
            elif item.name == 'crystal' and feature.name == 'statue':
                status =  self.crystal_statue_task(feature, rooms)
            # Part of game winning sequence B
            elif item.name == 'shears' and feature.name == 'vine':
                status = self.shears_vine_task(feature, rooms)
            # Part of game winning sequence B
            elif item.name == 'spade' and feature.name == 'grave':
                status = self.spade_task(feature, rooms)
            # Part of game winning sequence B
            elif item.name == 'locket' and feature.name == 'grave':
                status = self.locket_grave_task(feature, rooms)
            # Part of game winning sequence B
            elif item.name == 'stone' and feature.name == 'grave':
                status = self.stone_task(feature, rooms)
            # Part of game winning sequence B
            elif item.name == 'rose' and feature.name == 'girl':
                status = self.rose_task(feature, rooms)
            # Part of game losing sequence A
            elif item.name == 'ashes' and feature.name == 'fireplace':
                self.ashes_fireplace_task(feature, rooms)
            # Part of game losing sequence B
            elif item.name == 'axe' and feature.name == 'armor':
                status =  self.axe_armor_task(feature, rooms)
            # Part of game losing sequence B
            elif item.description == 'A simple key.' and feature.name == 'lock':
                status = self.key_task(feature, rooms)
            # Part of game losing sequence B
            elif item.name == 'hair' and feature.name == 'chef':
                self.hair_task(feature, rooms)
            else:
                # No valid combination
                status = False
        # Feature is not usable
        return status

    def perform_task_on_move(self, inventory, rooms_list, next_room_index):
        """Solves specific action associated with moving within the Game

        :param Inventoty inventory: the Game inventory
        :param list rooms_list: the Game.room_list
        :param int next_room_index: the room_id of the Room being moved to
        :return: bool True/Successful, False/Unsuccessful
        """
        status, item = inventory.in_inventory('journal')
        if next_room_index == 12 and status:
            self.journal_greenroom_task(rooms_list, next_room_index)
            return True
        return False

    def perform_task_on_look(self, thing_description, rooms, time):
        """Solves specific action associated with a look action

        :param str thing_description: a description of an Feature being looked at
        :param list rooms: the Game.rooms_list
        :param int time: the in-game time
        :return: bool True/Successful, False/Unsuccessful
        """
        if thing_description == 'You look closer at the dog. It\'s got three heads and glowing, red eyes! You feel a shiver and sense of revulsion, which thankfully passes quickly.':
            self.dog_easel_task(rooms)
            return True
        elif thing_description == 'A beautiful vintage pocketwatch.':
            if time < 12:
                if time == 0:
                    self.print_output('The time is currently midnight.')
                elif time < 1.0:
                    self.print_output('The time is half past midnight.')
                else:
                    meridiem = ' am.'
                    # Calculate if half hour
                    if ((time * 10) % 10 != 0):
                        time = math.floor(time)
                        self.print_output('The time is currently {}'.format(time) + ':30' +meridiem)
                    # Else on the hour
                    else:
                        time = math.floor(time)
                        self.print_output('The time is currently {}'.format(time) + ':00' + meridiem)
            else:
                meridiem = ' pm.'
                if time >= 13.0:
                    time = time - 12.0
                # Calculate if half hour
                if ((time * 10) % 10 != 0):
                    time = math.floor(time)
                    self.print_output('The time is currently {}'.format(time) + ':30' +meridiem)
                # Else on the hour
                else:
                    time = math.floor(time)
                    self.print_output('The time is currently {}'.format(time) + ':00' + meridiem)
        elif thing_description == 'You look at the magnificent old clock. Somehow, it\'s still working.':
            if time < 12:
                if time == 0:
                    self.print_output('The time is currently midnight.')
                elif time < 1.0:
                    self.print_output('The time is half past midnight.')
                else:
                    meridiem = ' am.'
                    # Calculate if half hour
                    if ((time * 10) % 10 != 0):
                        time = math.floor(time)
                        self.print_output('The time is currently {}'.format(time) + ':30' +meridiem)
                    # Else on the hour
                    else:
                        time = math.floor(time)
                        self.print_output('The time is currently {}'.format(time) + ':00' + meridiem)
            else:
                meridiem = ' pm.'
                if time >= 13.0:
                    time = time - 12.0
                # Calculate if half hour
                if ((time * 10) % 10 != 0):
                    time = math.floor(time)
                    self.print_output('The time is currently {}'.format(time) + ':30' +meridiem)
                # Else on the hour
                else:
                    time = math.floor(time)
                    self.print_output('The time is currently {}'.format(time) + ':00' + meridiem)
        elif thing_description == 'You look at the ^sack#, and see an ^apparition# appear.':
            self.sack_apparition_task(rooms)
            return True
        elif thing_description == 'You notice something barely sticking out of the hollow.':
            self.hollow_task(rooms)
            return True
        return False

    def perform_task_on_day(self, day):
        # One day has passed. output warning to the user.
        if day == 1:
            self.print_output('You hear a voice in your head. It sounds like the poltergeist.\n\n"...one day has now passed. What have you accomplished?\n\nYou have two days left. After that... you will be here forever.\n"')
        # Two days have passed. Output last warning to user
        if day == 2:
            self.print_output('You hear a voice in your head. It\'s the poltergeist again...\n\n"...two days have now come and gone.\n\nYou have one day left.\nHurry... I will not warn you again.\n"')
        # Three days have passed. Commence end_game based on expiration of time limit
        if day == 3:
            self.end_game(None, None)
    # THE BELOW TASKS ARE ALL ASSOCIATED WITH ACTIONS WITHIN THE GAME
    # DUE TO THE NUMBER OF THEM AND THE FACT THAT THEY ARE ALL SIMILIAR
    # DOCSTRINGS ARE NOT PROVIDED

    # This is part of game winning sequence A - dispatch undead chef staker
    def dog_easel_task(self, rooms):
        # Set the easel to usable and actionable
        rooms[10].features[0].actionable = True
        rooms[10].features[0].usable = True
        rooms[10].features[0].pre_action_des = 'This easel holds a blank canvas. There are also oil paints and a @paintbrush# next to it. You feel compelled to paint.'
        # Change the pink room description to reflect the easel and paint ready to use
        rooms[10].long_des = 'You are in the pink room. The easel is near the window, and a @paintbrush# stands ready nearby on the ^table#. You feel compelled to paint something on the easel. A small and steep staircase leads $up# into the attic. A door to the $West# leads to the red room. Another door to the $East# leads to the green room.'
        rooms[10].features[2].state = 1
        rooms[10].visited = False

    # This is part of game winning sequence A - dispatch undead chef staker
    def paintbrush_task(self, rooms):
        # Paintbrush taken. Set new state of table
        rooms[10].features[2].state = 2
        return True

    # This is part of game winning sequence A - dispatch undead chef staker
    def easel_task(self, feature, rooms):
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2
        # "Hear sound elsewhere output"
        self.print_output('You hear piano music playing from somewhere to the South.')
        # Change the landing description to reflect the playing piano
        rooms[11].long_des = 'You are on the second floor landing of the house. A grand ^piano# is here, playing music on it\'s own. A ^window# faces south, overlooking the lawns. There is a staircase spiraling $down# to the foyer below. A door to the $Northeast# leads to the green room. A door to the $Southeast# leads to a bath. There is also a door to the $Southwest# heading to a linen closet, and a door to the $Northwest# going to the red room.'
        rooms[11].visited = False
        # Change the state of the piano to reflect the playing tune
        rooms[11].features[0].state = 1

        return True

    # This is part of game winning sequence A - dispatch undead chef staker
    def key_drawer_task(self, feature, rooms):
        feature.state = 1
        self.print_output(feature.get_description())
        # Change the room short description and reprint the room description
        rooms[7].short_des = 'You are in the Mansion\'s kitchen. The door to the North goes to the Rose Garden. The door to the East is the formal Dining Room. There are stairs leading down.  There is also a row of drawers along the Northern wall. One drawer unlocked and now open.'
        rooms[7].visited = True
        return True

    # This is part of game winning sequence A - dispatch undead chef staker
    def knife_task(self, rooms):
        # Knife taken. Set new state of drawer
        rooms[7].features[1].state = 2
        # Set descriptions of crypt to include the shining knife
        rooms[17].long_des = 'You find yourself in a crypt. The light is very faint here - some comes from the crystal in the tunnel. There is some light seeming to come from the walls and floor also though, some dots of phosphorescence in tiny drops of water. The walls appear to be old wood. The air is thick with a stench of decay here. It’s a little hard to breathe. In the center of the room is a large rectangular crate, made of dark wood plans. A chain wraps around it and a heavy ^padlock# lies utop the box. The crate looks a bit like a ^coffin#. The markings on your ~knife# are shining lightly. There is a $door# leading back to the tunnel.'
        rooms[17].short_des = 'You are standing in the crypt below the mansion. There is a rank, foul odor on the air here. A large rectangular crate, much like a ^coffin#, dominates the center of the room. Your ~knife# is shining lightly in the darkness. There is a $door# leading back to the tunnel.'
        # Set the feature description of the chef to include shining knife
        rooms[17].features[2].pre_action_des = 'The glowing green eye of the ^chef# seems to track you, but the chef is otherwise still. The markings on your ~knife# are glowing.'
        # Set the feature description of the padlock to include shining knife
        rooms[17].features[1].in_action_des = 'You pry the ^padlock# open. The steel shatters as you apply all of the force you can muster.\n\nYou push the ^coffin# lid to the side. The markings on your ~knife# glow more strongly now.'
        return True

    # This is part of game winning sequence A - dispatch undead chef staker
    def prybar_plank_task(self, feature, rooms):
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2

        rooms[18].long_des = 'You are standing in the gazebo. You have uncovered a tunnel under the gazebo... it heads $down# into darkness. There is a sweet and sour smell on the air here, like something good has turned. A ^grill# stands in the corner. To the $West# are the rose gardens.'
        rooms[18].short_des = 'You are standing in the gazebo. There is a sweet and sour smell on the air here, like something good has turned. A ^grill# stands in the corner. To the $West# are the rose gardens. A tunnel heads $down# into darkness below the gazebo.'
        rooms[18].visited = False
        rooms[18].directions['down'] = 24

        return True

    # This is part of game winning sequence A - dispatch undead chef staker
    def crystal_statue_task(self, feature, rooms):
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2

        rooms[24].long_des = 'The tunnel is now illuminated by the crystal. You see that the tunnel continues further $down# into the darkness. You can also go back $up# to the gazebo. The ^statue# is now holding the crystal.'
        rooms[24].short_des = 'The tunnel is now illuminated by the crystal. You see that the tunnel continues further $down#. You can also go back $up# to the gazebo.'
        rooms[24].visited = False
        rooms[24].directions['down'] = 17

        return True

    # This is part of game winning sequence A - dispatch undead chef staker
    def prybar_padlock_task(self, feature, rooms):
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2

        rooms[17].features[0].state = 1

        rooms[17].long_des = 'You are standing in the crypt below the mansion. Having pried the ^padlock# loose, the ^coffin# now stands open. The undead ^chef# is within, pale and tracking you with one green glowing eye. Your ~knife# is shining in the dark. There is a $door# back to the tunnel.'
        rooms[17].visited = False

        return True

    # This is part of game winning sequence A - dispatch undead chef staker
    def knife_chef_task(self, feature, rooms):
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2
        # Pass feature and sequence letter
        self.end_game(feature, "A")

    # This is part of game winning sequence B - comfort the ghost daughter
    def book_task(self, rooms):
        # Change description of the front lawns to display the apparition of the girl
        rooms[21].long_des = 'You are on the front lawns of the mansion. The borders of the nearby flower ^garden# are of curious-looking stone.\nThere are two rows of tall trees here. Under one ^tree# you think that you can see a ^girl#... she appears to be crying.\nTo the $North# is the front porch of the house.'
        rooms[21].visited = False

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def shears_vine_task(self, feature, rooms):
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2

        rooms[3].long_des = 'You are standing in the Solarium. The air is stiflingly hot and humid. An exit leads to the $South#.'
        rooms[3].visited = False

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def locket_task(self, rooms):
        # "Hear sound elsewhere"
        self.print_output('You the sound of laughter coming from somewhere upstairs.')
        # Change the long description of the kitchen to output the vision. 
        rooms[9].long_des = 'You find yourself in what seems to be a young girl\'s room. A ^ghost# of a girl is twirling in the center of the room, laughing. She is saying something about birds splashing at a fountain. She is wearing a white dress, with white spots on it.\n\nThe vision fades. There are ^toys# about and a ^rocking horse#. A ^music box# stands upon a small ^table#.\n\nA door to the $Southeast# leads to the second floor landing. A door to the $Northwest# goes to the pink room.'
        rooms[9].visited = False
        # Change the in_action and post_action descriptions of the grave to take into account posession of the locket
        rooms[21].features[2].in_action_des = 'You dig a hole at the bottom of the tree, making a makeshift ^grave#.\n\nThe ~locket# you took from the Solarium glows in your hand now. Should you place it in the grave?'
        rooms[21].features[2].post_action_des = 'This is where you dug the ^grave#. Maybe you should place the ~locket# there?'
        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def spade_task(self, feature, rooms):
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2

        rooms[21].long_des = 'You are on the front lawns of the mansion. A ^grave# is dug at the base of a ^tree#. There is a flower ^garden# nearby bordered in strange stone. You see the mansion to the $North#.'
        rooms[21].visited = False

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def shears_task(self, rooms):
        # Change description of the front lawns to alter the apparition of the girl
        rooms[21].long_des = 'You are on the front lawns of the mansion. The borders of the nearby flower ^garden# are of curious-looking stone.\nThere are two rows of tall trees here. Under one ^tree# you think that you can see the ghost of a girl...\nTo the $North# is the front porch of the house.'
        rooms[21].short_des = 'You are on the front lawns of the mansion. The borders of the nearby flower ^garden# are of curious-looking stone.\nThere are two rows of tall trees here. Under one ^tree# you think that you can see the ghost of a girl...\nTo the $North# is the front porch of the house.'
        rooms[21].visited = False
        # Alter the girl feature
        rooms[21].features[3].pre_action_des = 'The ^girl# is crying, hovering near a tree. I wonder if this ^tree# might make a good spot for a ^grave#, a makeshift memorial of sorts.'
        rooms[21].features[3].state = 0
        # Alter the tree feature
        rooms[21].features[1].pre_action_des = 'This ^tree# seems special. You wonder if it might make a good spot for a ^grave#.'
        rooms[21].features[1].state = 0

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def locket_grave_task(self, feature, rooms):
        if feature.state != 2:
            self.print_output('You must dig the grave first')
            return False
        else:
            # Alter the description based on whether or not the player is in posession of the stone
            if rooms[21].features[0].state == 3:
                feature.in_action_des = 'You place the locket at the bottom of the grave, and fill the ^grave# in.\nThe ghost of the ^girl# is here, crying, at the head of the makeshift ^grave#. The ~stone# begins to vibrate.'
                feature.state = 1
                self.print_output(feature.get_description())
                feature.in_action_des = 'The ^grave# is filled in now. The ^girl# is here, crying, at the head of the grave. The ~stone# is vibrating.'
                feature.state = 1
            else:
                feature.in_action_des = 'You place the locket at the bottom of the grave, and fill the ^grave# in.\nThe ghost of the ^girl# is here, crying, at the head of the makeshift ^grave#.'
                feature.state = 1
                self.print_output(feature.get_description())
                feature.in_action_des = 'The ^grave# is filled in now. The ^girl# is here, crying, at the head of the grave.'
                feature.state = 1

            rooms[21].long_des = 'You are on the front lawns of the mansion. The freshly filled ^grave# is here. There is a flower ^garden# nearby. You see the mansion to the $North#.'
            rooms[21].visited = False

            return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def stone_task(self, feature, rooms):
        if feature.state != 1:
            self.print_output('You must dig the grave and place a memorial object within first')
            return False
        else:
            # Alter the description based on whether or not the player is in posession of the rose
            if rooms[19].features[1].state == 3:
                feature.in_action_des = 'You place the stone at the head of the grave. It looks right.\n\nThe ^girl# is still here, crying. Her hand is outstretched.\nHer dress is white with red splatters. The colors of the ~rose# seem to get more vibrant, almost blindingly so.'
                feature.state = 1
                self.print_output(feature.get_description())
                feature.post_action_des = 'The ^grave# is filled in now. The ^girl# is here, crying, hand outstretched. Her dress is white, spattered in red. The ~rose# is very bright now.'
                feature.state = 2
            else:
                feature.in_action_des = 'You place the stone at the head of the grave. It looks right.\n\nThe ^girl# is still here, crying. Her hand is outstretched.\nHer dress is white with red splatters.'
                feature.state = 1
                self.print_output(feature.get_description())
                feature.post_action_des = 'The ^grave# is filled in now. The ^girl# is here, crying, hand outstretched. Her dress is white, spattered in red.'
                feature.state = 2
            # Revise the state of the girl to usable for final interaction
            # Move this into a conditional that checks for stone, locket, and spade complete
            rooms[21].features[3].usable = True
            rooms[21].long_des = 'You are on the front lawns of the mansion. The ^grave# is here, with the crying ^girl# above, holding out her hand. There is a flower ^garden# nearby. You see the mansion to the $North#.'
            rooms[21].visited = False

            return True

    # This is part of game winning sequence B - comfort the ghost daughter
    # When the player uses the rose on the girl, end_game is triggered:
    def rose_task(self, feature, rooms):
        feature.in_action_des = 'You place the rose in the hand of the girl.\n\nThe girl stops crying, and looks up at you.\n\nShe says... "thank you".'
        feature.state = 1

        self.end_game(feature, "B")

        return True

    # This is part of game losing sequence A - attempt to fight the poltergeist
    def journal_task(self, rooms):
        # Revise description of landing to include apparition entering the linen closet
        rooms[11].long_des = 'You are on the second floor landing of the house. A grand ^piano# occupies much of the floor space here. A ^window# faces south, overlooking the lawns. There is a staircase spiraling $down# to the foyer below. You think you see a glowing figure going into the doorway to the $Southwest#, into the linen closet. A door to the $Northeast# leads to the greenroom. A door to the $Southeast# leads to a bath. There is also a door to the $Northwest# going to the red room.'
        rooms[11].visited = False

        return True

    # This is part of game winning sequence A - dispatch undead chef staker
    def sack_apparition_task(self, rooms):
        # Change the pre_action_des of the sack to indicate the updated description on witnessing the apparition
        rooms[8].features[1].pre_action_des = 'You look at the ^sack# again. You think that you see an ^apparition#...'

    # This is a part of game losing sequence A - attempt to fight the poltergeist
    def pistol_task(self, rooms):
        # "Hear sound elsewhere"
        self.print_output('You hear what sounds like pans banging, followed by a loud bang downstairs.')
        # Change the long description of the kitchen to output the vision.
        rooms[7].long_des = 'You are standing in the kitchen. A vision washes before your eyes. You see the servant, he is standing with his back to you, shouting at Chef Staker. The ^Chef# is swinging a pan at the servant. There is a bang.\n\nThe servant has shot the Chef in the eye, and the Chef falls to the floor.\n\nThe door to the $North# goes to the Rose Garden. The door to the $East# is the formal Dining Room. There are stairs leading $down#.  There is also a row of drawers along the Northern wall. One ^drawer# has a lock.'
        rooms[7].visited = False
        # Change the state of the apparition to indicate pistol taken
        rooms[8].features[0].state = 2
        return True

    # This is a part of game losing sequence A - attempt to fight the poltergeist
    # When the player uses ashes on the fireplace, end_game is triggered:
    def ashes_fireplace_task(self, feature, rooms):
        os.system('clear')
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2

        self.end_game(feature, "A")

    # This is part of game losing sequence B - attempt to comfort undead chef staker
    def journal_greenroom_task(self, rooms, green_room_index):
        # Change the long description of the green room to output the vision.
        rooms[green_room_index].long_des = 'As you walk into master\'s bedroom your vision blurs and sound washes over you. You see the Chef, yelling something, waving an axe and chasing a woman and a man about the room. The woman and man are running, screaming. Your head swims, and the scene fades.\n\nAs you regain your senses you see a ^glint# of light reflected on the ceiling above the ^bed#. You hear a crashing sound to the South, from the direction of the bath. There is a door to the $Southwest# that leads back to the second floor landing. A door to the $Northwest# leads to the pink room.'
        rooms[green_room_index].visited = False
        # Change the long description of the second floor bathroom so floor tile is on the floor now
        rooms[22].long_des = 'You are standing in a bathroom. One of the tiles has fallen to the floor. You see a ^hollow# in the wall where the tile was previously, near the ^tub#.  A door to the $West# exits to the landing.'
        rooms[22].visited = False

        return True

    # This is part of game losing sequence B - attempt to comfort undead chef staker
    def axe_task(self, rooms):
        # Axe taken. Set new state of glint
        rooms[12].features[1].state = 3
        # Set descriptions of green room to remove the glint
        rooms[12].long_des = 'You find yourself in the master’s bedroom. The walls are a deep green. There is a door to the $Southwest# that leads back to the second floor landing. A door to the $Northwest# leads to the pink room. There is a large ^bed# dominating the room.'
        rooms[12].short_des = 'You are in the green room, which was the master’s quarters. A door to the $Southwest# leads to the second floor landing. A door to the $Northwest# goes to the pink room. There is a large ^bed# dominating the room.'
        return True

    # This is part of game winning sequence A - dispatch undead chef staker
    def hollow_task(self, rooms):
        rooms[22].features[0].state = 1
        self.print_output(rooms[22].features[0].in_action_des)

    # This is part of game losing sequence B - attempt to comfort undead chef staker
    def key_task(self, feature, rooms):
        # Unlock the door
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2
        # Change the description of the servant's quarters to reflect the open door and open East as a direction the player can travel
        rooms[15].long_des = 'You are in the servant’s dwelling. There is a small ^table# and chairs in a nearby corner. A stack of books sits on top of the table. To the $North# is the cellar. To the $East# is a bathroom door which now stands open.'
        rooms[15].short_des = 'You are in the servant’s quarters. A ^table# stands nearby with books stacked upon it. A ^small bed# occupies the space opposite. A door to the $North# returns to the cellar proper. To the $East# a door to a bathroom stands open.'
        rooms[15].visited = False
        rooms[15].directions['east'] = 16

        return True

    # This is part of game losing sequence B - attempt to comfort undead chef staker
    def axe_armor_task(self, feature, rooms):
        feature.state = 1
        self.print_output(feature.get_description())
        feature.state = 2
        # If the attic has been visited, or not, revise accordingly to describe new room in appropriate manner
        if rooms[13].visited == True:
            rooms[13].long_des = 'You are standing in the attic. Everything remains as it was with one exception: the boards around the walled in area have fallen exposing the entrance to a hidden room to the $southeast#. There are stairs leading $down# to the pink room. One ^windowsill# among the others catches your eye.'
            rooms[13].short_des = 'You are in the attic of the mansion. One ^windowsill# in particular catches your eye. A steep staircase leads back $down# to the pink room below. A newly opened entrance to a hidden room is to the $southeast#.'
        else:
            rooms[13].long_des = 'You are standing in the attic. You notice in one corner of the attic some boards have fallen, revealing what seems to be a new path to a small room to the $Southeast#. There are stairs leading $down# to the pink room. One ^windowsill# among the others catches your eye.'
            rooms[13].short_des = 'You are in the attic of the mansion. One ^windowsill# in particular catches your eye. A steep staircase leads back $down# to the pink room below. To the $Southeast# is an entrance to a small room, wood boards fallen around it seeming to indicate this is a new path.'
        rooms[13].visited = False
        rooms[13].directions['southeast'] = 23

        return True

    # This is a part of game losing sequence B - attempt to comfort undead chef staker
    # When the player uses lock of hair on the chef, end_game is triggered:
    def hair_task(self, feature, rooms):
        os.system('clear')
        feature.state = 1
        self.print_output(feature.get_description())
        self.end_game(feature, "B")

    # Method handler for end_game choices and interactions. Could be a different class
    def end_game(self, feature, sequence):
        # Check for expiration of time losing sequence
        if feature is None and sequence is None:
            os.system('clear')
            self.print_output('\n')
            self.print_output('\n\n\nThe scene before you vanishes in a haze and the poltergeist appears before you.\n\nI told you that you had two days to resolve matters here. You have failed.\n\nIt is time...\n\n')
            time.sleep(7)
            self.print_output('You find yourself in the servant\'s quarters. You look down at yourself, and see you are wearing a tattered servant\'s suit.\n\nYou can\'t see your feet or your hands clearly, they are hazy, and you can see through them.\n\nYou feel cold, very cold.')
            time.sleep(7)
            self.print_output('\n\nThe hear laughter of the poltergeist, first strongly, then fading away.\n\nYou are horrified to realize this is your new home.')
            time.sleep(7)
            os.system('clear')
            print('\nThank you for playing. You have lost.\n')
            exit()

        # end_game sequence for Game Winning Sequence A
        if feature.name == 'chef' and sequence == 'A':
            os.system('clear')
            self.print_output('\n')
            self.print_output(feature.get_description())
            time.sleep(7)
            self.print_output('\n\n\nThe chef immediately begins to vaporize into green smoke.\nYou hear the poltergeist\'s voice as the chef disappears.\n\n"Thank you"\n\nYou know things will be OK.')
            time.sleep(7)
            os.system('clear')
            print('\nThank you for playing. You have won the game.\n')
            exit()

        # end_game sequence for Game Winning Sequence B
        if feature.name == 'girl' and sequence == 'B':
            os.system('clear')
            self.print_output('\n')
            self.print_output(feature.get_description())
            time.sleep(7)
            self.print_output('\n\n\nThe girl fades away.\nYou stand there for a minute, staring into the distance at the mansion. You\'re not sure how but you know things will be OK.')
            time.sleep(7)
            os.system('clear')
            print('\nThank you for playing. You have won the game.\n')
            exit()

        # end_game sequence for Game Losing Sequence A
        if feature.name == 'fireplace' and sequence == 'A':
            selection = -1
            while selection not in (1, 2):
                self.print_output('\nYou have a choice to make... \n "1" You attempt to fight the enraged poltergeist, shooting the pistol again. \n "2" In a panic you throw the rest of the ashes into the fire.\n\n')
                selection = int(input((' ' * 20) + 'What will it be? '))
            # If selection 1, output the appropriate losing message and exit the game
            if selection == 1:
                os.system('clear')
                self.print_output('\n\nYou shoot the poltergeist again and again, pulling the trigger over and over until the gun is empty.\nThe poltergeist laughs terribly.\n\n')
                time.sleep(7)
                self.print_output('The last thing you see is the ghost rushing toward you in a blur.\n\nThere is no pain.')
                time.sleep(7)
                os.system('clear')
                print('\nThank you for playing. You have lost.\n')
                exit()
            # Elif selection 1, output the appropriate losing message and exit the game
            elif selection == 2:
                os.system('clear')
                self.print_output('\n\nThe fireplace explodes in a violent burst of flames, casting you across the room.\n\nYou are lying the floor, and vaguely you see the flames are... everywhere now.\nYou hear the poltergeist shrieking. The mansion is engulfed in the subsequent inferno.\n\n')
                time.sleep(7)
                self.print_output('You are no more, but neither is the horror of the mansion.')
                time.sleep(7)
                os.system('clear')
                print('\nThank you for playing. You have lost.\n')
                exit()

        # end_game sequence for Game Losing Sequence B
        if feature.name == 'chef' and sequence == 'B':
            os.system('clear')
            self.print_output('\n')
            self.print_output(feature.get_description())
            time.sleep(7)
            self.print_output('\n\nIn the moments before all fades to black you know you\'ve made a grave mistake.\nYou are thrown backward and hit the floor.\n\nThe last thing you see is the chef\'s enraged face, filling all you can see.')
            time.sleep(7)
            os.system('clear')
            print('\nThank you for playing. You have lost.\n')
            exit()

    # Add a print_output function, similar to game.py. Includes newline handling
    def print_output(self, string):
        print()

        # Check for newlines & bold or character signifiers
        if ('\n' in string) or ('@' in string) or ('^' in string) or ('$' in string) or ('#' in string):
            processed = wrapper.wrap_processor(string)
            # Output the string
            for i in processed:
                print(i)

        # Else no newlines or bold color signifiers. Simple processing.
        else:
            print(textwrap.fill('{}'.format(string), 100, initial_indent=(' ' * 20), subsequent_indent=(' ' * 20)))
