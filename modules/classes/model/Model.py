# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Model
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + send_query()
# + next_tick()
# ==========================================================

from typing import Optional
from random import choice

from modules.classes.commons.Grid import Grid
from modules.classes.commons.Tetromino import Tetromino, tetromino_factory
from modules.classes.commons.ActiveTetromino import ActiveTetromino
from modules.classes.commons.Statistics import Statistics

from modules.classes.commons.Direction import Direction
from modules.classes.commons.TetrominoType import TetrominoType

from modules.settings import GRID_WIDTH, GRID_HEIGHT


class Model:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_grid",
        "_active_tetromino",
        "_stored_tetromino",
        "_statistics"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _grid: Grid
    _active_tetromino: ActiveTetromino
    _stored_tetromino: Optional[Tetromino]
    _statistics: Statistics

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            grid: Grid = None,
            active_tetromino: ActiveTetromino = None,
            stored_tetromino: Optional[Tetromino] = None,
            statistics: Statistics = None
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Model, caractérisé par :
        # - la grille de jeu (_grid)
        # - le tetromino actif (_active_tetromino)
        # - le tetromino stocké (_stored_tetromino)
        # - les statistiques de la partie (_statistics)
        # =============================
        if grid is None:
            grid = Grid()

        if active_tetromino is None:
            active_tetromino = ActiveTetromino(0, 0, tetromino=random_next_tetromino())

        if statistics is None:
            statistics = Statistics()

        self.set_grid(grid)
        self.set_active_tetromino(active_tetromino)
        self.set_stored_tetromino(stored_tetromino)
        self.set_statistics(statistics)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_grid(self) -> Grid:
        return self._grid

    def get_active_tetromino(self) -> ActiveTetromino:
        return self._active_tetromino

    def get_stored_tetromino(self) -> Optional[Tetromino]:
        return self._stored_tetromino

    def get_statistics(self) -> Statistics:
        return self._statistics

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_grid(self, grid: Grid) -> None:
        self._grid = grid

    def set_active_tetromino(self, active_tetromino: ActiveTetromino) -> None:
        self._active_tetromino = active_tetromino

    def set_stored_tetromino(self, stored_tetromino: Optional[Tetromino]) -> None:
        self._stored_tetromino = stored_tetromino

    def set_statistics(self, statistics: Statistics) -> None:
        self._statistics = statistics

    ###############################################################
    ########################## NEXT_TICK ##########################
    ###############################################################
    def next_tick(self):
        pass

    ###############################################################
    ################# CAN_ACTIVE_TETROMINO_MOVE ###################
    ###############################################################
    def can_active_tetromino_move(self, direction: Direction) -> bool:
        line = 0

        possible = True
        while line < 4 and possible:
            column = 0
            while column < 4 and possible:
                possible = (
                    (
                            0 <= self.get_active_tetromino().get_x() + column + direction.value.get_x() < GRID_WIDTH
                            and
                            0 <= self.get_active_tetromino().get_y() + line + direction.value.get_y() < GRID_HEIGHT
                    )
                    and not (
                        self.get_grid().is_occupied(
                            self.get_active_tetromino().get_x() + direction.value.get_x(),
                            self.get_active_tetromino().get_y() + direction.value.get_y()
                        )
                        and
                        self.get_active_tetromino().get_shape()[line][column]
                   )
                )
                column += 1
            line += 1
        return possible


###############################################################
################### RANDOM_NEXT_TETROMINO #####################
###############################################################
def random_next_tetromino() -> Tetromino:
    return tetromino_factory(choice(list(TetrominoType)))
