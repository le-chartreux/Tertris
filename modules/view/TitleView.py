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
# + GETTERS
# + SETTERS
# + set_backgrounds()
# + refresh_all()
# + print_without_parameter_windows()
# + print_logo()
# + print_buttons()
# + print_bottom_texts()
# + get_button_name()
# ==========================================================

import curses
import locale

from modules.view.View import View
from modules.ButtonName import ButtonName

from modules.Direction import Direction

from modules.settings import (
    TITLE_VIEW_LOGO_BEGIN_X,
    TITLE_VIEW_LOGO_BEGIN_Y,
    TITLE_VIEW_LOGO_WIDTH,
    TITLE_VIEW_LOGO_HEIGHT,

    TITLE_VIEW_BUTTONS_BEGIN_X,
    TITLE_VIEW_BUTTONS_BEGIN_Y,
    TITLE_VIEW_BUTTONS_WIDTH,
    TITLE_VIEW_BUTTONS_HEIGHT,

    TITLE_VIEW_TEXTS_BEGIN_X,
    TITLE_VIEW_TEXTS_BEGIN_Y,
    TITLE_VIEW_TEXTS_WIDTH,
    TITLE_VIEW_TEXTS_HEIGHT
)


class TitleView(View):
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_window_logo",
        "_window_buttons",
        "_window_bottom_texts",
        "_highlighted_button"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    # Since the curses module puts the _CursesWindow class private, I had
    # to declare them as objects :/
    _window_logo: object
    _window_buttons: object
    _window_bottom_texts: object
    _highlighted_button: ButtonName

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            highlighted_button: ButtonName = ButtonName.START
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet TitleView, héritant de View, ajoutant :
        # - une fenêtre contenant le logo (_window_logo)
        # - une fenêtre contenant les boutons de l'écran titre (_window_buttons)
        # - une fenêtre contenant les textes en bas de l'écran titre (_window_bottom_texts)
        # Et le paramètre pour qu'il soit capable de gérer la partie
        # -----------------------------
        # REMARQUES :
        # - Se referer aux remarques de View
        # =============================
        View.__init__(self)

        self.set_window_logo(
            curses.newwin(
                TITLE_VIEW_LOGO_HEIGHT,
                TITLE_VIEW_LOGO_WIDTH,
                TITLE_VIEW_LOGO_BEGIN_Y,
                TITLE_VIEW_LOGO_BEGIN_X
            )
        )

        self.set_window_buttons(
            curses.newwin(
                TITLE_VIEW_BUTTONS_HEIGHT,
                TITLE_VIEW_BUTTONS_WIDTH,
                TITLE_VIEW_BUTTONS_BEGIN_Y,
                TITLE_VIEW_BUTTONS_BEGIN_X
            )
        )

        self.set_window_texts(
            curses.newwin(
                TITLE_VIEW_TEXTS_HEIGHT,
                TITLE_VIEW_TEXTS_WIDTH,
                TITLE_VIEW_TEXTS_BEGIN_Y,
                TITLE_VIEW_TEXTS_BEGIN_X
            )
        )

        self.set_highlighted_button(highlighted_button)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_window_logo(self) -> object:
        return self._window_logo

    def get_window_buttons(self) -> object:
        return self._window_buttons

    def get_window_bottom_texts(self) -> object:
        return self._window_bottom_texts

    def get_highlighted_button(self) -> ButtonName:
        return self._highlighted_button

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_window_logo(self, window_logo) -> None:
        self._window_logo = window_logo

    def set_window_buttons(self, window_buttons) -> None:
        self._window_buttons = window_buttons

    def set_window_texts(self, window_bottom_texts) -> None:
        self._window_bottom_texts = window_bottom_texts

    def set_highlighted_button(self, highlighted_button: ButtonName):
        self._highlighted_button = highlighted_button

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
        View.set_backgrounds(self)
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
        View.refresh_all(self)
        self.get_window_logo().refresh()
        self.get_window_buttons().refresh()
        self.get_window_bottom_texts().refresh()

    ###############################################################
    ############## PRINT_WITHOUT_PARAMETER_WINDOWS ################
    ###############################################################
    def print_without_parameter_windows(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche toutes les fenêtres qui n'ont pas besoin de paramètres
        # =============================
        self.print_logo()
        self.print_bottom_texts()
        self.print_buttons()

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
        # Ligne 0
        self.get_window_logo().addstr(
            0, 11,
            "▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            0, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 1
        # début du >
        self.get_window_logo().addstr(
            1, 0,
            "▄".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        # bordure gauche
        self.get_window_logo().addstr(
            1, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        # début du T
        self.get_window_logo().addstr(
            1, 12,
            "▛▀▀▀▀▜".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        # début du E
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            "▀▀▀▀▜".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(11)
        )
        # début du R
        self.get_window_logo().addstr(
            "▛▀▀▀▀".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        # début du T
        self.get_window_logo().addstr(
            "▛▀▀▀▀▜".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        # début du deuxième R
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            "▀▀▀▀▜".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            " ",
            curses.color_pair(11)
        )
        # début du I
        self.get_window_logo().addstr(
            "▛▜".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        # début du S
        self.get_window_logo().addstr(
            "▐",
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            "▀▀▀▀▀".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        # bordure droite
        self.get_window_logo().addstr(
            1, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 2
        # début du >
        self.get_window_logo().addstr(
            2, 0,
            "▀█▄".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        # bordure gauche
        self.get_window_logo().addstr(
            2, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        # début du T
        self.get_window_logo().addstr(
            2, 12,
            "▙▄▖▗▄▟".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        # début du E
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            "   ▗".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            "▘ ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        # début du R
        self.get_window_logo().addstr(
            "▌▗▄▖▐".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            " ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        # début du deuxième T
        self.get_window_logo().addstr(
            "▙▄▖▗▄▟".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        # début du deuxième R
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            " ▄▄ ".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            "▌ ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        # début du I
        self.get_window_logo().addstr(
            "▙▟".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        # début du S
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            "    ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            " ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        # bordure droite
        self.get_window_logo().addstr(
            2, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 3
        # début du >
        self.get_window_logo().addstr(
            3, 2,
            "▀█▄".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        # bordure gauche
        self.get_window_logo().addstr(
            3, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            3, 12,
            "  ",
            curses.color_pair(11)
        )
        # début du T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        # début du E
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            " ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            "▀▀".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            "  ",
            curses.color_pair(11)
        )
        # début du R
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            "▗".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            "▘".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            "▌   ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        # début du deuxième T
        self.get_window_logo().addstr(
            "▌▐".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        # début du deuxième R
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            " ".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            "▌▟".encode(locale.getpreferredencoding()),  # on devrait afficher ▌▞ mais ça pose problème
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            "▐".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        # I et début du S
        self.get_window_logo().addstr(
            "  ▄▄▐".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            "  ▐".encode(locale.getpreferredencoding()),
            curses.color_pair(12)
        )
        self.get_window_logo().addstr(
            "▀▌ ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        # bordure droite
        self.get_window_logo().addstr(
            3, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 4 TODO continuer le coloriage
        self.get_window_logo().addstr(
            4, 4,
            "▀█▄".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        self.get_window_logo().addstr(
            4, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            4, 12,
            "  ▌▐  ▐ ▝▀▜  ▌▐▘▞    ▌▐  ▐ ▛▗▘  ▌▐ ▌  ▌  ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            4, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 5
        self.get_window_logo().addstr(
            5, 6,
            "▀█▄".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        self.get_window_logo().addstr(
            5, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            5, 12,
            "  ▌▐  ▐   ▌  ▌▐▚▝▖   ▌▐  ▐ ▛▖▚  ▌▐ ▐  ▐  ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            5, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 6
        self.get_window_logo().addstr(
            6, 6,
            "▄█▀".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        self.get_window_logo().addstr(
            6, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            6, 12,
            "  ▌▐  ▐ ▐▀   ▌▐ ▌▐   ▌▐  ▐ ▌▐ ▌ ▌▐  ▌  ▌ ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            6, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 7
        self.get_window_logo().addstr(
            7, 4,
            "▄█▀".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        self.get_window_logo().addstr(
            7, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            7, 12,
            "  ▌▐  ▐ ▐    ▌▐ ▐ ▌  ▌▐  ▐ ▌ ▌▐ ▌▐  ▐  ▐ ".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            7, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 8
        self.get_window_logo().addstr(
            8, 2,
            "▄█▀".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        self.get_window_logo().addstr(
            8, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            8, 12,
            "  ▌▐  ▐ ▐▄▄▖ ▌▐  ▌▐  ▌▐  ▐ ▌ ▐ ▌▌▐▐▄▄▌  ▌".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            8, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 9
        self.get_window_logo().addstr(
            9, 0,
            "▄█▀".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        self.get_window_logo().addstr(
            9, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            9, 12,
            "  ▌▐  ▐    ▐ ▌▐  ▐ ▌ ▌▐  ▐ ▌  ▌▐▌▐▐     ▌".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            9, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 10
        self.get_window_logo().addstr(
            10, 0,
            "▀".encode(locale.getpreferredencoding()),
            curses.color_pair(10)
        )
        self.get_window_logo().addstr(
            10, 11,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            10, 12,
            "  ▙▟  ▐▄▄▄▄▄▌▙▟   ▙▟ ▙▟  ▐▄▌  ▐▄█▟▐▄▄▄▄▄▌".encode(locale.getpreferredencoding()),
            curses.color_pair(11)
        )
        self.get_window_logo().addstr(
            10, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Ligne 11
        self.get_window_logo().addstr(
            11, 11,
            "▙▄▄▄▄▄▄▄▄▄▄▄▄▄▖             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            11, 53,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        # Lignes 12 à 22
        for line in range(12, 23):
            self.get_window_logo().addstr(
                line, 25,
                "▌             ".encode(locale.getpreferredencoding()),
                curses.color_pair(9)
            )
            self.get_window_logo().addstr(
                line, 39,
                "▌".encode(locale.getpreferredencoding()),
                curses.color_pair(6)
            )

        # Ligne 23
        self.get_window_logo().addstr(
            23, 25,
            "▙▄▄▄▄▄▄▄▄▄▄▄▄▄".encode(locale.getpreferredencoding()),
            curses.color_pair(9)
        )
        self.get_window_logo().addstr(
            23, 39,
            "▌".encode(locale.getpreferredencoding()),
            curses.color_pair(6)
        )

        self.get_window_logo().refresh()

    ###############################################################
    ######################## PRINT_BUTTONS ########################
    ###############################################################
    def print_buttons(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche les boutons, avec l'actif en surbrillance
        # =============================
        color_for_start = curses.color_pair(11)
        color_for_options = curses.color_pair(11)
        color_for_high_scores = curses.color_pair(11)
        color_for_quit = curses.color_pair(11)
        if self._highlighted_button == ButtonName.START:
            color_for_start = curses.color_pair(4)
        elif self._highlighted_button == ButtonName.OPTIONS:
            color_for_options = curses.color_pair(4)
        elif self._highlighted_button == ButtonName.HIGH_SCORES:
            color_for_high_scores = curses.color_pair(4)
        elif self._highlighted_button == ButtonName.QUIT:
            color_for_quit = curses.color_pair(4)

        self.get_window_buttons().addstr(0, 3, "START", color_for_start)
        self.get_window_buttons().addstr(2, 2, "OPTIONS", color_for_options)
        self.get_window_buttons().addstr(4, 0, "HIGH SCORES", color_for_high_scores)
        self.get_window_buttons().addstr(6, 3, "QUIT", color_for_quit)

        self.get_window_buttons().refresh()

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
        self.get_window_bottom_texts().addstr(
            0, 0,
            "Tertris is a Tetris © clone made by VMoM, under MIT License".encode(locale.getpreferredencoding()),
            curses.color_pair(4)
        )
        self.get_window_bottom_texts().addstr(
            1, 12,
            "Tetris © 1985~2021 Tetris Holding.".encode(locale.getpreferredencoding()),
            curses.color_pair(4)
        )
        self.get_window_bottom_texts().addstr(
            2, 4,
            "Tetris logos, Tetris theme song and Tetriminos are",
            curses.color_pair(4)
        )
        self.get_window_bottom_texts().addstr(
            3, 15,
            "trademarks of Tetris Holding.",
            curses.color_pair(4)
        )
        self.get_window_bottom_texts().addstr(
            4, 4,
            "The Tetris trade dress is owned by Tetris Holding.",
            curses.color_pair(4)
        )
        self.get_window_bottom_texts().addstr(
            5, 14,
            "Licensed to The Tetris Company.",
            curses.color_pair(4)
        )
        self.get_window_bottom_texts().addstr(
            6, 10,
            "Tetris Game Design by Alexey Pajitnov.",
            curses.color_pair(4)
        )
        self.get_window_bottom_texts().addstr(
            7, 13,
            "Tetris Logo Design by Roger Dean.",
            curses.color_pair(4)
        )
        self.get_window_bottom_texts().addstr(
            8, 19,
            "All Rights Reserved.",
            curses.color_pair(4)
        )

        self.get_window_bottom_texts().refresh()

    def get_button_name(self, direction: Direction) -> ButtonName:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne le nom du bouton selon la direction
        # =============================
        if direction == Direction.DOWN:
            return ButtonName(
                (self.get_highlighted_button().value + 1) % 4
            )
        elif direction == Direction.UP:
            return ButtonName(
                3 if (self.get_highlighted_button().value - 1 < 0) else (self.get_highlighted_button().value - 1)
            )
        else:
            return self.get_highlighted_button()
