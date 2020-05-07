from Item import Item


class Inventory:

    capacity = 5

    def __init__(self, items):

        self.items = []

        for i in items:
            new_item = Item(i['name'], i['description'], i['linkedFeature'])
            self.items.append(new_item)

    # ADD COMMENTS
    def add_item(self, item):

        if len(self.items) < self.capacity:
            self.items.append(item)
            print('{} - added to your inventory.'.format(item.name))
        else:
            print('You cannot hold anymore items in your inventory.')

    def remove_item(self, item):
        if item.name != 'prybar':
            self.items.remove(item)

    # ADD COMMENTS
    def in_inventory(self, str_input):

        for x in range(0, len(self.items)):
            if self.items[x].name == str_input:
                # return True, x
                return True, self.items[x]

        return False, None

    # ADD COMMENTS
    def drop_item(self, str_input):

        success = False
        status, item = self.in_inventory(str_input)

        if status:
            self.items.remove(item)
            success = True
            return success, item
        else:
            print('That item is not in your inventory.')
            return success, None

    # ADD COMMENTS
    def show_inventory(self):

        if len(self.items) > 0:
            print('These are the items in the inventory: ')
            for x in self.items:
                print(x.name)
        else:
            print('The inventory is empty.')

    # ADD COMMENTS
    def look_in_inventory(self, str_input):

        status, item = self.in_inventory(str_input)

        if status:
            return True, item.description
        else:
            return False, None

    # Simple boolean check. If there, return true. If not, return false.
    def checkInventory(self, str_input):
        for x in range(0, len(self.items)):
            if self.items[x].name == str_input:
                return True
        return False

    def save_inventory(self):

        save_list = list()

        for item in self.items:
            save_list.append(item.save_item())

        return save_list
