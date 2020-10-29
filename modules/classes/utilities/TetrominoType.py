# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe TetrominoTypes, les types de Tetromino
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
