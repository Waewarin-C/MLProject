import pygame
import GameWindow

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BUTTON_RADIUS = 4
FONT_PATH = './Open_Sans/OpenSans-Light.ttf'


class TitleScreenScene:

    def __init__(self, screen):
        self.screen = screen
        self.screen.fill(WHITE)
        self.parallax_graphic = pygame.image.load('geometric_line.png').convert()
        self.parallax_graphic = pygame.transform.smoothscale(self.parallax_graphic, (800, 750))

    def render_parallax_background_graphic(self):
        x, y = pygame.mouse.get_pos()
        self.screen.fill(WHITE)
        self.parallax_graphic.set_alpha(50)
        self.screen.blit(self.parallax_graphic, (x * -.2, y * -.2))

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
        self.draw_rectangle(button_center_x, button_center_y, height, width)
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

    def draw_rectangle(self, button_center_x, button_center_y, height, width):

        pygame.draw.rect(self.screen, BLACK,
                         [button_center_x, button_center_y + 3, width + 50, height + (height / 4)],
                         border_radius=BUTTON_RADIUS)

    def render(self):
        self.render_parallax_background_graphic()
        self.render_game_title()
        self.render_player_vs_agent_button()
        self.render_train_agent_button()
        self.render_player_vs_player_button()

        pygame.display.flip()

    def handle_events(self, events):
        pass
