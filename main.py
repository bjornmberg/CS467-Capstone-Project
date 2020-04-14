from Room import Room
import json

# this is a list that will hold all of the Room objects
# the index of each item is the roomId that can be seen in the json
# and the Room class implementation
roomsList = list()

# open the game file
gameFile = open('dataStore/newGame.json', 'r')

# load the json into a Python dictionary
fileData = json.loads(gameFile.read())
# the roomData is stored in the fileData in the 'rooms' list
roomData = fileData['rooms']

# iterate through the roomData and initialize Room objects for each item
for x in roomData:
    # initialize the object
    newRoom = Room(x['name'], x['longDes'], x['shortDes'], x['visited'], x['roomId'])
    # copy the droppedItems from the roomData to the object's droppedItems
    newRoom.droppedItems = x['droppedItems'].copy()
    # copy the linkedRooms from the roomData to the object's linkedRooms
    newRoom.linkedRooms = x['linkedRooms'].copy()
    # put the room into the roomsList at the index of its id - example: parlor's id == 0
    # so the parlor room is at roomsList[0]
    roomsList.insert(newRoom.roomId, newRoom)

# link the rooms together
for y in roomsList:
    # the linkedRooms list of each item will contain the index of the other rooms
    # it is linked to in the following order north, south, east, west, up, down
    # these values will either be the index of the room in the rooms list (if
    # a link exists, or None if there is no link in that direction
    n = roomsList[y.linkedRooms[0]] if y.linkedRooms[0] is not None else None
    s = roomsList[y.linkedRooms[1]] if y.linkedRooms[1] is not None else None
    e = roomsList[y.linkedRooms[2]] if y.linkedRooms[2] is not None else None
    w = roomsList[y.linkedRooms[3]] if y.linkedRooms[3] is not None else None
    u = roomsList[y.linkedRooms[4]] if y.linkedRooms[4] is not None else None
    d = roomsList[y.linkedRooms[5]] if y.linkedRooms[5] is not None else None
    # call to link the rooms
    y.linkRooms(n, s, e, w, u, d)


# test harness
def visitRoomsTesting(startingRoom):

    currentRoom = startingRoom
    i = 0

    while i <= 10:
        print("Current Room: {}".format(currentRoom.name))
        print(currentRoom.getDescription())
        currentRoom.setVisited()
        if currentRoom.north:
            currentRoom = currentRoom.north
        elif currentRoom.east:
            currentRoom = currentRoom.east
        elif currentRoom.west:
            currentRoom = currentRoom.west
        elif currentRoom.south:
            currentRoom = currentRoom.south
        else:
            break
        i += 1

def main():
    visitRoomsTesting(roomsList[0])

if __name__ == '__main__':
    main()