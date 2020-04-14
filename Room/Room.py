class Room:

    north = None
    south = None
    east = None
    west = None
    up = None
    down = None
    droppedItems = list()
    linkedRooms = list()

    # Initializer for the Room class
    def __init__(self, name, longDes, shortDes, visited, roomId):
        self.name = name
        self.longDes = longDes
        self.shortDes = shortDes
        self.visited = visited
        self.roomId = roomId

    # This function prints the description of the Room based on whether it has been visited or not
    def getDescription(self):
        if not self.visited:
            return(self.longDes)
        else:
            # print the shortDes if the Room has been visited and print any items dropped in the room
            if len(self.droppedItems) > 0:
                return("{}\nYou have left these items here: {}".format(self.shortDes, self.droppedItems))
            else:
                return(self.shortDes)

    # This function will need to be toggled when a player enters the Room (after calling the getDescription function)
    def setVisited(self):
        self.visited = True

    # this function will link the rooms together
    def linkRooms(self, north, south, east, west, up, down):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
