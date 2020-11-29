import pygame
import GameWindow
from ChooseSymbolScene import *
from ParallaxEffect import *
from Training import *
from GameEnvironment import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BUTTON_RADIUS = 4
FONT_PATH = './Open_Sans/OpenSans-Light.ttf'

button_regions = dict()


class TitleScreenScene:

    def __init__(self, screen):
        self.screen = screen
        self.screen.fill(WHITE)
        self.parallax = ParallaxEffect(self.screen)

    def render_game_title(self):
        font_size = 64
        font, text_surface = self.prepare_font_and_text_surface(FONT_PATH, font_size, 'TIC-TAC-TOE', BLACK)

        width = text_surface.get_width()
        middle_diff = abs((GameWindow.window_width / 2) - (width / 2))

        sub_font_size = 20
        sub_font, sub_text_surface = self.prepare_font_and_text_surface(FONT_PATH, sub_font_size,
                                                                        'Gabriel Morales, Chelsea Flores, Waewarin Chindarassami',
                                                                        BLACK)

        sub_width = sub_text_surface.get_width()
        sub_middle_diff = abs((GameWindow.window_width / 2) - (sub_width / 2))

        self.screen.blit(sub_text_surface, (sub_middle_diff, 100))
        self.screen.blit(text_surface, (middle_diff, 0))

    def render_train_agent_button(self):
        font_size = 30
        y_offset = 290
        button_text = 'Train Agent'

        self.create_and_draw_button(button_text, font_size, y_offset)

    def render_player_vs_agent_button(self):
        font_size = 30
        y_offset = 380
        button_text = 'Player vs. Agent'

        self.create_and_draw_button(button_text, font_size, y_offset)

    def create_and_draw_button(self, button_text, font_size, y_offset):
        font, text_surface = self.prepare_font_and_text_surface(FONT_PATH, font_size, button_text, WHITE)
        width = text_surface.get_width()
        height = text_surface.get_height()
        button_center_x, button_center_y, middle_diff = self.calculate_centers(height, width, y_offset)
        self.draw_rectangle(button_center_x, button_center_y, height, width, button_text)
        self.screen.blit(text_surface, (middle_diff, y_offset))

    def render_player_vs_player_button(self):
        font_size = 30
        y_offset = 470
        button_text = 'Player vs. Player'

        self.create_and_draw_button(button_text, font_size, y_offset)

    def calculate_centers(self, height, width, y_offset):

        middle_diff = abs((GameWindow.window_width / 2) - (width / 2))
        button_center_x = abs((GameWindow.window_width / 2) - (width + 50) / 2)
        button_center_y = abs((y_offset + (height / 2)) - ((height + (height / 4)) / 2))
        return button_center_x, button_center_y, middle_diff

    def prepare_font_and_text_surface(self, font_path, font_size, text_label, text_color):

        font = pygame.font.Font(font_path, font_size)
        text_surface = font.render(text_label, True, text_color)
        return font, text_surface

    def draw_rectangle(self, button_center_x, button_center_y, height, width, button_id):

        button_x_coord = button_center_x
        button_y_coord = button_center_y + 3

        button_width = width + 50
        button_height = height + (height / 4)

        button_regions[button_id] = dict()
        button_regions[button_id]['top_left'] = (button_x_coord, button_y_coord)
        button_regions[button_id]['top_right'] = (button_x_coord + button_width, button_y_coord)
        button_regions[button_id]['bottom_left'] = (button_x_coord, button_y_coord + button_height)
        button_regions[button_id]['bottom_right'] = (button_x_coord + button_width, button_y_coord + button_height)

        pygame.draw.rect(self.screen, BLACK,
                         [button_x_coord, button_y_coord, button_width, button_height],
                         border_radius=BUTTON_RADIUS)

    def render(self):
        self.parallax.render_parallax_background_graphic()
        self.render_game_title()
        self.render_player_vs_agent_button()
        self.render_train_agent_button()
        self.render_player_vs_player_button()

        pygame.display.flip()

    def goto_scene(self, new_scene):
        pass

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for id in button_regions.keys():
                x1, y1 = button_regions[id]['top_left']
                x2, _ = button_regions[id]['top_right']
                _, y2 = button_regions[id]['bottom_right']
                _, _ = button_regions[id]['bottom_left']

                if x1 <= mouse_x <= x2 and y1 <= mouse_y <= y2:

                    if id == 'Train Agent':
                        trainer = Training()
                        trainer.begin_training(number_of_battles=500)
                        break

                    GameWindow.GameWindowFoundation.scene = ChooseSymbolScene(self.screen, id)
                    break