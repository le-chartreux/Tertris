# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Direction, les directions que peuvent prendre un élément
# -----------------------------
# REMARQUES :
# - Les valeurs sont par rapport à un tableau d’haut en bas et de droite à gauche
# ==========================================================

from enum import Enum
from modules.classes.Utilities.Position import Position


class Direction(Enum):
    LEFT = Position(-1, 0)
    RIGHT = Position(1, 0)
    UP = Position(0, -1)
    DOWN = Position(0, 1)
