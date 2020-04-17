import json
import os
import platform
from Room import Room
from Hero import Hero

class Game:

    rooms_list = list()
    hero = Hero()

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

        plat = platform.system()

        while 1:
            selection =  self.display_menu()
            if selection == 'newgame':
                if plat == 'Windows':
                    self.play_game('datastore\\newGame.json')
                else:
                    self.play_game('dataStore/newGame.json')
            elif selection == 'loadgame':
                if plat == 'Windows':
                    self.play_game('datastore\\saveGame.json')
                else:
                    self.play_game('dataStore/saveGame.json')
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
            # copy the available directions dictionary to the object's directions dictionary
            new_room.directions = x['directions'].copy()
            # put the room into the roomsList at the index of its id - example: parlor's id == 0
            # so the parlor room is at roomsList[0]
            self.rooms_list.insert(new_room.room_id, new_room)


    def initialize_hero(self, name, location):

        self.hero.name = name
        self.hero.location = location


    def move(self):

        print('-----------------------------------------')
        current_room = self.rooms_list[self.hero.location]
        print('{}\'s Current Location: {}'.format(self.hero.name, current_room.name))
        print('{}'.format(current_room.get_description()))
        print('You can move in the following directions: ')

        for key in current_room.directions:
            print(key)

        direction = input('> ')

        if direction in current_room.directions:
            self.hero.location = current_room.directions[direction]
            current_room.set_visited()
        else:
            print('You cannot move in that direction.')


    # This function is the main game driver function
    def play_game(self, inputFile):

        game_file = open(inputFile, 'r', encoding='utf-8')
        file_data = json.loads(game_file.read())
        room_data = file_data['rooms']

        self.initialize_rooms(room_data)

        hero_data = file_data['hero']
        # hero = Hero(hero_data['name'], hero_data['location'])
        self.initialize_hero(hero_data['name'], hero_data['location'])

        print('{}'.format(file_data['intro']))

        while 1:
            self.move()


