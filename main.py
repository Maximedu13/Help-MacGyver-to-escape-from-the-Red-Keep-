# -*- coding: Utf-8 -*
"""It's the main page of the game."""
import sys
import pygame
from pygame.locals import *
from constants import *
from character import *
from maze import *

#INITIALISATION
pygame.init()

class loadGame():
    """Class which defines the game."""
    #CONSTRUCTOR
    def __init__(self):
        self.WINDOW = pygame.display.set_mode((SCREENSIZE_GAME), RESIZABLE)
        #DRAW THE MAZE
        self.maze = Maze("map")
        self.maze.generate()
        self.maze.display(self.WINDOW)

        #MACGYVER LOADING
        self.MACGYVER = pygame.image.load(MACGYVER_IMG).convert_alpha()
        self.MACGYVER = pygame.transform.scale(self.MACGYVER, (TILESIZE, TILESIZE))
        self.macgyver = Character("MacGyver", 0, 0, self.MACGYVER, self.maze)

        #GARDIAN LOADING
        self.GARDIAN = pygame.image.load(GARDIAN_IMG).convert_alpha()
        self.GARDIAN = pygame.transform.scale(self.GARDIAN, (TILESIZE, TILESIZE))
        self.gardian = Character("Gardienne", NBCASES*TILESIZE - TILESIZE, NBCASES*TILESIZE - TILESIZE, self.GARDIAN, self.maze)

        #INTERFACE BAG
        self.BAG = pygame.image.load(BAG_ITEM).convert_alpha()
        self.BAG = pygame.transform.scale(self.BAG, (TILESIZE, TILESIZE))
        self.NOITEM = pygame.image.load(NO_ITEM).convert_alpha()
        self.NOITEM = pygame.transform.scale(self.NOITEM, (TILESIZE, TILESIZE))
        self.NOITEM_1, self.NOITEM_2, self.NOITEM_3 = self.NOITEM, self.NOITEM, self.NOITEM
        self.FONT = pygame.font.Font(None, TILESIZE)
        self.BAG_TEXT = self.FONT.render(BAG_TXT, 1, (0, 0, 0))

        #ITEMS LOADING AND STICKING
        self.AIGUILLE = pygame.image.load("ressource/aiguille.png").convert_alpha()
        self.AIGUILLE = pygame.transform.scale(self.AIGUILLE, (TILESIZE, TILESIZE))
        self.AIGUILLE = Items("Aiguille", self.AIGUILLE, self.maze)
        self.ETHER = pygame.image.load("ressource/ether.png").convert_alpha()
        self.ETHER = pygame.transform.scale(self.ETHER, (TILESIZE, TILESIZE))
        self.ETHER = Items("Ether", self.ETHER, self.maze)
        self.TUBE = pygame.image.load("ressource/tube.png").convert_alpha()
        self.TUBE = pygame.transform.scale(self.TUBE, (TILESIZE, TILESIZE))
        self.TUBE = Items("Tube en plastique", self.TUBE, self.maze)

    def loadItems(self):
        #LIST OF THE ITEMS TO COLLECT TO WIN
        list_items = [self.AIGUILLE, self.ETHER, self.TUBE]
        #LOOP FOR, FOREACH ITEM IN THE LIST, WE DRAW IT ON THE SCREEN
        for item in list_items:
            #CALLING OF THE METHOD define_position
            item.define_position()
            #CALLING OF THE METHOD display_items
            item.display_items(self.WINDOW)
            #IF MACGVER COLLECTS AN ITEM...
            if (self.macgyver.position_x == list_items[list_items.index(item)].obj_sprite_x) and (self.macgyver.position_y == list_items[list_items.index(item)].obj_sprite_y):
                #IT MAKES A SOUND
                pygame.mixer.music.load(ITEM_SOUND)
                pygame.mixer.music.play()
                #IT INCREMENTS MACGYVER'S BAG
                self.macgyver.bag += 1
                #IT MOVES THE OBJECT TO THE BAG
                list_items[list_items.index(item)].obj_sprite_x = TILESIZE*(5 + list_items.index(item))
                list_items[list_items.index(item)].obj_sprite_y = NBCASES*TILESIZE
                #IT HIDES THE QUESTION MARKS
                self.NOITEM.fill(TRANSPARENT)

    def run(self):
        #LOOP WHILE
        while True:
            #EVENMENTS
            for event in pygame.event.get():
                #IF YOU PRESS THE RED CROSS ON THE LEFT TOP CORNER, YOU QUIT THE GAME
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    #IF YOU PRESS ESC, YOU QUIT THE GAME
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    #IF YOU PRESS TOP ARROW, MACGYVER GOES ON THE TOP OF THE SCREEN
                    if event.key == pygame.K_UP:
                        self.macgyver.moveToTheTop()
                    #IF YOU PRESS BOTTOM ARROW, MACGYVER GOES ON THE BOTTOM OF THE SCREEN
                    if event.key == pygame.K_DOWN:
                        self.macgyver.moveToTheBottom()
                    #IF YOU PRESS LEFT ARROW, MACGYVER GOES ON THE LEFT OF THE SCREEN
                    if event.key == pygame.K_LEFT:
                        self.macgyver.moveToTheLeft()
                    #IF YOU PRESS RIGHT ARROW, MACGYVER GOES ON THE RIGHT OF THE SCREEN
                    if event.key == pygame.K_RIGHT:
                        self.macgyver.moveToTheRight()

                #LOADING AND STICKING OF THE BACKGROUND
                self.WINDOW.fill(WHITECOLOR)
                self.maze.display(self.WINDOW)
                self.WINDOW.blit(self.MACGYVER, (self.macgyver.position_x, \
                self.macgyver.position_y))
                self.WINDOW.blit(self.GARDIAN, (self.gardian.position_x, self.gardian.position_y))
                self.WINDOW.blit(self.BAG, (TILESIZE, NBCASES*TILESIZE))
                self.WINDOW.blit(self.NOITEM_1, (TILESIZE*5, NBCASES*TILESIZE))
                self.WINDOW.blit(self.NOITEM_2, (TILESIZE*6, NBCASES*TILESIZE))
                self.WINDOW.blit(self.NOITEM_3, (TILESIZE*7, NBCASES*TILESIZE))
                self.WINDOW.blit(self.BAG_TEXT, (TILESIZE * 2.5, NBCASES*TILESIZE + TILESIZE/4))

                #CALLING THE METHOD TO LOAD AND STICK THE ITEMS TO COLLECT
                self.loadItems()

                #REFRESH
                pygame.display.flip()

                #END THE GAME
                self.macgyver.end_game(self)
