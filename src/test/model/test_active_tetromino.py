import unittest
import random

import model.active_tetromino as m_active_tetromino
import model.utils as m_utils

import common.direction as m_direction


class TestDirection(unittest.TestCase):
    def test_move(self) -> None:
        for _ in range(20):
            tetromino = m_active_tetromino.ActiveTetromino(
                m_utils.random_tetromino()
            )
            for _ in range(10):
                direction: m_direction.Direction = random.choice([
                    direction for direction in m_direction.Direction.__iter__()
                ])
                before_move_x = tetromino.get_x()
                before_move_y = tetromino.get_y()

                tetromino.move(direction)

                # we assume that get_x_variation & get_y_variation works since
                # they have a test
                self.assertEqual(
                    before_move_x + direction.get_x_variation(),
                    tetromino.get_x()
                )

                self.assertEqual(
                    before_move_y + direction.get_y_variation(),
                    tetromino.get_y()
                )


if __name__ == '__main__':
    unittest.main()
