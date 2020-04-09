from Room.Room import Room

class Cellar(Room):

    def __init__(self):
        self.longDes = 'Cellar LONG description'
        self.shortDes = 'Cellar SHORT description'
        self.visited = False