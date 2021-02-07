# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe abstraite de vue dont découlent GameView et TitleView
# ==========================================================

import curses

from modules.view.view_utilities import set_colorscheme, setup_curses, revert_curses
from modules.PlayerInput import PlayerInput


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
        # -----------------------------
        # REMARQUES :
        # - Fermer le programme sans qu'il puisse appeler le destructeur d'une instance peut dérégler le terminal de
        #   l'utilisateur !
        # - Les instances de View et de ses filles doivent toujours être des singletons !
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
        self.get_window_all().keypad(False)  # désactiver le mode de compatibilité avec le touches spéciales
        self.get_window_all().clear()
        revert_curses()

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
        setup_curses()
        # Paramétrage de _window_all pour les entrées texte
        self.get_window_all().nodelay(True)  # Ne pas attendre l'entrée d'un utilisateur à l'appel d'un getch()
        self.get_window_all().keypad(True)  # Permettre la compatibilité avec les touches spéciales (arrow-up par ex)
        # Gestion des couleurs
        set_colorscheme()
        self.set_backgrounds()

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
    ############## PRINT_WITHOUT_PARAMETER_WINDOWS ################
    ###############################################################
    def print_without_parameter_windows(self) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Affiche toutes les fenêtres qui n'ont pas besoin de paramètres
        # =============================
        pass

    ###############################################################
    ###################### GET_PLAYER_INPUT #######################
    ###############################################################
    def get_player_input(self) -> PlayerInput:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne le premier caractère non-récupéré
        # que le joueur a tapé au clavier
        # =============================
        try:
            return PlayerInput(self.get_window_all().getch())
        except ValueError:
            return PlayerInput.KEY_UNUSED
