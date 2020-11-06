import pygame
from pygame.locals import *
from TitleScreenScene import *

window_width = 600
window_height = 600


class GameWindowFoundation:

    scene = None

    def __init__(self):
        pygame.init()
        self.custom_cursor = None
        self.window_size = (window_width, window_height)
        self.screen = pygame.display.set_mode(self.window_size, depth=24)
        pygame.display.set_caption("ML Tic Tac Toe")

    def start_game(self):

        GameWindowFoundation.scene = TitleScreenScene(self.screen)

        # This is the main loop for the entire game application.
        while True:

            GameWindowFoundation.scene.render()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                GameWindowFoundation.scene.handle_events(event)

