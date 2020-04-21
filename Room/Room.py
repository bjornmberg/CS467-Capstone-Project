from Feature import Feature
from Item import Item


class Room:

    def __repr__(self):
        return self

    # Initializer for the Room class - this was a major pain-in-the-ass. Turns out that if you
    # do not clear the list each time through it will keep appending the same list to every Room
    # Parameters:
    #   name - str
    #   long_des - str, long description
    #   short_des - str, short description
    #   visited - bool, Room's state
    #   room_id - int, handles placement into the Game's rooms list()
    #   directions - dict, maps directions to connecting Rooms (ex: {'north': 1, 'south':2}
    #       where 1 and 2 are the room_ids of other Room objects
    #   s_items - list of dicts containing starting item information
    #   d_items - list of dicts containing dropped item information
    #   feats - list of dicts containing feature information
    def __init__(self, name, long_des, short_des, visited, room_id, directions, s_items, d_items, feats):
        self.name = name
        self.long_des = long_des
        self.short_des = short_des
        self.visited = visited
        self.room_id = room_id
        self.directions = directions.copy()
        self.starting_items = []
        self.dropped_items = []
        self.features = []

        # call this to get the information from the passed in list to the local lists
        self.generate_lists(s_items, d_items, feats)

    # This function is used by the constructor to initialize the starting_items, dropped_items,
    # and features list()s
    def generate_lists(self, s_items, d_items, feats):
        # go through each list and initialize Objects based on the information supplied
        for s in s_items:
            new_s_item = Item(s['name'], s['description'], s['linkedFeature'])
            self.starting_items.append(new_s_item)

        for d in d_items:
            new_d_item = Item(d['name'], d['description'], d['linkedFeature'])
            self.dropped_items.append(new_d_item)

        for f in feats:
            new_feat = Feature(
                f['name'],
                f['preActionDes'],
                f['inActionDes'],
                f['postActionDes'],
                f['state'],
                f['featureId']
            )
            self.features.insert(new_feat.feature_id, new_feat)


    # This function looks through the names of the Features and returns True
    # if the Feature is in the Room and the index of the Feature in the feature list()
    def get_feature_id(self, name):

        for x in self.features:
            if x.name == name:
                return True, x.feature_id

        return False, None

    # This function is used to see if an Item or Feature is in a Room
    # If it is an Item in either dropped_items of starting_items a 1 and the
    # Item is returned, if it is in the features list() a 2 and the Feature
    # is returned - this is used for the 'look' functionality
    def in_room(self, thing):

        for i in self.starting_items:
            if thing == i.name:
                return 1, i
        for j in self.dropped_items:
            if thing == j.name:
                return 1, j
        for k in self.features:
            if thing == k.name:
                return 2, k

        return False, None

    # This function takes a string and calls to see if the string matches the
    # name of a Feature or Item in the Room. If it does the appropriate description
    # is returned
    def look_in_room(self, name):

        status, thing = self.in_room(name)

        if status == 1:
            return True, thing.description
        elif status == 2:
            return True, thing.get_description()
        else:
            return False, None


    # This function takes some action against a Feature in the Room
    # Parameters:
    #   name - str, the name of the Room
    def action_feature(self, name):

        # make sure the Feature is in the Room and get its index
        # from the Features list
        status, index = self.get_feature_id(name)

        # if the item is present modify its state to in_action
        # and return the in_action description
        if status:
            self.features[index].state = 1
            return self.features[index].get_description()
        else:
            return 'You cannot do that'

    # takes a string and returns an index and an integer
    # the integer shows whether the item is in the starting items
    # or dropped items lists (or neither)
    def get_index_by_name(self, item):

        for x in range(0, len(self.starting_items)):
            if self.starting_items[x].name == item:
                return 1, x

        for y in range(0, len(self.dropped_items)):
            if self.dropped_items[y].name == item:
                return 2, y

        return 3, None

    # takes a string, tests that the item is in one of the lists,
    # sets variables on the item, gets the item, removes it from the
    # list and returns the item for adding to the inventory
    def take_item(self, item):

        status, x = self.get_index_by_name(item)

        # status 1 means this was a starting item
        if status == 1:
            self.features[self.starting_items[x].linked_feature].state = 3
            self.starting_items[x].linked_feature = None
            taken_item = self.starting_items[x]
            del self.starting_items[x]
            return True, taken_item
        # status 2 means this was a dropped item
        elif status == 2:
            taken_item = self.dropped_items[x]
            del self.dropped_items[x]
            return True, taken_item
        # anything else means the item is not here
        else:
            return False, None

    # Adds an Item object to the dropped_items list
    def leave_item(self, item):

        self.dropped_items.append(item)


    # This function prints the description of the Room based on whether it has been visited or not
    def get_description(self):

        print('-------------------------------------------------')
        print('CURRENT LOCATION: \n\t{}'.format(self.name))
        if not self.visited:
            print('DESCRIPTION: \n\t{}'.format(self.long_des))
        else:
            print('DESCRIPTION: \n\t{}'.format(self.short_des))

        print('AVAILABLE DIRECTIONS: ')
        for key in self.directions:
            print('\t{}'.format(key))

        print('FEATURES:')
        for feature in self.features:
            print('\t{}'.format(feature.name))

        if len(self.starting_items) > 0:
            print('STARTING ITEMS:')
            for x in range(0, len(self.starting_items)):
                print('\t{}'.format(self.starting_items[x].name))

        if len(self.dropped_items) > 0:
            print('DROPPED ITEMS:')
            for y in range(0, len(self.dropped_items)):
                print('\t{}'.format(self.dropped_items[y].name))

    # This function will need to be toggled when a player enters the Room (after calling the getDescription function)
    def set_visited(self):
        self.visited = True
