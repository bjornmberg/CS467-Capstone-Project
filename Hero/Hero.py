class Hero:
    """ Class used to represent the player of the Game

    Attributes:
    _________
    name: str
        the name of the Player
    location: int
        integer representing the index of the Room from Game.rooms_list
    time: int
        player's in-game time

    Methods:
    _______
    set_time()
        sets the in-game time for the Player
    save_hero()
        returns a dict representation of the Hero for saving
    """



    def __init__(self, name, location, time, day):
        """Constructor for the Hero class

        :param str name: the name of the Hero
        :param int location: the index of the current Room from Game.rooms_list
        :param int time: the in-game time for the Hero
        """
        self.name = name
        self.location = location
        self.time = time
        self.day = day

    def set_time(self):
        """Increases and returns the in-game time

        :param int time: the in-game time of the Hero
        :return: int: the increased time of the Hero
        """
        self.time = self.time + 1
        if self.time == 24:
            self.time = 0
            self.day += 1
        return self.time

    def save_hero(self):
        """Formats and returns a dict of the Hero for saving

        :return: dict: a representation of the Hero for saving
        """
        hero_dict = dict()
        hero_dict['name'] = self.name
        hero_dict['location'] = self.location
        hero_dict['time'] = self.time
        hero_dict['day'] = self.day

        return hero_dict
