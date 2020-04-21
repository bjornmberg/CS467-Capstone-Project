from Item import Item


class Inventory:

    items = list()
    capacity = 5


    def add_item(self, item):

        if len(self.items) <= self.capacity:
            self.items.append(item)
            print('{} - added to your inventory.'.format(item.name))
        else:
            print('You cannot hold anymore items in your inventory.')

    def find_item_index(self, item_name):

        for x in range(0, len(self.items)):
            if self.items[x].name == item_name:
                return True, x

        return False, None

    def drop_item(self, item_name):

        success = False
        status, index = self.find_item_index(item_name)

        if status:
            dropped_item = self.items[index]
            del self.items[index]
            success = True
            return success, dropped_item
        else:
            print('That item is not in your inventory.')
            return success, None

    def show_inventory(self):
        if len(self.items) > 0:
            print('These are the items in the inventory: ')
            for x in self.items:
                print(x.name)
        else:
            print('The inventory is empty.')

    def look_in_inventory(self, thing):

        status, index = self.find_item_index(thing)

        if status:
            return True, self.items[index].description
        else:
            return False, None

