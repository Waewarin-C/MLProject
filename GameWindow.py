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
        self.screen = pygame.display.set_mode(self.window_size, depth=24)
        self.screen.fill((255, 255, 255))
        self.parallax_graphic = pygame.image.load('geometric_line.png').convert()
        self.parallax_graphic = pygame.transform.smoothscale(self.parallax_graphic, (800, 750))

        pygame.display.set_caption("ML Tic Tac Toe")

    def render_parallax_background_graphic(self):
        x, y = pygame.mouse.get_pos()
        self.screen.blit(self.parallax_graphic, (x * -.2, y * -.2))

    def render_game_title(self):
        font_size = 32
        font = pygame.font.Font('freesansbold.tiff', font_size)

    def start_game(self):

        # This is the main loop for the entire game application.
        while True:

            self.render_parallax_background_graphic()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
