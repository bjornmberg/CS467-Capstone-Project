from Room import Parlor, Library, Solarium, GameRoom, DSBathroom, DiningRoom, Foyer, Kitchen


parlor = Parlor()
library = Library()

print(parlor.getDescription())
print("VISITING THE ROOM")
parlor.setVisited()
print(parlor.getDescription())
print("OVERRIDING VISITED TO GET LONG DESCRIPTION")
print(parlor.longDes)
