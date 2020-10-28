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

from modules.settings import (
    VIEW_GRID_BEGIN_X,
    VIEW_GRID_BEGIN_Y,
    VIEW_GRID_WIDTH,
    VIEW_GRID_HEIGHT,

    VIEW_STATISTICS_BEGIN_X,
    VIEW_STATISTICS_BEGIN_Y,
    VIEW_STATISTICS_WIDTH,
    VIEW_STATISTICS_HEIGHT,

    VIEW_KEYMAPS_BEGIN_X,
    VIEW_KEYMAPS_BEGIN_Y,
    VIEW_KEYMAPS_WIDTH,
    VIEW_KEYMAPS_HEIGHT
)


class View:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_window_all",
        "_window_game",
        "_window_statistics",
        "_window_keymaps"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _window_all: object
    _window_game: object
    _window_statistics: object
    _window_keymaps: object

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet View, caractérisé par :
        # - son stdscr, l'écran entier du terminal (_stdscr)
        # - sa position sur l'axe Y (_y)
        # =============================
        window_all = curses.initscr()


        curses.curs_set(False)
        curses.noecho()
        curses.cbreak()
        window_all.keypad(True)

        self.set_window_all(window_all)

        self.set_window_game(
            curses.newwin(
                VIEW_GRID_HEIGHT,
                VIEW_GRID_WIDTH,
                VIEW_GRID_BEGIN_Y,
                VIEW_GRID_BEGIN_X
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
                VIEW_KEYMAPS_HEIGHT,
                VIEW_KEYMAPS_WIDTH,
                VIEW_KEYMAPS_BEGIN_Y,
                VIEW_KEYMAPS_BEGIN_X
            )
        )

        self.print_keymaps()

    ###############################################################
    ########################### __DEL__ ###########################
    ###############################################################
    def __del__(self):
        curses.curs_set(True)
        curses.nocbreak()
        self.get_window_all().keypad(False)
        curses.echo()
        curses.endwin()

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_window_all(self) -> object:
        return self._window_all

    def get_window_game(self) -> object:
        return self._window_game

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

    def set_window_statistics(self, window_statistics) -> None:
        self._window_statistics = window_statistics

    def set_window_keymaps(self, window_keymaps) -> None:
        self._window_keymaps = window_keymaps

    ###############################################################
    ###################### PRINT_STATISTICS #######################
    ###############################################################
    def print_statistics(self, level: int, score: int, lines: int, time: int):
        from time import sleep
        self.get_window_statistics().addstr(0, 0, "Statistics:", curses.A_BOLD)
        self.get_window_statistics().addstr(1, 0, "Level: " + str(level))
        self.get_window_statistics().addstr(2, 0, "Score: " + str(score))
        self.get_window_statistics().addstr(3, 0, "Lines: " + str(lines))
        self.get_window_statistics().addstr(4, 0, "Time: " + str(time))
        self.get_window_statistics().refresh()

        while self.get_window_statistics().getch() != 27:
            pass

    ###############################################################
    ######################## PRINT_KEYMAPS ########################
    ###############################################################
    def print_keymaps(self) -> None:
        self.get_window_keymaps().addstr(0, 0, "Keymaps:", curses.A_BOLD)
        self.get_window_keymaps().addstr(1, 0, "Arrow-left: Left")
        self.get_window_keymaps().addstr(2, 0, "Arrow-right: Right")
        self.get_window_keymaps().addstr(3, 0, "Arrow-down: Down")
        self.get_window_keymaps().addstr(4, 0, "S: Rotate left")
        self.get_window_keymaps().addstr(5, 0, "F: Rotate right")
        self.get_window_keymaps().addstr(6, 0, "Esc: Quit")
        self.get_window_keymaps().refresh()
