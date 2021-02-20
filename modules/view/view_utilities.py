# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir les fonctions communes utiles aux vues
# ==========================================================

import curses
import locale

from modules.tetromino.TetrominoType import TetrominoType
import modules.view.color_pairs as color_pairs


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
def set_colorscheme() -> None:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Met en place les paires de couleurs
    # =============================
    curses.start_color()

    curses.init_pair(color_pairs.I_COLOR, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(color_pairs.O_COLOR, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(color_pairs.T_COLOR, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(color_pairs.L_COLOR, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(color_pairs.J_COLOR, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(color_pairs.Z_COLOR, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(color_pairs.S_COLOR, curses.COLOR_GREEN, curses.COLOR_WHITE)

    curses.init_pair(color_pairs.BLACK_N_WHITE, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(color_pairs.RED_N_BLUE, curses.COLOR_RED, curses.COLOR_BLUE)
    curses.init_pair(color_pairs.BLACK_N_BLUE, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(color_pairs.BLACK_N_BLACK, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(color_pairs.RED_N_WHITE, curses.COLOR_RED, curses.COLOR_WHITE)


###############################################################
####################### GET_COLOR_PAIR ########################
###############################################################
def get_color_pair(tetromino_type: TetrominoType) -> int:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Retourne la couleur du tetromino en fonction de son type
    # =============================
    if tetromino_type == TetrominoType.I:
        return color_pairs.I_COLOR
    elif tetromino_type == TetrominoType.O:
        return color_pairs.O_COLOR
    elif tetromino_type == TetrominoType.T:
        return color_pairs.T_COLOR
    elif tetromino_type == TetrominoType.L:
        return color_pairs.L_COLOR
    elif tetromino_type == TetrominoType.J:
        return color_pairs.J_COLOR
    elif tetromino_type == TetrominoType.Z:
        return color_pairs.Z_COLOR
    elif tetromino_type == TetrominoType.S:
        return color_pairs.S_COLOR
