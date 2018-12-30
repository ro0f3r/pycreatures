import pygame

from world import World
from plant import Plant
from thing import Thing
from animal import Animal


class GameSurface:
    # define all necessary colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BROWN = (102, 51, 0)
    GREEN = (0, 255, 0)

    def __init__(self):
        self.window_height = 800
        self.window_width = 800
        self.simulation_height = self.window_height
        self.simulation_width = self.window_width
        self.window_caption = "PyCreatures"
        self.background_color = self.BLACK
        self.fps = 60

        # initialize all necessary pygame stuff
        pygame.init()
        pygame.display.set_caption(self.window_caption)
        self.game_window = pygame.display.set_mode((self.window_width, self.window_width))
        self.game_clock = pygame.time.Clock()

        self.world = World(40, 40)
        self.tile_width = self.window_width // self.world.get_width()
        self.tile_height = self.window_height // self.world.get_height()
        # print(self.tile_width, self.tile_width)
        self.start_game()

    def start_game(self):
        self.draw_simulation_field()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_SPACE:
                        self.world.compute_one_year()
                        self.draw_simulation_field()
                    if event.key == pygame.QUIT:
                        pygame.quit()
                        quit()

    def draw_simulation_field(self):
        for row in self.world.get_all_objects():
            for thing in row:
                if isinstance(thing, Plant):
                    x1 = self.world.get_coordinates(thing)[0]
                    x2 = self.world.get_coordinates(thing)[1]
                    pygame.draw.rect(self.game_window, self.GREEN,
                                     [x1 * self.tile_width, x2 * self.tile_height, self.tile_width, self.tile_height])
                elif isinstance(thing, Animal):
                    x1 = self.world.get_coordinates(thing)[0]
                    x2 = self.world.get_coordinates(thing)[1]
                    pygame.draw.rect(self.game_window, self.BROWN,
                                     [x1 * self.tile_width, x2 * self.tile_height, self.tile_width, self.tile_height])
                elif isinstance(thing, Thing):
                    x1 = self.world.get_coordinates(thing)[0]
                    x2 = self.world.get_coordinates(thing)[1]
                    pygame.draw.rect(self.game_window, self.BLACK,
                                     [x1 * self.tile_width, x2 * self.tile_height, self.tile_width, self.tile_height])

        pygame.display.update()
        self.game_clock.tick(self.fps)


game_window = GameSurface()
