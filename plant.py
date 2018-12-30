from PyCreatures.thing import Thing


class Plant(Thing):
    MAX_AGE = 5
    PROBABILITY_TO_SPREAD = 70

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "$"

    def get_probability_to_spread(self):
        return self.PROBABILITY_TO_SPREAD
