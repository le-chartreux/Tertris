# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe View, qui gère la partie Vue du MVC
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# ==========================================================

import curses

from typing import Optional

from modules.classes.commons.ActiveTetromino import ActiveTetromino
from modules.classes.commons.Tetromino import Tetromino
from modules.classes.commons.Statistics import Statistics
from modules.classes.commons.PlayerAction import PlayerAction
from modules.classes.commons.Grid import Grid

from modules.settings import (
    GRID_WIDTH,
    GRID_HEIGHT,

    VIEW_GRID_BEGIN_X,
    VIEW_GRID_BEGIN_Y,
    VIEW_GRID_WIDTH,
    VIEW_GRID_HEIGHT,

    VIEW_NEXT_BEGIN_X,
    VIEW_NEXT_BEGIN_Y,
    VIEW_NEXT_WIDTH,
    VIEW_NEXT_HEIGHT,

    VIEW_STORED_BEGIN_X,
    VIEW_STORED_BEGIN_Y,
    VIEW_STORED_WIDTH,
    VIEW_STORED_HEIGHT,

    VIEW_LOGO_BEGIN_X,
    VIEW_LOGO_BEGIN_Y,
    VIEW_LOGO_WIDTH,
    VIEW_LOGO_HEIGHT,

    VIEW_STATISTICS_BEGIN_X,
    VIEW_STATISTICS_BEGIN_Y,
    VIEW_STATISTICS_WIDTH,
    VIEW_STATISTICS_HEIGHT,

    VIEW_KEYBINDS_BEGIN_X,
    VIEW_KEYBINDS_BEGIN_Y,
    VIEW_KEYBINDS_WIDTH,
    VIEW_KEYBINDS_HEIGHT
)


class View:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_window_all",
        "_window_game",
        "_window_next",
        "_window_stored",
        "_window_logo",
        "_window_statistics",
        "_window_keymaps"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _window_all: object
    _window_game: object
    _window_next: object
    _window_stored: object
    _window_logo: object
    _window_statistics: object
    _window_keymaps: object

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
        # Crée un objet View, caractérisé par :
        # - une fenêtre de tout le terminal (_window_all)
        # - une fenêtre du jeu, partie de _window_all (_window_game)
        # - une fenêtre des statistiques, partie de _window_all (_window_statistics)
        # - une fenêtre des touches, partie de _window_all (_window_keymaps)
        # Et le paramètre pour qu'il soit capable de gérer la partie
        # =============================
        window_all = curses.initscr()

        curses.curs_set(False)
        curses.noecho()
        curses.cbreak()
        window_all.keypad(True)
        window_all.nodelay(True)

        self.set_window_all(window_all)

        self.set_window_game(
            curses.newwin(
                VIEW_GRID_HEIGHT,
                VIEW_GRID_WIDTH,
                VIEW_GRID_BEGIN_Y,
                VIEW_GRID_BEGIN_X
            )
        )

        self.set_window_next(
            curses.newwin(
                VIEW_NEXT_HEIGHT,
                VIEW_NEXT_WIDTH,
                VIEW_NEXT_BEGIN_Y,
                VIEW_NEXT_BEGIN_X
            )
        )

        self.set_window_stored(
            curses.newwin(
                VIEW_STORED_HEIGHT,
                VIEW_STORED_WIDTH,
                VIEW_STORED_BEGIN_Y,
                VIEW_STORED_BEGIN_X
            )
        )

        self.set_window_logo(
            curses.newwin(
                VIEW_LOGO_HEIGHT,
                VIEW_LOGO_WIDTH,
                VIEW_LOGO_BEGIN_Y,
                VIEW_LOGO_BEGIN_X
            )
        )

        self.set_window_statistics(
            curses.newwin(
                VIEW_STATISTICS_HEIGHT,
                VIEW_STATISTICS_WIDTH,
                VIEW_STATISTICS_BEGIN_Y,
                VIEW_STATISTICS_BEGIN_X
            )
        )

        self.set_window_keymaps(
            curses.newwin(
                VIEW_KEYBINDS_HEIGHT,
                VIEW_KEYBINDS_WIDTH,
                VIEW_KEYBINDS_BEGIN_Y,
                VIEW_KEYBINDS_BEGIN_X
            )
        )

        self.get_window_logo().nodelay(True)
        self.get_window_logo().keypad(True)
        # Gestion des couleurs
        set_colorscheme()
        self.set_backgrounds()

    ###############################################################
    ########################### __DEL__ ###########################
    ###############################################################
    def __del__(self):
        curses.curs_set(True)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_window_all(self) -> object:
        return self._window_all

    def get_window_game(self) -> object:
        return self._window_game

    def get_window_next(self) -> object:
        return self._window_next

    def get_window_stored(self) -> object:
        return self._window_stored

    def get_window_logo(self) -> object:
        return self._window_logo

    def get_window_statistics(self) -> object:
        return self._window_statistics

    def get_window_keymaps(self) -> object:
        return self._window_keymaps

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_window_all(self, window_all) -> None:
        self._window_all = window_all

    def set_window_game(self, window_game) -> None:
        self._window_game = window_game

    def set_window_next(self, window_next) -> None:
        self._window_next = window_next

    def set_window_stored(self, window_stored) -> None:
        self._window_stored = window_stored

    def set_window_logo(self, window_logo) -> None:
        self._window_logo = window_logo

    def set_window_statistics(self, window_statistics) -> None:
        self._window_statistics = window_statistics

    def set_window_keymaps(self, window_keymaps) -> None:
        self._window_keymaps = window_keymaps

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
        # PRÉCONDITION :
        # set_colorscheme() a déjà été appelé
        # =============================
        self.get_window_all().bkgd(' ', curses.color_pair(8))
        self.get_window_game().bkgd(' ', curses.color_pair(8))
        self.get_window_next().bkgd(' ', curses.color_pair(8))
        self.get_window_stored().bkgd(' ', curses.color_pair(8))
        self.get_window_logo().bkgd(' ', curses.color_pair(8))
        self.get_window_statistics().bkgd(' ', curses.color_pair(8))
        self.get_window_keymaps().bkgd(' ', curses.color_pair(8))

        self.refresh_all()

    ###############################################################
    ######################## REFRESH_ALL ##########################
    ###############################################################
    def refresh_all(self) -> None:
        self.get_window_all().refresh()
        self.get_window_game().refresh()
        self.get_window_next().refresh()
        self.get_window_stored().refresh()
        self.get_window_logo().refresh()
        self.get_window_statistics().refresh()
        self.get_window_keymaps().refresh()

    ###############################################################
    ##################### SETUP_STATIC_WINDOWS ####################
    ###############################################################
    def setup_static_windows(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Charge les fenêtres qui ne bougent pas
        # =============================
        self.print_grid_border()
        self.print_next_border()
        self.print_stored_border()
        self.print_logo()
        self.print_logo_border()
        self.print_statistics_border()
        self.print_keymaps()
        self.print_keymaps_border()

    ###############################################################
    ########################## PRINT_GRID #########################
    ###############################################################
    def print_grid(self, grid: Grid) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche la grille de jeu dans la fenêtre de jeu
        # /!\ pas le tétromino actif ! /!\
        # =============================
        for line in range(GRID_HEIGHT):
            for column in range(GRID_WIDTH):
                if grid.is_occupied(x=column, y=line):
                    # On met un bloc
                    self.get_window_game().addstr(line + 1, column + 1, "█", curses.color_pair(8))
                else:
                    # On met un espace pour supprimer un éventuel ancien bloc
                    self.get_window_game().addstr(line + 1, column + 1, " ", curses.color_pair(8))

        self.get_window_game().refresh()

    ###############################################################
    ###################### PRINT_GRID_BORDER ######################
    ###############################################################
    def print_grid_border(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche la bordure autour de la grille de jeu
        # =============================
        # Première ligne
        self.get_window_game().addstr(0, 0, "╔", curses.color_pair(8))
        self.get_window_game().addstr("══", curses.color_pair(8))
        self.get_window_game().addstr("════════", curses.color_pair(8))
        self.get_window_game().addstr("══", curses.color_pair(8))
        self.get_window_game().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, VIEW_GRID_HEIGHT - 1):
            self.get_window_game().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_game().addstr(line, VIEW_GRID_WIDTH - 2, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_game().addstr(VIEW_GRID_HEIGHT - 1, 0, "╚", curses.color_pair(8))
        self.get_window_game().addstr("════════════", curses.color_pair(8))
        self.get_window_game().addstr("╝", curses.color_pair(8))

        self.get_window_game().refresh()

    ###############################################################
    ################### PRINT_ACTIVE_TETROMINO ####################
    ###############################################################
    def print_active_tetromino(self, active_tetromino: ActiveTetromino) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche le tétromino actif dans la fenêtre de jeu
        # =============================
        for line in range(4):
            for column in range(4):
                if active_tetromino.is_occupied(x=column, y=line):
                    self.get_window_game().addstr(
                        line + active_tetromino.get_y() + 1,
                        column + active_tetromino.get_x() + 1,
                        "█",
                        curses.A_BOLD | curses.color_pair(5)
                    )

        self.get_window_game().refresh()

    ###############################################################
    ########################## PRINT_NEXT #########################
    ###############################################################
    def print_next(self, next_tetromino: Tetromino):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche le tétromino suivant dans la fenêtre next
        # =============================
        for line in range(4):
            for column in range(4):
                if next_tetromino.is_occupied(x=column, y=line):
                    self.get_window_next().addstr(
                        line + 1,
                        column + 1,
                        "█",
                        curses.A_BOLD | curses.color_pair(5)
                    )
                else:
                    self.get_window_next().addstr(
                        line + 1,
                        column + 1,
                        " ",
                        curses.A_BOLD | curses.color_pair(8)
                    )

        self.get_window_next().refresh()

    ###############################################################
    ##################### PRINT_NEXT_BORDER #######################
    ###############################################################
    def print_next_border(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche la bordure autour du tetromino suivant
        # =============================
        # Première ligne
        self.get_window_next().addstr(0, 0, "╔", curses.color_pair(8))
        self.get_window_next().addstr("Next", curses.color_pair(8))
        self.get_window_next().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, VIEW_NEXT_HEIGHT - 2):
            self.get_window_next().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_next().addstr(line, VIEW_NEXT_WIDTH - 1, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_next().addstr(VIEW_NEXT_HEIGHT - 2, 0, "╚", curses.color_pair(8))
        self.get_window_next().addstr("════", curses.color_pair(8))
        self.get_window_next().addstr("╝", curses.color_pair(8))

        self.get_window_next().refresh()

    ###############################################################
    ######################## PRINT_STORED #########################
    ###############################################################
    def print_stored(self, stored_tetromino: Optional[Tetromino]):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche le tétromino suivant dans la fenêtre stored
        # =============================
        for line in range(4):
            for column in range(4):
                if stored_tetromino is not None and stored_tetromino.is_occupied(x=column, y=line):
                    self.get_window_stored().addstr(
                        line + 1,
                        column + 1,
                        "█",
                        curses.A_BOLD | curses.color_pair(5)
                    )
                else:
                    self.get_window_stored().addstr(
                        line + 1,
                        column + 1,
                        " ",
                        curses.A_BOLD | curses.color_pair(8)
                    )

        self.get_window_stored().refresh()

    ###############################################################
    ################### PRINT_STORED_BORDER #######################
    ###############################################################
    def print_stored_border(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche la bordure autour du tetromino stocké
        # =============================
        # Première ligne
        self.get_window_stored().addstr(0, 0, "Stored", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, VIEW_STORED_HEIGHT - 2):
            self.get_window_stored().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_stored().addstr(line, VIEW_STORED_WIDTH - 1, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_stored().addstr(VIEW_STORED_HEIGHT - 2, 0, "╚", curses.color_pair(8))
        self.get_window_stored().addstr("════", curses.color_pair(8))
        self.get_window_stored().addstr("╝", curses.color_pair(8))

        self.get_window_stored().refresh()

    ###############################################################
    ########################## PRINT_LOGO #########################
    ###############################################################
    def print_logo(self):
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche le logo dans la fenêtre logo
        # =============================
        self.get_window_logo().addstr(2, 1, ">", curses.color_pair(8))
        self.get_window_logo().addstr("███", curses.color_pair(6))
        self.get_window_logo().addstr(3, 3, "█", curses.color_pair(6))

        self.get_window_stored().refresh()

    ###############################################################
    ##################### PRINT_LOGO_BORDER #######################
    ###############################################################
    def print_logo_border(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche la bordure autour du logo
        # =============================
        # Première ligne
        self.get_window_logo().addstr(0, 0, "╔", curses.color_pair(8))
        self.get_window_logo().addstr("Logo", curses.color_pair(8))
        self.get_window_logo().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, VIEW_LOGO_HEIGHT - 2):
            self.get_window_logo().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_logo().addstr(line, VIEW_LOGO_WIDTH - 1, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_logo().addstr(VIEW_LOGO_HEIGHT - 2, 0, "╚", curses.color_pair(8))
        self.get_window_logo().addstr("════", curses.color_pair(8))
        self.get_window_logo().addstr("╝", curses.color_pair(8))

        self.get_window_logo().refresh()

    ###############################################################
    ###################### PRINT_STATISTICS #######################
    ###############################################################
    def print_statistics(self, statistics: Statistics) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche les statistiques dans la fenêtre de statistiques
        # =============================
        self.get_window_statistics().addstr(1, 1, "Level: " + str(statistics.get_level()))
        self.get_window_statistics().addstr(2, 1, "Score: " + str(statistics.get_score()))
        self.get_window_statistics().addstr(3, 1, "Lines: " + str(statistics.get_lines_completed()))
        self.get_window_statistics().addstr(4, 1, "Time: " + str(statistics.get_duration()))

        self.get_window_statistics().refresh()

    ###############################################################
    ################## PRINT_STATISTICS_BORDER ####################
    ###############################################################
    def print_statistics_border(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche la bordure autour des statistiques de jeu
        # =============================
        # Première ligne
        self.get_window_statistics().addstr(0, 0, "╔", curses.color_pair(8))
        self.get_window_statistics().addstr("════", curses.color_pair(8))
        self.get_window_statistics().addstr("Statistics", curses.color_pair(8))
        self.get_window_statistics().addstr("════", curses.color_pair(8))
        self.get_window_statistics().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, VIEW_STATISTICS_HEIGHT - 2):
            self.get_window_statistics().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_statistics().addstr(line, VIEW_STATISTICS_WIDTH - 1, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_statistics().addstr(VIEW_STATISTICS_HEIGHT - 2, 0, "╚", curses.color_pair(8))
        self.get_window_statistics().addstr("══════════════════", curses.color_pair(8))
        self.get_window_statistics().addstr("╝", curses.color_pair(8))

        self.get_window_statistics().refresh()

    ###############################################################
    ######################## PRINT_KEYMAPS ########################
    ###############################################################
    def print_keymaps(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche les raccourcis dans la fenêtre de raccourcis
        # =============================
        self.get_window_keymaps().addstr(1, 1, "Q: Left")
        self.get_window_keymaps().addstr(2, 1, "D: Right")
        self.get_window_keymaps().addstr(3, 1, "S: Down")

        self.get_window_keymaps().addstr(5, 1, "J: Rotate left")
        self.get_window_keymaps().addstr(6, 1, "L: Rotate right")
        self.get_window_keymaps().addstr(7, 1, "Esc: Quit")

        self.get_window_keymaps().refresh()

    ###############################################################
    ##################### PRINT_KEYMAPS_BORDER ####################
    ###############################################################
    def print_keymaps_border(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche la bordure autour des raccourcis
        # =============================
        # Première ligne
        self.get_window_keymaps().addstr(0, 0, "╔", curses.color_pair(8))
        self.get_window_keymaps().addstr("═════", curses.color_pair(8))
        self.get_window_keymaps().addstr("Keybinds", curses.color_pair(8))
        self.get_window_keymaps().addstr("═════", curses.color_pair(8))
        self.get_window_keymaps().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, VIEW_KEYBINDS_HEIGHT - 2):
            self.get_window_keymaps().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_keymaps().addstr(line, VIEW_KEYBINDS_WIDTH - 1, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_keymaps().addstr(VIEW_KEYBINDS_HEIGHT - 2, 0, "╚", curses.color_pair(8))
        self.get_window_keymaps().addstr("══════════════════", curses.color_pair(8))
        self.get_window_keymaps().addstr("╝", curses.color_pair(8))

        self.get_window_keymaps().refresh()

    ###############################################################
    ###################### GET_PLAYER_INPUT #######################
    ###############################################################
    def get_player_input(self) -> PlayerAction:
        player_input = self.get_window_logo().getch()
        if player_input == curses.ERR:
            return PlayerAction.NOTHING
        if player_input == 81 or player_input == 113 or player_input == curses.KEY_LEFT:  # Q ou q
            return PlayerAction.MOVE_ACTIVE_TETROMINO_LEFT
        elif player_input == 68 or player_input == 100 or player_input == curses.KEY_RIGHT:  # D ou d
            return PlayerAction.MOVE_ACTIVE_TETROMINO_RIGHT
        elif player_input == 83 or player_input == 115 or player_input == curses.KEY_DOWN:  # S ou s
            return PlayerAction.MOVE_ACTIVE_TETROMINO_DOWN
        elif player_input == 74 or player_input == 106:  # J ou j
            return PlayerAction.ROTATE_ACTIVE_TETROMINO_LEFT
        elif player_input == 76 or player_input == 108:  # L ou l
            return PlayerAction.ROTATE_ACTIVE_TETROMINO_RIGHT
        elif player_input == 27:  # Esc
            return PlayerAction.QUIT_GAME
        else:
            return PlayerAction.MISSCLIC

    ###############################################################
    ########################## WAIT_ESC ###########################
    ###############################################################
    def wait_esc(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Attend que l'utilisateur appuie sur Esc
        # =============================
        from time import sleep
        while self.get_window_logo().getch() != 27:
            # pour une raison curse (lul), le code est + rapide si on getch() sur une petite fenêtre
            sleep(0.03)


###############################################################
###################### SET_COLORSCHEME ########################
###############################################################
def set_colorscheme() -> None:
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)  # I
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)  # O
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_WHITE)  # T
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_WHITE)  # L
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_WHITE)  # J
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_WHITE)  # Z
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_WHITE)   # S
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Background & texts
