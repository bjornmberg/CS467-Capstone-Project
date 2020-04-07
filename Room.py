

class Room:

    def __init__(self):
        self.longDes = ''
        self.shortDes = ''
        self.visited = False

    def getDescription(self):
        if not self.visited:
            return self.longDes
        else:
            return self.shortDes

    def getLongDesc(self):
        return self.longDes

    def setVisited(self):
        if not self.visited:
            self.visited = True
        else:
            self.visited = False