# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe PlayerAction, l'énumération des actions que peut faire le joueur
# ==========================================================

from enum import Enum, auto


class PlayerAction(Enum):
    MOVE_ACTIVE_TETROMINO_RIGHT = auto()
    MOVE_ACTIVE_TETROMINO_LEFT = auto()
    MOVE_ACTIVE_TETROMINO_DOWN = auto()

    ROTATE_ACTIVE_TETROMINO_RIGHT = auto()
    ROTATE_ACTIVE_TETROMINO_LEFT = auto()

    STORE_ACTIVE_TETROMINO = auto()

    PAUSE_GAME = auto()
    QUIT_GAME = auto()

    NOTHING = auto()

    MISSCLIC = auto()