from Item import Item
from Room import Room
from Feature import Feature


class Task:

    def perform_task(self, item, feature, rooms):

        status = False

        if feature.usable:

            if item.name == 'axe' and feature.name == 'armor':
                status =  self.axe_amor_task(feature, rooms)
            elif item.name == 'prybar' and feature.name == 'plank':
                status = self.prybar_plank_task(feature, rooms)
            elif item.name == 'crystal' and feature.name == 'statue':
                status =  self.crystal_statue_task(feature, rooms)
            else:
                status = False

        return status



    def crystal_statue_task(self, feature, rooms):
        feature.state = 1
        print(feature.get_description())
        feature.state = 2

        rooms[24].long_des = 'The tunnel is now illuminated by the crystal. You see an open door down the tunnel.'
        rooms[24].visited = False
        rooms[24].directions['down'] = 17

        return True

    def prybar_plank_task(self, feature, rooms):
        feature.state = 1
        print(feature.get_description())
        feature.state = 2

        rooms[18].long_des = 'You have uncovered a tunnel under the gazebo....'
        rooms[18].visited = False
        rooms[18].directions['down'] = 24

        return True

    def axe_amor_task(self, feature, rooms):
        feature.state = 1
        print(feature.get_description())
        feature.state = 2

        rooms[13].long_des = 'You are standing in the Attic. Everything remains as it was with one exception: the boards around the walled in area have fallen exposing the entrance to a hidden room to the southseast.'
        rooms[13].visited = False
        rooms[13].directions['southeast'] = 23

        return True