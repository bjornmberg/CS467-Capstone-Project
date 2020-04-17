import json
import platform
from Room import Room
from Hero import Hero
from Inventory import Inventory

class Game:

    rooms_list = list()
    inventory = Inventory()
    hero = Hero()

    # This function will display the credits for the Game
    # Needs formatting
    def display_credits(self):

        print('THIS IS WHERE THE CREDITS WILL BE!')
        input('PRESS ANY KEY AND ENTER TO RETURN')
        return

    # This function displays the menu and asks the user for input
    # The input (string) is returned to the calling function
    # Needs formatting
    def display_menu(self):

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
            # copy the available directions dictionary to the object's directions dictionary
            new_room.directions = x['directions'].copy()
            # copy the items that start in the rooms dictionary to the object's initial_items dictionary
            new_room.items = x['items'].copy()
            # put the room into the roomsList at the index of its id - example: parlor's id == 0
            # so the parlor room is at roomsList[0]
            self.rooms_list.insert(new_room.room_id, new_room)

    # FUNCTION COMMENT PLACEHOLDER
    def initialize_hero(self, data):

        self.hero.name = data['name']
        self.hero.location = data['location']

    # FUNCTION COMMENT PLACEHOLDER
    def initialize_inventory(self, data):
        self.inventory.used_slots = data['usedSlots']
        self.inventory.items = data['items'].copy()

    # FUNCTION COMMENT PLACEHOLDER
    def move(self, direction):

        current_room = self.rooms_list[self.hero.location]

        if direction in current_room.directions:
            self.hero.location = current_room.directions[direction]
            current_room.set_visited()
        else:
            print('You cannot move in that direction.')

    # FUNCTION COMMENT PLACEHOLDER
    def take(self, item):

        current_room = self.rooms_list[self.hero.location]
        self.inventory.add_item(item ,current_room.items[item])
        del current_room.items[item]


    # FUNCTION COMMENT PLACEHOLDER
    def get_command(self):

        current_room = self.rooms_list[self.hero.location]
        current_room.get_description()
        command = input('> ').split(' ')

        if command[0] == 'move':
            self.move(command[1])
        elif command[0] == 'take':
            self.take(command[1])
        elif command[0] == 'inventory':
            self.inventory.show_inventory()
        elif command[0] == 'drop':
            status, item = self.inventory.drop_item((command[1]))
            if status == True:
                current_room.items[command[1]] = item

    # This function is the main game driver function
    def play_game(self, inputFile):

        game_file = open(inputFile, 'r', encoding='utf-8')
        file_data = json.loads(game_file.read())

        room_data = file_data['rooms']
        hero_data = file_data['hero']
        inventory_data = file_data['inventory']

        self.initialize_rooms(room_data)
        self.initialize_hero(hero_data)
        self.initialize_inventory(inventory_data)

        print('{}'.format(file_data['intro']))

        while 1:
            self.get_command()


