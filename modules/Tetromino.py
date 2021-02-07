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
# + get_height()
# + get_width()
# + is_occupied()
# + get_tetromino_type()
# + copy_shape()
# + tetromino_factory() <- fonction
# ==========================================================

from typing import List, Optional

from modules.TetrominoType import TetrominoType


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
    _shape: List[List[Optional[TetrominoType]]]

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            shape: List[List[Optional[TetrominoType]]]
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
    def get_shape(self) -> List[List[Optional[TetrominoType]]]:
        return self._shape

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_shape(self, shape: List[List[Optional[TetrominoType]]]) -> None:
        self._shape = shape

    ###############################################################
    ######################## GET_HEIGHT ###########################
    ###############################################################
    def get_height(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la hauteur du tétromino
        # =============================
        return len(self.get_shape())

    ###############################################################
    ######################## GET_HEIGHT ###########################
    ###############################################################
    def get_width(self) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la largeur
        # =============================
        if self.get_height() == 0:  # On fait ça pour éviter un IndexError si le tétromino est vide
            return 0
        else:
            return len(self.get_shape()[0])

    ###############################################################
    ######################### IS_OCCUPIED #########################
    ###############################################################
    def is_occupied(self, x: int, y: int) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne si le tétromino a un bloc à cet emplacement dans sa grille
        # =============================
        return self.get_shape()[y][x] is not None

    ###############################################################
    ##################### GET_TETROMINO_TYPE ######################
    ###############################################################
    def get_tetromino_type(self) -> TetrominoType:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne le type du tétromino
        # =============================
        tetromino_type = None
        line = 0
        while line < 4 and tetromino_type is None:
            column = 0
            while column < 4 and tetromino_type is None:
                tetromino_type = self.get_shape()[line][column]
                column += 1
            line += 1

        if tetromino_type is None:
            raise TypeError("Error: impossible to get the type of a tetromino : all of its blocs are None")
        return tetromino_type

    ###############################################################
    ######################### COPY_SHAPE ##########################
    ###############################################################
    def copy_shape(self) -> List[List[Optional[TetrominoType]]]:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne une copie de la forme du tétromino (_shape)
        # =============================
        new_shape = []
        for line in range(self.get_height()):
            new_shape.append(self.get_shape()[line][:])
        return new_shape


###############################################################
##################### TETROMINO_FACTORY #######################
###############################################################
def tetromino_factory(tetromino_type: TetrominoType) -> Tetromino:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Crée puis retourne un tétromino correspondant au TetrominoType donné
    # =============================
    if tetromino_type == TetrominoType.I:
        return Tetromino(
            [
                [None, None, None, None],
                [TetrominoType.I, TetrominoType.I, TetrominoType.I, TetrominoType.I],
                [None, None, None, None],
                [None, None, None, None],
            ]
        )
    elif tetromino_type == TetrominoType.O:
        return Tetromino(
            [
                [None, None, None, None],
                [None, TetrominoType.O, TetrominoType.O, None],
                [None, TetrominoType.O, TetrominoType.O, None],
                [None, None, None, None],
            ]
        )
    elif tetromino_type == TetrominoType.T:
        return Tetromino(
            [
                [None, None, None, None],
                [None, TetrominoType.T, None, None],
                [None, TetrominoType.T, TetrominoType.T, None],
                [None, TetrominoType.T, None, None]
            ]
        )
    elif tetromino_type == TetrominoType.L:
        return Tetromino(
            [
                [None, None, None, None],
                [None, TetrominoType.L, TetrominoType.L, TetrominoType.L],
                [None, TetrominoType.L, None, None],
                [None, None, None, None],
            ]
        )
    elif tetromino_type == TetrominoType.J:
        return Tetromino(
            [
                [None, None, None, None],
                [None, TetrominoType.J, TetrominoType.J, TetrominoType.J],
                [None, None, None, TetrominoType.J],
                [None, None, None, None],
            ]
        )
    elif tetromino_type == TetrominoType.Z:
        return Tetromino(
            [
                [None, None, None, None],
                [None, TetrominoType.Z, TetrominoType.Z, None],
                [None, None, TetrominoType.Z, TetrominoType.Z],
                [None, None, None, None],
            ]
        )
    elif tetromino_type == TetrominoType.S:
        return Tetromino(
            [
                [None, None, None, None],
                [None, TetrominoType.S, TetrominoType.S, None],
                [TetrominoType.S, TetrominoType.S, None, None],
                [None, None, None, None],
            ]
        )
