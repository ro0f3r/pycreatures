from random import choice
import random as rnd

from thing import Thing
from plant import Plant
from animal import Animal


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.game_objects = []

        for _ in range(self.height):
            available_things = ["plant", "thing", "animal"]
            thing_row = []
            for _ in range(self.width):
                chosen_object = choice(available_things)
                if chosen_object == "plant" and rnd.random() < 0.5:
                    thing_row.append(Plant())
                elif chosen_object == "animal" and rnd.random() < 0.5:
                    thing_row.append(Animal())
                else:
                    thing_row.append(Thing())
            self.game_objects.append(thing_row)

    def __repr__(self):
        return self.game_objects

    def __str__(self):
        world_string = ""
        for row in self.game_objects:
            for obj in row:
                world_string += str(obj) + " "
            world_string += "\n"

        return world_string

    def get_all_objects(self):
        return self.game_objects

    def compute_one_year(self):
        for row in self.get_all_objects():
            for world_object in row:
                world_object.age += 1
        self.compute_plants()
        self.compute_animals()

    def compute_animals(self):
        for row in self.get_all_objects():
            for animal in row:
                if isinstance(animal, Animal):
                    animal_neighbors = self.get_neighbors(animal)
                    neighbor_position = choice(["upper_neighbor", "right_neighbor", "lower_neighbor", "left_neighbor"])
                    chosen_neighbor = animal_neighbors[neighbor_position]
                    if isinstance(chosen_neighbor, Plant):
                        # print("Plant @", self.get_coordinates(chosen_neighbor), "got eaten. (", neighbor_position, ")")
                        self.get_all_objects()[self.get_coordinates(chosen_neighbor)[1]][self.get_coordinates(chosen_neighbor)[0]] = Thing()

    def compute_plants(self):
        for row in self.get_all_objects():
            for plant in row:
                if isinstance(plant, Plant):
                    self.spread_plant(plant)

    def spread_plant(self, plant):
        # print(plant.get_name(), self.get_coordinates(plant), sep="\t")

        # spread plant with its probability
        if (rnd.random() * 100) < plant.get_probability_to_spread():
            object_neighbors = self.get_neighbors(plant)

            for neighbor_name in object_neighbors:
                # print(object_neighbors[neighbor_name].get_name(), neighbor_name, "@",
                    # self.get_coordinates(object_neighbors[neighbor_name]), "age:", object_neighbors[neighbor_name].age,
                    # sep="\t")
                if isinstance(object_neighbors[neighbor_name], Thing) \
                        and not isinstance(object_neighbors[neighbor_name], Plant) \
                        and not isinstance(object_neighbors[neighbor_name], Animal) and isinstance(plant, Plant):
                    self.get_all_objects()[self.get_coordinates(object_neighbors[neighbor_name])[1]][
                        self.get_coordinates(object_neighbors[neighbor_name])[0]] = Plant()
            else:
                pass
                # print(plant.get_name(), "didn't spread.")

    def get_neighbors(self, object_from_world):
        """Gets a thing from the world and returns a dictionary containing string keys that describe
        where a certain neighbor is. The dictionary's values contain a tuple representing that neighbor's
        coordinates in the world.
        """
        # get object position
        object_coordinates = self.get_coordinates(object_from_world)

        return {"upper_neighbor": self.get_upper_neighbor(object_coordinates),
                "right_neighbor": self.get_right_neighbor(object_coordinates),
                "lower_neighbor": self.get_lower_neighbor(object_coordinates),
                "left_neighbor": self.get_left_neighbor(object_coordinates)
                }

    def get_coordinates(self, object_from_world):
        for x2 in range(self.height):
            for x1 in range(self.width):
                if object_from_world == self.get_all_objects()[x2][x1]:
                    return x1, x2
        return -1, -1

    def get_upper_neighbor(self, object_coordinates):
        try:
            return self.get_all_objects()[object_coordinates[1] - 1][object_coordinates[0]]
        except IndexError:
            return self.get_all_objects()[self.get_height()][object_coordinates[0]]

    def get_right_neighbor(self, object_coordinates):
        try:
            return self.get_all_objects()[object_coordinates[1]][object_coordinates[0] + 1]
        except IndexError:
            return self.get_all_objects()[object_coordinates[1]][0]

    def get_lower_neighbor(self, object_coordinates):
        try:
            return self.get_all_objects()[object_coordinates[1] + 1][object_coordinates[0]]
        except IndexError:
            return self.get_all_objects()[0][object_coordinates[0]]

    def get_left_neighbor(self, object_coordinates):
        try:
            return self.get_all_objects()[object_coordinates[1]][object_coordinates[0] - 1]
        except IndexError:
            return self.get_all_objects()[object_coordinates[1]][self.get_width()]

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width


