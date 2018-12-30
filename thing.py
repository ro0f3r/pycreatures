class Thing:
    def __init__(self):
        self.age = 0

    def __str__(self):
        return "0"

    def __repr__(self):
        return self.name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.__class__.__name__

