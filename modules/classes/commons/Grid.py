# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Grid, qui sert à représenter la grille de jeu
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + is_occupied()
# + add_active_tetromino()
# ==========================================================

from typing import List

from modules.classes.commons.ActiveTetromino import ActiveTetromino

from modules.settings import GRID_HEIGHT, GRID_WIDTH


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
            for line in range(GRID_HEIGHT):
                self._shape.append([])
                for _ in range(GRID_WIDTH):
                    self._shape[line].append(False)
        else:
            self._shape = shape

    ###############################################################
    ######################### IS_OCCUPIED #########################
    ###############################################################
    def is_occupied(self, x: int, y: int) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne si la case est occupée par un bloc
        # =============================
        return self.get_shape()[y][x]

    ###############################################################
    #################### ADD_ACTIVE_TETROMINO #####################
    ###############################################################
    def add_active_tetromino(self, active_tetromino: ActiveTetromino):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Ajoute le tétromino actuel dans la grille
        # =============================
        for line in range(4):
            for column in range(4):
                if (
                        0 <= active_tetromino.get_x() + column < GRID_WIDTH
                        and 0 <= active_tetromino.get_y() + line < GRID_HEIGHT
                ):
                    self.get_shape()[
                            line + int(active_tetromino.get_y())
                        ][
                            column + int(active_tetromino.get_x())
                        ] = self.is_occupied(
                            x=column + int(active_tetromino.get_x()),
                            y=line + int(active_tetromino.get_y())
                        ) or active_tetromino.is_occupied(x=column, y=line)

