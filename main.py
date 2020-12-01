from GameWindow import *

if __name__ == '__main__':
    icn = pygame.image.load('icn2.png')
    pygame.display.set_icon(icn)

    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.1)

    game = GameWindowFoundation()
    game.start_game()