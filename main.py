import os, sys
import pygame
from pygame.locals import *
from FirstTestRun import *

# Testing UI configurations
def begin_game():

    while True:

        pygame.init()
        window_size = (600, 600)
        screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("ML Tic Tac Toe")

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        screen.blit(background, (0, 0))
        pygame.display.flip()

        if sys.platform == "darwin":
            custom_cursor = pygame.image.load(os.path.join('./', 'macmouse.png')).convert_alpha()
            custom_cursor = pygame.transform.scale(custom_cursor, (18, 27))
            pygame.mouse.set_visible(False)
            screen.blit(custom_cursor, (pygame.mouse.get_pos()))
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                return


if __name__ == '__main__':
    begin_game()
