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
        self.screen.fill((255, 255, 255))
        self.parallax_graphic.set_alpha(50)
        self.screen.blit(self.parallax_graphic, (x * -.2, y * -.2))

    def render_game_title(self):

        font_size = 64

        font = pygame.font.Font('./Open_Sans/OpenSans-Light.ttf', font_size)
        text_surface = font.render('TIC-TAC-TOE', True, (0, 0, 0))

        width = text_surface.get_width()
        middle_diff = abs((GameWindow.window_width / 2) - (width / 2))

        sub_font_size = 20

        sub_font = pygame.font.Font('./Open_Sans/OpenSans-Light.ttf', sub_font_size)
        sub_text_surface = sub_font.render('Gabriel Morales, Chelsea Flores, Waewarin Chindarassami', True, (0, 0, 0))

        sub_width = sub_text_surface.get_width()
        sub_middle_diff = abs((GameWindow.window_width / 2) - (sub_width / 2))

        self.screen.blit(sub_text_surface, (sub_middle_diff, 100))
        self.screen.blit(text_surface, (middle_diff, 0))

    def render_train_agent_button(self):

        font_size = 30
        y_offset = 290

        font = pygame.font.Font('./Open_Sans/OpenSans-Light.ttf', font_size)
        text_surface = font.render('Train Agent', True, (255, 255, 255))


        width = text_surface.get_width()
        height = text_surface.get_height()
        middle_diff = abs((GameWindow.window_width / 2) - (width / 2))

        button_center_x = abs((GameWindow.window_width / 2) - (width + 50)/2)
        button_center_y = abs((y_offset + (height/2)) - ((height+(height/4))/2))

        pygame.draw.rect(self.screen, (0, 0, 0), [button_center_x, button_center_y+4, width+50, height+(height/4)], border_radius=4)

        self.screen.blit(text_surface, (middle_diff, y_offset))

    def render_player_vs_agent_button(self):

        font_size = 30
        y_offset = 380

        font = pygame.font.Font('./Open_Sans/OpenSans-Light.ttf', font_size)
        text_surface = font.render('Player vs. Agent', True, (255, 255, 255))

        width = text_surface.get_width()
        height = text_surface.get_height()
        middle_diff = abs((GameWindow.window_width / 2) - (width / 2))

        button_center_x = abs((GameWindow.window_width / 2) - (width + 50) / 2)
        button_center_y = abs((y_offset + (height / 2)) - ((height + (height / 4)) / 2))

        pygame.draw.rect(self.screen, (0, 0, 0), [button_center_x, button_center_y+3, width + 50, height + (height / 4)],
                         border_radius=4)

        self.screen.blit(text_surface, (middle_diff, y_offset))

    def render_player_vs_player_button(self):
        font_size = 30
        y_offset = 470

        font = pygame.font.Font('./Open_Sans/OpenSans-Light.ttf', font_size)
        text_surface = font.render('Player vs. Player', True, (255, 255, 255))


        width = text_surface.get_width()
        height = text_surface.get_height()
        middle_diff = abs((GameWindow.window_width / 2) - (width / 2))

        button_center_x = abs((GameWindow.window_width / 2) - (width + 50) / 2)
        button_center_y = abs((y_offset + (height / 2)) - ((height + (height / 4)) / 2))

        pygame.draw.rect(self.screen, (0, 0, 0), [button_center_x, button_center_y+3, width + 50, height + (height / 4)],
                         border_radius=4)

        self.screen.blit(text_surface, (middle_diff, y_offset))

    def start_game(self):

        # This is the main loop for the entire game application.
        while True:
            self.render_parallax_background_graphic()
            self.render_game_title()
            self.render_player_vs_agent_button()
            self.render_train_agent_button()
            self.render_player_vs_player_button()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
