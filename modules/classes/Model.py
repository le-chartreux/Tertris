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
# + have_to_go_down()
# + do_tick()
# + can_active_tetromino_move()
# + can_active_tetromino_rotate()
# + store_active_tetromino()
# ==========================================================

from time import time
from typing import Optional
from random import choice

from modules.classes.Grid import Grid
from modules.classes.Tetromino import Tetromino, tetromino_factory
from modules.classes.ActiveTetromino import ActiveTetromino
from modules.classes.Statistics import Statistics
from modules.classes.Rotation import Rotation

from modules.classes.Direction import Direction
from modules.classes.TetrominoType import TetrominoType

from modules.settings import GRID_WIDTH, GRID_HEIGHT


class Model:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_grid",
        "_active_tetromino",
        "_next_tetromino",
        "_stored_tetromino",
        "_statistics",
        "_last_down",
        "_can_player_store"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _grid: Grid
    _active_tetromino: ActiveTetromino
    _next_tetromino: Tetromino
    _stored_tetromino: Optional[Tetromino]
    _statistics: Statistics
    _last_down: float
    _can_player_store: bool

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            grid: Grid = None,
            active_tetromino: ActiveTetromino = None,
            next_tetromino: Tetromino = None,
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
        # - le prochain tétromino (_next_tetromino)
        # - le tetromino stocké (_stored_tetromino)
        # - les statistiques de la partie (_statistics)
        # - la dernière fois que l'action de baisser le tétromino actif a été faite (_last_down)
        # - si le joueur peut stocker son tétromino maintenant (_can_player_store)
        # =============================
        self._last_down = time()
        self._can_player_store = True

        if grid is None:
            grid = Grid()

        if active_tetromino is None:
            active_tetromino = ActiveTetromino(tetromino=random_next_tetromino())

        if next_tetromino is None:
            next_tetromino = random_next_tetromino()

        if statistics is None:
            statistics = Statistics()

        self.set_grid(grid)
        self.set_active_tetromino(active_tetromino)
        self.set_next_tetromino(next_tetromino)
        self.set_stored_tetromino(stored_tetromino)
        self.set_statistics(statistics)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_grid(self) -> Grid:
        return self._grid

    def get_active_tetromino(self) -> ActiveTetromino:
        return self._active_tetromino

    def get_next_tetromino(self) -> Tetromino:
        return self._next_tetromino

    def get_stored_tetromino(self) -> Optional[Tetromino]:
        return self._stored_tetromino

    def get_statistics(self) -> Statistics:
        return self._statistics

    def get_last_down(self) -> float:
        return self._last_down

    def get_can_player_switch(self) -> bool:
        return self._can_player_store

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_grid(self, grid: Grid) -> None:
        self._grid = grid

    def set_active_tetromino(self, active_tetromino: ActiveTetromino) -> None:
        self._active_tetromino = active_tetromino

    def set_next_tetromino(self, next_tetromino: Tetromino) -> None:
        self._next_tetromino = next_tetromino

    def set_stored_tetromino(self, stored_tetromino: Optional[Tetromino]) -> None:
        self._stored_tetromino = stored_tetromino

    def set_statistics(self, statistics: Statistics) -> None:
        self._statistics = statistics

    def set_last_down(self, new_last_down: float) -> None:
        self._last_down = new_last_down

    def set_can_player_switch(self, can_player_switch: bool) -> None:
        self._can_player_store = can_player_switch

    ###############################################################
    ####################### HAVE_TO_GO_DOWN #######################
    ###############################################################
    def have_to_go_down(self) -> bool:
        # Oui si plus de (0.8 - (level - 1)*0.007)**(level - 1) secondes se sont écoulées depuis le derniers vers le bas
        # (cf le guideline de Tetris)
        level = self.get_statistics().get_level()
        return (time() - self.get_last_down()) > (0.8 - (level - 1)*0.007)**(level - 1)

    ###############################################################
    ########################### DO_TICK ###########################
    ###############################################################
    def do_tick(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Effectue la séquence d'évènement qui se joue à chaque tick
        # dans le modèle :
        # - Regarder si le tétromino actif peut faire un mouvement vers le bas
        # - Si oui et qu'il faut qu'il descende : le faire
        # - Si non :
        #   l'ajouter à la grille
        #   passer au prochain tétromino
        #   générer un nouveau prochain tétromino
        #   autoriser le joueur à switcher à nouveau
        #   regarder si des lignes ont été complétées
        #   ajouter les lignes complétées et les points engendrés aux statistiques
        # =============================
        if self.have_to_go_down():
            self.set_last_down(time())
            if self.can_active_tetromino_move(Direction.DOWN):
                self.get_active_tetromino().move(Direction.DOWN)
            else:
                self.get_grid().add_active_tetromino(self.get_active_tetromino())
                self.set_active_tetromino(ActiveTetromino(tetromino=self.get_next_tetromino()))
                self.set_next_tetromino(random_next_tetromino())
                self.set_can_player_switch(True)

                # On regarde si des lignes ont été remplies :
                number_of_completed_lines = 0
                for line in range(GRID_HEIGHT):
                    if self.get_grid().is_line_full(line):
                        self.get_grid().drop_lines_upper(line)
                        number_of_completed_lines += 1
                self.get_statistics().add_lines_completed(number_of_completed_lines)
                self.get_statistics().add_points_for_lines(number_of_completed_lines)

    ###############################################################
    ################# CAN_ACTIVE_TETROMINO_MOVE ###################
    ###############################################################
    def can_active_tetromino_move(self, direction: Direction) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne si le tétromino actuel peut effectuer le déplacement
        # =============================
        line = 0

        possible = True
        while line < 4 and possible:
            column = 0
            while column < 4 and possible:
                possible = (
                    not self.get_active_tetromino().is_occupied(x=column, y=line)  # Soit il n'y a pas de bloc
                    or  # ou
                    (  # Soit le bloc va aller dans les bordures de la grille ...
                        0 <= self.get_active_tetromino().get_x() + column + direction.value.get_x() < GRID_WIDTH
                        and
                        0 <= self.get_active_tetromino().get_y() + line + direction.value.get_y() < GRID_HEIGHT
                    )
                    and not (  # ... et l'emplacement futur n'est pas occupé
                        self.get_grid().is_occupied(
                            self.get_active_tetromino().get_x() + direction.value.get_x() + column,
                            self.get_active_tetromino().get_y() + direction.value.get_y() + line
                        )
                    )
                )
                column += 1
            line += 1
        return possible

    ###############################################################
    ################# CAN_ACTIVE_TETROMINO_MOVE ###################
    ###############################################################
    def can_active_tetromino_rotate(self, rotation: Rotation) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne si le tétromino actuel peut effectuer la rotation
        # =============================
        possible = True
        new_shape = [
            self.get_active_tetromino().get_shape()[0][:],
            self.get_active_tetromino().get_shape()[1][:],
            self.get_active_tetromino().get_shape()[2][:],
            self.get_active_tetromino().get_shape()[3][:],
        ]

        tetromino_after_rotation = ActiveTetromino(
            self.get_active_tetromino().get_x(),
            self.get_active_tetromino().get_y(),
            shape=new_shape
        )
        tetromino_after_rotation.rotate(rotation)

        line = 0
        while line < 4 and possible:
            column = 0
            while column < 4 and possible:
                possible = (
                    not tetromino_after_rotation.is_occupied(x=column, y=line)  # Soit il n'y a pas de bloc
                    or  # ou
                    (  # Soit le bloc est dans les bordures de la grille ...
                            0 <= tetromino_after_rotation.get_x() + column < GRID_WIDTH
                            and
                            0 <= tetromino_after_rotation.get_y() + line < GRID_HEIGHT
                    )
                    and not (  # ... et son emplacement n'est pas occupé
                        self.get_grid().is_occupied(
                            int(tetromino_after_rotation.get_x() + column),
                            int(tetromino_after_rotation.get_y() + line)
                        )
                    )
                )
                column += 1
            line += 1
        return possible

    ###############################################################
    ################### STORE_ACTIVE_TETROMINO ####################
    ###############################################################
    def store_active_tetromino(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # - Si il y a un tétromino stocké :
        #   Échange le tétromino actif avec celui stocké
        # - Si non :
        #   Stock le tétromino actif, passe au tétromino suivant et génère un nouveau tétromino suivant
        # =============================
        tetromino_to_swap_with = self.get_stored_tetromino()
        if tetromino_to_swap_with is None:
            tetromino_to_swap_with = self.get_next_tetromino()
            self.set_next_tetromino(random_next_tetromino())

        self.set_stored_tetromino(self.get_active_tetromino())

        # On regarde à quel y il faut mettre le nouveau tétromino actif
        # -> quelle est la première ligne où il y a un bloc ?
        y_new_active_tetromino = 0
        while(
            not tetromino_to_swap_with.is_occupied(x=0, y=-y_new_active_tetromino)
            and not tetromino_to_swap_with.is_occupied(x=1, y=-y_new_active_tetromino)
            and not tetromino_to_swap_with.is_occupied(x=2, y=-y_new_active_tetromino)
            and not tetromino_to_swap_with.is_occupied(x=3, y=-y_new_active_tetromino)
        ):
            y_new_active_tetromino -= 1

        self.set_active_tetromino(ActiveTetromino(y=y_new_active_tetromino, tetromino=tetromino_to_swap_with))


###############################################################
################### RANDOM_NEXT_TETROMINO #####################
###############################################################
def random_next_tetromino() -> Tetromino:
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Tire au hazard le prochain tétromino
    # =============================
    return tetromino_factory(choice(list(TetrominoType)))
