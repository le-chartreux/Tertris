# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe TetrominoTypes, énumération des noms de Tetromino.
# Utilisé pour créer un tétromino avec tetromino_factory()
# ==========================================================

from enum import Enum, auto


class TetrominoType(Enum):
    I = auto()
    O = auto()
    T = auto()
    L = auto()
    J = auto()
    Z = auto()
    S = auto()
