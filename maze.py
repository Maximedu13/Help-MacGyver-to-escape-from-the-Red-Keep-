# -*- coding: Utf-8 -*
"""It is the maze and items (design) game page."""
import random
import pygame
from constants import TILESIZE, WALL_IMG, FLOOR_IMG, FINISH_LINE_IMG, \
START_LINE_IMG, NBCASES

class Maze:
    """Class to create the maze"""
	#CONSTRUCTOR
    def __init__(self, file):
        self.fichier = file
        self.structure = 0

    def generate(self):
        """Method to read the map file and create it"""
        with open(self.fichier, "r") as fichier:
            structure_maze = []
            for ligne in fichier:
                ligne_maze = []
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_maze.append(sprite)
                structure_maze.append(ligne_maze)
            self.structure = structure_maze

    def display(self, window):
        """Method to draw the maze"""
		#SPRITES LOADING
        wall = pygame.image.load(WALL_IMG).convert_alpha()
        wall = pygame.transform.scale(wall, (TILESIZE, TILESIZE))

        floor = pygame.image.load(FLOOR_IMG).convert_alpha()
        floor = pygame.transform.scale(floor, (TILESIZE, TILESIZE))

        finishline = pygame.image.load(FINISH_LINE_IMG).convert_alpha()
        finishline = pygame.transform.scale(finishline, (TILESIZE, TILESIZE))

        startline = pygame.image.load(START_LINE_IMG).convert_alpha()
        startline = pygame.transform.scale(startline, (TILESIZE, TILESIZE))

		#PROCESS READING AND DRAWING FILE MAP
        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * TILESIZE
                y = num_ligne * TILESIZE
				#IF THE SPRITE IS A ■, A WALL SPRITE WILL BE CREATED
                if sprite == '■':
                    window.blit(wall, (x, y))
				#IF THE SPRITE IS A –, A WAY SPRITE WILL BE CREATED
                elif sprite == '–':
                    window.blit(floor, (x, y))
				#IF THE SPRITE IS A ○, A STARTLINE SPRITE WILL BE CREATED
                elif sprite == '○':
                    window.blit(startline, (x, y))
				#IF THE SPRITE IS A ◘, A FINISHLINE SPRITE WILL BE CREATED
                elif sprite == '◘':
                    window.blit(finishline, (x, y))
                num_case += 1
            num_ligne += 1

class Items:
    """Class to create the items."""
    #CONSTRUCTOR
    def __init__(self, name, image, maze):
        self.name = name
        self.position_x = 0
        self.position_y = 0
        self.image = image
        self.obj_sprite_x = 0
        self.obj_sprite_y = 0
        self.maze = maze

    def define_position(self):
        """Method to get a randomly position for the items."""
        list_random = []
        while self.maze.structure[self.position_y][self.position_x] != '–':
            self.position_x = random.randint(0, NBCASES - 1)
            self.position_y = random.randint(0, NBCASES - 1)
            self.obj_sprite_x = self.position_x * TILESIZE
            self.obj_sprite_y = self.position_y * TILESIZE
            a = (self.position_x, self.position_y)
            list_random.append(a)
            print(a)
            if a[0] == a[1]:
                return self.define_position()

    def display_items(self, window):
        """Method to display the items on the maze."""
        window.blit(self.image, (self.obj_sprite_x, self.obj_sprite_y))
