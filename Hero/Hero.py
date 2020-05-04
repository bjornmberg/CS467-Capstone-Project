class Hero:

    name = None
    location = None

    def save_hero(self):

        hero_dict = dict()
        hero_dict['name'] = self.name
        hero_dict['location'] = self.location

        return hero_dict
