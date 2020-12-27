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
# + has_to_go_down()
# + do_tick()
# + treat_game_lost()
# + treat_tetromino_placed()
# + can_active_tetromino_move()
# + can_active_tetromino_rotate()
# + can_player_store_active_tetromino()
# + store_active_tetromino()
# + is_game_lose()
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
        "_player_already_store",
        "_first_down_new_tetromino"
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
    _player_already_store: bool
    _first_down_new_tetromino: bool

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            grid: Grid = None,
            active_tetromino: ActiveTetromino = None,
            next_tetromino: Tetromino = None,
            stored_tetromino: Optional[Tetromino] = None,
            statistics: Statistics = None,
            last_down: float = None,
            player_already_store: bool = False,
            first_down_new_tetromino: bool = True
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
        # - si le joueur a déjà stocké son tétromino à ce tick (_player_already_store)
        # - si c'est le tétromino actif n'as pas encore été baissé (_first_down_new_tetromino)
        # =============================
        if grid is None:
            grid = Grid()

        if active_tetromino is None:
            active_tetromino = ActiveTetromino(tetromino=random_next_tetromino())

        if next_tetromino is None:
            next_tetromino = random_next_tetromino()

        if statistics is None:
            statistics = Statistics(level=0)

        if last_down is None:
            last_down = time()

        self.set_grid(grid)
        self.set_active_tetromino(active_tetromino)
        self.set_next_tetromino(next_tetromino)
        self.set_stored_tetromino(stored_tetromino)
        self.set_statistics(statistics)
        self.set_last_down(last_down)
        self.set_player_already_store(player_already_store)
        self.set_first_down_new_tetromino(first_down_new_tetromino)

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

    def get_player_already_store(self) -> bool:
        return self._player_already_store

    def get_first_down_new_tetromino(self) -> bool:
        return self._first_down_new_tetromino

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

    def set_last_down(self, last_down: float) -> None:
        self._last_down = last_down

    def set_player_already_store(self, player_already_store: bool) -> None:
        self._player_already_store = player_already_store

    def set_first_down_new_tetromino(self, first_down_new_tetromino: bool) -> None:
        self._first_down_new_tetromino = first_down_new_tetromino

    ###############################################################
    ######################## HAS_TO_GO_DOWN #######################
    ###############################################################
    def has_to_go_down(self) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne si le tétromino actuel doit faire un déplacement vers le bas
        # --> Oui si plus de (0.8 - (level - 1)*0.007)**(level - 1) secondes
        #     se sont écoulées depuis le derniers vers le bas
        #     (cf le guideline de Tetris)
        # =============================
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
        # - Regarder si le tétromino actif doit faire un mouvement vers le bas
        # - Si oui et qu'il peut :
        #   - Le descende
        # - Si non et que la partie est perdue :
        #   Exécuter les routines de la perte de la partie
        # - Sinon :
        #   Exécuter l'ensemble des routines quand un tétromino est placé (donc qu'il touche le sol)
        # =============================
        if self.has_to_go_down():
            self.set_last_down(time())
            if self.can_active_tetromino_move(Direction.DOWN):
                self.get_active_tetromino().move(Direction.DOWN)
                self.set_first_down_new_tetromino(False)
            elif self.is_game_lost():
                self.treat_game_lost()
            else:
                self.treat_tetromino_placed()

    ###############################################################
    ###################### TREAT_GAME_LOST ########################
    ###############################################################
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Exécute les routines de la perte de la partie :
    # - Découpe le tétromino actif pour qu'il puisse rentrer dans la grille à l'affichage final
    # - Passe au prochain tétromino (juste pour que le joueur puisse voir quel aurait été le suivant)
    # =============================
    def treat_game_lost(self):
        # Découpage du tétromino actif pour qu'il puisse rentrer dans l'affichage :

        # On monte le tétromino de sa hauteur
        # (comme ça on est sûr qu'il n'est plus en collision avec un bloc)
        for _ in range(self.get_active_tetromino().get_height()):
            self.get_active_tetromino().move(Direction.UP)

        # On regarde jusqu'où il peut descendre
        number_of_down = 0
        while self.can_active_tetromino_move(Direction.DOWN):
            number_of_down += 1
            self.get_active_tetromino().move(Direction.DOWN)

        # On le redescend complement
        for _ in range(self.get_active_tetromino().get_height() - number_of_down + 1):
            self.get_active_tetromino().move(Direction.DOWN)

        # On le découpe sur les parties qui ne s'afficheront pas
        for _ in range(self.get_active_tetromino().get_height() - number_of_down + 1):
            del self.get_active_tetromino().get_shape()[0]

        self.set_next_tetromino(random_next_tetromino())

    ###############################################################
    ################## TREAT_TETROMINO_PLACED ###################
    ###############################################################
    # =============================
    # INFORMATIONS :
    # -----------------------------
    # UTILITÉ :
    # Execute l'ensemble des routines quand un tétromino est placé (donc qu'il touche le sol)
    #   - Ajoute le tetromino actif à la grille
    #   - Passe au prochain tétromino
    #   - Génère un nouveau prochain tétromino
    #   - Passe _player_already_store à False
    #   - Regarde si des lignes ont été complétées
    #   - Ajoute les lignes complétées et les points engendrés aux statistiques
    # =============================
    def treat_tetromino_placed(self):
        self.get_grid().add_active_tetromino(self.get_active_tetromino())
        self.set_active_tetromino(ActiveTetromino(tetromino=self.get_next_tetromino()))
        self.set_next_tetromino(random_next_tetromino())
        self.set_first_down_new_tetromino(True)

        self.set_player_already_store(False)

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
        while line < self.get_active_tetromino().get_height() and possible:
            column = 0
            while column < self.get_active_tetromino().get_width() and possible:
                possible = (
                    not self.get_active_tetromino().is_occupied(x=column, y=line)  # Soit il n'y a pas de bloc
                    or  # ou
                    (  # Soit le bloc va aller dans les bordures de la grille ...
                        0 <= self.get_active_tetromino().get_x() + column + direction.value.get_x() < GRID_WIDTH
                        and
                        # Pas le 0 <= car le seul cas où on monte est quand on veut découper le tétromino actif à la fin
                        # de la partie et on peut que ça valide à ce moment là
                        self.get_active_tetromino().get_y() + line + direction.value.get_y() < GRID_HEIGHT
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
    ################ CAN_ACTIVE_TETROMINO_ROTATE ##################
    ###############################################################
    def can_active_tetromino_rotate(self, rotation: Rotation) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne si le tétromino actif peut effectuer la rotation
        # =============================
        possible = True

        # On crée une copie du tétromino actif pour ne pas modifier le vrai actif
        tetromino_after_rotation = ActiveTetromino(
            Tetromino(self.get_active_tetromino().copy_shape()),
            self.get_active_tetromino().get_x(),
            self.get_active_tetromino().get_y(),
        )
        tetromino_after_rotation.rotate(rotation)

        line = 0
        while line < self.get_active_tetromino().get_height() and possible:
            column = 0
            while column < self.get_active_tetromino().get_width() and possible:
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
                            tetromino_after_rotation.get_x() + column,
                            tetromino_after_rotation.get_y() + line
                        )
                    )
                )
                column += 1
            line += 1
        return possible

    ###############################################################
    ############# CAN_PLAYER_STORE_ACTIVE_TETROMINO ###############
    ###############################################################
    def can_player_store_active_tetromino(self) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # - Retourne si le joueur peut stocker le tétromino actif, donc que :
        #   - _can_player_switch est vrai
        #   - le tétromino stocké a la place de spawn
        # =============================
        possible = not self.get_player_already_store()
        # S'il n'y a pas de tétromino stocké, le tétromino stocké peut forcément être posé (puisqu'il ne sera pos posé)
        if possible and self.get_stored_tetromino() is None:
            return True

        # On sauvegarde la position
        position_sav = self.get_active_tetromino().get_position()
        # On intervertit les deux tétrominos et on regarde si ça marche puis on remet dans l'état original
        self.store_active_tetromino()
        possible = possible and self.can_active_tetromino_move(Direction.HERE)
        self.store_active_tetromino()
        self.get_active_tetromino().set_position(position_sav.get_x(), position_sav.get_y())  # On restaure la position
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
    ######################## IS_GAME_LOSE #########################
    ###############################################################
    def is_game_lost(self) -> bool:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # - Retourne si la partie est finie :
        #   - True si le tétromino actif ne peut pas bouger et qu'il avait spawn au dernier DOWN
        #   - False sinon
        # =============================
        return not self.can_active_tetromino_move(Direction.DOWN) and self.get_first_down_new_tetromino()


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
