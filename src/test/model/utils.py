"""
File that contains various utils for testing
"""
import random

import model.grid as m_grid
import model.active_tetromino as m_active_tetromino
import model.utils as m_utils


def fill_grid_with_tetrominos(grid: m_grid.Grid, number_of_tetromino: int) -> None:
    for _ in range(number_of_tetromino):
        tetromino_to_add = m_active_tetromino.ActiveTetromino(m_utils.random_tetromino())
        tetromino_to_add._x = random.randint(0, grid.get_width() - 4)  # -4 since it's the max size of tetromino
        tetromino_to_add._y = random.randint(0, grid.get_height() - 4)  # -4 since it's the max size of tetromino

        grid.add_tetromino(tetromino_to_add)
