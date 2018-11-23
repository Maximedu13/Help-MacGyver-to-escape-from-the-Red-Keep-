# -*- coding: Utf-8 -*
"""It's the homepage and the game launch file."""
import pygame
import sys
from constants import *
from pygame.locals import *
from main import loadGame

class Menu():
    """Class which defines the menu game."""
    #CONSTRUCTOR
    def __init__(self):
        #INITIALISATION
        pygame.init()
        self.WINDOW = pygame.display.set_mode((SCREENSIZE_MENU), RESIZABLE)
        pygame.display.set_caption(GAME_TITLE)
        #BACKGROUNDS LOADING AND STICKING
        self.HOME = pygame.image.load(BG_IMAGE).convert()
        pygame.mixer.music.load(START_SOUND)
        pygame.mixer.music.play()
        self.GARDIAN = pygame.image.load(GARDIAN_IMG).convert_alpha()
        pygame.display.set_icon(self.GARDIAN)
        self.FONT = pygame.font.Font(FONT_BG, 20)
        self.TEXT_1 = self.FONT.render(INSTRUCTIONS_HOME_1, 1, (0, 0, 0))
        self.TEXT_2 = self.FONT.render(INSTRUCTIONS_HOME_2, 1, (0, 0, 0))
        self.TEXT_3 = self.FONT.render(INSTRUCTIONS_HOME_3, 1, (0, 0, 0))
        self.WINDOW.fill(WHITECOLOR)
        self.WINDOW.blit(self.HOME, (0, 0))
        self.WINDOW.blit(self.TEXT_1, (100, 550))
        self.WINDOW.blit(self.TEXT_2, (100, 600))
        self.WINDOW.blit(self.TEXT_3, (100, 650))
        pygame.display.flip()

    def render(self):
        """Method for the render."""
        while True:
            #INITIALISATION
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_F2:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_F1:
                        main = loadGame()
                        main.run()
                    if event.key == pygame.K_F3:
                        pygame.mixer.music.stop()
        pygame.quit()

if __name__ == "__main__":
    #EXECUTE ONLY IF RUN AS A SCRIPT
    menu = Menu()
    menu.render()
