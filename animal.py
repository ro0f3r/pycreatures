from thing import Thing


class Animal(Thing):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "A"
