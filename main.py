from Room import Parlor, Library, Solarium, GameRoom, DSBathroom, \
    DiningRoom, Foyer, Kitchen, LinenCloset, RedRoom, \
    PinkRoom, SecFloorLanding, SecFloorBathroom, GreenRoom, Attic, \
    Cellar, ServQuarters, ServBathroom, Crypt, Gazebo, \
    RoseGarden, Porch, FrontLawns


parlor = Parlor(True, ['ParItem1', 'ParItem2'])
library = Library(False, [])
solarium = Solarium(True, ['SolItem1', 'SolItem2'])
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

rooms = [parlor, library, solarium, gameRoom, dsBathroom, diningRoom, foyer, kitchen, linenCloset, redRoom, pinkRoom, secFloorLanding,
         secFloorBathroom, greenRoom, attic, cellar, servQuarters, servBathroom, crypt, gazebo, roseGarden, porch, frontLawns]


for x in rooms:
    print('DESCRIPTION FOR THE INITIALIZED VISITED STATE: {}'.format(x.getDescription()))
    print("Visiting Room")
    x.setVisited()
    print('DESCRIPTION AFTER ENTERING THE ROOM: {}'.format(x.getDescription()))
    print('MANUALLY GET THE LONG DESCRIPTION: {}'.format(x.longDes))
    print('\n')

