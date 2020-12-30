# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe GameView, qui gère la partie Vue du MVC (quand on a une partie en cours)
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
# + setup_static_window()
# + print_grid()
# + print_grid_border()
# + print_active_tetromino()
# + print_next()
# + print_next_border()
# + print_stored()
# + print_stored_border()
# + print_statistics()
# + print_statistics_border()
# + print_keybinds()
# + print_keybinds_border()
# + get_player_input()
# + set_colorscheme() <- fonction
# + get_color_pair() <- fonction
# ==========================================================

import curses
from math import floor, ceil  # Utilisé pour le calcul de nombre de ═ à mettre dans les bordures

from typing import Optional

from modules.classes.ActiveTetromino import ActiveTetromino
from modules.classes.Tetromino import Tetromino
from modules.classes.Statistics import Statistics
from modules.classes.PlayerAction import PlayerAction
from modules.classes.Grid import Grid

from modules.classes.view.view_utilities import set_colorscheme, get_color_pair

from modules.settings import (
    GRID_WIDTH,
    GRID_HEIGHT,

    GAME_VIEW_GRID_BEGIN_X,
    GAME_VIEW_GRID_BEGIN_Y,
    GAME_VIEW_GRID_WIDTH,
    GAME_VIEW_GRID_HEIGHT,

    GAME_VIEW_NEXT_BEGIN_X,
    GAME_VIEW_NEXT_BEGIN_Y,
    GAME_VIEW_NEXT_WIDTH,
    GAME_VIEW_NEXT_HEIGHT,

    GAME_VIEW_STORED_BEGIN_X,
    GAME_VIEW_STORED_BEGIN_Y,
    GAME_VIEW_STORED_WIDTH,
    GAME_VIEW_STORED_HEIGHT,

    GAME_VIEW_STATISTICS_BEGIN_X,
    GAME_VIEW_STATISTICS_BEGIN_Y,
    GAME_VIEW_STATISTICS_WIDTH,
    GAME_VIEW_STATISTICS_HEIGHT,

    GAME_VIEW_KEYBINDS_BEGIN_X,
    GAME_VIEW_KEYBINDS_BEGIN_Y,
    GAME_VIEW_KEYBINDS_WIDTH,
    GAME_VIEW_KEYBINDS_HEIGHT
)


class GameView:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_window_all",
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
    # to declare them as objects :/
    _window_all: object
    _window_game: object
    _window_next: object
    _window_stored: object
    _window_statistics: object
    _window_keybinds: object

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
        # Crée un objet GameView, caractérisé par :
        # - une fenêtre de tout le terminal (_window_all)
        # - une fenêtre du jeu, partie de _window_all (_window_game)
        # - une fenêtre des statistiques, partie de _window_all (_window_statistics)
        # - une fenêtre des touches, partie de _window_all (_window_keymaps)
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
                GAME_VIEW_GRID_HEIGHT,
                GAME_VIEW_GRID_WIDTH,
                GAME_VIEW_GRID_BEGIN_Y,
                GAME_VIEW_GRID_BEGIN_X
            )
        )

        self.set_window_next(
            curses.newwin(
                GAME_VIEW_NEXT_HEIGHT,
                GAME_VIEW_NEXT_WIDTH,
                GAME_VIEW_NEXT_BEGIN_Y,
                GAME_VIEW_NEXT_BEGIN_X
            )
        )

        self.set_window_stored(
            curses.newwin(
                GAME_VIEW_STORED_HEIGHT,
                GAME_VIEW_STORED_WIDTH,
                GAME_VIEW_STORED_BEGIN_Y,
                GAME_VIEW_STORED_BEGIN_X
            )
        )

        self.set_window_statistics(
            curses.newwin(
                GAME_VIEW_STATISTICS_HEIGHT,
                GAME_VIEW_STATISTICS_WIDTH,
                GAME_VIEW_STATISTICS_BEGIN_Y,
                GAME_VIEW_STATISTICS_BEGIN_X
            )
        )

        self.set_window_keybinds(
            curses.newwin(
                GAME_VIEW_KEYBINDS_HEIGHT,
                GAME_VIEW_KEYBINDS_WIDTH,
                GAME_VIEW_KEYBINDS_BEGIN_Y,
                GAME_VIEW_KEYBINDS_BEGIN_X
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

    def get_window_game(self) -> object:
        return self._window_game

    def get_window_next(self) -> object:
        return self._window_next

    def get_window_stored(self) -> object:
        return self._window_stored

    def get_window_statistics(self) -> object:
        return self._window_statistics

    def get_window_keybinds(self) -> object:
        return self._window_keybinds

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

    def set_window_statistics(self, window_statistics) -> None:
        self._window_statistics = window_statistics

    def set_window_keybinds(self, window_keymaps) -> None:
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
        self.get_window_all().bkgd(' ', curses.color_pair(8))
        self.get_window_game().bkgd(' ', curses.color_pair(8))
        self.get_window_next().bkgd(' ', curses.color_pair(8))
        self.get_window_stored().bkgd(' ', curses.color_pair(8))
        self.get_window_statistics().bkgd(' ', curses.color_pair(8))
        self.get_window_keybinds().bkgd(' ', curses.color_pair(8))

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
        self.get_window_all().refresh()
        self.get_window_game().refresh()
        self.get_window_next().refresh()
        self.get_window_stored().refresh()
        self.get_window_statistics().refresh()
        self.get_window_keybinds().refresh()

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
        for line in range(GRID_HEIGHT):
            for column in range(GRID_WIDTH):
                if grid.is_occupied(x=column, y=line):
                    # On met un bloc
                    self.get_window_game().addstr(
                        line + 1,
                        column*2 + 1,
                        "██",
                        curses.color_pair(get_color_pair(grid.get_element(column, line)))
                    )
                    # *2 car les tétrominos font 2 de large
                else:
                    # On met un espace pour supprimer un éventuel ancien bloc
                    self.get_window_game().addstr(line + 1, column*2 + 1, "  ", curses.color_pair(8))
                    # *2 car les tétrominos font 2 de large

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
        for _ in range(1, GAME_VIEW_GRID_WIDTH - 2):
            self.get_window_game().addstr("═", curses.color_pair(8))
        self.get_window_game().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, GAME_VIEW_GRID_HEIGHT - 1):
            self.get_window_game().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_game().addstr(line, GAME_VIEW_GRID_WIDTH - 2, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_game().addstr(GAME_VIEW_GRID_HEIGHT - 1, 0, "╚", curses.color_pair(8))
        for _ in range(1, GAME_VIEW_GRID_WIDTH - 2):
            self.get_window_game().addstr("═", curses.color_pair(8))
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
        for line in range(active_tetromino.get_height()):
            for column in range(active_tetromino.get_width()):
                if active_tetromino.is_occupied(x=column, y=line):
                    self.get_window_game().addstr(
                        line + active_tetromino.get_y() + 1,
                        (column + active_tetromino.get_x())*2 + 1,  # *2 car les tétrominos font 2 de large
                        "██",
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
                        column*2 + 1,
                        "██",  # *2 car les tétrominos font 2 de large
                        curses.color_pair(get_color_pair(next_tetromino.get_tetromino_type()))
                    )
                else:
                    # On affiche du vide pour effacer un éventuel résidu de bloc du suivant précédent
                    self.get_window_next().addstr(
                        line + 1,
                        column*2 + 1,
                        "  ",  # *2 car les tétrominos font 2 de large
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
        for _ in range(ceil((GAME_VIEW_NEXT_WIDTH - 4 - 2) / 2)):  # -4 car Next, -1 car ╗
            self.get_window_next().addstr("═", curses.color_pair(8))
        self.get_window_next().addstr("Next", curses.color_pair(8))
        for _ in range(floor((GAME_VIEW_NEXT_WIDTH - 4 - 2) / 2)):  # -4 car Next, -1 car ╗
            self.get_window_next().addstr("═", curses.color_pair(8))
        self.get_window_next().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, GAME_VIEW_NEXT_HEIGHT - 2):
            self.get_window_next().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_next().addstr(line, GAME_VIEW_NEXT_WIDTH - 1, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_next().addstr(GAME_VIEW_NEXT_HEIGHT - 2, 0, "╚", curses.color_pair(8))
        for _ in range(1, GAME_VIEW_NEXT_WIDTH - 1):
            self.get_window_next().addstr("═", curses.color_pair(8))
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
        if stored_tetromino is not None:
            for line in range(stored_tetromino.get_height()):
                for column in range(stored_tetromino.get_width()):
                    if stored_tetromino is not None and stored_tetromino.is_occupied(x=column, y=line):
                        self.get_window_stored().addstr(
                            line + 1,
                            column*2 + 1,
                            "██",  # *2 car les tétrominos font 2 de large
                            curses.color_pair(get_color_pair(stored_tetromino.get_tetromino_type()))
                        )
                    else:
                        self.get_window_stored().addstr(
                            line + 1,
                            column*2 + 1,  # *2 car les tétrominos font 2 de large
                            "  ",
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
        self.get_window_stored().addstr(0, 0, "╔", curses.color_pair(8))
        for _ in range(ceil((GAME_VIEW_STORED_WIDTH - 6 - 2) / 2)):  # -6 car Stored, -2 car ╔ et ╗
            self.get_window_stored().addstr("═", curses.color_pair(8))
        self.get_window_stored().addstr("Stored", curses.color_pair(8))
        for _ in range(floor((GAME_VIEW_STORED_WIDTH - 6 - 2) / 2)):  # -6 car Stored, -2 car ╔ et ╗
            self.get_window_stored().addstr("═", curses.color_pair(8))
        self.get_window_stored().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, GAME_VIEW_STORED_HEIGHT - 2):
            self.get_window_stored().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_stored().addstr(line, GAME_VIEW_STORED_WIDTH - 1, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_stored().addstr(GAME_VIEW_STORED_HEIGHT - 2, 0, "╚", curses.color_pair(8))
        for _ in range(1, GAME_VIEW_STORED_WIDTH - 1):
            self.get_window_stored().addstr("═", curses.color_pair(8))
        self.get_window_stored().addstr("╝", curses.color_pair(8))

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
        for _ in range(ceil((GAME_VIEW_STATISTICS_WIDTH - 10 - 2) / 2)):  # -10 car Statistics, -2 car ╔ et ╗
            self.get_window_statistics().addstr("═", curses.color_pair(8))
        self.get_window_statistics().addstr("Statistics", curses.color_pair(8))
        for _ in range(floor((GAME_VIEW_STATISTICS_WIDTH - 10 - 2) / 2)):  # -10 car Statistics, -2 car ╔ et ╗
            self.get_window_statistics().addstr("═", curses.color_pair(8))
        self.get_window_statistics().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, GAME_VIEW_STATISTICS_HEIGHT - 2):
            self.get_window_statistics().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_statistics().addstr(line, GAME_VIEW_STATISTICS_WIDTH - 1, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_statistics().addstr(GAME_VIEW_STATISTICS_HEIGHT - 2, 0, "╚", curses.color_pair(8))
        for _ in range(1, GAME_VIEW_STATISTICS_WIDTH - 1):
            self.get_window_statistics().addstr("═", curses.color_pair(8))
        self.get_window_statistics().addstr("╝", curses.color_pair(8))

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
        self.get_window_keybinds().addstr(1, 1, "Arrow-left: Left")
        self.get_window_keybinds().addstr(2, 1, "Arrow-right: Right")
        self.get_window_keybinds().addstr(3, 1, "Arrow-down: Down")

        self.get_window_keybinds().addstr(4, 1, "Q: Rotate left")
        self.get_window_keybinds().addstr(5, 1, "D: Rotate right")
        self.get_window_keybinds().addstr(6, 1, "S: Store actual")

        self.get_window_keybinds().addstr(7, 1, "P: Pause")
        self.get_window_keybinds().addstr(8, 1, "Esc: Quit")

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
        self.get_window_keybinds().addstr(0, 0, "╔", curses.color_pair(8))
        for _ in range(ceil((GAME_VIEW_KEYBINDS_WIDTH - 8 - 2) / 2)):  # -8 car Keybinds, -2 car ╔ et ╗
            self.get_window_keybinds().addstr("═", curses.color_pair(8))
        self.get_window_keybinds().addstr("Keybinds", curses.color_pair(8))
        for _ in range(floor((GAME_VIEW_KEYBINDS_WIDTH - 8 - 2) / 2)):  # -8 car Keybinds, -2 car ╔ et ╗
            self.get_window_keybinds().addstr("═", curses.color_pair(8))
        self.get_window_keybinds().addstr("╗", curses.color_pair(8))

        # Lignes intermédiaires
        for line in range(1, GAME_VIEW_KEYBINDS_HEIGHT - 2):
            self.get_window_keybinds().addstr(line, 0, "║", curses.color_pair(8))
            self.get_window_keybinds().addstr(line, GAME_VIEW_KEYBINDS_WIDTH - 1, "║", curses.color_pair(8))

        # Dernière ligne
        self.get_window_keybinds().addstr(GAME_VIEW_KEYBINDS_HEIGHT - 2, 0, "╚", curses.color_pair(8))
        for _ in range(1, GAME_VIEW_KEYBINDS_WIDTH - 1):
            self.get_window_keybinds().addstr("═", curses.color_pair(8))
        self.get_window_keybinds().addstr("╝", curses.color_pair(8))

        self.get_window_keybinds().refresh()

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
