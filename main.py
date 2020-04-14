from Room import Room


# Just initializing all of the Rooms to default values
parlor = Room("Parlor Long", "Parlor Short", False, [])
library = Room("Library Long", "Library Short",False, [])
solarium = Room("Solarium Long", "Solarium Short",False, [])
gameRoom = Room("Game Room Long", "Game Room Short",False, [])
dsBathroom = Room("Downstairs Bathroom Long", "Downstairs Bathroom Short",False, [])
diningRoom = Room("Dining Room Long", "Dining Room Short",False, [])
foyer = Room("Foyer Long", "Foyer Short",False, [])
kitchen = Room("Kitchen Long", "Kitchen Short",False, [])
linenCloset = Room("Linen Closet Long", "Linen Closet Short",False, [])
redRoom = Room("Red Room Long", "Red Room Short",False, [])
pinkRoom = Room("Pink Room Long", "Pink Room Short",False, [])
secFloorLanding = Room("Landing Long", "Landing Short",False, [])
secFloorBathroom = Room("Upstairs Bathroom Long", "Upstairs Bathroom Short",False, [])
greenRoom = Room("Green Room Long", "Green Room Short",False, [])
attic = Room("Attic Long", "Attic Short",False, [])
cellar = Room("Cellar Long", "Cellar Short",False, [])
servQuarters = Room("Servant Quarters Long", "Servant Quarters Short",False, [])
servBathroom = Room("Servant Bathroom Long", "Servant Bathroom Short", False, [])
crypt = Room("Crypt Long", "Crypt Short", False, [])
gazebo = Room("Gazebo Long", "Gazebo Short", False, [])
roseGarden = Room("Rose Garden Long", "Rose Garden Short", False, [])
porch = Room("Porch Long", "Porch Short", False, [])
frontLawns = Room("Front Lawns Long", "Front Lawns Short", False, [])

# calling the linking function to point all of the Rooms at each other
# this only represents the first floor right now, for testing
frontLawns.linkRooms(porch, None, None, None, None, None)
porch.linkRooms(foyer, frontLawns, None, None, None, None)
foyer.linkRooms(dsBathroom, porch, parlor, library, secFloorLanding, None)
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