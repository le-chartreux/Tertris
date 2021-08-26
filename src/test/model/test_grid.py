import unittest
import random

import model.grid as m_grid
import model.active_tetromino as m_active_tetromino
import model.utils as m_utils


class TestGrid(unittest.TestCase):

    def test_add_tetromino(self) -> None:
        for _ in range(50):
            grid = m_grid.Grid()
            for _ in range(10):
                active = m_active_tetromino.ActiveTetromino(m_utils.random_tetromino())

                pos_x = random.randint(0, grid.get_width() - active.get_width() - 1)
                pos_y = random.randint(0, grid.get_height() - active.get_height() - 1)

                active._x = pos_x
                active._y = pos_y

                after_add_grid = m_grid.Grid()
                after_add_grid.set_boxes(grid.copy_shape().get_boxes())
                after_add_grid.add_tetromino(active)

                for x in range(active.get_width()):
                    for y in range(active.get_height()):
                        already_occupied = grid.is_occupied(pos_x + x, pos_y + y)
                        self.assertEqual(
                            active.is_occupied(x, y) or already_occupied,
                            after_add_grid.is_occupied(pos_x + x, pos_y + y)
                        )

                grid.set_boxes(after_add_grid.get_boxes())

    def test_is_line_full(self) -> None:
        for _ in range(50):
            grid = m_grid.Grid()

            line_to_test = random.randint(0, grid.get_height() - 1)
            tetromino_type = m_utils.random_tetromino()

            column_index_to_fill = list(range(grid.get_width()))
            random.shuffle(column_index_to_fill)

            number_of_columns_to_leave_empty = random.randint(0, grid.get_width() - 1)
            for _ in range(number_of_columns_to_leave_empty):
                column_index_to_fill.pop()

            for x_to_put in column_index_to_fill:
                grid.set_box(tetromino_type, x_to_put, line_to_test)

            self.assertTrue(
                (
                        number_of_columns_to_leave_empty == 0
                        and
                        grid.is_line_full(line_to_test)
                )
                or
                (
                        number_of_columns_to_leave_empty != 0
                        and
                        not grid.is_line_full(line_to_test)
                )
            )

    def test_drop_lines_upper(self) -> None:
        for _ in range(50):
            grid = m_grid.Grid()
            tetromino = m_utils.random_tetromino()
            line_to_drop = random.randint(0, grid.get_height() - 1)

            # filling the grid
            for _ in range(random.randint(0, 20)):
                grid.set_box(
                    tetromino,
                    random.randint(0, grid.get_width() - 5),
                    random.randint(0, grid.get_height() - 5)
                )

            # creating a copy and making it drop, so we can compare
            # with the original
            grid_after_drop = m_grid.Grid()
            grid_after_drop.set_boxes(grid.copy_shape().get_boxes())
            grid_after_drop.drop_lines_upper(line_to_drop)

            # checking that the grid dropped correctly
            for x in range(grid.get_width()):
                for y in range(0, line_to_drop):
                    self.assertEqual(
                        grid.get_box(x, y),
                        grid_after_drop.get_box(x, y + 1)
                    )
            # checking that the first line is empty
            for x in range(grid_after_drop.get_width()):
                self.assertFalse(
                    grid_after_drop.is_occupied(x, 0)
                )


if __name__ == '__main__':
    unittest.main()
