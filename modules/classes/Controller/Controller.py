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
# ==========================================================

from modules.classes.Model.Model import Model
from modules.classes.View.View import View


class Controller:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_model",
        "_view"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _model: Model
    _view: View

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            model: Model = None,
            view: View = None
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Controller, caractérisé par :
        # - son model (_model)
        # - sa vue (_view)
        # =============================
        if model is None:
            model = Model()
        if view is None:
            view = View()

        self.set_model(model)
        self.set_view(view)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_model(self) -> Model:
        return self._model

    def get_view(self) -> View:
        return self._view

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_model(self, model: Model) -> None:
        self._model = model

    def set_view(self, view: View) -> None:
        self._view = view
