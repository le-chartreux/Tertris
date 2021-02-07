# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe ActiveTetromino, le tétromino contrôlé par le joueur
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

from modules.Tetromino import Tetromino

from modules.Position import Position
from modules.Direction import Direction
from modules.Rotation import Rotation


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
            tetromino: Tetromino,
            x: int = 4,
            y: int = -1  # -1 car la première ligne du tetromino est toujours vide
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet ActiveTetromino, caractérisé par :
        # - sa forme (_shape), hérité de Tetromino
        # - la position sur l'axe X de son coin haut-gauche (_x)
        # - la position sur l'axe Y de son coin haut-gauche (_y)
        # =============================
        super().__init__(tetromino.get_shape())
        self._position = Position(x, y)  # On n'utilise pas le setter, pour initialiser la position

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_position(self) -> Position:
        return self._position

    def get_x(self) -> int:
        return self.get_position().get_x()

    def get_y(self) -> int:
        return self.get_position().get_y()

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_position(self, x: int, y: int):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x: int):
        self.get_position().set_x(x)

    def set_y(self, y: int):
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
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Fait pivoter le tétromino de 90° vers la gauche ou vers la droite
        # =============================
        # Création de la nouvelle forme :
        new_shape = []
        for line in range(self.get_height()):
            new_shape.append([])
            for column in range(self.get_width()):
                new_shape[line].append(None)

        # Rotation
        if rotation == Rotation.LEFT:
            for line in range(self.get_height()):
                self.get_shape()[line].reverse()
        elif rotation == Rotation.RIGHT:
            self.get_shape().reverse()
        else:
            raise ValueError("Error: impossible to rotate the active tetromino: rotation argument incorrect")

        for line in range(self.get_height()):
            for column in range(self.get_width()):
                new_shape[line][column] = self.get_shape()[column][line]

        # Assignation de la nouvelle forme
        self.set_shape(new_shape)
