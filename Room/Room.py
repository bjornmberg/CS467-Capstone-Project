import textwrap
from Feature import Feature
from Item import Item
from Wrapper import wrapper

class Room:
    """Class used to represent a Room within the Game

    Attributes
    ----------
    name: str
        the name of the Room
    long_des: str
        the long description of the Room
    short_des: str
        the short description of the Room
    visited: bool
        if the Room has been visited or not
    room_id: int
        unique identifier of the Room (also the index within Game.room_list
    directions: dict
        key - direction, value - index of adjacent Room ex: {'north': 1}
    dropped_items: list (of Item objects)
        Items the player has dropped in the Room
    starting_items: list (of Item objects)
        Items that are initialized in the Room

    Methods
    -------
    generate_lists()
        initializes Items and Room state
    get_feature()
        returns a Feature based on the Feature name
    in_room()
        checks if a Feature or Item is present and returns it
    look_in_room()
        returns the description of a Feature or Item
    action_feature()
        performs an action on a Feature and alters its state
    get_item()
        gets an Item from the staring_items or dropped_items lists
    take_item()
        removes the Item from the starting_items or dropped_items lists
    leave_item()
        adds an Item to the dropped_items list
    get_description()
        returns the description of the Feature or Item called
    set_visited()
        sets the visited bool to True
    save_room()
        formats the Room into a dict representation for saving
    """

    def __repr__(self):
        return self

    def __init__(self, name, long_des, short_des, visited, room_id, directions, s_items, d_items, feats):
        """Constructor for the Room class

        :param str name: name of the Room
        :param str long_des: long description of the Room
        :param str short_des: short description of the Room
        :param bool visited: visited status of the Room
        :param int room_id: unique identifier of the Room
        :param dict directions: ex {"north": 1}
        :param list s_items: list of starting Items
        :param list d_items: list of dropped Items
        :param list feats: list of Room Features
        """
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

    def generate_lists(self, s_items, d_items, feats):
        """Initializes the Items that are in a Room

        :param list s_items: starting Items
        :param list d_items: dropped Items
        :param list feats: Features
        :return: VOID
        """
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

    def get_feature(self, name):
        """Gets a Feature by its name (Feature.name)

        :param str name: name of Feature
        :return: True/Feature if Feature present, False/None if not present
        """
        for feat in self.features:
            if feat.name == name:
                return True, feat

        return False, None

    def in_room(self, str_input):
        """Check that a Feature or Item is in a Room base on user input

        :param str str_input: a user input of a Feature or Item name
        :return: int - representing Item or Feature and the Item, False/None if no Item or Feature
        """
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

    def look_in_room(self, str_input):
        """Gets the description of an Item or Feature if it is in a Room

        :param str str_input: user input for a Feature or Item name
        :return: True/description if Feature/Item present, False/None if not present
        """
        status, item_or_feature = self.in_room(str_input)

        if status == 1:
            return True, item_or_feature.description
        elif status == 2:
            return True, item_or_feature.get_description()
        else:
            return False, None

    def action_feature(self, str_input):
        """Performs an action on a Feature and modifies its state

        :param str str_input: user input of Feature wished to be acted on
        :return: description of the modified Feature or failure message
        """
        # make sure the Feature is in the Room and get its index
        # from the Features list
        status, feat = self.get_feature(str_input)

        # if the item is present modify its state to in_action
        # and return the in_action description
        if status:
            if feat.actionable:
                feat.state = 1
                return feat.get_description()
            else:
                return 'You cannot do that to the {}.'.format(feat.name)
        else:
            return 'You cannot do that'

    def get_item(self, str_input):
        """Gets an Item from the Room based on user input of the name

        :param str str_input: user input of the name of an Item in the Room
        :return: Int representing starting/dropped Item and Item or None
        """
        for x in self.starting_items:
            if x.name == str_input:
                return 1, x

        for y in self.dropped_items:
            if y.name == str_input:
                return 2, y

        return 3, None

    def take_item(self, str_input):
        """Removes an Item from starting or dropped items and returns it

        :param str str_input: user input of Item wished to be taken
        :return: True/Item if present - False/None if not present
        """
        status, item = self.get_item(str_input)

        status, item = self.verify_takable_on_game_progress(status, item)

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

    def leave_item(self, item):
        """Adds an Item to the dropped_items list

        :param Item item: the Item wished to be dropped
        :return: VOID
        """
        self.dropped_items.append(item)

    def get_description(self):
        """Formats and prints the current description of the Room

        :return: VOID
        """
        center_left_right = 125
        print()
        print((' ' * 20) + ('▃' * 85) + '\n')
        print('CURRENT LOCATION: {}\n'.format(self.name).center(center_left_right))

        # If not visited, check for newlines and output long description
        if not self.visited:

            # Check for newlines & bold or character signifiers
            if ('\n' in self.long_des) or ('@' in self.long_des) or ('^' in self.long_des) or ('$' in self.long_des) or ('~' in self.long_des) or ('#' in self.long_des):
                processed = wrapper.wrap_processor(self.long_des)
                for i in processed:
                    print(i)

            # Else no newlines or bold color signifiers. Simple processing.
            else:
                print(textwrap.fill('{}'.format(self.long_des), 100, initial_indent=(' ' * 20), subsequent_indent=(' ' * 20)))
        # Else player has visited before, output short description
        else:
            # Check for newlines & bold or character signifiers
            if ('\n' in self.short_des) or ('@' in self.short_des) or ('^' in self.short_des) or ('$' in self.short_des) or ('~' in self.long_des) or ('#' in self.short_des):
                processed = wrapper.wrap_processor(self.short_des)
                for i in processed:
                    print(i)

            # Else no newlines or bold color signifiers. Simple processing.
            else:
                print(textwrap.fill('{}'.format(self.short_des), 100, initial_indent=(' ' * 20), subsequent_indent=(' ' * 20)))

        print()
        print()
        if len(self.dropped_items) > 0:
            print(textwrap.fill('You seem to have left these items on the floor: ', initial_indent=(' ' * 20)))
            for y in range(0, len(self.dropped_items)):
                print(textwrap.fill('\t{}'.format(self.dropped_items[y].name), initial_indent=(' ' * 18)))
        print((' ' * 20) + ('▃' * 85) + '\n\n')

    def set_visited(self):
        """Sets the state of the Room to visited

        :return: VOID
        """
        self.visited = True

    def save_room(self):
        """Formats the Room into a dict for saving

        :return: dict representation of the Room object
        """
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

    def verify_takable_on_game_progress(self, status, item):
        """Checks if an item has a special check on task-progression

        :param status item: True/False status based on precense of item
        :return: True/Item if present & feature status OK's progression - False/None if not present
        pre-existing bool / Item (or None), if item does not have special check
        """
        if item.name == 'locket':
            if self.features[0].state == 2:
                return status, item
            else:
                status = False
                item = None
                return status, item
        else:
            return status, item
