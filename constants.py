# -*- coding: Utf-8 -*
"""It's the game MacGyver constants"""

# COLOR CSS
WHITECOLOR = (255, 255, 255)
BLACKCOLOR = (0, 0, 0)
TRANSPARENT = (0, 0, 0, 0)

# SIZE OF THE MENU
SCREENSIZE_MENU = (700, 680)

# BACKGROUNDS OF THE MENU
FONT_BG = "fonts/Games.ttf"
INSTRUCTIONS_HOME_1 = "Press F1 to start the game"
INSTRUCTIONS_HOME_2 = "Press F2 to quit"
INSTRUCTIONS_HOME_3 = "Press F3 to turn the sound off"
BG_IMAGE = "ressource/pixiz-montage.jpg"
START_SOUND = "ressource/2cellos-game-of-thrones.wav"

#GAME FIXES
GAME_TITLE = "Help MacGyver to escape from the Red Keep !"
NBCASES, TILESIZE = 15, 43
SCREENSIZE_GAME = (NBCASES*TILESIZE, NBCASES*TILESIZE + TILESIZE)

#BAG
BAG_ITEM = "ressource/kisspng-apple-icon-image-format-css-sprites-icon-dollar-gold-coin-bags-5a7efeaf340251.9631686615182721752131.jpg"
BAG_TXT = "BAG ="
NO_ITEM = "ressource/motif-thermocollant-point-d-interrogation.jpg"

#CHARACTERS
MACGYVER_IMG = "ressource/MacGyver.png"
GARDIAN_IMG = "ressource/gardian.png"

#SPRITES IMAGES
WALL_IMG = "ressource/wall.png"
FLOOR_IMG = "ressource/floor.png"
FINISH_LINE_IMG = "ressource/finishline.png"
START_LINE_IMG = "ressource/startline.png"

#BACKGROUNDS OF THE ENDS OF THE GAME
FONT_END = "fonts/Carnage 1974.otf"
FONT_STORY = "fonts/Pada.ttf"
INSTRUCTIONS_END_1 = "YOU WON !"
INSTRUCTIONS_END_2 = "YOU LOST !"
INSTRUCTIONS_END_3 = "PRESS F1 TO PLAY AGAIN"
INSTRUCTIONS_END_4 = "PRESS F2 TO QUIT"
INSTRUCTIONS_END_5 = ["A new day was dawning in King\'s Landing, after a quick breakfast taken in her private apartments",
"Cersei decided to take a little walk over the dungeons beneath the Red Keep", "As she slowly approached your prison cell, and in a last desperate attempt to escape", "you tried to pick the lock of it. Unfortunately for you, it's too late and Cersei sentences you to death."]
INSTRUCTIONS_END_6 = ["Congratulations to you !", "A new day was dawning in King\'s Landing, you escaped from your cell", "and get to the docks of King's Landing.", "In exchange for the needle made of the items you collected,", "you got a cabin on board of and reached the city of Volantis..."]

#FINISH GAME IMAGES AND SOUNDS
VICTORY_IMG = "ressource/MacGyver-Richard-Dean-Anderson.jpg"
DEFEAT_IMG = "ressource/cersei-vin-e1481793839930.jpg"
ITEM_SOUND = "ressource/691.wav"
END_SOUND = "ressource/mortal-kombat-deceptions-fatality-sound-byte.wav"
