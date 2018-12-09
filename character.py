#! /usr/bin/env python3
# -*- coding: Utf-8 -*
"""It's the page for the actions of the character."""
import pygame
from constants import TILESIZE, END_SOUND, NBCASES
from victory import VictoryGame
from defeat import DefeatGame


class Character:
    """Class which defines a character."""
    # CONSTRUCTOR
    def __init__(self, name, position_x, position_y, image, maze):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.image = image
        self.bag = 0
        self.case_x = 0
        self.case_y = 0
        self.maze = maze

    def move_to_the_top(self):
        """Method for the movement to the top."""
        # We verifiy if the destination point is not a wall
        if self.case_y > 0:
            # We verifiy if the destination point is not a wall
            if self.maze.structure[self.case_y - 1][self.case_x] != '■':
                self.case_y -= 1
                self.position_y = self.case_y * TILESIZE

    def move_to_the_bottom(self):
        """Method for the movement to the bottom."""
        if self.case_y < (NBCASES - 1):
            # We verifiy if the destination point is not a wall
            if self.maze.structure[self.case_y + 1][self.case_x] != '■':
                self.case_y += 1
                self.position_y = self.case_y * TILESIZE

    def move_to_the_right(self):
        """Method for the movement to the right."""
        if self.case_x < (NBCASES - 1):
            # We verifiy if the destination point is not a wall
            if self.maze.structure[self.case_y][self.case_x + 1] != '■':
                self.case_x += 1
                self.position_x = self.case_x * TILESIZE

    def move_to_the_left(self):
        """Method for the movement to the left."""
        if self.case_x > 0:
            # We verifiy if the destination point is not a wall
            if self.maze.structure[self.case_y][self.case_x - 1] != '■':
                self.case_x -= 1
                self.position_x = self.case_x * TILESIZE

    def end_game(self, main):
        """Method to end the game."""
        # VICTORY
        if self.maze.structure[self.case_y][self.case_x] == '◘' \
                and self.bag == 3:
            print('Victory')
            pygame.mixer.music.load(END_SOUND)
            pygame.mixer.music.play()
            victory = VictoryGame()
            d_b = victory.run()
            main.__init__()
            return d_b

        # DEFEAT
        if self.maze.structure[self.case_y][self.case_x] == '◘' \
                and self.bag != 3:
            print('Defeat')
            pygame.mixer.music.load(END_SOUND)
            pygame.mixer.music.play()
            defeat = DefeatGame()
            d_b = defeat.run()
            main.__init__()
            return d_b
        return 0
