from modules.config_general import *

GAME_VIEW_GRID_BEGIN_X = 1
GAME_VIEW_GRID_BEGIN_Y = 1
GAME_VIEW_GRID_WIDTH = GRID_WIDTH * 2 + 2 + 1  # grille*2 + bordures + l'espace pour pouvoir tout print
# (*2 car les tétrominos font 2 de large)
GAME_VIEW_GRID_HEIGHT = GRID_HEIGHT + 2  # grille + bordures

GAME_VIEW_NEXT_BEGIN_X = GAME_VIEW_GRID_BEGIN_X + GAME_VIEW_GRID_WIDTH + 2
GAME_VIEW_NEXT_BEGIN_Y = 1
GAME_VIEW_NEXT_WIDTH = 4 * 2 + 2  # grille*2 + bordures (*2 car les tétrominos font 2 de large)
GAME_VIEW_NEXT_HEIGHT = 2 + 4 + 1  # grille + bordures + l'espace pour pouvoir tout print

GAME_VIEW_STORED_BEGIN_X = GAME_VIEW_NEXT_BEGIN_X + GAME_VIEW_NEXT_WIDTH + 2
GAME_VIEW_STORED_BEGIN_Y = 1
GAME_VIEW_STORED_WIDTH = 4 * 2 + 2  # grille*2 + bordures (*2 car les tétrominos font 2 de large)
GAME_VIEW_STORED_HEIGHT = 2 + 4 + 1  # grille + bordures + l'espace pour pouvoir tout print

GAME_VIEW_STATISTICS_BEGIN_X = GAME_VIEW_GRID_BEGIN_X + GAME_VIEW_GRID_WIDTH + 2
GAME_VIEW_STATISTICS_BEGIN_Y = GAME_VIEW_NEXT_BEGIN_Y + GAME_VIEW_NEXT_HEIGHT
GAME_VIEW_STATISTICS_WIDTH = 18 + 2 + 2  # Statistiques + bordures
GAME_VIEW_STATISTICS_HEIGHT = 4 + 2 + 1  # grille + bordures + l'espace pour pouvoir tout print

GAME_VIEW_KEYBINDS_BEGIN_X = GAME_VIEW_GRID_BEGIN_X + GAME_VIEW_GRID_WIDTH + 2
GAME_VIEW_KEYBINDS_BEGIN_Y = GAME_VIEW_STATISTICS_BEGIN_Y + GAME_VIEW_STATISTICS_HEIGHT
GAME_VIEW_KEYBINDS_WIDTH = 18 + 2 + 2  # Keymaps + bordures
GAME_VIEW_KEYBINDS_HEIGHT = 8 + 2 + 1  # Keymaps + bordures + l'espace pour pouvoir tout print
