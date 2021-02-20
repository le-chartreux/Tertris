# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Controller
# ==========================================================

from time import time, sleep
from typing import Optional

from modules.model import Model

from modules.view.game_view import GameView
from modules.direction import Direction
from modules.rotation import Rotation

from modules.view.title_view import TitleView
from modules.player_input import PlayerInput
import modules.view.title_view.config as config_title_view


class Controller:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_model",
        "_continue_execution",
        "_title_view",
        "_game_view"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _model: Model
    _continue_execution: bool
    _title_view: Optional[TitleView]
    _game_view: Optional[GameView]

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
        self.set_title_view(TitleView())
        self.set_game_view(None)

        self._continue_execution = True

        # On met en place la vue
        self.get_title_view().setup()
        self.get_title_view().print_without_parameter_windows()

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_model(self) -> Model:
        return self._model

    def get_continue_execution(self) -> bool:
        return self._continue_execution

    def get_title_view(self) -> Optional[TitleView]:
        return self._title_view

    def get_game_view(self) -> Optional[GameView]:
        return self._game_view

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_model(self, model: Model) -> None:
        self._model = model

    def set_continue_execution(self, continue_program: bool) -> None:
        self._continue_execution = continue_program

    def set_title_view(self, title_view: Optional[TitleView]) -> None:
        self._title_view = title_view

    def set_game_view(self, game_view: Optional[GameView]) -> None:
        self._game_view = game_view

    ###############################################################
    ###################### SWITCH_LOADED_VIEW #####################
    ###############################################################
    def switch_loaded_view(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Switch la vue : puisque de seule une vue peut exister, il faut supprimer l'autre
        # =============================
        if self.get_title_view() is None:
            self.get_game_view().__del__()
            self.set_title_view(TitleView())
            self.set_game_view(None)
        elif self.get_game_view() is None:
            self.get_title_view().__del__()
            self.set_title_view(None)
            self.set_game_view(GameView())

    ###############################################################
    ############################ RUN ##############################
    ###############################################################
    def run(self):
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
        if self.get_game_view() is not None:
            if self.get_model().is_game_lost():
                # Gestion des input du joueur inter-tick
                self.treat_action_game_lost()
                # Rien d'autre ne se passe
            else:
                # Gestion des input du joueur inter-tick
                self.treat_action_game_not_lost()

                # Gestion des actions normales du modèle :
                self.get_model().do_tick()

                # Actualisation de la vue :
                self.get_game_view().print_grid(self.get_model().get_grid())
                self.get_game_view().print_active_tetromino(self.get_model().get_active_tetromino())
                self.get_game_view().print_next(self.get_model().get_next_tetromino())
                self.get_game_view().print_stored(self.get_model().get_stored_tetromino())
                self.get_game_view().print_statistics(self.get_model().get_statistics())

        elif self.get_title_view() is not None:
            self.treat_action_title_screen()

    ###############################################################
    ################ TREAT_ACTION_TITLE_SCREEN ####################
    ###############################################################
    def treat_action_title_screen(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Gère les input du joueur sur l'écran titre
        # =============================
        player_input = PlayerInput.KEY_UNUSED
        while player_input != PlayerInput.NOTHING:
            player_input = self.get_title_view().get_player_input()
            # On gère les missclicks
            while player_input == PlayerInput.KEY_UNUSED:
                player_input = self.get_title_view().get_player_input()

            # Entrée
            if player_input in (PlayerInput.KEY_ENTER_1, PlayerInput.KEY_ENTER_2, PlayerInput.KEY_ENTER_3):
                active_button = self.get_title_view().get_highlighted_button()
                if active_button == config_title_view.BUTTON_START:
                    self.switch_loaded_view()
                    self.get_game_view().setup()
                    self.get_game_view().print_without_parameter_windows()
                    player_input = PlayerInput.NOTHING
                elif active_button == config_title_view.BUTTON_OPTIONS:
                    pass  # TODO implémenter la vue d'options
                elif active_button == config_title_view.BUTTON_HIGH_SCORES:
                    pass  # TODO implémenter la vue des meilleurs scores
                elif active_button == config_title_view.BUTTON_QUIT:
                    self.set_continue_execution(False)

            # Touches directionnelles
            if player_input == PlayerInput.KEY_UP:
                self.get_title_view().set_highlighted_button(
                    self.get_title_view().get_button(Direction.UP)
                )
                self.get_title_view().print_buttons()
            elif player_input == PlayerInput.KEY_DOWN:
                self.get_title_view().set_highlighted_button(
                    self.get_title_view().get_button(Direction.DOWN)
                )
                self.get_title_view().print_buttons()

            # Esc
            elif player_input == PlayerInput.KEY_ESC:
                self.set_continue_execution(False)

    ###############################################################
    ################## TREAT_ACTION_GAME_LOST #####################
    ###############################################################
    def treat_action_game_lost(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Gère les input du joueur si la partie est perdue
        # =============================
        # La seule chose qu'il peut faire est quitter
        player_input = PlayerInput.KEY_UNUSED
        while player_input != PlayerInput.NOTHING:
            player_input = self.get_game_view().get_player_input()
            if player_input == PlayerInput.KEY_ESC:
                self.set_continue_execution(False)

    ###############################################################
    ################ TREAT_ACTION_GAME_NOT_LOST ###################
    ###############################################################
    def treat_action_game_not_lost(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Gère les input du joueur si la partie n'est pas perdue
        # =============================
        # Tant qu'il peut y avoir des actions dans le buffer, on effectue les actions demandées si elles sont possibles
        player_input = PlayerInput.KEY_UNUSED
        while player_input != PlayerInput.NOTHING:
            player_input = self.get_game_view().get_player_input()
            # On gère les missclicks
            while player_input == PlayerInput.KEY_UNUSED:
                player_input = self.get_game_view().get_player_input()

            # Déplacements
            if (
                    player_input == PlayerInput.KEY_RIGHT
                    and self.get_model().can_active_tetromino_move(Direction.RIGHT)
            ):
                self.get_model().get_active_tetromino().move(Direction.RIGHT)
            elif (
                    player_input == PlayerInput.KEY_LEFT
                    and self.get_model().can_active_tetromino_move(Direction.LEFT)
            ):
                self.get_model().get_active_tetromino().move(Direction.LEFT)
            elif (
                    player_input == PlayerInput.KEY_DOWN
                    and self.get_model().can_active_tetromino_move(Direction.DOWN)
            ):
                self.get_model().get_active_tetromino().move(Direction.DOWN)
                self.get_model().set_first_down_new_tetromino(False)

            # Rotations
            elif (
                    player_input == PlayerInput.KEY_D
                    and self.get_model().can_active_tetromino_rotate(Rotation.RIGHT)
            ):
                self.get_model().get_active_tetromino().rotate(Rotation.RIGHT)
            elif (
                    player_input == PlayerInput.KEY_Q
                    and self.get_model().can_active_tetromino_rotate(Rotation.LEFT)
            ):
                self.get_model().get_active_tetromino().rotate(Rotation.LEFT)

            # Stockage
            elif (
                    player_input == PlayerInput.KEY_S
                    and self.get_model().can_player_store_active_tetromino()
            ):
                self.get_model().store_active_tetromino()
                self.get_model().set_player_already_store(True)

            # Pause
            elif player_input == PlayerInput.KEY_P:
                begin_of_the_pause = time()
                player_input = self.get_game_view().get_player_input()
                while player_input != PlayerInput.KEY_P and player_input != PlayerInput.KEY_ESC:
                    player_input = self.get_game_view().get_player_input()
                    sleep(0.1)
                # on fait en sorte que le temps de pause ne soit pas comptabilisé
                self.get_model().get_statistics().add_paused_time(time() - begin_of_the_pause)

            # Arrêt
            if player_input == PlayerInput.KEY_ESC:
                self.set_continue_execution(False)
