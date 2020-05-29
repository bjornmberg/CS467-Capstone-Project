from Item import Item

class Inventory:
    """ Class used to represent the Game Inventory

    Attributes:
    _________
    capacity: int
        the maximum items the Inventory can hold
    items: list (of Item objects)
        holds the current Items in the Inventory

    Methods:
    _______
    add_item()
        adds Item to the items list
    remove_item()
        removes Item from the items list
    in_inventory()
        checks that Item is present in inventory and returns the Item
    drop_item()
        removes Item from the items list
    show_inventory()
        displays the Items in the Inventory
    look_in_inventory()
        displays the description of an Item in the Inventory
    save_inventory()
    """
    capacity = 5    # the maximum amount of Items that can be held

    def __init__(self, items):
        """Constructor for the Inventory class

        :param list items: list of dictionary's containing Item information
        """
        self.items = []
        # go through each dict and initialize and Item adding it to the items list
        for i in items:
            new_item = Item(i['name'], i['description'], i['linkedFeature'])
            self.items.append(new_item)

    def space_available(self):
        if len(self.items) < self.capacity:
            return True
        else:
            return False

    def add_item(self, item):
        """Places an Item into the Inventory

        :param Item item: an Item object
        :return: VOID
        """
        # check that the Item can fit in the Inventory, add if possible
        self.items.append(item)
        print('\n' + (' ' * 20) + '{} - added to your inventory.\n'.format(item.name), end='')


    def remove_item(self, item):
        """Removes an Item from the items list

        :param Item item: an Item object to be removed
        :return: VOID
        """
        # Remove any Item except the prybar which can be used multiple times
        if item.name != 'prybar':
            self.items.remove(item)

    def in_inventory(self, str_input):
        """Check that an Item is in the items list and return the Item object

        :param str str_input: the item being searched for
        :return: True if Item present and Item, False if Item not present and None
        """
        for x in range(0, len(self.items)):
            if self.items[x].name == str_input:
                # return True, x
                return True, self.items[x]

        return False, None

    def key_in_inventory(self, str_input):
        """Check that a specific key Item is in the items list and return the key Item object

        :param str str_input: the item being searched for, by description
        :return: True if Item present and Item, False if Item not present and None
        """
        for x in range(0, len(self.items)):
            if self.items[x].description == str_input:
                # return True, x
                return True, self.items[x]

        return False, None

    def drop_item(self, str_input):
        """Pops an Item from the inventory and provides status and feedback

        :param str str_input: name of an Item wishing to be dropped
        :return: True if Item present and Item, False if Item not present and None
        """
        success = False
        # check that the Item is in the Inventory
        status, item = self.in_inventory(str_input)

        # if Item in inventory return success and the Item
        if status:
            self.items.remove(item)
            success = True
            return success, item
        # Else success is fals and Item is None
        else:
            return success, None

    def show_inventory(self):
        """Displays the Items currently in the Inventory

        :return: VOID
        """
        if len(self.items) > 0:
            print('\n' + (' ' * 20) + 'These are the items in your inventory:\n')
            if len(self.items) == 1:
                print((' ' * 20) + self.items[0].name)
            elif len(self.items) == 2:
                if self.items[1].name == 'shears' or self.items[1].name == 'ashes':
                    print((' ' * 20) + self.items[0].name, end=' and ')
                    print(self.items[1].name)
                else:
                    print((' ' * 20) + self.items[0].name, end=' and a ')
                    print(self.items[1].name)
            else:
                print((' ' * 19), end=' ')
                for x in range(0, len(self.items)):
                    if x < (len(self.items) - 1):
                        print(self.items[x].name, end=', ')
                    else:
                        if self.items[x].name == 'shears' or self.items[x].name == 'ashes':
                            print('and ' + self.items[x].name)
                        else:
                            print('and a ' + self.items[x].name)
        else:
            print('\n' + (' ' * 20) + 'Your inventory is empty.')

    def show_inventory_map_screen(self):
        """Displays the Items currently in the Inventory to map screen

        :return: VOID
        """
        if len(self.items) > 0:
            print('These are the items in your inventory:', end=' ')
            if len(self.items) == 1:
                print(self.items[0].name)
            elif len(self.items) == 2:
                if self.items[1].name == 'shears' or self.items[1].name == 'ashes':
                    print(self.items[0].name, end=' and ')
                    print(self.items[1].name)
                else:
                    print(self.items[0].name, end=' and a ')
                    print(self.items[1].name)
            else:
                for x in range(0, len(self.items)):
                    if x < (len(self.items) - 1):
                        print(self.items[x].name, end=', ')
                    else:
                        if self.items[x].name == 'shears' or self.items[x].name == 'ashes':
                            print('and ' + self.items[x].name)
                        else:
                            print('and a ' + self.items[x].name)
        else:
            print('Your inventory is empty.')

    def look_in_inventory(self, str_input):
        """Gets description of an Item if it is in the Inventory

        :param str str_input: user input of Item name wishing to be displayed
        :return: True if Item present and description, False if not present and None
        """
        status, item = self.in_inventory(str_input)

        if status:
            return True, item.description
        else:
            return False, None

    def save_inventory(self):
        """Formats and returns list of Items in inventory for saving

        :return: list : representation of the Inventory for saving
        """
        save_list = list()

        for item in self.items:
            save_list.append(item.save_item())

        return save_list
