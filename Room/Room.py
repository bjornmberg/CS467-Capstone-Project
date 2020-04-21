import textwrap

class Room:

    directions = dict()
    # items = dict()     # dictionary of items a room starts with
    starting_items = {}
    dropped_items = {}

    # Initializer for the Room class
    def __init__(self, name, long_des, short_des, visited, room_id):
        self.name = name
        self.long_des = long_des
        self.short_des = short_des
        self.visited = visited
        self.room_id = room_id

    def in_starting_items(self, item):
        if item in self.starting_items:
            return True
        else:
            return False

    def in_dropped_items(self, item):
        if item in self.dropped_items:
            return True
        else:
            return False

    # This function prints the description of the Room based on whether it has been visited or not
    def get_description(self):
        centerLeftRight = 100
        print()
        print('▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\n'.center(centerLeftRight))
        print('CURRENT LOCATION: {}\n'.format(self.name).center(centerLeftRight))
        if not self.visited:
            print(textwrap.fill('DESCRIPTION: {}'.format(self.long_des), 85, initial_indent='            ', subsequent_indent='            '))
        else:
            print('DESCRIPTION: {}'.format(self.short_des))
        print()
        print(textwrap.fill('YOU CAN \'move\': ', initial_indent='            '))
        for key in self.directions:
            print(textwrap.fill(key, initial_indent='                '))

        if self.items:
            print()
            print(textwrap.fill('ITEMS IN THIS ROOM: ', initial_indent='            '))
            for key, value in self.items.items():
                if value['dropped'] == False:
                    print(textwrap.fill('INITIALIZED HERE: {}'.format(key), initial_indent='                '))
                    #print('INITIALIZED HERE: {}'.format(key))
                elif value['dropped'] == True:
                    print(textwrap.fill('DROPPED HERE: {}'.format(key), initial_indent='                '))
                    #print('DROPPED HERE: {}'.format(key))
        
        print('▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\n\n'.center(centerLeftRight))
        if self.starting_items:
            print('Starting Items:')
            for key, value in self.starting_items.items():
                print('{}'.format(key))

        if self.dropped_items:
            print('You Seem to have left these items on the floor: ')
            for key, value  in self.dropped_items.items():
                print('{}'.format(key))



    # This function will need to be toggled when a player enters the Room (after calling the getDescription function)
    def set_visited(self):
        self.visited = True
