class Hero:

    name = None
    location = None
    heroTime = 9

    def setTime(self, time):
        time = time + 1
        # If new day, set to 0
        if time == 24:
            time = 0
        return time

    def __init__(self, name, location):

        self.name = name
        self.location = location

    def save_hero(self):

        hero_dict = dict()
        hero_dict['name'] = self.name
        hero_dict['location'] = self.location

        return hero_dict

