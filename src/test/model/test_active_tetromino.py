import unittest
import random

import model.active_tetromino as m_active_tetromino
import model.utils as m_utils
import model.config as m_config

import common.tetromino_type as m_tetromino_type
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

    def test_get_spawn_location_x(self) -> None:
        for tetromino_type in m_tetromino_type.TetrominoType.__iter__():
            if tetromino_type in (m_tetromino_type.TetrominoType.I_SHAPE, m_tetromino_type.TetrominoType.O_SHAPE):
                # the I and O spawn in the middle columns
                self.assertEqual(
                    m_active_tetromino.ActiveTetromino.get_spawn_location_x(tetromino_type),
                    (m_config.GRID_WIDTH // 2) - (4 // 2)
                )
            else:
                # the rest spawn in the left-middle columns
                self.assertEqual(
                    m_active_tetromino.ActiveTetromino.get_spawn_location_x(tetromino_type),
                    (m_config.GRID_WIDTH // 2) - (4 // 2) - 1
                )

    def test_put_at_spawnpoint(self) -> None:
        for tetromino_type in m_tetromino_type.TetrominoType.__iter__():
            active = m_active_tetromino.ActiveTetromino(tetromino_type)
            active.put_at_spawnpoint()

            self.assertEqual(
                active.get_x(),
                active.get_spawn_location_x(tetromino_type)
            )
            self.assertEqual(
                active.get_y(),
                m_config.SPAWN_LINE
            )


if __name__ == '__main__':
    unittest.main()
