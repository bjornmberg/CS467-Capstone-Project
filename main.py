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

print(parlor.getDescription())
print("VISITING THE ROOM")
parlor.setVisited()
print(parlor.getDescription())
print("OVERRIDING VISITED TO GET LONG DESCRIPTION")
print(parlor.longDes)
