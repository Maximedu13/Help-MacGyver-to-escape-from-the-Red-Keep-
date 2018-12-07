# -*- coding: Utf-8 -*
"""It's the homepage and the game launch file."""
import sys
import pygame
from constants import (SCREENSIZE_MENU, GAME_TITLE, GARDIAN_IMG,
                       INSTRUCTIONS_HOME_1, INSTRUCTIONS_HOME_2,
                       INSTRUCTIONS_HOME_3, WHITECOLOR,
                       BG_IMAGE, FONT_BG, START_SOUND)
from main import LoadGame

# INITIALISATION
pygame.init()


class Menu():
    """Class which defines the menu game."""
    # CONSTRUCTOR
    def __init__(self):
        self.window = pygame.display.set_mode((SCREENSIZE_MENU))
        pygame.display.set_caption(GAME_TITLE)
        # BACKGROUNDS LOADING AND STICKING
        self.home = pygame.image.load(BG_IMAGE).convert()
        pygame.mixer.music.load(START_SOUND)
        pygame.mixer.music.play()
        self.gardian = pygame.image.load(GARDIAN_IMG).convert_alpha()
        pygame.display.set_icon(self.gardian)
        self.font = pygame.font.Font(FONT_BG, 20)
        self.text_1 = self.font.render(INSTRUCTIONS_HOME_1, 1, (0, 0, 0))
        self.text_2 = self.font.render(INSTRUCTIONS_HOME_2, 1, (0, 0, 0))
        self.text_3 = self.font.render(INSTRUCTIONS_HOME_3, 1, (0, 0, 0))
        self.window.fill(WHITECOLOR)
        self.window.blit(self.home, (0, 0))
        self.window.blit(self.text_1, (100, 550))
        self.window.blit(self.text_2, (100, 600))
        self.window.blit(self.text_3, (100, 650))
        pygame.display.flip()

    def render(self):
        """Method for the render."""
        while True:
            # EVENMENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or \
                                    event.key == pygame.K_F2:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_F1:
                        main = LoadGame()
                        main.run()
                    if event.key == pygame.K_F3:
                        pygame.mixer.music.stop()
        pygame.quit()


if __name__ == "__main__":
    # EXECUTE ONLY IF RUN AS A SCRIPT
    MENU = Menu()
    MENU.render()
