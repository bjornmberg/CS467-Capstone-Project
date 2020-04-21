from Item import Item


class Inventory:

    items = list()
    capacity = 5


    def add_item(self, item):

        print('HERE')
        if len(self.items) <= self.capacity:
            self.items.append(item)
            print('{} - added to your inventory.'.format(item.name))
        else:
            print('You cannot hold anymore items in your inventory.')

    # def drop_item(self, item):
    #
    #     success = None
    #
    #     if item in self.items:
    #         dropped_item = self.items[item]
    #         dropped_item['dropped'] = True
    #         del self.items[item]
    #         success = True
    #         print('Dropping {}'.format(item))
    #         return success, dropped_item
    #     else:
    #         success = False
    #         print('That item is not in your inventory.')
    #         return success, {}
    #
    def show_inventory(self):
        if len(self.items) > 0:
            print('These are the items in the inventory: ')
            for x in self.items:
                print(x.name)
        else:
            print('The inventory is empty.')