"""
File that contains the declaration of the Statistics class
"""

import time
import typing


class Statistics:

    def __init__(
            self,
            score: int = 0,
            lines_completed: int = 0,
            begin_time: float = time.monotonic(),
            paused_time: float = 0.0
    ) -> None:
        """
        Creates a Statistics object, characterized by:
        - a score (starts at 0 and increments during the game)
        - the number of completed lines
        - a begin time (the moment where the game started)
        - a paused time (the sum of duration of moments where the game was paused)
        - _chrono_paused_since, to manage pauses

        The level is computed with the score, so we don't store it.
        """
        self._score = score
        self._lines_completed = lines_completed
        self._begin_time = begin_time
        self._paused_time = paused_time
        self._chrono_paused_since: typing.Optional[float] = None

    # GETTERS
    def get_level(self) -> int:
        return 1  # TODO trouver comment ça marche

    def get_score(self) -> int:
        return self._score

    def get_lines_completed(self) -> int:
        return self._lines_completed

    def get_duration(self, end_time: typing.Optional[float] = None) -> int:
        """
        :param end_time: the moment until when we want to know the duration
        :return: the duration (in seconds) between the begin time and <end_time>, where the paused time is subtracted
        """
        if end_time is None:
            # end_time = now
            return int(time.monotonic() - self._begin_time - self._get_total_paused_time())
        else:
            return int(end_time - self._begin_time - self._paused_time)

    def _get_total_paused_time(self) -> float:
        """
        :return: the current total of paused time (with the current pause)
        """
        if self._chrono_paused_since is None:
            return self._paused_time
        else:
            return self._paused_time + time.monotonic() - self._chrono_paused_since

    def get_points_for_lines(self, number_of_lines: int) -> int:
        """
        Computes the number of points that gives the action of destroying <number_of_lines> lines
        """
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

    # ADDERS
    def add_score(self, score_to_add) -> None:
        self._score += score_to_add

    def add_lines_completed(self, lines_completed_to_add: int) -> None:
        self._lines_completed += lines_completed_to_add

    def add_points_for_lines(self, number_of_lines: int) -> None:
        self.add_score(self.get_points_for_lines(number_of_lines))

    # OTHER METHODS
    def run_chrono(self) -> None:
        """
        Quit the pause mod of the chrono and start tracking time
        """
        # we add the current chrono_paused_since
        if self._chrono_paused_since is not None:
            self._paused_time += time.monotonic() - self._chrono_paused_since
        self._chrono_paused_since = None

    def pause_chrono(self) -> None:
        """
        Pause the chrono, so when the game is paused the duration of the game don't change
        """
        # we add the current chrono_paused_since
        if self._chrono_paused_since is not None:
            self._paused_time += time.monotonic() - self._chrono_paused_since
        self._chrono_paused_since = time.monotonic()
