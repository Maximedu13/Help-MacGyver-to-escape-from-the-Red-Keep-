#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""It is the maze and items (design) game page."""
import random
import pygame
from constants import (TILESIZE, WALL_IMG, FLOOR_IMG, FINISH_LINE_IMG,
                       START_LINE_IMG, NBCASES)


class Maze:
    """Class to create the maze"""
    # CONSTRUCTOR
    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):
        """Method to read the map file and create it"""
        # OPEN THE FILE
        with open(self.file, "r") as file:
            # CREATE EMPTY LIST
            maze_structure = []
            # SCAN FILE LINES
            for line in file:
                line_maze = []
                # SCAN FILE LETTERS/SPRITES
                for sprite in line:
                    # IGNORE THE ENDS LINES
                    if sprite != '\n':
                        # ADD THE SPRITE TO THE LIST OF THE LINE
                        line_maze.append(sprite)
                # ADD THE LINE TO THE LEVEL LIST
                maze_structure.append(line_maze)
            self.structure = maze_structure

    def display(self, window):
        """Method to draw the maze"""
        # SPRITES LOADING
        wall = pygame.image.load(WALL_IMG).convert_alpha()
        wall = pygame.transform.scale(wall, (TILESIZE, TILESIZE))

        floor = pygame.image.load(FLOOR_IMG).convert_alpha()
        floor = pygame.transform.scale(floor, (TILESIZE, TILESIZE))

        finishline = pygame.image.load(FINISH_LINE_IMG).convert_alpha()
        finishline = pygame.transform.scale(finishline, (TILESIZE, TILESIZE))

        startline = pygame.image.load(START_LINE_IMG).convert_alpha()
        startline = pygame.transform.scale(startline, (TILESIZE, TILESIZE))

        # PROCESS READING LEVEL FILE
        num_line = 0
        for line in self.structure:
            # PROCESS READING LINES LISTS
            num_case = 0
            for sprite in line:
                # REAL POSITIONS IN PIXELS
                x_x = num_case * TILESIZE
                y_y = num_line * TILESIZE
                # IF THE SPRITE IS A ■, A WALL SPRITE WILL BE CREATED
                if sprite == '■':
                    window.blit(wall, (x_x, y_y))
                # IF THE SPRITE IS A –, A WAY SPRITE WILL BE CREATED
                elif sprite == '–':
                    window.blit(floor, (x_x, y_y))
                # IF THE SPRITE IS A ○, A STARTLINE SPRITE WILL BE CREATED
                elif sprite == '○':
                    window.blit(startline, (x_x, y_y))
                # IF THE SPRITE IS A ◘, A FINISHLINE SPRITE WILL BE CREATED
                elif sprite == '◘':
                    window.blit(finishline, (x_x, y_y))
                num_case += 1
            num_line += 1


class Items:
    """Class to create the items."""
    # CONSTRUCTOR
    def __init__(self, name, image, maze):
        self.name = name
        self.image = image
        self.position_x = 0
        self.position_y = 0
        self.obj_sprite_x = 0
        self.obj_sprite_y = 0
        self.maze = maze

    def define_position_item_1(self):
        """Method to get a randomly position for the item number one."""
        while self.maze.structure[self.position_y][self.position_x] != '–':
            self.position_x = random.randint(0, 4)
            self.position_y = random.randint(0, NBCASES - 1)
            self.obj_sprite_x = self.position_x * TILESIZE
            self.obj_sprite_y = self.position_y * TILESIZE

    def define_position_item_2(self):
        """Method to get a randomly position for the item number two."""
        while self.maze.structure[self.position_y][self.position_x] != '–':
            self.position_x = random.randint(5, 9)
            self.position_y = random.randint(0, NBCASES - 1)
            self.obj_sprite_x = self.position_x * TILESIZE
            self.obj_sprite_y = self.position_y * TILESIZE

    def define_position_item_3(self):
        """Method to get a randomly position for the item number three."""
        while self.maze.structure[self.position_y][self.position_x] != '–':
            self.position_x = random.randint(9, NBCASES - 1)
            self.position_y = random.randint(0, NBCASES - 1)
            self.obj_sprite_x = self.position_x * TILESIZE
            self.obj_sprite_y = self.position_y * TILESIZE

    def display_items(self, window):
        """Method to display the items on the maze."""
        window.blit(self.image, (self.obj_sprite_x, self.obj_sprite_y))
