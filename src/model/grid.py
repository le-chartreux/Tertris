"""
File that contains the declaration of the Shape class
"""

import model.active_tetromino as m_active_tetromino
import model.shape as m_shape

import model.config as m_config


class Grid(m_shape.Shape):
    def __init__(self):
        super().__init__(m_config.GRID_HEIGHT, m_config.GRID_WIDTH)

    def add_tetromino(self, active_tetromino: m_active_tetromino.ActiveTetromino) -> None:
        """
        Includes the active tetromino to the grid
        """
        self.set_boxes(
            self.combine(
                active_tetromino,
                active_tetromino.get_x(),
                active_tetromino.get_y()
            ).get_boxes()
        )

    def is_line_full(self, line_number: int) -> bool:
        """
        :return: if the asked line is full (no empty boxes)
        """
        column_number = 0
        while column_number < self.get_width() and self.is_occupied(column_number, line_number):
            column_number += 1
        return column_number == self.get_width()

    def drop_lines_upper(self, line_number: int) -> None:
        """
        Replaces each line higher than <line_number> by it's higher.
        The first line of the grid will become empty.
        The line <line_number> is included.

        :param line_number: number of the first line to replace by it's higher
        """
        # replaces each line higher than <line_number> by it's higher
        line = line_number
        while line != 0:
            # TODO faire quelque chose de plus propre
            self.get_boxes()[line][:] = self.get_boxes()[line - 1][:]
            line -= 1
        # We put None on the higher line
        for column in range(self.get_width()):
            self.set_box(None, column, 0)
