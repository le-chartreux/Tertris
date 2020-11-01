# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Rotation, l'énumération des rotations réalisables par un tétromino actif
# ==========================================================

from enum import Enum


class Rotation(Enum):
    LEFT = 90
    RIGHT = -90
