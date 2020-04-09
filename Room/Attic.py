from Room.Room import Room

class Attic(Room):

    def __init__(self):
        self.longDes = 'Attic LONG description'
        self.shortDes = 'Attic SHORT description'
        self.visited = False