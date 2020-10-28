# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Statistics, qui sert à contenir les informations liées aux statistiques de la partie
# -----------------------------
# CONTENU :
# + __slots__
# + HINTS
# + __init__()
# + GETTERS
# + SETTERS
# + get_duration()
# + get_speed()
# ==========================================================

import time


class Statistics:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_level",
        "_score",
        "_lines_completed",
        "_begin_time"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _level: int
    _score: int
    _lines_completed: int
    _begin_time: float

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            level: int = 0,
            score: int = 0,
            lines_completed: int = 0,
            begin_time: float = time.time()
    ) -> None:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Crée un objet Statistics, caractérisé par :
        # - un niveau (_level)
        # - un score (_score)
        # - un nombre de lignes complétées (_lines_completed)
        # - un temps de début (_begin_time)
        # =============================
        self.set_level(level)
        self.set_score(score)
        self.set_lines_completed(lines_completed)
        self.set_begin_time(begin_time)

    ###############################################################
    ########################### GETTERS ###########################
    ###############################################################
    def get_level(self) -> int:
        return self._level

    def get_score(self) -> int:
        return self._score

    def get_lines_completed(self) -> int:
        return self._lines_completed

    def get_begin_time(self) -> float:
        return self._begin_time

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_level(self, level: int) -> None:
        self._level = level

    def set_score(self, score: int) -> None:
        self._score = score

    def set_lines_completed(self, lines_completed: int) -> None:
        self._lines_completed = lines_completed

    def set_begin_time(self, begin_time) -> None:
        self._begin_time = begin_time

    ###############################################################
    ######################### GET_DURATION ########################
    ###############################################################
    def get_duration(self, end_time: float) -> float:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la durée, en secondes, depuis le temps de début
        # =============================
        return end_time - self.get_begin_time()

    ###############################################################
    ########################### GET_SPEED #########################
    ###############################################################
    def get_speed(self) -> float:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la vitesse de chute du tétromino du joueur, en case / seconde
        # =============================
        return self.get_level()
