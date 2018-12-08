#! /usr/bin/env python3
# -*- coding: Utf-8 -*
"""It is the defeat game page."""
import sys
import pygame
from constants import (DEFEAT_IMG, FONT_END, INSTRUCTIONS_END_2,
                       INSTRUCTIONS_END_3, INSTRUCTIONS_END_4,
                       INSTRUCTIONS_END_5, GAME_TITLE,
                       SCREENSIZE_MENU, FONT_BG, FONT_STORY, WHITECOLOR)


class DefeatGame():
    """Class which defines the defeat."""
    # CONSTRUCTOR
    def __init__(self):
        # GAME FIXES
        self.window = pygame.display.set_mode((SCREENSIZE_MENU))
        pygame.display.set_caption(GAME_TITLE)
        # DEFEAT IMAGE AND TEXT INSTRUCTIONS
        self.defeat = pygame.image.load(DEFEAT_IMG).convert()
        self.defeat = pygame.transform.scale(self.defeat, (500, 330))
        self.font = pygame.font.Font(FONT_END, 50)
        self.text_1 = self.font.render(INSTRUCTIONS_END_2, 1, (0, 0, 0))
        self.font_2 = pygame.font.Font(FONT_BG, 25)
        self.font_history = pygame.font.Font(FONT_STORY, 23)
        self.text_2 = self.font_2.render(INSTRUCTIONS_END_3, 1, (0, 0, 0))
        self.text_3 = self.font_2.render(INSTRUCTIONS_END_4, 1, (0, 0, 0))
        self.window.fill(WHITECOLOR)
        self.window.blit(self.defeat, (100, 25))
        self.window.blit(self.text_1, (250, 360))
        self.window.blit(self.text_2, (10, 620))
        self.window.blit(self.text_3, (460, 650))

        # LOOP TO DISPLAY THE INSTRUCTIONS STORY
        i = 0
        height = 400
        for phrase in INSTRUCTIONS_END_5:
            history = self.font_history.render(
                INSTRUCTIONS_END_5[INSTRUCTIONS_END_5.index(phrase)], 1,
                (0, 0, 0))
            i += 40
            self.window.blit(history, (10, height + i))
            pygame.display.flip()

    def run(self):
        """Method to launch defeat_game."""
        while True:
            # INITIALISATION
            pygame.init()
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
                        return 1
                    if event.key == pygame.K_F3:
                        pygame.mixer.music.stop()
        return 0
