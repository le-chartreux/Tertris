# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir les fonctions communes utiles aux vues (devrait disparaitre et
#  finir dans une classe abstraite View quand j'aurai factorisé les vues)
# -----------------------------
# CONTENU :
# + set_colorscheme()
# + get_color_pair()
# ==========================================================

import curses

from modules.classes.TetrominoType import TetrominoType


###############################################################
###################### SET_COLORSCHEME ########################
###############################################################
def set_colorscheme() -> None:
    curses.start_color()
    # GameView
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)  # I
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)  # O
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_WHITE)  # T
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)  # L
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_WHITE)  # J
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_WHITE)  # Z
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_WHITE)   # S
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Background & textes

    # TitleView
    curses.init_pair(9, curses.COLOR_RED, curses.COLOR_BLUE)  # bordure T logo
    curses.init_pair(10, curses.COLOR_BLACK, curses.COLOR_WHITE)  # >
    curses.init_pair(11, curses.COLOR_BLACK, curses.COLOR_BLUE)  # lettres


###############################################################
####################### GET_COLOR_PAIR ########################
###############################################################
def get_color_pair(tetromino_type: TetrominoType) -> int:
    if tetromino_type == TetrominoType.I:
        return 1
    elif tetromino_type == TetrominoType.O:
        return 2
    elif tetromino_type == TetrominoType.T:
        return 3
    elif tetromino_type == TetrominoType.L:
        return 4
    elif tetromino_type == TetrominoType.J:
        return 5
    elif tetromino_type == TetrominoType.Z:
        return 6
    elif tetromino_type == TetrominoType.S:
        return 7
