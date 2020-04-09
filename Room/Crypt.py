from Room.Room import Room

class Crypt(Room):

    def __init__(self):
        self.longDes = 'Crypt LONG description'
        self.shortDes = 'Crypt SHORT description'
        self.visited = False