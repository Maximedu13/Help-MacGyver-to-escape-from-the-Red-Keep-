# -*- coding: Utf-8 -*
"""It is the victory game page."""
import pygame
import sys
from constants import *
from pygame.locals import *

class victory_game():
    """Class which defines the victory."""
    #CONSTRUCTOR
    def __init__(self):
        #GAME FIXES
        self.WINDOW = pygame.display.set_mode((SCREENSIZE_MENU), RESIZABLE)
        pygame.display.set_caption(GAME_TITLE)
        #VICTORY IMAGE AND TEXT STORY
        self.VICTORY = pygame.image.load(VICTORY_IMG).convert()
        self.VICTORY = pygame.transform.scale(self.VICTORY, (500, 330))
        self.FONT = pygame.font.Font(FONT_END, 50)
        self.TEXT_1 = self.FONT.render(INSTRUCTIONS_END_1, 1, (0, 0, 0))
        self.FONT_2 = pygame.font.Font(FONT_BG, 20)
        self.TEXT_2 = self.FONT_2.render(INSTRUCTIONS_END_3, 1, (0, 0, 0))
        self.TEXT_3 = self.FONT_2.render(INSTRUCTIONS_END_4, 1, (0, 0, 0))
        self.FONT_HISTORY = pygame.font.Font(FONT_STORY, 25)
        self.WINDOW.fill(WHITECOLOR)
        self.WINDOW.blit(self.VICTORY, (100, 0))
        self.WINDOW.blit(self.TEXT_1, (250, 340))
        self.WINDOW.blit(self.TEXT_2, (30, 650))
        self.WINDOW.blit(self.TEXT_3, (460, 650))

        #LOOP TO DISPLAY THE INSTRUCTIONS STORY
        i = 0
        height = 370
        for phrase in INSTRUCTIONS_END_6:
            HISTORY = self.FONT_HISTORY.render(INSTRUCTIONS_END_6[INSTRUCTIONS_END_6.index(phrase)], 1, (0, 0, 0))
            i = i + 40
            self.WINDOW.blit(HISTORY, (50, height + i))
            pygame.display.flip()

    def run(self):
        """Method to launch victory_game."""
        while True:
            #INITIALISATION
            pygame.init()
            #EVENMENTS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_F2:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_F1:
                        return 1
                    if event.key == pygame.K_F3:
                        pygame.mixer.music.stop()
        return 0
