# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe ButtonName, l'énumération des noms de boutons existants
# ==========================================================

from enum import Enum


class ButtonName(Enum):
    # TitleScreen
    START = 0
    OPTIONS = 1
    HIGH_SCORES = 2
    QUIT = 3
