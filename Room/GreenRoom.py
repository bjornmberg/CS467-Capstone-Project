from Room.Room import Room

class GreenRoom(Room):

    # Member variables for the child class
    longDes = 'Green Room LONG description'
    shortDes = 'Green Room SHORT description'

    # In order to initialize from a file the 'visited' and 'droppedItems' will need to be initialized
    def __init__(self, visited, droppedItems):
        super().__init__(self.longDes, self.shortDes, visited, droppedItems)