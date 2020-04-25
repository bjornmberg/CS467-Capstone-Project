class Item:

    def __init__(self, name, description, linked_feature):

        self.name = name
        self.description = description
        self.linked_feature = linked_feature


    def __repr__(self):
        return self
