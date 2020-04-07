from Room.Room import Room

class Kitchen(Room):

    def __init__(self):
        self.longDes = 'Kitchen LONG description'
        self.shortDes = 'Kitchen SHORT description'
        self.visited = False