# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Query, qui sert à gérer les demandes de la vue et du modèle
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# ==========================================================

from modules.classes.Utilities.Subject import Subject


class Query:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_subject",
        "_content"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _subject: Subject
    _content: object

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            subject: Subject,
            content: object
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Query, caractérisé par :
        # - un sujet (_subject)
        # - un contenu (_content)
        # =============================
        self.set_subject(subject)
        self.set_content(content)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_subject(self) -> Subject:
        return self._subject

    def get_content(self) -> object:
        return self._content

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_subject(self, subject: Subject):
        self._subject = subject

    def set_content(self, content: object):
        self._content = content
