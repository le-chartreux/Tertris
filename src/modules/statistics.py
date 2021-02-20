# ==========================================================
# INFORMATIONS SUR CE PACKAGE :
# -----------------------------
# UTILITÉ DE SON CONTENU :
# Définir la classe Statistics, qui contient les statistiques de la partie en cours
# ==========================================================

import time
from typing import Optional


class Statistics:
    ###############################################################
    ########################## __SLOTS__ ##########################
    ###############################################################
    __slots__ = (
        "_level",
        "_score",
        "_lines_completed",
        "_begin_time",
        "_paused_time"
    )

    ###############################################################
    ############################ HINTS ############################
    ###############################################################
    _level: int
    _score: int
    _lines_completed: int
    _begin_time: float
    _paused_time: float

    ###############################################################
    ########################## __INIT__ ###########################
    ###############################################################
    def __init__(
            self,
            level: int = 0,
            score: int = 0,
            lines_completed: int = 0,
            begin_time: float = time.time(),
            paused_time: float = 0
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
        self.set_paused_time(paused_time)

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

    def get_paused_time(self) -> float:
        return self._paused_time

    ###############################################################
    ########################### SETTERS ###########################
    ###############################################################
    def set_level(self, level: int) -> None:
        self._level = level

    def set_score(self, score: int) -> None:
        self._score = score

    def set_lines_completed(self, lines_completed: int) -> None:
        self._lines_completed = lines_completed

    def set_begin_time(self, begin_time: float) -> None:
        self._begin_time = begin_time

    def set_paused_time(self, paused_time: float) -> None:
        self._paused_time = paused_time

    ###############################################################
    ############################ ADDERS ###########################
    ###############################################################
    def add_level(self, level_to_add: int) -> None:
        self.set_level(self.get_level() + level_to_add)

    def add_score(self, score_to_add: int) -> None:
        self.set_score(self.get_score() + score_to_add)

    def add_lines_completed(self, lines_completed_to_add: int) -> None:
        self.set_lines_completed(self.get_lines_completed() + lines_completed_to_add)

    def add_paused_time(self, paused_time_to_add: float) -> None:
        self.set_paused_time(self.get_paused_time() + paused_time_to_add)

    ###############################################################
    ######################### GET_DURATION ########################
    ###############################################################
    def get_duration(self, end_time: Optional[float] = None) -> int:
        # =============================
        # INFORMATIONS :
        # -----------------------------
        # UTILITÉ :
        # Retourne la durée, en secondes, depuis le temps de début, auquel est soustrait le temps de pause
        # =============================
        if end_time is None:
            return int(time.time() - self.get_begin_time() - self.get_paused_time())
        else:
            return int(end_time - self.get_begin_time() - self.get_paused_time())

    ###############################################################
    #################### GET_POINTS_FOR_LINES #####################
    ###############################################################
    def get_points_for_lines(self, number_of_lines: int) -> int:
        multiplier = 0
        if number_of_lines == 1:
            multiplier = 40
        elif number_of_lines == 2:
            multiplier = 100
        elif number_of_lines == 3:
            multiplier = 300
        elif number_of_lines == 4:
            multiplier = 1200
        return multiplier * (self.get_level() + 1)

    ###############################################################
    #################### ADD_POINTS_FOR_LINES #####################
    ###############################################################
    def add_points_for_lines(self, number_of_lines: int) -> None:
        self.add_score(self.get_points_for_lines(number_of_lines))
