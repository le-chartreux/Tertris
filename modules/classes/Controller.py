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
# + play()
# + do_tick()
# + treat_input_game_lost()
# + treat_input_game_not_lost()
# ==========================================================

from time import time, sleep

from modules.classes.Model import Model
from modules.classes.view.GameView import GameView
from modules.classes.view.TitleView import TitleView

from modules.classes.PlayerAction import PlayerAction
from modules.classes.Direction import Direction
from modules.classes.Rotation import Rotation


class Controller:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_model",
        "_game_view",
        "_title_view",
        "_continue_execution",
        "_loaded_view"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _model: Model
    _title_view: TitleView
    _game_view: GameView
    _continue_execution: bool
    _loaded_view: # TODO implementer

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
        # - s’il doit continuer à s'exécuter (_continue_program)
        # =============================
        self.set_model(Model())
        self.set_loaded_view(ViewName.NO_VIEW)
        self._continue_execution = True

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_model(self) -> Model:
        return self._model

    def get_game_view(self) -> GameView:
        return self._game_view

    def get_title_view(self) -> TitleView:
        return self._title_view

    def get_continue_execution(self) -> bool:
        return self._continue_execution

    def get_loaded_view(self):
        return self._loaded_view

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_model(self, model: Model) -> None:
        self._model = model

    def set_game_view(self, game_view: GameView) -> None:
        self._game_view = game_view

    def set_title_view(self, title_view: TitleView):
        self._title_view = title_view

    def set_continue_execution(self, continue_program: bool) -> None:
        self._continue_execution = continue_program

    def set_loaded_view(self, view_to_load) -> None:
        self._loaded_view = view_to_load

    ###############################################################
    ###################### SETUP_TITLE_VIEW #######################
    ###############################################################
    def print_title_view(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Setup la vue de titre (le modèle est déjà setup avec son __init__)
        # =============================
        self.set_title_view(TitleView())
        self.get_title_view().setup_static_windows()

    ###############################################################
    ####################### SETUP_GAME_VIEW #######################
    ###############################################################
    def setup_game_view(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Setup la vue de jeu
        # =============================
        self.set_game_view(GameView())
        self.get_game_view().setup_static_windows()

    ###############################################################
    ############################ PLAY #############################
    ###############################################################
    def play(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Execute le jeu tant que l'utilisateur ne demande pas de quitter
        # =============================
        while self.get_continue_execution():
            self.do_tick()
            sleep(0.05)

    ###############################################################
    ########################### DO_TICK ###########################
    ###############################################################
    def do_tick(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Execute l'ensemble des actions d'un tick.
        # =============================
        if self.get_model().is_game_lost():
            # Gestion des input du joueur inter-tick
            self.treat_input_game_lost()
            # Rien d'autre ne se passe
        else:
            # Gestion des input du joueur inter-tick
            self.treat_input_game_not_lost()

            # Gestion des actions normales du modèle :
            self.get_model().do_tick()

            # Actualisation de la vue :
            self.get_game_view().print_grid(self.get_model().get_grid())
            self.get_game_view().print_active_tetromino(self.get_model().get_active_tetromino())
            self.get_game_view().print_next(self.get_model().get_next_tetromino())
            self.get_game_view().print_stored(self.get_model().get_stored_tetromino())
            self.get_game_view().print_statistics(self.get_model().get_statistics())

    ###############################################################
    ################## TREAT_INPUT_GAME_LOST ######################
    ###############################################################
    def treat_input_game_lost(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Gère les input du joueur si la partie est perdue
        # =============================
        # La seule chose qu'il peut faire est quitter
        player_action = PlayerAction.MISSCLIC
        while player_action != PlayerAction.NOTHING:
            player_action = self.get_game_view().get_player_input()
            if player_action == PlayerAction.QUIT_GAME:
                self.set_continue_execution(False)

    ###############################################################
    ################# TREAT_INPUT_GAME_NOT_LOST ###################
    ###############################################################
    def treat_input_game_not_lost(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Gère les input du joueur si la partie n'est pas perdue
        # =============================

        # Tant qu'il peut y avoir des actions dans le buffer, on effectue les actions demandées si elles sont possibles
        player_action = PlayerAction.MISSCLIC
        while player_action != PlayerAction.NOTHING:
            player_action = self.get_game_view().get_player_input()

            # On gère le(s) missclic
            while player_action == PlayerAction.MISSCLIC:
                player_action = self.get_game_view().get_player_input()

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
                self.get_model().set_first_down_new_tetromino(False)

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
                    and self.get_model().can_player_store_active_tetromino()
            ):
                self.get_model().store_active_tetromino()
                self.get_model().set_player_already_store(True)

            # Pause
            elif player_action == PlayerAction.PAUSE_GAME:
                begin_of_the_pause = time()
                player_action = self.get_game_view().get_player_input()
                while player_action != PlayerAction.PAUSE_GAME and player_action != PlayerAction.QUIT_GAME:
                    player_action = self.get_game_view().get_player_input()
                    sleep(0.1)
                self.get_model().get_statistics().add_paused_time(time() - begin_of_the_pause)

            # Arrêt
            if player_action == PlayerAction.QUIT_GAME:
                self.set_continue_execution(False)
