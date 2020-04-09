from Room.Room import Room

class ServBathroom(Room):

    def __init__(self):
        self.longDes = 'ServBathroom LONG description'
        self.shortDes = 'ServBathroom SHORT description'
        self.visited = False