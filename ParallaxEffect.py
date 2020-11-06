import pygame

WHITE = (255, 255, 255)


class ParallaxEffect:

    def __init__(self, screen):
        self.screen = screen
        self.parallax_graphic = pygame.image.load('geometric_line.png').convert()
        self.parallax_graphic = pygame.transform.smoothscale(self.parallax_graphic, (800, 750))

    def render_parallax_background_graphic(self):
        x, y = pygame.mouse.get_pos()
        self.screen.fill(WHITE)
        self.parallax_graphic.set_alpha(50)
        self.screen.blit(self.parallax_graphic, (x * -.2, y * -.2))