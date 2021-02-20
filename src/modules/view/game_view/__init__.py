# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe GameView, qui gère la partie Vue du MVC
# quand on a une partie en cours
# ==========================================================

import curses
import locale  # pour encoder les chaines de caractère non ASCII

from math import floor, ceil  # Utilisé pour le calcul de nombre de ═ à mettre dans les bordures

from typing import Optional, Any

from modules.view import View

from modules.tetromino.active_tetromino import ActiveTetromino
from modules.tetromino import Tetromino
from modules.statistics import Statistics
from modules.grid import Grid

from modules.view.view_utilities import get_color_pair
import modules.view.color_pairs as color_pairs

import modules.view.game_view.config as config
import modules.config_general as config_general


class GameView(View):
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_window_game",
        "_window_next",
        "_window_stored",
        "_window_statistics",
        "_window_keybinds"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    # Since the curses module puts the _CursesWindow class private, I had
    # to declare them as Any :/
    _window_game: Any
    _window_next: Any
    _window_stored: Any
    _window_statistics: Any
    _window_keybinds: Any

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
        # Crée un objet GameView, héritant de View, ajoutant :
        # - une fenêtre du jeu (_window_game)
        # - une fenêtre indiquant le prochain tétromino (_window_next)
        # - une fenêtre indiquant le tétromino stocké (_window_stored)
        # - une fenêtre des statistiques (_window_statistics)
        # - une fenêtre des touches (_window_keymaps)
        # -----------------------------
        # REMARQUES :
        # - Se referer aux remarques de View
        # =============================
        View.__init__(self)

        self.set_window_game(
            curses.newwin(
                config.GRID_HEIGHT,
                config.GRID_WIDTH,
                config.GRID_BEGIN_Y,
                config.GRID_BEGIN_X
            )
        )

        self.set_window_next(
            curses.newwin(
                config.NEXT_HEIGHT,
                config.NEXT_WIDTH,
                config.NEXT_BEGIN_Y,
                config.NEXT_BEGIN_X
            )
        )

        self.set_window_stored(
            curses.newwin(
                config.STORED_HEIGHT,
                config.STORED_WIDTH,
                config.STORED_BEGIN_Y,
                config.STORED_BEGIN_X
            )
        )

        self.set_window_statistics(
            curses.newwin(
                config.STATISTICS_HEIGHT,
                config.STATISTICS_WIDTH,
                config.STATISTICS_BEGIN_Y,
                config.STATISTICS_BEGIN_X
            )
        )

        self.set_window_keybinds(
            curses.newwin(
                config.KEYBINDS_HEIGHT,
                config.KEYBINDS_WIDTH,
                config.KEYBINDS_BEGIN_Y,
                config.KEYBINDS_BEGIN_X
            )
        )

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_window_game(self) -> Any:
        return self._window_game

    def get_window_next(self) -> Any:
        return self._window_next

    def get_window_stored(self) -> Any:
        return self._window_stored

    def get_window_statistics(self) -> Any:
        return self._window_statistics

    def get_window_keybinds(self) -> Any:
        return self._window_keybinds

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_window_game(self, window_game: Any) -> None:
        self._window_game = window_game

    def set_window_next(self, window_next: Any) -> None:
        self._window_next = window_next

    def set_window_stored(self, window_stored: Any) -> None:
        self._window_stored = window_stored

    def set_window_statistics(self, window_statistics: Any) -> None:
        self._window_statistics = window_statistics

    def set_window_keybinds(self, window_keymaps: Any) -> None:
        self._window_keybinds = window_keymaps

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
        self.get_window_game().bkgd(" ", curses.color_pair(color_pairs.BLACK_N_WHITE))
        self.get_window_next().bkgd(" ", curses.color_pair(color_pairs.BLACK_N_WHITE))
        self.get_window_stored().bkgd(" ", curses.color_pair(color_pairs.BLACK_N_WHITE))
        self.get_window_statistics().bkgd(" ", curses.color_pair(color_pairs.BLACK_N_WHITE))
        self.get_window_keybinds().bkgd(" ", curses.color_pair(color_pairs.BLACK_N_WHITE))

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
        # - Toutes les fenêtres existent encore !
        # =============================
        View.refresh_all(self)
        self.get_window_game().refresh()
        self.get_window_next().refresh()
        self.get_window_stored().refresh()
        self.get_window_statistics().refresh()
        self.get_window_keybinds().refresh()

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
        self.print_grid_border()
        self.print_next_border()
        self.print_stored_border()
        self.print_statistics_border()
        self.print_keybinds()
        self.print_keybinds_border()

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
        for line in range(config_general.GRID_HEIGHT):
            for column in range(config_general.GRID_WIDTH):
                if grid.is_occupied(x=column, y=line):
                    # On met un bloc
                    self.get_window_game().addstr(
                        line + 1,
                        column * 2 + 1,
                        "██".encode(locale.getpreferredencoding()),
                        curses.color_pair(get_color_pair(grid.get_element(column, line)))
                    )
                    # *2 car les tétrominos font 2 de large
                else:
                    # On met un espace pour supprimer un éventuel ancien bloc
                    self.get_window_game().addstr(
                        line + 1,
                        column * 2 + 1,  # *2 car les tétrominos font 2 de large
                        "  ",
                        curses.color_pair(color_pairs.BLACK_N_WHITE)
                    )

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
        self.get_window_game().addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(1, config.GRID_WIDTH - 2):
            self.get_window_game().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_game().addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

        # Lignes intermédiaires
        for line in range(1, config.GRID_HEIGHT - 1):
            self.get_window_game().addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
            self.get_window_game().addstr(
                line, config.GRID_WIDTH - 2,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )

        # Dernière ligne
        self.get_window_game().addstr(
            config.GRID_HEIGHT - 1, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(1, config.GRID_WIDTH - 2):
            self.get_window_game().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_game().addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

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
        for line in range(active_tetromino.get_height()):
            for column in range(active_tetromino.get_width()):
                if active_tetromino.is_occupied(x=column, y=line):
                    self.get_window_game().addstr(
                        line + active_tetromino.get_y() + 1,
                        (column + active_tetromino.get_x()) * 2 + 1,  # *2 car les tétrominos font 2 de large
                        "██".encode(locale.getpreferredencoding()),
                        curses.color_pair(get_color_pair(active_tetromino.get_tetromino_type()))
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
        for line in range(next_tetromino.get_height()):
            for column in range(next_tetromino.get_width()):
                if next_tetromino.is_occupied(x=column, y=line):
                    # On affiche un "pixel"
                    self.get_window_next().addstr(
                        line + 1,
                        column * 2 + 1,
                        "██".encode(locale.getpreferredencoding()),
                        curses.color_pair(get_color_pair(next_tetromino.get_tetromino_type()))
                    )
                else:
                    # On affiche du vide pour effacer un éventuel résidu de bloc du suivant précédent
                    self.get_window_next().addstr(
                        line + 1,
                        column * 2 + 1,
                        "  ".encode(locale.getpreferredencoding()),  # *2 car les tétrominos font 2 de large
                        curses.A_BOLD | curses.color_pair(color_pairs.BLACK_N_WHITE)
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
        # Affiche la bordure autour du tétromino suivant
        # =============================
        # Première ligne
        self.get_window_next().addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(ceil((config.NEXT_WIDTH - 4 - 2) / 2)):  # -4 car Next, -1 car ╗
            self.get_window_next().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_next().addstr(
            "Next",  # que de l'ASCII donc pas besoin de l'encoder
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(floor((config.NEXT_WIDTH - 4 - 2) / 2)):  # -4 car Next, -1 car ╗
            self.get_window_next().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_next().addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

        # Lignes intermédiaires
        for line in range(1, config.NEXT_HEIGHT - 2):
            self.get_window_next().addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
            self.get_window_next().addstr(
                line, config.NEXT_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )

        # Dernière ligne
        self.get_window_next().addstr(
            config.NEXT_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(1, config.NEXT_WIDTH - 1):
            self.get_window_next().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_next().addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

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
        if stored_tetromino is not None:
            for line in range(stored_tetromino.get_height()):
                for column in range(stored_tetromino.get_width()):
                    if stored_tetromino is not None and stored_tetromino.is_occupied(x=column, y=line):
                        self.get_window_stored().addstr(
                            line + 1,
                            column * 2 + 1,
                            "██".encode(locale.getpreferredencoding()),
                            curses.color_pair(get_color_pair(stored_tetromino.get_tetromino_type()))
                        )
                    else:
                        self.get_window_stored().addstr(
                            line + 1,
                            column * 2 + 1,  # *2 car les tétrominos font 2 de large
                            "  ",  # que de l'ASCII donc pas besoin de l'encoder
                            curses.A_BOLD | curses.color_pair(color_pairs.BLACK_N_WHITE)
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
        self.get_window_stored().addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(ceil((config.STORED_WIDTH - 6 - 2) / 2)):  # -6 car Stored, -2 car ╔ et ╗
            self.get_window_stored().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_stored().addstr(
            "Stored",
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(floor((config.STORED_WIDTH - 6 - 2) / 2)):  # -6 car Stored, -2 car ╔ et ╗
            self.get_window_stored().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_stored().addstr("╗", curses.color_pair(color_pairs.BLACK_N_WHITE))

        # Lignes intermédiaires
        for line in range(1, config.STORED_HEIGHT - 2):
            self.get_window_stored().addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
            self.get_window_stored().addstr(
                line, config.STORED_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )

        # Dernière ligne
        self.get_window_stored().addstr(
            config.STORED_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(1, config.STORED_WIDTH - 1):
            self.get_window_stored().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_stored().addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

        self.get_window_stored().refresh()

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
        self.get_window_statistics().addstr(1, 2, "Level: " + str(statistics.get_level()))
        self.get_window_statistics().addstr(2, 2, "Score: " + str(statistics.get_score()))
        self.get_window_statistics().addstr(3, 2, "Lines: " + str(statistics.get_lines_completed()))
        self.get_window_statistics().addstr(4, 2, "Time: " + str(statistics.get_duration()))

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
        self.get_window_statistics().addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(ceil((config.STATISTICS_WIDTH - 10 - 2) / 2)):  # -10 car Statistics, -2 car ╔ et ╗
            self.get_window_statistics().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_statistics().addstr("Statistics", curses.color_pair(color_pairs.BLACK_N_WHITE))
        for _ in range(floor((config.STATISTICS_WIDTH - 10 - 2) / 2)):  # -10 car Statistics, -2 car ╔ et ╗
            self.get_window_statistics().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_statistics().addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

        # Lignes intermédiaires
        for line in range(1, config.STATISTICS_HEIGHT - 2):
            self.get_window_statistics().addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
            self.get_window_statistics().addstr(
                line, config.STATISTICS_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )

        # Dernière ligne
        self.get_window_statistics().addstr(
            config.STATISTICS_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(1, config.STATISTICS_WIDTH - 1):
            self.get_window_statistics().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_statistics().addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

        self.get_window_statistics().refresh()

    ###############################################################
    ####################### PRINT_KEYBINDS ########################
    ###############################################################
    def print_keybinds(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche les raccourcis dans la fenêtre de raccourcis
        # =============================
        self.get_window_keybinds().addstr(1, 2, "Arrow-left: Left")
        self.get_window_keybinds().addstr(2, 2, "Arrow-right: Right")
        self.get_window_keybinds().addstr(3, 2, "Arrow-down: Down")

        self.get_window_keybinds().addstr(4, 2, "Q: Rotate left")
        self.get_window_keybinds().addstr(5, 2, "D: Rotate right")
        self.get_window_keybinds().addstr(6, 2, "S: Store actual")

        self.get_window_keybinds().addstr(7, 2, "P: Pause")
        self.get_window_keybinds().addstr(8, 2, "Esc: Quit")

        self.get_window_keybinds().refresh()

    ###############################################################
    #################### PRINT_KEYBINDS_BORDER ####################
    ###############################################################
    def print_keybinds_border(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche la bordure autour des raccourcis
        # =============================
        # Première ligne
        self.get_window_keybinds().addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(ceil((config.KEYBINDS_WIDTH - 8 - 2) / 2)):  # -8 car Keybinds, -2 car ╔ et ╗
            self.get_window_keybinds().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_keybinds().addstr("Keybinds", curses.color_pair(color_pairs.BLACK_N_WHITE))
        for _ in range(floor((config.KEYBINDS_WIDTH - 8 - 2) / 2)):  # -8 car Keybinds, -2 car ╔ et ╗
            self.get_window_keybinds().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_keybinds().addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

        # Lignes intermédiaires
        for line in range(1, config.KEYBINDS_HEIGHT - 2):
            self.get_window_keybinds().addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
            self.get_window_keybinds().addstr(
                line, config.KEYBINDS_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )

        # Dernière ligne
        self.get_window_keybinds().addstr(
            config.KEYBINDS_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )
        for _ in range(1, config.KEYBINDS_WIDTH - 1):
            self.get_window_keybinds().addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(color_pairs.BLACK_N_WHITE)
            )
        self.get_window_keybinds().addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(color_pairs.BLACK_N_WHITE)
        )

        self.get_window_keybinds().refresh()
