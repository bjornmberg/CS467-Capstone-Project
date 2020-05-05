class Hero:

    def __init__(self, name, location):

        self.name = name
        self.location = location

    def save_hero(self):

        hero_dict = dict()
        hero_dict['name'] = self.name
        hero_dict['location'] = self.location

        return hero_dict
