from Item import Item
from Room import Room
from Feature import Feature


class Task:


    # This is called from Game when a user attempts the command 'use Item Feature'
    # This takes in the Item, the Feature, and the rooms_list and calls the correct
    # task. It will return the status of the task function if there is a workable
    # combination, or return False if there is no workable combination.
    def perform_task(self, item, feature, rooms):

        status = False

        # Check that the Feature is usable
        if feature.usable:

            # check it there is a valid Feature/Item combination and call that function
            if item.name == 'axe' and feature.name == 'armor':
                status =  self.axe_amor_task(feature, rooms)
            elif item.name == 'prybar' and feature.name == 'plank':
                status = self.prybar_plank_task(feature, rooms)
            elif item.name == 'crystal' and feature.name == 'statue':
                status =  self.crystal_statue_task(feature, rooms)
            else:
                # No valid combination
                status = False
        # Feature is not usable
        return status


    # Do whatever you want in here. You can change the description to describe features
    # that were previously hidden, add directions to the directions Dictionary for the Room
    # you can do this for the Room you are in or any other Room based on the Room index. Just
    # make sure that you seed those things in the JSON
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