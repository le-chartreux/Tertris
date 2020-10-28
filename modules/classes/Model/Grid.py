# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Grid, qui sert à représenter la grille de jeu du côté modèle
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + get_duration
# ==========================================================

from typing import List

from modules.settings import VERTICAL_SIZE, HORIZONTAL_SIZE


class Grid:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_shape"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _shape: List[List[bool]]

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            shape: List[List[bool]] = None
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Grid, caractérisé par :
        # - une forme (_shape)
        # =============================
        self.set_shape(shape)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_shape(self) -> List[List[bool]]:
        return self._shape

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_shape(self, shape: List[List[bool]]) -> None:
        if shape is None:
            # On crée un tableau à deux dimensions rempli de False
            self._shape = []
            for line in range(VERTICAL_SIZE):
                self._shape.append([])
                for _ in range(HORIZONTAL_SIZE):
                    self._shape[line].append(False)
        else:
            self._shape = shape

    ###############################################################
    ######################### IS_OCCUPIED #########################
    ###############################################################
    def is_occupied(self, x: int, y: int) -> bool:
        return self.get_shape()[y][x]
