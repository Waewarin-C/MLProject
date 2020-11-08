import pygame
import GameWindow
import TitleScreenScene
import TicTacToeBoardScene
from ParallaxEffect import *
from TicTacToe import *
from Player import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BUTTON_RADIUS = 4
FONT_PATH = './Open_Sans/OpenSans-Regular.ttf'


class ChooseSymbolScene:

    def __init__(self, screen, game_id):
        self.screen = screen
        self.screen.fill(WHITE)
        self.game_id = game_id

        self.circle_sprite = pygame.image.load('./osprites.png')
        self.circle_sprite = pygame.transform.smoothscale(self.circle_sprite, (200, 200))

        self.x_sprite = pygame.image.load('./xsprites.png')
        self.x_sprite = pygame.transform.smoothscale(self.x_sprite, (200, 200))

        self.parallax = ParallaxEffect(self.screen)
        self.back_button = pygame.image.load('./back_arrow.png').convert_alpha()
        self.font = pygame.font.Font(FONT_PATH, 26)
        self.prompt_text_surface = self.font.render('Player 1 Choose Symbol', True, BLACK)
        self.width = self.prompt_text_surface.get_width()
        self.middle_diff = abs((GameWindow.window_width / 2) - (self.width / 2))

        pygame.display.update()

    def render(self):
        self.parallax.render_parallax_background_graphic()
        self.screen.blit(self.prompt_text_surface, (self.middle_diff, 500))
        self.screen.blit(self.back_button, (10, 10))

        self.screen.blit(self.circle_sprite, (50, 175))
        self.screen.blit(self.x_sprite, (310, 175))

        pygame.display.flip()

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_coords = pygame.mouse.get_pos()


            # Back button region
            if 10 <= mouse_coords[0] <= 10 + 36 and 10 <= mouse_coords[1] <= 10 + 36:
                GameWindow.GameWindowFoundation.scene = TitleScreenScene.TitleScreenScene(self.screen)

            # Circle symbol
            if 50 <= mouse_coords[0] <= 50 + 200 and 175 <= mouse_coords[1] <= 175 + 200:

                game_model = None
                if self.game_id == 'Train Agent':
                    pass
                elif self.game_id == 'Player vs. Player':
                    game_model = TicTacToe(Player('O', 'Player 1'), Player('X', 'Player 2'))
                else:
                    pass

                GameWindow.GameWindowFoundation.scene = TicTacToeBoardScene.TicTacToeBoardScene(self.screen, game_model)

            # X symbol
            if 310 <= mouse_coords[0] <= 310 + 200 and 175 <= mouse_coords[1] <= 175 + 200:

                game_model = None
                if self.game_id == 'Train Agent':
                    pass
                elif self.game_id == 'Player vs. Player':
                    game_model = TicTacToe(Player('X', 'Player 1'), Player('O', 'Player 2'))
                else:
                    pass

                GameWindow.GameWindowFoundation.scene = TicTacToeBoardScene.TicTacToeBoardScene(self.screen, game_model)