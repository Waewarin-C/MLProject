import os, sys
import pygame
from pygame.locals import *


class GameWindow:
    window_width = 600
    window_height = 600

    def __init__(self):
        pygame.init()

        self.custom_cursor = None
        self.window_size = (GameWindow.window_width, GameWindow.window_height)
        self.screen = pygame.display.set_mode(self.window_size)
        self.screen.fill((255, 255, 255))
        self.parallax_graphic = pygame.image.load('geometry_line.png').convert_alpha()
        self.parallax_graphic = pygame.transform.scale(self.parallax_graphic, (667, 490))

        pygame.display.set_caption("ML Tic Tac Toe")

    def render_mac_mouse(self):
        if sys.platform == "darwin":
            self.custom_cursor = pygame.image.load(os.path.join('./', 'macmouse.png')).convert_alpha()
            self.custom_cursor = pygame.transform.scale(self.custom_cursor, (18, 27))
            pygame.mouse.set_visible(False)
            self.screen.blit(self.custom_cursor, (pygame.mouse.get_pos()))

    def render_parallax_background_graphic(self):
        self.screen.blit(self.parallax_graphic, (0, 0))

    def start_game(self):

        # This is the main loop for the entire game application.
        while True:

            self.render_mac_mouse()
            self.render_parallax_background_graphic()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
