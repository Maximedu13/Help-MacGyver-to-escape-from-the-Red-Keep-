#! /usr/bin/env python3
# -*- coding: Utf-8 -*
"""It's the main page of the game."""
import sys
import pygame
from constants import (SCREENSIZE_GAME, TILESIZE, MACGYVER_IMG,
                       GARDIAN_IMG, BAG_ITEM,
                       NBCASES, NO_ITEM, BAG_TXT, WHITECOLOR,
                       TRANSPARENT, ITEM_SOUND)
from maze import Maze, Items
from character import Character

# INITIALISATION
# pylint: disable=E1101
pygame.init()


class LoadGame():
    """Class which defines the game."""
    # pylint: disable=too-many-instance-attributes
    # CONSTRUCTOR
    def __init__(self):
        self.window = pygame.display.set_mode((SCREENSIZE_GAME))
        # DRAW THE MAZE
        self.maze = Maze("map")
        self.maze.generate()
        self.maze.display(self.window)

        # MACGYVER LOADING
        self.macgyver_img = pygame.image.load(MACGYVER_IMG).convert_alpha()
        self.macgyver_img = pygame.transform.scale(
            self.macgyver_img, (TILESIZE, TILESIZE))
        self.macgyver = Character(
            "MacGyver", 0, 0, self.macgyver_img, self.maze)

        # GARDIAN LOADING
        self.gardian_img = pygame.image.load(GARDIAN_IMG).convert_alpha()
        self.gardian_img = pygame.transform.scale(
            self.gardian_img, (TILESIZE, TILESIZE))
        self.gardian = Character(
            "Gardienne", NBCASES*TILESIZE - TILESIZE,
            NBCASES*TILESIZE - TILESIZE, self.gardian_img, self.maze)

        # INTERFACE BAG
        self.bag = pygame.image.load(BAG_ITEM).convert_alpha()
        self.bag = pygame.transform.scale(self.bag, (TILESIZE, TILESIZE))
        self.noitem = pygame.image.load(NO_ITEM).convert_alpha()
        self.noitem = pygame.transform.scale(self.noitem, (TILESIZE, TILESIZE))
        self.noitem_1, self.noitem_2, self.noitem_3 = \
            self.noitem, self.noitem, self.noitem
        self.font = pygame.font.Font(None, TILESIZE)
        self.bag_text = self.font.render(BAG_TXT, 1, (0, 0, 0))

        # ITEMS LOADING AND STICKING
        self.aiguille = pygame.image.load(
            "ressource/aiguille.png").convert_alpha()
        self.aiguille = pygame.transform.scale(
            self.aiguille, (TILESIZE, TILESIZE))
        self.aiguille = Items("Aiguille", self.aiguille, self.maze)
        self.ether = pygame.image.load("ressource/ether.png").convert_alpha()
        self.ether = pygame.transform.scale(self.ether, (TILESIZE, TILESIZE))
        self.ether = Items("Ether", self.ether, self.maze)
        self.tube = pygame.image.load("ressource/tube.png").convert_alpha()
        self.tube = pygame.transform.scale(self.tube, (TILESIZE, TILESIZE))
        self.tube = Items("Tube en plastique", self.tube, self.maze)

    def load_items(self):
        """Method to load the items and collect them."""
        # LIST OF THE ITEMS TO COLLECT TO WIN
        list_items = [self.aiguille, self.ether, self.tube]
        # CALLING OF THE METHODS define_position
        list_items[0].define_position_item_1()
        list_items[1].define_position_item_2()
        list_items[2].define_position_item_3()

        # LOOP FOR, FOREACH ITEM IN THE LIST, WE DRAW IT ON THE SCREEN
        for item in list_items:
            # CALLING OF THE METHOD display_items
            item.display_items(self.window)
            # IF MACGVER COLLECTS AN ITEM...
            if (self.macgyver.position_x == list_items
                    [list_items.index(item)].obj_sprite_x) \
                    and (self.macgyver.position_y == list_items
                         [list_items.index(item)].obj_sprite_y):
                # IT MAKES A SOUND
                pygame.mixer.music.load(ITEM_SOUND)
                pygame.mixer.music.play()
                # IT INCREMENTS MACGYVER'S BAG
                self.macgyver.bag += 1
                # IT MOVES THE OBJECT TO THE BAG
                list_items[list_items.index(item)].obj_sprite_x = \
                    TILESIZE*(5 + list_items.index(item))
                list_items[list_items.index(item)].obj_sprite_y = \
                    NBCASES*TILESIZE
                # IT HIDES THE QUESTIONS MARK
                self.noitem.fill(TRANSPARENT)

    def run(self):
        """Method to run LoadGame."""
        # LOOP WHILE
        while True:
            # EVENMENTS
            for event in pygame.event.get():
                ''' IF YOU PRESS THE RED CROSS ON THE LEFT TOP CORNER,
                YOU QUIT THE GAME'''
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # IF YOU PRESS ESC, YOU QUIT THE GAME
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    ''' IF YOU PRESS TOP ARROW,
                    MACGYVER GOES ON THE TOP OF THE SCREEN '''
                    if event.key == pygame.K_UP:
                        self.macgyver.move_to_the_top()
                    ''' IF YOU PRESS BOTTOM ARROW,
                    MACGYVER GOES ON THE BOTTOM OF THE SCREEN'''
                    if event.key == pygame.K_DOWN:
                        self.macgyver.move_to_the_bottom()
                    ''' IF YOU PRESS LEFT ARROW,
                    MACGYVER GOES ON THE LEFT OF THE SCREEN'''
                    if event.key == pygame.K_LEFT:
                        self.macgyver.move_to_the_left()
                    ''' IF YOU PRESS RIGHT ARROW,
                    MACGYVER GOES ON THE RIGHT OF THE SCREEN'''
                    if event.key == pygame.K_RIGHT:
                        self.macgyver.move_to_the_right()

                # LOADING AND STICKING OF THE BACKGROUND
                self.window.fill(WHITECOLOR)
                self.maze.display(self.window)
                self.window.blit(
                    self.macgyver_img,
                    (self.macgyver.position_x, self.macgyver.position_y))
                self.window.blit(
                    self.gardian_img,
                    (self.gardian.position_x, self.gardian.position_y))
                self.window.blit(self.bag, (TILESIZE, NBCASES*TILESIZE))
                self.window.blit(self.noitem_1, (TILESIZE*5, NBCASES*TILESIZE))
                self.window.blit(self.noitem_2, (TILESIZE*6, NBCASES*TILESIZE))
                self.window.blit(self.noitem_3, (TILESIZE*7, NBCASES*TILESIZE))
                self.window.blit(self.bag_text,
                                 (TILESIZE * 2.5,
                                  NBCASES*TILESIZE + TILESIZE/4))

                # CALLING THE METHOD TO LOAD AND STICK THE ITEMS TO COLLECT
                self.load_items()

                # REFRESH
                pygame.display.flip()

                # END THE GAME
                self.macgyver.end_game(self)
