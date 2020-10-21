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
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))

        pygame.display.set_caption("ML Tic Tac Toe")

    def render_mac_mouse(self):
        if sys.platform == "darwin":
            self.custom_cursor = pygame.image.load(os.path.join('./', 'macmouse.png')).convert_alpha()
            self.custom_cursor = pygame.transform.scale(self.custom_cursor, (18, 27))
            pygame.mouse.set_visible(False)
            self.screen.blit(self.custom_cursor, (pygame.mouse.get_pos()))
            pygame.display.flip()

    def start_game(self):
        # This is the main loop for the entire game.
        # We can setup scenes from here potentially.
        while True:
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()
            self.render_mac_mouse()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
