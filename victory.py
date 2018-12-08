#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""It is the victory game page."""
import sys
import pygame
from constants import (VICTORY_IMG, FONT_END, INSTRUCTIONS_END_1,
                       INSTRUCTIONS_END_3, INSTRUCTIONS_END_4,
                       INSTRUCTIONS_END_6, GAME_TITLE,
                       SCREENSIZE_MENU, FONT_BG, FONT_STORY, WHITECOLOR)


class VictoryGame():
    """Class which defines the victory."""
    # CONSTRUCTOR
    def __init__(self):
        # GAME FIXES
        self.window = pygame.display.set_mode((SCREENSIZE_MENU))
        pygame.display.set_caption(GAME_TITLE)
        # VICTORY IMAGE AND TEXT STORY
        self.victory = pygame.image.load(VICTORY_IMG).convert()
        self.victory = pygame.transform.scale(self.victory, (500, 330))
        self.font = pygame.font.Font(FONT_END, 50)
        self.text_1 = self.font.render(INSTRUCTIONS_END_1, 1, (0, 0, 0))
        self.font_2 = pygame.font.Font(FONT_BG, 20)
        self.text_2 = self.font_2.render(INSTRUCTIONS_END_3, 1, (0, 0, 0))
        self.text_3 = self.font_2.render(INSTRUCTIONS_END_4, 1, (0, 0, 0))
        self.font_history = pygame.font.Font(FONT_STORY, 25)
        self.window.fill(WHITECOLOR)
        self.window.blit(self.victory, (100, 0))
        self.window.blit(self.text_1, (250, 340))
        self.window.blit(self.text_2, (30, 650))
        self.window.blit(self.text_3, (460, 650))

        # LOOP TO DISPLAY THE INSTRUCTIONS STORY
        i = 0
        height = 370
        for phrase in INSTRUCTIONS_END_6:
            history = self.font_history.render(
                INSTRUCTIONS_END_6[INSTRUCTIONS_END_6.index(phrase)],
                1, (0, 0, 0))
            i = i + 40
            self.window.blit(history, (50, height + i))
            pygame.display.flip()

    def run(self):
        """Method to launch victory_game."""
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
