# -*- coding: Utf-8 -*
"""It's the page for the actions of the character."""
import pygame
from pygame.locals import *
from constants import *
from maze import *
from main import *
from victory import victory_game
from defeat import defeat_game

class Character:
    """Class which defines a character."""
    #CONSTRUCTOR
    def __init__(self, name, position_x, position_y, image, maze):
        self.name = name
        self.position_x = position_x
        self.position_y = position_y
        self.image = image
        self.bag = 0
        self.case_x = 0
        self.case_y = 0
        self.maze = maze
        self.win = False

    def moveToTheTop(self):
        """Method for the movement to the top."""
        #We verifiy if the destination point is not a wall
        if self.case_y > 0:
            if self.maze.structure[self.case_y - 1][self.case_x] != '■':
                self.case_y -= 1
                self.position_y = self.case_y * TILESIZE

    def moveToTheBottom(self):
        """Method for the movement to the bottom."""
        #We verifiy if the destination point is not a wall
        if self.case_y < (NBCASES - 1):
            if self.maze.structure[self.case_y + 1][self.case_x] != '■':
                self.case_y += 1
                self.position_y = self.case_y * TILESIZE

    def moveToTheRight(self):
        """Method for the movement to the right."""
        #We verifiy if the destination point is not a wall
        if self.case_x < (NBCASES - 1):
            if self.maze.structure[self.case_y][self.case_x + 1] != '■':
                self.case_x += 1
                self.position_x = self.case_x * TILESIZE

    def moveToTheLeft(self):
        """Method for the movement to the left."""
        #We verifiy if the destination point is not a wall
        if self.case_x > 0:
            if self.maze.structure[self.case_y][self.case_x - 1] != '■':
                self.case_x -= 1
                self.position_x = self.case_x * TILESIZE


    def end_game(self, main):
        """Method to end the game."""
        #VICTORY
        if self.maze.structure[self.case_y][self.case_x] == '◘' and self.bag == 3:
            self.win == True
            print('Victory')
            pygame.mixer.music.load(END_SOUND)
            pygame.mixer.music.play()
            victory = victory_game()
            db = victory.run()
            main.__init__()
            return db

        #DEFEAT
        if self.maze.structure[self.case_y][self.case_x] == '◘' and self.bag != 3:
            self.win == False
            print('Defeat')
            pygame.mixer.music.load(END_SOUND)
            pygame.mixer.music.play()
            defeat = defeat_game()
            db = defeat.run()
            main.__init__()
            return db
        return 0
