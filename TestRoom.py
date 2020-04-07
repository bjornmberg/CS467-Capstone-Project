
from Room import Room

class TestRoom(Room):

    def __init__(self):
        self.longDes = 'Test Room Long Description'
        self.shortDes = 'Test Room Short Description'
        self.visited = False