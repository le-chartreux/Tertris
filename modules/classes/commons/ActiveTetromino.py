# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe ActiveTetromino, le tétromino actuellement joué
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + move()
# + rotate()
# ==========================================================

from typing import List, Optional

from modules.classes.commons.Tetromino import Tetromino

from modules.classes.commons.Position import Position
from modules.classes.commons.Direction import Direction
from modules.classes.commons.Rotation import Rotation


class ActiveTetromino(Tetromino):
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_position"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _position: Position

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            x: float = 4,
            y: float = -1,  # -1 car la première ligne du tetromino est toujours vide
            shape: Optional[List[List[bool]]] = None,
            tetromino: Optional[Tetromino] = None
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet ActiveTetromino, caractérisé par :
        # - sa forme (_shape)
        # - la position sur l'axe X de son coin haut-gauche (_x)
        # - la position sur l'axe Y de son coin haut-gauche (_y)
        # =============================
        if shape is not None:
            super().__init__(shape)
        elif tetromino is not None:
            super().__init__(tetromino.get_shape())
        else:
            raise AttributeError("Erreur: il manque l'attribut shape ou tetromino pour créer un ActiveTetromino")

        self._position = Position(x, y)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_position(self) -> Position:
        return self._position

    def get_x(self) -> float:
        return self.get_position().get_x()

    def get_y(self) -> float:
        return self.get_position().get_y()

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_position(self, x: float, y: float):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x: float):
        self.get_position().set_x(x)

    def set_y(self, y: float):
        self.get_position().set_y(y)

    ###############################################################
    ############################# MOVE ############################
    ###############################################################
    def move(self, direction: Direction):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Modifie la position du Tetromino en fonction de la direction
        # =============================
        self.set_x(self.get_x() + direction.value.get_x())
        self.set_y(self.get_y() + direction.value.get_y())

    ###############################################################
    ########################### ROTATE ############################
    ###############################################################
    def rotate(self, rotation: Rotation):
        # Création de la nouvelle forme :
        new_shape = []
        for line in range(4):
            new_shape.append([False, False, False, False])

        # Rotation
        if rotation == Rotation.LEFT:
            for i in range(4):
                self.get_shape()[i].reverse()
        elif rotation == Rotation.RIGHT:
            self.get_shape().reverse()
        else:
            raise ValueError("Error: impossible to rotate the active tetromino: rotation argument incorrect")

        for line in range(4):
            for column in range(4):
                new_shape[line][column] = self.get_shape()[column][line]

        # Assignation de la nouvelle forme
        self.set_shape(new_shape)
