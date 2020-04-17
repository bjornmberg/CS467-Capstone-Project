
class Inventory:

    items = {}
    capacity = 5
    used_slots = None

    def add_item(self, key, value):

        if self.used_slots <= self.capacity:
            self.items[key] = value
            self.used_slots = self.used_slots + 1
            print('{} - added to your inventory.'.format(key))
        else:
            print('You cannot hold anymore items in your inventory.')

    def drop_item(self, item):

        success = None

        if item in self.items:
            dropped_item = self.items[item]
            dropped_item['dropped'] = True
            del self.items[item]
            success = True
            print('Dropping {}'.format(item))
            return success, dropped_item
        else:
            success = False
            print('That item is not in your inventory.')
            return success, {}

    def show_inventory(self):
        if self.items:
            print('These are the items in the inventory: ')
            for key in self.items:
                print(key)
        else:
            print('The inventory is empty.')