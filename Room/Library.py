from Room.Room import Room

class Library(Room):

    def __init__(self):
        self.longDes = 'Library LONG description'
        self.shortDes = 'Library SHORT description'
        self.visited = False