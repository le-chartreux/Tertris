# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir les fonctions communes utiles aux vues
# ==========================================================

import curses
import locale

from modules.tetromino.TetrominoType import TetrominoType
from modules.view.ColorPair import ColorPair

###############################################################
######################## SETUP_CURSES #########################
###############################################################
def setup_curses() -> None:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Paramètre tout ce qui est nécessaire pour pouvoir correctement utiliser curses
    # =============================
    locale.setlocale(locale.LC_ALL, "")
    curses.curs_set(0)  # Ne pas afficher le curseur
    curses.noecho()  # Ne pas afficher ce que marque l'utilisateur
    curses.cbreak()  # Ne pas attendre que l'utilisateur appui sur Entrée pour récupérer son entrée


###############################################################
####################### REVERT_CURSES #########################
###############################################################
def revert_curses() -> None:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Remet curses dans son état original et le ferme
    # =============================
    curses.curs_set(1)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


###############################################################
###################### SET_COLORSCHEME ########################
###############################################################
def set_colorscheme() -> None:  # TODO : améliorer ça
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Met en place les paires de couleurs
    # =============================
    curses.start_color()

    curses.init_pair(ColorPair.I_COLOR.value, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(ColorPair.O_COLOR.value, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(ColorPair.T_COLOR.value, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(ColorPair.L_COLOR.value, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(ColorPair.J_COLOR.value, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(ColorPair.Z_COLOR.value, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(ColorPair.S_COLOR.value, curses.COLOR_GREEN, curses.COLOR_WHITE)

    curses.init_pair(ColorPair.BLACK_N_WHITE.value, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(ColorPair.RED_N_BLUE.value, curses.COLOR_RED, curses.COLOR_BLUE)
    curses.init_pair(ColorPair.BLACK_N_BLUE.value, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(ColorPair.BLACK_N_BLACK.value, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(ColorPair.RED_N_WHITE.value, curses.COLOR_RED, curses.COLOR_WHITE)


###############################################################
####################### GET_COLOR_PAIR ########################
###############################################################
def get_color_pair(tetromino_type: TetrominoType) -> ColorPair:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Retourne la couleur du tetromino en fonction de son type
    # =============================
    if tetromino_type == TetrominoType.I:
        return ColorPair.I_COLOR
    elif tetromino_type == TetrominoType.O:
        return ColorPair.O_COLOR
    elif tetromino_type == TetrominoType.T:
        return ColorPair.T_COLOR
    elif tetromino_type == TetrominoType.L:
        return ColorPair.L_COLOR
    elif tetromino_type == TetrominoType.J:
        return ColorPair.J_COLOR
    elif tetromino_type == TetrominoType.Z:
        return ColorPair.Z_COLOR
    elif tetromino_type == TetrominoType.S:
        return ColorPair.S_COLOR
