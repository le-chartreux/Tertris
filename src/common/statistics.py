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
            begin_time: typing.Optional[float] = None,
            paused_time: float = 0.0,
            paused: bool = True
    ) -> None:
        """
        Creates a Statistics object, characterized by:
        - a score (starts at 0 and increments during the game)
        - the number of completed lines
        - a begin time (the moment when the game started, or when the Statistics object was created)
        - a paused time (the sum of duration of moments where the game was paused)
        - _timer_paused_since, to manage pauses

        The level is computed with the score, so we don't store it.
        """
        self._score = score
        self._lines_completed = lines_completed
        self._begin_time = time.monotonic() if begin_time is None else begin_time
        self._paused_time = paused_time
        self._timer_paused_since: typing.Optional[float] = time.monotonic() if paused else None

    # GETTERS
    def get_level(self) -> int:
        """
        Computes the level. Since the level increments each 10 lines completed, there is no need to store it as a
        variable
        """
        return 1 + self._lines_completed // 10

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
        if self._timer_paused_since is None:
            return self._paused_time
        else:
            return self._paused_time + time.monotonic() - self._timer_paused_since

    def get_points_for_lines(self, number_of_lines: int) -> int:
        """
        Computes the number of points that gives the action of destroying <number_of_lines> lines.

        :param number_of_lines: integer between 1 and 4
        """
        assert 1 <= number_of_lines <= 4
        correspondence_table = {
            1: 40,
            2: 100,
            3: 300,
            4: 1200
        }
        return correspondence_table[number_of_lines] * self.get_level()

    # ADDERS
    def add_score(self, score_to_add) -> None:
        self._score += score_to_add

    def add_lines_completed(self, lines_completed_to_add: int) -> None:
        self._lines_completed += lines_completed_to_add

    def add_points_for_lines(self, number_of_lines: int) -> None:
        self.add_score(self.get_points_for_lines(number_of_lines))

    # OTHER METHODS
    def run_timer(self) -> None:
        """
        Quit the pause mod of the timer and start tracking time
        """
        # we add the current timer_paused_since
        if self._timer_paused_since is not None:
            self._paused_time += time.monotonic() - self._timer_paused_since
        self._timer_paused_since = None

    def pause_timer(self) -> None:
        """
        Pause the timer, so when the game is paused the duration of the game don't change
        """
        # we add the current timer_paused_since
        if self._timer_paused_since is not None:
            self._paused_time += time.monotonic() - self._timer_paused_since
        self._timer_paused_since = time.monotonic()
