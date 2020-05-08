import textwrap
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
                f['actionable'],
                f['usable'],
                f['state'],
                f['featureId']
            )
            self.features.insert(new_feat.feature_id, new_feat)


    # This function looks through the names of the Features and returns True
    # if the Feature is in the Room and the index of the Feature in the feature list()
    def get_feature(self, name):

        for feat in self.features:
            if feat.name == name:
                return True, feat

        return False, None

    # This function is used to see if an Item or Feature is in a Room
    # If it is an Item in either dropped_items of starting_items a 1 and the
    # Item is returned, if it is in the features list() a 2 and the Feature
    # is returned - this is used for the 'look' functionality
    def in_room(self, str_input):

        for i in self.starting_items:
            if str_input == i.name:
                return 1, i
        for j in self.dropped_items:
            if str_input == j.name:
                return 1, j
        for k in self.features:
            if str_input == k.name:
                return 2, k

        return False, None

    # This function takes a string and calls to see if the string matches the
    # name of a Feature or Item in the Room. If it does the appropriate description
    # is returned
    def look_in_room(self, str_input):

        status, item_or_feature = self.in_room(str_input)

        if status == 1:
            return True, item_or_feature.description
        elif status == 2:
            return True, item_or_feature.get_description()
        else:
            return False, None

    # takes a string and returns an index and an integer
    # the integer shows whether the item is in the starting items
    # or dropped items lists (or neither)
    def get_item(self, str_input):

        for x in self.starting_items:
            if x.name == str_input:
                return 1, x

        for y in self.dropped_items:
            if y.name == str_input:
                return 2, y

        return 3, None

    # takes a string, tests that the item is in one of the lists,
    # sets variables on the item, gets the item, removes it from the
    # list and returns the item for adding to the inventory
    def take_item(self, str_input):

        status, item = self.get_item(str_input)

        # status 1 means this was a starting item
        if status == 1:
            self.features[item.linked_feature].state = 3
            item.linked_feature = None
            self.starting_items.remove(item)
            return True, item
        # status 2 means this was a dropped item
        elif status == 2:
            self.dropped_items.remove(item)
            return True, item
        # anything else means the item is not here
        else:
            return False, None

    # Adds an Item object to the dropped_items list
    def leave_item(self, item):

        self.dropped_items.append(item)


    # This function prints the description of the Room based on whether it has been visited or not
    def get_description(self):
        centerLeftRight = 100
        description = "DESCRIPTION: "
        print()
        print('▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\n'.center(centerLeftRight))
        print('CURRENT LOCATION: {}\n'.format(self.name).center(centerLeftRight))

        # If not visited, check for newlines and output long description
        if not self.visited:
            # description += self.long_des
            if '\n' in self.long_des:
                listLines = self.long_des.splitlines()
                print('            DESCRIPTION:')
                for x in listLines:
                    print(textwrap.fill('{}'.format(x), 85, initial_indent='            ', subsequent_indent='            '))
            # Else player has visited before, output short description
            else:
                print(textwrap.fill('DESCRIPTION: {}'.format(self.long_des), 85, initial_indent='            ', subsequent_indent='            '))
        else:
            description += self.short_des
            wrappedText = textwrap.wrap(description, width=74)
            for i in wrappedText:
                print('            ' + i)

        print()
        print(textwrap.fill('YOU CAN \'move\': ', initial_indent='            '))
        for key in self.directions:
            print(textwrap.fill(key, initial_indent='                        '))
        print()
        # print('            FEATURES:')
        # for feature in self.features:
        #     print(textwrap.fill('\t{}'.format(feature.name), initial_indent='                '))
        print()
        if len(self.dropped_items) > 0:
            print(textwrap.fill('You Seem to have left these items on the floor: ', initial_indent='            '))
            for y in range(0, len(self.dropped_items)):
                print(textwrap.fill('\t{}'.format(self.dropped_items[y].name), initial_indent='                '))
        print('▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃\n\n'.center(centerLeftRight))


        # if len(self.starting_items) > 0:
        #     print(textwrap.fill('Starting Items:', initial_indent='            '))
        #     for x in range(0, len(self.starting_items)):
        #         print(textwrap.fill('\t{}'.format(self.starting_items[x].name), initial_indent='                '))



    # This function will need to be toggled when a player enters the Room (after calling the getDescription function)
    def set_visited(self):
        self.visited = True


    def save_room(self):

        room_dict = {
            'name': self.name,
            'longDes': self.long_des,
            'shortDes': self.short_des,
            'visited': self.visited,
            'startingItems': [],
            'droppedItems': [],
            'features': [],
            'roomId': self.room_id,
            'directions': self.directions.copy()
        }

        for si in self.starting_items:
            room_dict['startingItems'].append(si.save_item())

        for di in self.dropped_items:
            room_dict['droppedItems'].append(di.save_item())

        for f in self.features:
            room_dict['features'].append(f.save_feature())

        return room_dict
        # feature_list = list()
        #
        # for feat in self.features:
        #     feature_list.append(feat.save_feature())
