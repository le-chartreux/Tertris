###############################################################
############################ MODEL ############################
###############################################################
# Size of the grid
GRID_WIDTH = 12
GRID_HEIGHT = 22


###############################################################
############################ VIEW #############################
###############################################################
VIEW_GRID_BEGIN_X = 1
VIEW_GRID_BEGIN_Y = 1
VIEW_GRID_WIDTH = GRID_WIDTH*2 + 2 + 1  # grille*2 + bordures + l'espace pour pouvoir tout print
# (*2 car les tétrominos font 2 de large)
VIEW_GRID_HEIGHT = GRID_HEIGHT + 2  # grille + bordures

VIEW_NEXT_BEGIN_X = VIEW_GRID_BEGIN_X + VIEW_GRID_WIDTH + 2
VIEW_NEXT_BEGIN_Y = 1
VIEW_NEXT_WIDTH = 4*2 + 2  # grille*2 + bordures (*2 car les tétrominos font 2 de large)
VIEW_NEXT_HEIGHT = 2 + 4 + 1  # grille + bordures + l'espace pour pouvoir tout print

VIEW_STORED_BEGIN_X = VIEW_NEXT_BEGIN_X + VIEW_NEXT_WIDTH + 2
VIEW_STORED_BEGIN_Y = 1
VIEW_STORED_WIDTH = 4*2 + 2  # grille*2 + bordures (*2 car les tétrominos font 2 de large)
VIEW_STORED_HEIGHT = 2 + 4 + 1  # grille + bordures + l'espace pour pouvoir tout print

VIEW_STATISTICS_BEGIN_X = VIEW_GRID_BEGIN_X + VIEW_GRID_WIDTH + 2
VIEW_STATISTICS_BEGIN_Y = VIEW_NEXT_BEGIN_Y + VIEW_NEXT_HEIGHT
VIEW_STATISTICS_WIDTH = 18 + 2 + 2  # Statistiques + bordures
VIEW_STATISTICS_HEIGHT = 4 + 2 + 1  # grille + bordures + l'espace pour pouvoir tout print

VIEW_KEYBINDS_BEGIN_X = VIEW_GRID_BEGIN_X + VIEW_GRID_WIDTH + 2
VIEW_KEYBINDS_BEGIN_Y = VIEW_STATISTICS_BEGIN_Y + VIEW_STATISTICS_HEIGHT
VIEW_KEYBINDS_WIDTH = 18 + 2 + 2  # Keymaps + bordures
VIEW_KEYBINDS_HEIGHT = 8 + 2 + 1  # Keymaps + bordures + l'espace pour pouvoir tout print
