import json
import os
from Room import Room
from Hero import Hero

class Game:

    rooms_list = list()

    # This function will display the credits for the Game
    # Needs formatting
    def display_credits(self):
        # os.system('cls')
        print('THIS IS WHERE THE CREDITS WILL BE!')
        input('PRESS ANY KEY AND ENTER TO RETURN')
        return

    # This function displays the menu and asks the user for input
    # The input (string) is returned to the calling function
    # Needs formatting
    def display_menu(self):

        # os.system('cls')

        print('--------- The Spook Mansion Mystery ---------')
        print('Please Make a Selection:')
        print('\'newgame\' - to start a new game')
        print('\'loadgame\' - to load a saved game')
        print('\'credits\' - to view the game credits')
        print('\'exit\' - to exit the game')

        selection = input("Enter Selection: ")
        # Return the user's selection
        return selection

    # This function handles loop control for the menu and game
    def start(self):

        while 1:
            selection =  self.display_menu()
            if selection == 'newgame':
                self.play_game('datastore\\newGame.json')
            elif selection == 'loadgame':
                self.play_game('datastore\\saveGame.json')
            elif selection == 'credits':
                self.display_credits()
            elif selection == 'exit':
                break

    # This function is used to initialize the Room objects to a state from either
    # a save file or a start file.
    def initialize_rooms(self, data):

        # iterate through the roomData and initialize Room objects for each item
        for x in data:
            # initialize the object
            new_room = Room(x['name'], x['longDes'], x['shortDes'], x['visited'], x['roomId'])
            # copy the droppedItems from the roomData to the object's droppedItems
            new_room.dropped_items = x['droppedItems'].copy()
            # copy the linkedRooms from the roomData to the object's linkedRooms
            new_room.linked_rooms = x['linkedRooms'].copy()
            # put the room into the roomsList at the index of its id - example: parlor's id == 0
            # so the parlor room is at roomsList[0]
            self.rooms_list.insert(new_room.room_id, new_room)

        # go through the rooms and link them
        for y in self.rooms_list:
            # the linkedRooms list of each item will contain the index of the other rooms
            # it is linked to in the following order north, south, east, west, up, down
            # these values will either be the index of the room in the rooms list (if
            # a link exists, or None if there is no link in that direction
            n = self.rooms_list[y.linked_rooms[0]] if y.linked_rooms[0] is not None else None
            s = self.rooms_list[y.linked_rooms[1]] if y.linked_rooms[1] is not None else None
            e = self.rooms_list[y.linked_rooms[2]] if y.linked_rooms[2] is not None else None
            w = self.rooms_list[y.linked_rooms[3]] if y.linked_rooms[3] is not None else None
            u = self.rooms_list[y.linked_rooms[4]] if y.linked_rooms[4] is not None else None
            d = self.rooms_list[y.linked_rooms[5]] if y.linked_rooms[5] is not None else None
            # call to link the rooms
            y.link_rooms(n, s, e, w, u, d)

    # This function is the main game driver function
    def play_game(self, inputFile):

        game_file = open(inputFile, 'r')
        file_data = json.loads(game_file.read())
        room_data = file_data['rooms']

        self.initialize_rooms(room_data)

        hero_data = file_data['hero']
        hero = Hero(hero_data['name'], hero_data['location'])

        while 1:
            print('--------------------------------------')
            current_room = self.rooms_list[hero.location]
            print('{}\'s Current Location: {}'.format(hero.name, current_room.name))
            print('Description: {}'.format(current_room.get_description()))
            print('Linked Room Indices: {}'.format(current_room.linked_rooms))
            direction = input('Enter n, s, e, w, u, d: ')

            if direction == 'n':
                if current_room.north is not None:
                    hero.location = current_room.north.room_id
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 's':
                if current_room.south is not None:
                    hero.location = current_room.south.room_id
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 'e':
                if current_room.east is not None:
                    hero.location = current_room.east.room_id
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 'w':
                if current_room.west is not None:
                    hero.location = current_room.west.room_id
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 'u':
                if current_room.up is not None:
                    hero.location = current_room.up.room_id
                else:
                    print('No Room in that direction')
                    continue
            elif direction == 'd':
                if current_room.down is not None:
                    hero.location = current_room.down.room_id
                else:
                    print('No Room in that direction')
                    continue

            current_room.set_visited()

