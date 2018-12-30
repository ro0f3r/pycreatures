from thing import Thing


class Plant(Thing):
    def __init__(self):
        super().__init__()
        self.probability_to_spread = 50

    def __str__(self):
        return "$"

    def get_probability_to_spread(self):
        return self.probability_to_spread
