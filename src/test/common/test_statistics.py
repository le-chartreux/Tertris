import unittest
import common.statistics as m_statistics
import time
import random


class TestStatistics(unittest.TestCase):

    def setUp(self) -> None:
        self._default_stats = m_statistics.Statistics()

    def tearDown(self) -> None:
        # resetting default stats to it's initial state
        self._default_stats = m_statistics.Statistics()

    def test_get_level(self) -> None:
        for level in range(1, 31):
            for line in range(10):
                # at the beginning of a game, should be 1, then at
                # each 10 new lines the level should be incremented
                self.assertEqual(self._default_stats.get_level(), level, "Should be %i" % level)
                self._default_stats.add_lines_completed(1)

    # warning: this testing will last 9 seconds so it is commented
    """
    def test_get_duration(self) -> None:
        # testing without pause time
        # there is no pause at init, so the duration is just <int(end_time - self._begin_time)>
        for ds in range(30):
            end_time = time.monotonic()
            last_result = self._default_stats.get_duration(end_time)
            self.assertEqual(
                last_result,
                int(end_time - self._default_stats._begin_time)
            )
            # checking that the result is logic
            self.assertIn(
                last_result,
                (ds // 10, ds // 10 + 1),
                "Should be around %i and %i since it init %i ds ago" % (ds // 10, ds // 10 + 1, ds)
            )
            time.sleep(0.1)

        # testing with pause time
        total_duration = self._default_stats.get_duration()
        for pause_number in range(4):
            # 4 pauses: one of 0 sec, one of 1 sec, one of 2 sec and one of 3 sec
            # the total duration should not change
            self._default_stats.pause_chrono()
            time.sleep(pause_number)
            # between 2 values to counter the case where the loop process lasts enough to add 1 sec
            self.assertIn(
                total_duration,
                (self._default_stats.get_duration(), self._default_stats.get_duration() + 1)
            )
            self._default_stats.run_chrono()
    """

if __name__ == '__main__':
    unittest.main()
