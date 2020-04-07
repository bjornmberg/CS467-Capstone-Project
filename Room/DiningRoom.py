from Room.Room import Room

class DiningRoom(Room):

    def __init__(self):
        self.longDes = 'Dining Room LONG description'
        self.shortDes = 'Dining Room SHORT description'
        self.visited = False