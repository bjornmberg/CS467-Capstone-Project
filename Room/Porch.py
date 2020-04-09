from Room.Room import Room

class Porch(Room):

    def __init__(self):
        self.longDes = 'Porch LONG description'
        self.shortDes = 'Porch SHORT description'
        self.visited = False