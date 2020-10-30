# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Rotation, les rotations réalisables
# par le tétromino actif
# ==========================================================

from enum import Enum


class Rotation(Enum):
    LEFT = 90
    RIGHT = -90
