from Room import Parlor, Library, Solarium, GameRoom, DSBathroom, \
    DiningRoom, Foyer, Kitchen, LinenCloset, RedRoom, \
    PinkRoom, SecFloorLanding, SecFloorBathroom, GreenRoom, Attic, \
    Cellar, ServQuarters, ServBathroom, Crypt, Gazebo, \
    RoseGarden, Porch, FrontLawns


parlor = Parlor()
library = Library()
solarium = Solarium()
gameRoom = GameRoom()
dsBathroom = DSBathroom()
diningRoom = DiningRoom()
foyer = Foyer()
kitchen = Kitchen()
linenCloset = LinenCloset()
redRoom = RedRoom()
pinkRoom = PinkRoom()
secFloorLanding = SecFloorLanding()
secFloorBathroom = SecFloorBathroom()
greenRoom = GreenRoom()
attic = Attic()
cellar = Cellar()
servQuarters = ServQuarters()
servBathroom = ServBathroom()
crypt = Crypt()
gazebo = Gazebo()
roseGarden = RoseGarden()
porch = Porch()
frontLawns = FrontLawns()

rooms = [parlor, library, solarium, gameRoom, dsBathroom, diningRoom, foyer, kitchen, linenCloset, redRoom, pinkRoom, secFloorLanding,
         secFloorBathroom, greenRoom, attic, cellar, servQuarters, servBathroom, crypt, gazebo, roseGarden, porch, frontLawns]


for x in rooms:
    print('Prior to being visited description: {}'.format(x.getDescription()))
    print("Visiting Room")
    x.setVisited()
    print('After being visited description: {}'.format(x.getDescription()))
    print('Manually getting long description: {}'.format(x.longDes))
    print('\n')

