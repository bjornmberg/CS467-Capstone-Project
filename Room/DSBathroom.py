from Room.Room import Room

class DSBathroom(Room):

    def __init__(self):
        self.longDes = 'Downstairs Bathroom LONG description'
        self.shortDes = 'Downstairs Bathroom SHORT description'
        self.visited = False