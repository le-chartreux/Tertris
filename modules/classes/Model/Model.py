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
# ==========================================================

from typing import Optional

from modules.classes.Model.Grid import Grid
from modules.classes.Model.Tetromino import Tetromino
from modules.classes.Model.Statistics import Statistics

from modules.classes.Controller.Controller import Controller


class Model:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_controller",
        "_grid",
        "_active_tetromino",
        "_stored_tetromino",
        "_statistics"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _controller: Controller
    _grid: Grid
    _active_tetromino: Tetromino
    _stored_tetromino: Optional[Tetromino]
    _statistics: Statistics

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            controller: Controller,
            grid: Grid = None,
            active_tetromino: Tetromino = None,
            stored_tetromino: Optional[Tetromino] = None,
            statistics: Statistics = None
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Model, caractérisé par :
        # - son controller (_controller)
        # - la grille de jeu (_grid)
        # - le tetromino actif (_active_tetromino)
        # - le tetromino stocké (_stored_tetromino)
        # - les statistiques de la partie (_statistics)
        # =============================
        if grid is None:
            grid = Grid()

        if active_tetromino is None:
            active_tetromino = Tetromino()

        if statistics is None:
            statistics = Statistics()

        self.set_controller(controller)
        self.set_grid(grid)
        self.set_active_tetromino(active_tetromino)
        self.set_stored_tetromino(stored_tetromino)
        self.set_statistics(statistics)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_controller(self) -> Controller:
        return self._controller

    def get_grid(self) -> Grid:
        return self._grid

    def get_active_tetromino(self) -> Tetromino:
        return self._active_tetromino

    def get_stored_tetromino(self) -> Optional[Tetromino]:
        return self._stored_tetromino

    def get_statistics(self) -> Statistics:
        return self._statistics

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_controller(self, controller: Controller):
        self._controller = controller

    def set_grid(self, grid: Grid) -> None:
        self._grid = grid

    def set_active_tetromino(self, active_tetromino: Tetromino) -> None:
        self._active_tetromino = active_tetromino

    def set_stored_tetromino(self, stored_tetromino: Optional[Tetromino]) -> None:
        self._stored_tetromino = stored_tetromino

    def set_statistics(self, statistics: Statistics) -> None:
        self._statistics = statistics

    ###############################################################
    ########################## SEND_QUERY #########################
    ###############################################################
    def send_query(self, query: Query):
        self._controller
