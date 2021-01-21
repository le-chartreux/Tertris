# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe abstraite de vue dont découle GameView et TitleView
# ==========================================================

import curses

from modules.classes.view.view_utilities import set_colorscheme
from modules.classes.PlayerInput import PlayerInput


class View:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_window_all"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    # Since the curses module puts the _CursesWindow class private, I had
    # to declare them as objects :/
    _window_all: object

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
        # Et paramètre curses
        # -----------------------------
        # REMARQUES :
        # - Fermer le programme sans qu'il puisse appeler le destructeur d'une instance peut dérégler le terminal de
        #   l'utilisateur !
        # =============================
        self.set_window_all(curses.initscr())

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
        self.revert_curses()

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_window_all(self) -> object:
        return self._window_all

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_window_all(self, window_all) -> None:
        self._window_all = window_all

    ###############################################################
    ############################ SETUP ############################
    ###############################################################
    def setup(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Paramètre tout ce qui est nécessaire pour pouvoir correctement utiliser la vue
        # =============================
        # On setup curses
        self.setup_curses()
        # Paramétrage de _window_all pour les entrées texte
        self.get_window_all().nodelay(True)  # Ne pas attendre l'entrée d'un utilisateur à l'appel d'un getch()
        self.get_window_all().keypad(True)  # Permettre la compatibilité avec les touches spéciales (arrow-up par ex)
        # Gestion des couleurs
        set_colorscheme()
        self.set_backgrounds()

    ###############################################################
    ######################## SETUP_CURSES #########################
    ###############################################################
    def setup_curses(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Paramètre tout ce qui est nécessaire pour pouvoir correctement utiliser curses
        # =============================
        curses.curs_set(False)  # Ne pas afficher le curseur
        curses.noecho()  # Ne pas afficher ce que marque l'utilisateur
        curses.cbreak()  # Ne pas attendre que l'utilisateur appui sur Entrée pour récupérer son entrée

    ###############################################################
    ####################### REVERT_CURSES #########################
    ###############################################################
    def revert_curses(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Remet curses dans son état original et le ferme
        # =============================
        curses.curs_set(True)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

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
        pass

    ###############################################################
    ###################### GET_PLAYER_INPUT #######################
    ###############################################################
    def get_player_input(self) -> PlayerInput:
        return self.get_window_all().getch()
