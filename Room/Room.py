class Room:

    north = None            # Room to the North
    south = None            # Room to the South
    east = None             # Room to the East
    west = None             # Room to the West
    up = None               # Room upstairs
    down = None             # Room downstairs
    dropped_items = list()   # list of items dropped in this room
    linked_rooms = list()    # list of the indexes of linkedRooms

    # Initializer for the Room class
    def __init__(self, name, long_des, short_des, visited, room_id):
        self.name = name
        self.long_des = long_des
        self.short_des = short_des
        self.visited = visited
        self.room_id = room_id


    # This function prints the description of the Room based on whether it has been visited or not
    def get_description(self):
        if not self.visited:
            return(self.long_des)
        else:
            # print the shortDes if the Room has been visited and print any items dropped in the room
            if len(self.dropped_items) > 0:
                return("{}\nYou have left these items here: {}".format(self.short_des, self.dropped_items))
            else:
                return(self.short_des)

    # This function will need to be toggled when a player enters the Room (after calling the getDescription function)
    def set_visited(self):
        self.visited = True

    # this function will link the rooms together, it takes room objects in the various
    # directions and links them
    def link_rooms(self, north, south, east, west, up, down):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
