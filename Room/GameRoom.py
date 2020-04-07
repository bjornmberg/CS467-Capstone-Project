from Room.Room import Room

class GameRoom(Room):

    def __init__(self):
        self.longDes = 'GameRoom LONG description'
        self.shortDes = 'GameRoom SHORT description'
        self.visited = False