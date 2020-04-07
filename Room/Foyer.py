from Room.Room import Room

class Foyer(Room):

    def __init__(self):
        self.longDes = 'Foyer LONG description'
        self.shortDes = 'Foyer SHORT description'
        self.visited = False