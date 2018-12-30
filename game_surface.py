import pygame
import time

from PyCreatures.world import World
from PyCreatures.plant import Plant
from PyCreatures.thing import Thing
from PyCreatures.animal import Animal


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
        self.round_no = 0
        self.sprites = {}

        # initialize all necessary pygame stuff
        pygame.init()
        pygame.display.set_caption(self.window_caption)
        self.game_window = pygame.display.set_mode((self.window_width, self.window_width))
        self.game_clock = pygame.time.Clock()
        self.initialize_sprites()

        self.world = World(40, 40)
        self.tile_width = self.window_width // self.world.get_width()
        self.tile_height = self.window_height // self.world.get_height()
        # print(self.tile_width, self.tile_width)
        self.start_game()

    def initialize_sprites(self):
        self.sprites["plant"] = [pygame.image.load("assets/plant.png")]
        self.sprites["animal"] = [pygame.image.load("assets/animal.png")]

    def start_game(self):
        self.draw_simulation_field()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_SPACE:
                        self.round_no += 1
                        start_time = time.time()
                        self.world.compute_one_year()
                        self.draw_simulation_field()
                        print("Round #%i took %.2f seconds to compute." % (self.round_no, time.time() - start_time))
                    if event.key == pygame.QUIT:
                        pygame.quit()
                        quit()

    def draw_simulation_field(self):
        for row in self.world.get_all_objects():
            for thing in row:
                x1 = self.world.get_coordinates(thing)[0]
                x2 = self.world.get_coordinates(thing)[1]
                if isinstance(thing, Plant):
                    self.game_window.blit(self.sprites["plant"][0], [x1 * self.tile_width, x2 * self.tile_height])
                elif isinstance(thing, Animal):
                    self.game_window.blit(self.sprites["animal"][0], [x1 * self.tile_width, x2 * self.tile_height])
                elif isinstance(thing, Thing):
                    pygame.draw.rect(self.game_window, self.WHITE,
                                     [x1 * self.tile_width, x2 * self.tile_height, self.tile_width, self.tile_height])

        pygame.display.update()
        self.game_clock.tick(self.fps)


game_window = GameSurface()
