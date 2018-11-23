# -*- coding: Utf-8 -*
"""It is the defeat game page."""
import pygame
import sys
from constants import *
from pygame.locals import *

class defeat_game():
    """Class which defines the defeat."""
    #CONSTRUCTOR
    def __init__(self):
        #GAME FIXES
        self.WINDOW = pygame.display.set_mode((SCREENSIZE_MENU), RESIZABLE)
        pygame.display.set_caption(GAME_TITLE)
        #DEFEAT IMAGE AND TEXT INSTRUCTIONS
        self.DEFEAT = pygame.image.load(DEFEAT_IMG).convert()
        self.DEFEAT = pygame.transform.scale(self.DEFEAT, (500, 330))
        self.FONT = pygame.font.Font(FONT_END, 50)
        self.TEXT_1 = self.FONT.render(INSTRUCTIONS_END_2, 1, (0, 0, 0))
        self.FONT_2 = pygame.font.Font(FONT_BG, 25)
        self.FONT_HISTORY = pygame.font.Font(FONT_STORY, 23)
        self.TEXT_2 = self.FONT_2.render(INSTRUCTIONS_END_3, 1, (0, 0, 0))
        self.TEXT_3 = self.FONT_2.render(INSTRUCTIONS_END_4, 1, (0, 0, 0))
        self.WINDOW.fill(WHITECOLOR)
        self.WINDOW.blit(self.DEFEAT, (100, 25))
        self.WINDOW.blit(self.TEXT_1, (250, 360))
        self.WINDOW.blit(self.TEXT_2, (10, 620))
        self.WINDOW.blit(self.TEXT_3, (460, 650))

        #LOOP TO DISPLAY THE INSTRUCTIONS STORY
        i = 0
        height = 400
        for phrase in INSTRUCTIONS_END_5:
            HISTORY = self.FONT_HISTORY.render(INSTRUCTIONS_END_5[INSTRUCTIONS_END_5.index(phrase)], 1, (0, 0, 0))
            i = i + 40
            self.WINDOW.blit(HISTORY, (10, height + i))
            pygame.display.flip()

    def run(self):
        """Method to launch defeat_game."""
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
