from Feature import Feature
from Item import Item


class Room:

    directions = dict()
    starting_items = []
    dropped_items = []
    features = []

    # Initializer for the Room class
    def __init__(self, name, long_des, short_des, visited, room_id):
        self.name = name
        self.long_des = long_des
        self.short_des = short_des
        self.visited = visited
        self.room_id = room_id

    # take what is in the dictionary and create starting objects
    def set_up(self, data):
        self.directions = data['directions'].copy()
        for i in data['features']:
            newFeature = Feature(
                i['name'],
                i['actionable'],
                i['preActionDes'],
                i['inActionDes'],
                i['postActionDes'],
                i['state'],
                i['featureId']
            )
            self.features.insert(newFeature.feature_id, newFeature)
        for j in data['startingItems']:
            newItem = Item(
                j['name'],
                j['description'],
                j['linkedFeature']
            )
            self.starting_items.append(newItem)

    # takes a string and returns the feature_id, which is also its index
    def get_feature_id(self, name):

        for x in self.features:
            if x.name == name:
                return True, x.feature_id

        return False, None

    # takes a string and prints the description of the feature
    def look_at_feature(self, name):

        status, index = self.get_feature_id(name)

        if status:
            print(self.get_feature_description(index))
        else:
            print('There is not a {} in this room.'.format(name))

    # returns the appropriate description based on how the feature has been interacted with
    def get_feature_description(self, index):

        state = self.features[index].state

        if state == 0:
            return self.features[index].pre_action_des
        elif state == 1:
            return self.features[index].in_action_des
        else:
            return self.features[index].post_action_des

    # this needs work
    def action_feature(self, name):

        status, index = self.get_feature_id(name)

        if status:
            if self.features[index].actionable:
                self.features[index].state = 1
                print(self.get_feature_description(index))
            else:
                print('You cannot do that')

    # takes a string and returns an index and an integer
    # the integer shows whether the item is in the starting items
    # or dropped items lists (or neither)
    def get_item_by_name(self, item):

        for x in range(0, len(self.starting_items)):
            if self.starting_items[x].name == item:
                return 1, x

        for y in range(0, len(self.dropped_items)):
            if self.dropped_items[x].name == item:
                return 2, y

        return 3, None

    # takes a string, tests that the item is in one of the lists,
    # sets variables on the item, gets the item, removes it from the
    # list and returns the item for adding to the inventory
    def take_item(self, item):

        status, x = self.get_item_by_name(item)

        if status == 1:
            self.features[self.starting_items[x].linked_feature].state = 3
            self.starting_items[x].linked_feature = None
            taken_item = self.starting_items[x].get_item()
            del self.starting_items[x]
            return True, taken_item
        elif status == 2:
            taken_item = self.dropped_items[x].get_item()
            del self.dropped_items[x]
            return True, taken_item
        else:
            return False, None


    # This function prints the description of the Room based on whether it has been visited or not
    def get_description(self):

        print('-----------------------------')
        print('CURRENT LOCATION: {}'.format(self.name))
        if not self.visited:
            print('DESCRIPTION: {}'.format(self.long_des))
        else:
            print('DESCRIPTION: {}'.format(self.short_des))

        print('YOU CAN \'move\': ')
        for key in self.directions:
            print(key)

        if self.starting_items:
            print('Starting Items:')
            for x in self.starting_items:
                print('{}'.format(x.name))

        if len(self.dropped_items) > 0:
            print('You Seem to have left these items on the floor: ')
            for y in self.dropped_items:
                print('{}'.format(y.name))



    # This function will need to be toggled when a player enters the Room (after calling the getDescription function)
    def set_visited(self):
        self.visited = True
