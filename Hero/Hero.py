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
