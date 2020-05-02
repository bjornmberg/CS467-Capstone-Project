import os
import time
from Item import Item
from Room import Room
from Feature import Feature

class Task:


    # This is called from Game when a user attempts the command 'use Item Feature'
    # This takes in the Item, the Feature, and the rooms_list and calls the correct
    # task. It will return the status of the task function if there is a workable
    # combination, or return False if there is no workable combination.
    def perform_task(self, item, feature, rooms):

        # Perform check to determine if this is task driven by taking an item alone
        if feature is None:
            # Part of game losing sequence B
            if item.name == 'pistol':
                status =  self.pistol_task(rooms)
            # Part of game winning sequence B
            elif item.name == 'book':
                status =  self.book_task(rooms)
            # Part of game winning sequence B
            elif item.name == 'locket':
                status =  self.locket_task(rooms)
            return False

        status = False

        # Check that the Feature is usable
        if feature.usable:

            # check it there is a valid Feature/Item combination and call that function
            if item.name == 'axe' and feature.name == 'armor':
                status =  self.axe_amor_task(feature, rooms)
            elif item.name == 'prybar' and feature.name == 'plank':
                status = self.prybar_plank_task(feature, rooms)
            elif item.name == 'crystal' and feature.name == 'statue':
                status =  self.crystal_statue_task(feature, rooms)
            # Part of game losing sequence B
            elif item.name == 'ashes' and feature.name == 'fireplace':
                self.ashes_fireplace_task(feature, rooms)
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
            else:
                # No valid combination
                status = False
        # Feature is not usable
        return status


    # Do whatever you want in here. You can change the description to describe features
    # that were previously hidden, add directions to the directions Dictionary for the Room
    # you can do this for the Room you are in or any other Room based on the Room index. Just
    # make sure that you seed those things in the JSON
    def crystal_statue_task(self, feature, rooms):
        feature.state = 1
        print(feature.get_description())
        feature.state = 2

        rooms[24].long_des = 'The tunnel is now illuminated by the crystal. You see an open door down the tunnel.'
        rooms[24].visited = False
        rooms[24].directions['down'] = 17

        return True

    def prybar_plank_task(self, feature, rooms):
        feature.state = 1
        print(feature.get_description())
        feature.state = 2

        rooms[18].long_des = 'You have uncovered a tunnel under the gazebo....'
        rooms[18].visited = False
        rooms[18].directions['down'] = 24

        return True

    def axe_amor_task(self, feature, rooms):
        feature.state = 1
        print(feature.get_description())
        feature.state = 2

        rooms[13].long_des = 'You are standing in the Attic. Everything remains as it was with one exception: the boards around the walled in area have fallen exposing the entrance to a hidden room to the southseast.'
        rooms[13].visited = False
        rooms[13].directions['southeast'] = 23

        return True

    ####################################################################################################################################################
    # The below is in active development for game winning and losing sequences

    # This is part of game winning sequence B - comfort the ghost daughter
    def book_task(self, rooms):
        # Change description of the front lawns to display the 
        rooms[21].long_des = 'You are on the front lawns of the mansion. The borders of the nearby flower gardens are of curious-looking stone.\nThere are two rows of tall trees here. Under one tree you think that you can see a girl... she appears to be crying.\nThere is a pair of shears at the base of the tree near the apparition.\nTo the North is the front porch of the house. To the South are the locked gates of the grounds.'
        rooms[21].visited = False

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def shears_vine_task(self, feature, rooms):
        feature.state = 1
        print(feature.get_description())
        feature.state = 2

        rooms[3].long_des = 'You are standing in the Solarium. The air is stiflingly hot and humid. An exit leads to the South.'
        rooms[3].visited = False

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def locket_task(self, rooms):
        # "Hear sound elsewhere"
        print('You the sound of laughter coming from somewhere upstairs.')
        # Change the long description of the kitchen to output the vision. 
        rooms[9].long_des = 'You find yourself in a room with walls of a deep red color. A ghost of a girl is twirling in the center of the room, laughing. She is saying something about birds splashing.\n\nThe vision fades.To the Northeast is a door to the pink room. Through a door to the Southeast you can see the second floor landing.'
        rooms[9].visited = False

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def spade_task(self, feature, rooms):
        feature.state = 1
        print(feature.get_description())
        feature.state = 2

        rooms[21].long_des = 'You are on the front lawns of the mansion. A grave is dug at the base of a tree. There are some gardens nearby bordered in strange stone. You see the mansion to the North.'
        rooms[21].visited = False

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def locket_grave_task(self, feature, rooms):
        feature.in_action_des = 'You place the locket at the bottom of the grave, and fill the grave in. The ghost of the girl is here, crying, at the head of the makeshift grave.'
        feature.state = 1
        print(feature.get_description())
        feature.post_action_des = 'The grave is filled in now. The girl is here, crying, at the head of the grave.'
        feature.state = 2

        rooms[21].long_des = 'You are on the front lawns of the mansion. The freshly filled grave is here. There are some gardens nearby bordered in strange stone. You see the mansion to the North.'
        rooms[21].visited = False

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    def stone_task(self, feature, rooms):
        feature.in_action_des = 'You place the stone at the head of the grave. It looks right.\n\nThe girl is still here, crying. Her hand is outstretched.\nHer dress is white with red splatters.'
        feature.state = 1
        print(feature.get_description())
        feature.post_action_des = 'The grave is filled in now. The girl is here, crying, hand outstretched. Her dress is white, spattered in red.'
        feature.state = 2
        # Revise the state of the girl to usable for final interaction
        # Move this into a conditional that checks for stone, locket, and spade complete
        rooms[21].features[3].usable = True
        rooms[21].long_des = 'You are on the front lawns of the mansion. The grave grave is here, with the crying girl above, holding out her hand. There are some gardens nearby bordered in strange stone. You see the mansion to the North.'
        rooms[21].visited = False

        return True

    # This is part of game winning sequence B - comfort the ghost daughter
    # When the player uses the rose on the girl, endGame is triggered:
    def rose_task(self, feature, rooms):
        feature.in_action_des = 'You place the rose in the hand of the girl.\n\nThe girl stops crying, and looks up at you.\n\nShe says... "thank you".'
        feature.state = 1

        self.endGame(feature)

        return True

    # This is a part of game losing sequence A - attempt to fight the poltergeist
    def pistol_task(self, rooms):
        # "Hear sound elsewhere"
        print('You hear what sounds like pans banging, followed by a loud bang downstairs.')
        # Change the long description of the kitchen to output the vision. 
        rooms[7].long_des = 'You are standing in the Kitchen. A vision washes before your eyes. You see the servant, he is standing with his back to you, shouting at Chef Staker. The Chef is swinging a pan at the servant. There is a bang.\n\nThe servant has shot the Chef in the eye, and the Chef falls to the floor.'
        rooms[7].visited = False

        return True

    # This is a part of game losing sequence A - attempt to fight the poltergeist
    # When the player uses ashes on the fireplace, endGame is triggered:
    def ashes_fireplace_task(self, feature, rooms):
        os.system('clear')
        feature.state = 1
        print(feature.get_description())
        feature.state = 2

        self.endGame(feature)

    # Method handler for endGame choices and interactions. Could be a different class
    def endGame(self, feature):
        # endGame sequence for Game Losing Scenario A
        if feature.name == 'fireplace':
            selection = -1
            while selection not in (1, 2):
                print('\n\nYou have a choice to make... \n "1" You attempt to fight the enraged poltergeist, shooting the pistol again. \n "2" In a panic you throw the rest of the ashes into the fire.\n\n')
                selection = int(input('What will it be? '))
            # If selection 1, output the appropriate losing message and exit the game
            if selection == 1:
                os.system('clear')
                print('\n\n\nYou shoot the poltergeist again, and again, pulling the trigger over and over until the gun is empty.\n The poltergeist laughs terribly.\n The last thing you see is the ghost rushing toward you in a blur.\n There is no pain.')
                time.sleep(7)
                os.system('clear')
                print('\nThank you for playing. You have lost.')
                exit()
            # Elif selection 1, output the appropriate losing message and exit the game
            elif selection == 2:
                os.system('clear')
                print('\n\n\nThe fireplace explodes in a violent burst of flames, casting you across the room. \n You are lying the floor, and vaguely you see the flames are... everywhere now.\n You hear the poltergeist shrieking. The mansion is engulfed in the subsequent inferno.\n You are no more, but neither is the horror of the mansion.')
                time.sleep(7)
                os.system('clear')
                print('\nThank you for playing. You have lost.')
                exit()

        # endGame sequence for Game Winning Scenario B
        if feature.name == 'girl':
            os.system('clear')
            print('\n\n')
            print(feature.get_description())
            time.sleep(7)
            print('\n\n\nThe girl fades away.\nYou stand there for a minute, staring into the distance at the mansion. You\'re not sure how but you know things will be OK.')
            time.sleep(7)
            os.system('clear')
            print('\nThank you for playing. You have won the game.')
            exit()