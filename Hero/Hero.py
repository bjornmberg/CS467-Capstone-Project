class Hero:

    name = None
    location = None
    # hero_time = 9

    # def setTime(self, time):
    #     time = time + 1
    #     # If new day, set to 0
    #     if time == 24:
    #         time = 0
    #     return time

    def __init__(self, name, location):

        self.name = name
        self.location = location
        # self.hero_time = hero_time

    def save_hero(self):

        hero_dict = dict()
        hero_dict['name'] = self.name
        hero_dict['location'] = self.location
        # hero_dict['hero_time'] = self.hero_time

        return hero_dict

