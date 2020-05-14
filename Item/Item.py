class Item:
    """Classed used to represent a collectible object within the Game

    Attributes
    ----------
    name: str
        name of the Item
    description: str
        the description of the Item
    linked_feature: int
        the feature_id of any Feature within a Room linked to the Item

    Methods
    -------
    save_item()
        returns a dict representation of the Item for saving
    """

    def __init__(self, name, description, linked_feature):

        self.name = name
        self.description = description
        self.linked_feature = linked_feature

    def __repr__(self):
        return self

    def save_item(self):
        """Formats and returns a dict representation of the Item for saving

        :return: dict - representing the Items current state
        """
        item_dict = {
            'name':self.name,
            'description': self.description,
            'linkedFeature': self.linked_feature
        }
        return item_dict
