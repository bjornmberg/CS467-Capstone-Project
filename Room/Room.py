
class Room:

    directions = {}
    items = dict()     # list of items a room starts with

    # Initializer for the Room class
    def __init__(self, name, long_des, short_des, visited, room_id):
        self.name = name
        self.long_des = long_des
        self.short_des = short_des
        self.visited = visited
        self.room_id = room_id

    # This function prints the description of the Room based on whether it has been visited or not
    def get_description(self):

        print('-----------------------------')
        print('CURRENT LOCATION: {}'.format(self.name))
        if not self.visited:
            print('DESCRIPTION: {}'.format(self.long_des))
        else:
            print('DESCRIPTION: {}'.format(self.short_des))

        print('YOU CAN \'move\': ')
        for key in self.directions:
            print(key)

        if self.items:
            print('Items that can be taken: ')
            for key, value in self.items.items():
                if value['dropped'] == False:
                    print('Initialized Here: {}'.format(key))
                elif value['dropped'] == True:
                    print('Dropped Here: {}'.format(key))



    # This function will need to be toggled when a player enters the Room (after calling the getDescription function)
    def set_visited(self):
        self.visited = True
