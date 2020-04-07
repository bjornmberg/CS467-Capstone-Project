
from Room.Room import Room

class Parlor(Room):

    def __init__(self):
        self.longDes = 'Parlor LONG description'
        self.shortDes = 'Parlor SHORT description'
        self.visited = False