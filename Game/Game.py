import json
import platform
from Credits import credits
from Hero import Hero
from Intro import intro
from Inventory import Inventory
from Menu import menu
from Room import Room

class Game:

    rooms_list = list()
    inventory = Inventory()
    hero = Hero()

    # This function handles loop control for the menu and game
    def start(self):
        # Determine the system type running the game
        plat = platform.system()

        while 1:
            selection =  menu.display()
            if selection == 'newgame':
                if plat == 'Windows':
                    # self.play_game('datastore\\newGame.json')
                    intro.display()
                    self.play_game('dataStore\\newGame\\load_file.json', 'dataStore\\newGame\\RoomState\\')
                else:
                    intro.display()
                    self.play_game('dataStore/newGame/load_file.json', 'dataStore/newGame/RoomState/')
            elif selection == 'loadgame':
                if plat == 'Windows':
                    self.play_game('datastore\\savedGame\\load_file.json', 'dataStore\\savedGame\\RoomState\\')
                else:
                    self.play_game('dataStore/saveGame/load_file.json', 'dataStore/newGame/RoomState/')
            elif selection == 'credits':
                credits.display()
            elif selection == 'exit':
                break

    # This function is used to initialize the Room objects.
    # Parameters:
    #   data - a list of the room files
    #   file_path - a string that shows the full path to these room files
    def initialize_rooms(self, data, file_path):

        for x in data:
            room_file = open(file_path + x, 'r', encoding='utf-8')
            room_data = json.loads(room_file.read())
            new_room = Room(
                room_data['name'],
                room_data['longDes'],
                room_data['shortDes'],
                room_data['visited'],
                room_data['roomId'])
            new_room.directions = room_data['directions'].copy()
            new_room.items = room_data['items'].copy()
            self.rooms_list.insert(new_room.room_id, new_room)

    # This function is used to set the state of the hero
    # Parameters:
    #   data - a dictionary representing the hero
    def initialize_hero(self, data):

        self.hero.name = data['name']
        self.hero.location = data['location']

    # This function is used to set the state of the inventory
    # Parameters:
    #   data - a dictionary representing the inventory
    def initialize_inventory(self, data):
        self.inventory.used_slots = data['usedSlots']
        self.inventory.items = data['items'].copy()

    # This function is used to move the hero through the rooms
    # Parameters:
    # direction - a string representing the direction to move
    def move(self, direction):

        # set the current room to where the hero is located
        current_room = self.rooms_list[self.hero.location]

        # check to see if the direction to move possible within that room
        if direction in current_room.directions:
            # change the hero's location to the new room
            self.hero.location = current_room.directions[direction]
            # set the room being left to visited
            current_room.set_visited()
        # if the hero cannot move in that direction print and return
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
    def play_game(self, input_file, file_path):

        game_file = open(input_file, 'r', encoding='utf-8')
        file_data = json.loads(game_file.read())

        room_data = file_data['rooms']
        hero_data = file_data['hero']
        inventory_data = file_data['inventory']

        self.initialize_rooms(room_data, file_path)
        self.initialize_hero(hero_data)
        self.initialize_inventory(inventory_data)

        print('{}'.format(file_data['intro']))

        while 1:
            self.get_command()
