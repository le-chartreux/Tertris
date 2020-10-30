# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Tetromino, qui sert à représenter un tétromino
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + is_occupied()
# ==========================================================
from typing import List

from modules.classes.commons.TetrominoType import TetrominoType


class Tetromino:
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
            shape: List[List[bool]]
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Tetromino, caractérisé par :
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
        self._shape = shape

    ###############################################################
    ######################### IS_OCCUPIED #########################
    ###############################################################
    def is_occupied(self, x: int, y: int) -> bool:
        return self.get_shape()[y][x]


###############################################################
##################### TETROMINO_FACTORY #######################
###############################################################
def tetromino_factory(tetromino_type: TetrominoType) -> Tetromino:
    if tetromino_type == TetrominoType.I:
        return Tetromino(
            [
                [True, True, True, True],
                [False, False, False, False],
                [False, False, False, False],
                [False, False, False, False],
            ]
        )
    elif tetromino_type == TetrominoType.O:
        return Tetromino(
            [
                [False, False, False, False],
                [False, True, True, False],
                [False, True, True, False],
                [False, False, False, False],
            ]
        )
    elif tetromino_type == TetrominoType.T:
        return Tetromino(
            [
                [False, True, False, False],
                [False, True, True, False],
                [False, True, False, False],
                [False, False, False, False],
            ]
        )
    elif tetromino_type == TetrominoType.L:
        return Tetromino(
            [
                [False, False, False, False],
                [False, True, True, True],
                [False, True, False, False],
                [False, False, False, False],
            ]
        )
    elif tetromino_type == TetrominoType.J:
        return Tetromino(
            [
                [False, False, False, False],
                [False, True, True, True],
                [False, False, False, True],
                [False, False, False, False],
            ]
        )
    elif tetromino_type == TetrominoType.Z:
        return Tetromino(
            [
                [False, False, False, False],
                [False, True, True, False],
                [False, False, True, True],
                [False, False, False, False],
            ]
        )
    elif tetromino_type == TetrominoType.S:
        return Tetromino(
            [
                [False, False, False, False],
                [False, True, True, False],
                [True, True, False, False],
                [False, False, False, False],
            ]
        )
