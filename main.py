from Room import Parlor, Library, Solarium, GameRoom, DSBathroom, \
    DiningRoom, Foyer, Kitchen, LinenCloset, RedRoom, \
    PinkRoom, SecFloorLanding, SecFloorBathroom, GreenRoom, Attic, \
    Cellar, ServQuarters, ServBathroom, Crypt, Gazebo, \
    RoseGarden, Porch, FrontLawns


# Just initializing all of the Rooms to default values
parlor = Parlor(False, [])
library = Library(False, [])
solarium = Solarium(False, [])
gameRoom = GameRoom(False, [])
dsBathroom = DSBathroom(False, [])
diningRoom = DiningRoom(False, [])
foyer = Foyer(False, [])
kitchen = Kitchen(False, [])
linenCloset = LinenCloset(False, [])
redRoom = RedRoom(False, [])
pinkRoom = PinkRoom(False, [])
secFloorLanding = SecFloorLanding(False, [])
secFloorBathroom = SecFloorBathroom(False, [])
greenRoom = GreenRoom(False, [])
attic = Attic(False, [])
cellar = Cellar(False, [])
servQuarters = ServQuarters(False, [])
servBathroom = ServBathroom(False, [])
crypt = Crypt(False, [])
gazebo = Gazebo(False, [])
roseGarden = RoseGarden(False, [])
porch = Porch(False, [])
frontLawns = FrontLawns(False, [])

# calling the linking function to point all of the Rooms at each other
# this only represents the first floor right now, for testing
frontLawns.linkRooms(porch, None, None, None, None, None)
porch.linkRooms(foyer, frontLawns, None, None, None, None)
foyer.linkRooms(dsBathroom, Porch, parlor, library, secFloorLanding, None)
library.linkRooms(gameRoom, None, foyer, None, None, None)
gameRoom.linkRooms(solarium, library, dsBathroom, None, None, None)
solarium.linkRooms(None, gameRoom, None, None, None, None)
dsBathroom.linkRooms(None, foyer, None, gameRoom, None, None)
parlor.linkRooms(diningRoom, None, None, foyer, None, None)
diningRoom.linkRooms(None, parlor, None, kitchen, None, None)
kitchen.linkRooms(roseGarden, None, diningRoom, None, None, cellar)
roseGarden.linkRooms(None, kitchen, None, None, None, None)

# this is a little function that will walk through the rooms and make
# sure that they give the correct description (long vs short) depending
# on if they have been visited. Depending on what you pass in as the
# startingRoom (below in def main) you may just end up looping around.
# but it works.
def visitRoomsTesting(startingRoom):

    currentRoom = startingRoom
    i = 0

    while i <= 10:
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
    visitRoomsTesting(parlor)

if __name__ == '__main__':
    main()