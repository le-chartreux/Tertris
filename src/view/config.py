"""
File that contains configurations used by the view
"""

import common.config as config_general
GRID_BEGIN_X = 1
GRID_BEGIN_Y = 1
GRID_WIDTH = config_general.GRID_WIDTH * 2 + 2 + 1  # grille*2 + bordures + l'espace pour pouvoir tout print
# (*2 car les tétrominos font 2 de large)
GRID_HEIGHT = config_general.GRID_HEIGHT + 2  # grille + bordures

NEXT_BEGIN_X = GRID_BEGIN_X + GRID_WIDTH + 2
NEXT_BEGIN_Y = 1
NEXT_WIDTH = 4 * 2 + 2  # grille*2 + bordures (*2 car les tétrominos font 2 de large)
NEXT_HEIGHT = 2 + 4 + 1  # grille + bordures + l'espace pour pouvoir tout print

STORED_BEGIN_X = NEXT_BEGIN_X + NEXT_WIDTH + 2
STORED_BEGIN_Y = 1
STORED_WIDTH = 4 * 2 + 2  # grille*2 + bordures (*2 car les tétrominos font 2 de large)
STORED_HEIGHT = 2 + 4 + 1  # grille + bordures + l'espace pour pouvoir tout print

STATISTICS_BEGIN_X = GRID_BEGIN_X + GRID_WIDTH + 2
STATISTICS_BEGIN_Y = NEXT_BEGIN_Y + NEXT_HEIGHT
STATISTICS_WIDTH = 18 + 2 + 2  # Statistiques + bordures
STATISTICS_HEIGHT = 4 + 2 + 1  # grille + bordures + l'espace pour pouvoir tout print

KEYBINDS_BEGIN_X = GRID_BEGIN_X + GRID_WIDTH + 2
KEYBINDS_BEGIN_Y = STATISTICS_BEGIN_Y + STATISTICS_HEIGHT
KEYBINDS_WIDTH = 18 + 2 + 2  # Keymaps + bordures
KEYBINDS_HEIGHT = 8 + 2 + 1  # Keymaps + bordures + l'espace pour pouvoir tout print
