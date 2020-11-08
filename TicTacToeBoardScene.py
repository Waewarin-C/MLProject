import GameWindow
import pygame
from TicTacToe import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPRITE_DIMENSIONS = (111, 111)
BUTTON_RADIUS = 4
FONT_PATH = './Open_Sans/OpenSans-Light.ttf'

# design system for hitboxes: x1, y1, width, height
hit_box_1 = (70, 106, 144, 139)
hit_box_2 = (223, 106, 149, 139)
hit_box_3 = (383, 106, 144, 139)
hit_box_4 = (70, 254, 145, 161)
hit_box_5 = (224, 254, 149, 160)
hit_box_6 = (381, 254, 147, 161)
hit_box_7 = (70, 423, 144, 139)
hit_box_8 = (223, 422, 149, 140)
hit_box_9 = (381, 423, 148, 139)

board_to_UI = {(0, 0): hit_box_1, (0, 1): hit_box_2, (0, 2): hit_box_3,
               (1, 0): hit_box_4, (1, 1): hit_box_5, (1, 2): hit_box_6,
               (2, 0): hit_box_7, (2, 1): hit_box_8, (2, 2): hit_box_9}


class TicTacToeBoardScene:

    def __init__(self, screen, game_model):
        self.screen = screen
        self.screen.fill(WHITE)
        self.game_model = game_model

        self.x_symbol_sprite = self.prepare_sprite_with_path('./xsprites.png')
        self.o_symbol_sprite = self.prepare_sprite_with_path('./osprites.png')
        self.render_player_prompt_with_text('Player 1')

        self.symbol_dict = {'O': self.o_symbol_sprite,
                            'X': self.x_symbol_sprite}

        self.draw_game_board()
        pygame.display.update()

    def render(self):
        pass

    # This function will deal with interacting with the game based on screen UI interactions.
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player_symbol = self.game_model.get_current_player().get_player_symbol()
            board_coords = self.get_board_coordinates_from_click_and_render(mouse_x, mouse_y, player_symbol)
            if board_coords is None:
                return
            self.game_model.play_round(board_coords)
            self.render_player_prompt_with_text(self.game_model.get_current_player_tag())


    def get_board_coordinates_from_click_and_render(self, mouse_x, mouse_y, current_player_symbol):

        coords = None
        hit_box = None

        if hit_box_1[0] <= mouse_x <= hit_box_1[0] + hit_box_1[2] and hit_box_1[1] <= mouse_y <= hit_box_1[1] + hit_box_1[3]:
            coords = (0, 0)
            hit_box = hit_box_1

        if hit_box_2[0] <= mouse_x <= hit_box_2[0] + hit_box_2[2] and hit_box_2[1] <= mouse_y <= hit_box_2[1] + hit_box_2[3]:
            coords = (0, 1)
            hit_box = hit_box_2

        if hit_box_3[0] <= mouse_x <= hit_box_3[0] + hit_box_3[2] and hit_box_3[1] <= mouse_y <= hit_box_3[1] + hit_box_3[3]:
            coords = (0, 2)
            hit_box = hit_box_3

        if hit_box_4[0] <= mouse_x <= hit_box_4[0] + hit_box_4[2] and hit_box_4[1] <= mouse_y <= hit_box_4[1] + hit_box_4[3]:
            coords = (1, 0)
            hit_box = hit_box_4

        if hit_box_5[0] <= mouse_x <= hit_box_5[0] + hit_box_5[2] and hit_box_5[1] <= mouse_y <= hit_box_5[1] + hit_box_5[3]:
            coords = (1, 1)
            hit_box = hit_box_5

        if hit_box_6[0] <= mouse_x <= hit_box_6[0] + hit_box_6[2] and hit_box_6[1] <= mouse_y <= hit_box_6[1] + hit_box_6[3]:
            coords = (1, 2)
            hit_box = hit_box_6

        if hit_box_7[0] <= mouse_x <= hit_box_7[0] + hit_box_7[2] and hit_box_7[1] <= mouse_y <= hit_box_7[1] + hit_box_7[3]:
            coords = (2, 0)
            hit_box = hit_box_7

        if hit_box_8[0] <= mouse_x <= hit_box_8[0] + hit_box_8[2] and hit_box_8[1] <= mouse_y <= hit_box_8[1] + hit_box_8[3]:
            coords = (2, 1)
            hit_box = hit_box_8

        if hit_box_9[0] <= mouse_x <= hit_box_9[0] + hit_box_9[2] and hit_box_9[1] <= mouse_y <= hit_box_9[1] + hit_box_9[3]:
            coords = (2, 2)
            hit_box = hit_box_9

        if not self.game_model.isValidMove(coords):
            return None

        self.render_symbol_sprite_from_hitbox_with_symbol(hit_box, current_player_symbol)

        return coords


    '''
    Use this function to pass in the current symbol being used by the player (or agent)
    and pass the hitbox obtained from the click or the generated coordinate from the agent 
    using the 'board_to_UI' dictionary. The rendering will be done for you.
    '''
    def render_symbol_sprite_from_hitbox_with_symbol(self, hit_box, symbol):

        symbol_sprite = self.symbol_dict[symbol]
        sprite_height = SPRITE_DIMENSIONS[0]
        sprite_width = SPRITE_DIMENSIONS[1]

        middle_diff_x =  abs((hit_box[2] / 2) - (sprite_width/2))
        middle_diff_y = abs((hit_box[3] / 2) - (sprite_height / 2))

        self.screen.blit(symbol_sprite, (hit_box[0] + middle_diff_x, hit_box[1] + middle_diff_y))

        pygame.display.update()







    # Helper render functions below



    def prepare_sprite_with_path(self, path):
        sprite = pygame.image.load(path)
        sprite = pygame.transform.smoothscale(sprite, SPRITE_DIMENSIONS)
        return sprite

    def render_player_prompt_with_text(self, text):

        font = pygame.font.Font(FONT_PATH, 36)
        prompt_text_surface = font.render(text + '\'s Turn', True, BLACK)
        width = prompt_text_surface.get_width()
        middle_diff = abs((GameWindow.window_width / 2) - (width / 2))

        pygame.draw.rect(self.screen, WHITE,
                         [middle_diff, 26, width, prompt_text_surface.get_height()])

        self.screen.blit(prompt_text_surface, (middle_diff, 26))
        pygame.display.update()

    def draw_game_board(self):
        pole_one_x = 214.5
        pole_one_y = 106

        pole_two_x = 372.06
        pole_two_y = 106

        pole_three_x = 70
        pole_three_y = 245.28

        pole_four_x = 70
        pole_four_y = 413.28

        pole_vert_height = 457
        pole_vert_width = 9.58

        pole_horiz_height = 9.58
        pole_horiz_width = 457

        pygame.draw.rect(self.screen, BLACK,
                         [pole_one_x, pole_one_y, pole_vert_width, pole_vert_height],
                         border_radius=BUTTON_RADIUS)

        pygame.draw.rect(self.screen, BLACK,
                         [pole_two_x, pole_two_y, pole_vert_width, pole_vert_height],
                         border_radius=BUTTON_RADIUS)

        pygame.draw.rect(self.screen, BLACK,
                         [pole_three_x, pole_three_y, pole_horiz_width, pole_horiz_height],
                         border_radius=BUTTON_RADIUS)

        pygame.draw.rect(self.screen, BLACK,
                         [pole_four_x, pole_four_y, pole_horiz_width, pole_horiz_height],
                         border_radius=BUTTON_RADIUS)
