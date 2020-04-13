from Room.Room import Room

class Gazebo(Room):

    # Member variables for the child class
    longDes = 'Gazebo LONG description'
    shortDes = 'Gazebo SHORT description'

    # In order to initialize from a file the 'visited' and 'droppedItems' will need to be initialized
    def __init__(self, visited, droppedItems):
        super().__init__(self.longDes, self.shortDes, visited, droppedItems)