# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe TitleView, qui gère la partie Vue du MVC
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + __del__()
# + GETTERS
# + SETTERS
# + set_backgrounds()
# + refresh_all()
# + print_logo()
# + print_buttons(active_button: int = 1)
# + print_bottom_texts()
# + get_player_input()
# + set_colorscheme() <- fonction
# + get_color_pair() <- fonction
# ==========================================================

import curses

from typing import Optional

from modules.classes.PlayerAction import PlayerAction
from modules.classes.view.view_utilities import set_colorscheme, get_color_pair

from modules.settings import (
    TITLE_VIEW_LOGO_BEGIN_X,
    TITLE_VIEW_LOGO_BEGIN_Y,
    TITLE_VIEW_LOGO_WIDTH,
    TITLE_VIEW_LOGO_HEIGHT
)


class TitleView:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_window_all",
        "_window_logo",
        "_window_buttons",
        "_window_bottom_texts"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    # Since the curses module puts the _CursesWindow class private, I had
    # to declare them as objects :/
    _window_all: object
    _window_logo: object
    _window_buttons: object
    _window_bottom_texts: object

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
        # Crée un objet TitleView, caractérisé par :
        # - une fenêtre de tout le terminal (_window_all)
        # - une fenêtre contenant le logo (_window_logo)
        # - une fenêtre contenant les boutons de l'écran titre (_window_buttons)
        # - une fenêtre contenant les textes en bas de l'écran titre (_window_bottom_texts)
        # Et le paramètre pour qu'il soit capable de gérer la partie
        # -----------------------------
        # REMARQUES :
        # - Fermer le programme sans qu'il puisse appeler le destructeur d'une instance peut dérégler le terminal de
        #   l'utilisateur !
        # =============================
        window_all = curses.initscr()

        # Paramétrage de curses
        curses.curs_set(False)  # Ne pas afficher le curseur
        curses.noecho()  # Ne pas afficher ce que marque l'utilisateur
        curses.cbreak()  # Ne pas attendre que l'utilisateur appui sur Entrée pour récupérer son entrée

        self.set_window_all(window_all)

        self.set_window_game(
            curses.newwin(
                TITLE_VIEW_LOGO_HEIGHT,
                TITLE_VIEW_LOGO_WIDTH,
                TITLE_VIEW_LOGO_BEGIN_Y,
                TITLE_VIEW_LOGO_BEGIN_X
            )
        )

        # Paramétrage de _window_all pour les entrées texte
        self.get_window_all().nodelay(True)  # Ne pas attendre l'entrée d'un utilisateur à l'appel d'un getch()
        self.get_window_all().keypad(True)  # Permettre la compatibilité avec les touches spéciales (arrow-up par ex)

        # Gestion des couleurs
        set_colorscheme()
        self.set_backgrounds()

    ###############################################################
    ########################### __DEL__ ###########################
    ###############################################################
    def __del__(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Détruit proprement l'instance et remet le terminal de l'utilisateur dans son état original
        # =============================
        curses.curs_set(True)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_window_all(self) -> object:
        return self._window_all

    def get_window_logo(self) -> object:
        return self._window_logo

    def get_window_buttons(self) -> object:
        return self._window_buttons

    def get_window_bottom_texts(self) -> object:
        return self._window_bottom_texts

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_window_all(self, window_all) -> None:
        self._window_all = window_all

    def set_window_game(self, window_logo) -> None:
        self._window_logo = window_logo

    def set_window_next(self, window_buttons) -> None:
        self._window_buttons = window_buttons

    def set_window_stored(self, window_bottom_texts) -> None:
        self._window_bottom_texts = window_bottom_texts

    ###############################################################
    ####################### SET_BACKGROUNDS #######################
    ###############################################################
    def set_backgrounds(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Met les fonds d'écran des différentes fenêtres de la bonne couleur
        # -----------------------------
        # PRÉCONDITIONS :
        # - set_colorscheme() a déjà été appelé
        # =============================
        self.get_window_all().bkgd(' ', curses.color_pair(8))
        self.get_window_logo().bkgd(' ', curses.color_pair(8))
        self.get_window_buttons().bkgd(' ', curses.color_pair(8))
        self.get_window_bottom_texts().bkgd(' ', curses.color_pair(8))

        self.refresh_all()

    ###############################################################
    ######################## REFRESH_ALL ##########################
    ###############################################################
    def refresh_all(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Actualise toutes les fenêtres
        # -----------------------------
        # PRÉCONDITIONS :
        # - Toutes les fenêtres existent
        # =============================
        self.get_window_all().refresh()
        self.get_window_logo().refresh()
        self.get_window_buttons().refresh()
        self.get_window_bottom_texts().refresh()

    ###############################################################
    ##################### SETUP_STATIC_WINDOWS ####################
    ###############################################################
    def setup_static_windows(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Charge les fenêtres qui ne bougent pas (donc toutes sauf les boutons)
        # =============================
        self.print_logo()
        self.print_bottom_texts()

    ###############################################################
    ########################## PRINT_LOGO #########################
    ###############################################################
    def print_logo(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche le logo
        # =============================
        # Première ligne
        self.get_window_logo().addstr(0, 11, "▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌", curses.color_pair(9))
        # Deuxième ligne
        self.get_window_logo().addstr(1, 0, "▄", curses.color_pair(10))
        self.get_window_logo().addstr(1, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(1, 11,  "▛▀▀▀▀▜▐▀▀▀▀▜ ▛▀▀▀▀▌▛▀▀▀▀▜▐▀▀▀▀▜ ▛▜▐▀▀▀▀▀▌", curses.color_pair(11))
        self.get_window_logo().addstr(1, 53, "▌", curses.color_pair(9))

        # Troisième ligne
        self.get_window_logo().addstr(2, 0, "▀█▄", curses.color_pair(10))
        self.get_window_logo().addstr(2, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(2, 11, "▙▄▖▗▄▟▐   ▗▘ ▌▗▄▖▐ ▙▄▖▗▄▟▐ ▄▄ ▌ ▙▟▐    ▐ ", curses.color_pair(11))
        self.get_window_logo().addstr(2, 53, "▌", curses.color_pair(9))

        # Quatrième ligne
        self.get_window_logo().addstr(3, 1, "▀█▄", curses.color_pair(10))
        self.get_window_logo().addstr(3, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(3, 11, "  ▌▐  ▐ ▐▀▀  ▌▐▗▘▌   ▌▐  ▐ ▌▞▐  ▄▄▐  ▐▀▌ ", curses.color_pair(11))
        self.get_window_logo().addstr(3, 53, "▌", curses.color_pair(9))

        # Cinquième ligne
        self.get_window_logo().addstr(4, 2, "▀█▄", curses.color_pair(10))
        self.get_window_logo().addstr(4, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(4, 11, "  ▌▐  ▐ ▝▀▜  ▌▐▘▞    ▌▐  ▐ ▛▗▘  ▌▐ ▌  ▌  ", curses.color_pair(11))
        self.get_window_logo().addstr(4, 53, "▌", curses.color_pair(9))

        # Sixième ligne
        self.get_window_logo().addstr(5, 3, "▀█▄", curses.color_pair(10))
        self.get_window_logo().addstr(5, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(5, 11, "  ▌▐  ▐   ▌  ▌▐▚▝▖   ▌▐  ▐ ▛▖▚  ▌▐ ▐  ▐  ", curses.color_pair(11))
        self.get_window_logo().addstr(5, 53, "▌", curses.color_pair(9))

        # Septième ligne
        self.get_window_logo().addstr(6, 4, "▀█▄", curses.color_pair(10))
        self.get_window_logo().addstr(6, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(6, 11, "  ▌▐  ▐ ▐▀   ▌▐ ▌▐   ▌▐  ▐ ▌▐ ▌ ▌▐  ▌  ▌ ", curses.color_pair(11))
        self.get_window_logo().addstr(6, 53, "▌", curses.color_pair(9))

        # Huitième ligne
        self.get_window_logo().addstr(7, 5, "▀█▄", curses.color_pair(10))
        self.get_window_logo().addstr(7, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(7, 11, "  ▌▐  ▐ ▐    ▌▐ ▐ ▌  ▌▐  ▐ ▌ ▌▐ ▌▐  ▐  ▐ ", curses.color_pair(11))
        self.get_window_logo().addstr(7, 53, "▌", curses.color_pair(9))

        # Neuvième ligne
        self.get_window_logo().addstr(8, 6, "▀█▄", curses.color_pair(10))
        self.get_window_logo().addstr(8, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(8, 11, "  ▌▐  ▐ ▐▄▄▖ ▌▐  ▌▐  ▌▐  ▐ ▌ ▐ ▌▌▐▐▄▄▌  ▌", curses.color_pair(11))
        self.get_window_logo().addstr(8, 53, "▌", curses.color_pair(9))

        # Dixième ligne
        self.get_window_logo().addstr(9, 6, "▀█▄", curses.color_pair(10))
        self.get_window_logo().addstr(9, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(9, 11, "  ▌▐  ▐    ▐ ▌▐  ▐ ▌ ▌▐  ▐ ▌  ▌▐▌▐▐     ▌", curses.color_pair(11))
        self.get_window_logo().addstr(9, 53, "▌", curses.color_pair(9))

        # Onzième ligne
        self.get_window_logo().addstr(10, 6, "▀█▄", curses.color_pair(10))
        self.get_window_logo().addstr(10, 11, "▌", curses.color_pair(9))
        self.get_window_logo().addstr(10, 11, "  ▙▟  ▐▄▄▄▄▄▌▙▟   ▙▟ ▙▟  ▐▄▌  ▐▄█▟▐▄▄▄▄▄▌", curses.color_pair(11))
        self.get_window_logo().addstr(10, 53, "▌", curses.color_pair(9))



        self.get_window_game().refresh()

    ###############################################################
    ##################### PRINT_BOTTOM_TEXTS ######################
    ###############################################################
    def print_buttons(self, active_button: int) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche les boutons, avec l'actif en surbrillance
        # =============================
        pass

    ###############################################################
    ##################### PRINT_BOTTOM_TEXTS ######################
    ###############################################################
    def print_bottom_texts(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche les texts en bas de l'écran
        # =============================
        pass

    ###############################################################
    ###################### GET_PLAYER_INPUT #######################
    ###############################################################
    def get_player_input(self) -> PlayerAction:
        player_input = self.get_window_all().getch()
        if player_input == curses.ERR:
            return PlayerAction.NOTHING
        if player_input == curses.KEY_LEFT:
            return PlayerAction.MOVE_ACTIVE_TETROMINO_LEFT
        elif player_input == curses.KEY_RIGHT:
            return PlayerAction.MOVE_ACTIVE_TETROMINO_RIGHT
        elif player_input == curses.KEY_DOWN:
            return PlayerAction.MOVE_ACTIVE_TETROMINO_DOWN
        elif player_input == 81 or player_input == 113:  # Q ou q
            return PlayerAction.ROTATE_ACTIVE_TETROMINO_LEFT
        elif player_input == 68 or player_input == 100:  # D ou d
            return PlayerAction.ROTATE_ACTIVE_TETROMINO_RIGHT
        elif player_input == 27:  # Esc
            return PlayerAction.QUIT_GAME
        elif player_input == 80 or player_input == 112:  # P ou p
            return PlayerAction.PAUSE_GAME
        elif player_input == 83 or player_input == 115:  # S ou s
            return PlayerAction.STORE_ACTIVE_TETROMINO
        else:
            return PlayerAction.MISSCLIC
