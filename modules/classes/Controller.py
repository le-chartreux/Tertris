# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Controller
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + setup()
# + do_tick()
# ==========================================================

from time import sleep

from modules.classes.Model import Model
from modules.classes.View import View

from modules.classes.PlayerAction import PlayerAction
from modules.classes.Direction import Direction
from modules.classes.Rotation import Rotation


class Controller:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_model",
        "_view",
        "_continue_game"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _model: Model
    _view: View
    _continue_game: bool

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Controller, caractérisé par :
        # - son model (_model)
        # - sa vue (_view)
        # =============================
        self.set_model(Model())
        self.set_view(View())
        self._continue_game = True

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_model(self) -> Model:
        return self._model

    def get_view(self) -> View:
        return self._view

    def get_continue_game(self) -> bool:
        return self._continue_game

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_model(self, model: Model) -> None:
        self._model = model

    def set_view(self, view: View) -> None:
        self._view = view

    def set_continue_game(self, continue_game: bool) -> None:
        self._continue_game = continue_game

    ###############################################################
    ############################ SETUP ############################
    ###############################################################
    def setup(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Setup la vue (le modèle est déjà setup avec son __init__)
        # =============================
        self.get_view().setup_static_windows()

    ###############################################################
    ########################### DO_TICK ###########################
    ###############################################################
    def do_tick(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Execute l'ensemble des actions d'un tick.
        # Retourne s’il faut continuer ou non
        # =============================

        # Gestion des actions du joueur
        player_action = PlayerAction.MISSCLIC
        while player_action != PlayerAction.NOTHING:
            player_action = self.get_view().get_player_input()

            # On gère le(s) missclic
            while player_action == PlayerAction.MISSCLIC:
                player_action = self.get_view().get_player_input()

            # Déplacements
            if (
                    player_action == PlayerAction.MOVE_ACTIVE_TETROMINO_RIGHT
                    and self.get_model().can_active_tetromino_move(Direction.RIGHT)
            ):
                self.get_model().get_active_tetromino().move(Direction.RIGHT)
            elif (
                    player_action == PlayerAction.MOVE_ACTIVE_TETROMINO_LEFT
                    and self.get_model().can_active_tetromino_move(Direction.LEFT)
            ):
                self.get_model().get_active_tetromino().move(Direction.LEFT)
            elif (
                    player_action == PlayerAction.MOVE_ACTIVE_TETROMINO_DOWN
                    and self.get_model().can_active_tetromino_move(Direction.DOWN)
            ):
                self.get_model().get_active_tetromino().move(Direction.DOWN)

            # Rotations
            elif (
                    player_action == PlayerAction.ROTATE_ACTIVE_TETROMINO_RIGHT
                    and self.get_model().can_active_tetromino_rotate(Rotation.RIGHT)
            ):
                self.get_model().get_active_tetromino().rotate(Rotation.RIGHT)
            elif (
                    player_action == PlayerAction.ROTATE_ACTIVE_TETROMINO_LEFT
                    and self.get_model().can_active_tetromino_rotate(Rotation.LEFT)
            ):
                self.get_model().get_active_tetromino().rotate(Rotation.LEFT)

            # Stockage
            elif (
                    player_action == PlayerAction.STORE_ACTIVE_TETROMINO
                    and self.get_model().get_can_player_switch()
            ):
                self.get_model().store_active_tetromino()
                self.get_model().set_can_player_switch(False)

            # Pause
            elif player_action == PlayerAction.PAUSE_GAME:
                player_action = self.get_view().get_player_input()
                while player_action != PlayerAction.PAUSE_GAME and player_action != PlayerAction.QUIT_GAME:
                    player_action = self.get_view().get_player_input()
                    sleep(0.1)

            # Arrêt
            if player_action == PlayerAction.QUIT_GAME:
                self._continue_game = False

        # Gestion des actions normales du modèle :
        self.get_model().do_tick()

        # Actualisation de la vue :
        self.get_view().print_grid(self.get_model().get_grid())
        self.get_view().print_active_tetromino(self.get_model().get_active_tetromino())
        self.get_view().print_next(self.get_model().get_next_tetromino())
        self.get_view().print_stored(self.get_model().get_stored_tetromino())
        self.get_view().print_statistics(self.get_model().get_statistics())
