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
# ==========================================================

from modules.classes.model.Model import Model
from modules.classes.view.View import View

from modules.classes.commons.PlayerAction import PlayerAction
from modules.classes.commons.Direction import Direction
from modules.classes.commons.Rotation import Rotation


class Controller:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_model",
        "_view"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _model: Model
    _view: View

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

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_model(self) -> Model:
        return self._model

    def get_view(self) -> View:
        return self._view

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_model(self, model: Model) -> None:
        self._model = model

    def set_view(self, view: View) -> None:
        self._view = view

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
        # Execute l'ensemble des actions d'un tick
        # =============================
        # Gestion des actions du joueur
        player_action = PlayerAction.MISSCLIC
        # On gère le(s) missclic
        while player_action != PlayerAction.NOTHING:
            player_action = self.get_view().get_player_input()

            while player_action == PlayerAction.MISSCLIC:
                player_action = self.get_view().get_player_input()

            if player_action == PlayerAction.QUIT_GAME:
                exit()
            # Déplacements
            elif (
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
            elif player_action == PlayerAction.ROTATE_ACTIVE_TETROMINO_RIGHT:
                self.get_model().get_active_tetromino().rotate(Rotation.RIGHT)
            elif player_action == PlayerAction.ROTATE_ACTIVE_TETROMINO_LEFT:
                self.get_model().get_active_tetromino().rotate(Rotation.LEFT)

        # Gestion des actions normales du modèle :
        self.get_model().do_tick()

        # Actualisation de la vue :
        self.get_view().print_grid(self.get_model().get_grid())
        self.get_view().print_active_tetromino(self.get_model().get_active_tetromino())
        self.get_view().print_next(self.get_model().get_next_tetromino())
        self.get_view().print_stored(self.get_model().get_stored_tetromino())
        self.get_view().print_statistics(self.get_model().get_statistics())

