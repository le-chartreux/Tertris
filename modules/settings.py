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
VIEW_GRID_WIDTH = GRID_WIDTH + 2 + 1  # grille + bordures + l'espace pour pouvoir tout print
VIEW_GRID_HEIGHT = GRID_HEIGHT + 2  # grille + bordures

VIEW_NEXT_BEGIN_X = VIEW_GRID_BEGIN_X + VIEW_GRID_WIDTH
VIEW_NEXT_BEGIN_Y = 1
VIEW_NEXT_WIDTH = 4 + 2  # grille + bordures
VIEW_NEXT_HEIGHT = 2 + 4 + 1  # grille + bordures + l'espace pour pouvoir tout print

VIEW_STORED_BEGIN_X = VIEW_NEXT_BEGIN_X + VIEW_NEXT_WIDTH + 1
VIEW_STORED_BEGIN_Y = 1
VIEW_STORED_WIDTH = 4 + 2  # grille + bordures
VIEW_STORED_HEIGHT = 2 + 4 + 1  # grille + bordures + l'espace pour pouvoir tout print

VIEW_LOGO_BEGIN_X = VIEW_STORED_BEGIN_X + VIEW_STORED_WIDTH + 1
VIEW_LOGO_BEGIN_Y = 1
VIEW_LOGO_WIDTH = 4 + 2  # grille + bordures
VIEW_LOGO_HEIGHT = 2 + 4 + 1  # grille + bordures + l'espace pour pouvoir tout print

VIEW_STATISTICS_BEGIN_X = VIEW_GRID_BEGIN_X + VIEW_GRID_WIDTH
VIEW_STATISTICS_BEGIN_Y = VIEW_NEXT_BEGIN_Y + VIEW_NEXT_HEIGHT
VIEW_STATISTICS_WIDTH = 18 + 2  # Statistiques + bordures
VIEW_STATISTICS_HEIGHT = 4 + 2 + 1  # grille + bordures + l'espace pour pouvoir tout print

VIEW_KEYBINDS_BEGIN_X = VIEW_GRID_BEGIN_X + VIEW_GRID_WIDTH
VIEW_KEYBINDS_BEGIN_Y = VIEW_STATISTICS_BEGIN_Y + VIEW_STATISTICS_HEIGHT
VIEW_KEYBINDS_WIDTH = 18 + 2  # Keymaps + bordures
VIEW_KEYBINDS_HEIGHT = 7 + 2 + 1  # Statistiques + bordures + l'espace pour pouvoir tout print
