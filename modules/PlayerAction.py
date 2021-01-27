# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe PlayerAction, l'énumération des actions que peut faire le joueur
# ==========================================================

from enum import Enum, auto
from modules.PlayerInput import PlayerInput


class PlayerAction(Enum):
    # Commons
    NOTHING = PlayerInput.NOTHING
    MISSCLIC = PlayerInput.KEY_UNUSED

    # Game
    MOVE_ACTIVE_TETROMINO_RIGHT = PlayerInput.KEY_RIGHT
    MOVE_ACTIVE_TETROMINO_LEFT = PlayerInput.KEY_LEFT
    MOVE_ACTIVE_TETROMINO_DOWN = PlayerInput.KEY_DOWN

    ROTATE_ACTIVE_TETROMINO_RIGHT = PlayerInput.KEY_D
    ROTATE_ACTIVE_TETROMINO_LEFT = PlayerInput.KEY_S

    STORE_ACTIVE_TETROMINO = PlayerInput.KEY_S

    PAUSE_GAME = PlayerInput.KEY_P
    QUIT_GAME = PlayerInput.KEY_ESC

    # Title
