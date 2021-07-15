"""
File that contains the declaration of the Shape class
"""

import model.active_tetromino as m_active_tetromino
import model.shape as m_shape


class Grid:
    def __init__(self):
        self.shape = m_shape.Shape(40, 10)

    def add_tetromino(self, active_tetromino: m_active_tetromino.ActiveTetromino) -> None:
        """
        Includes the active tetromino to the grid
        """
        self.set_shape(
            self.shape.combine(
                active_tetromino.get_shape(),
                active_tetromino.get_x(),
                active_tetromino.get_y()
            )
        )

    # GETTERS
    def get_shape(self) -> m_shape.Shape:
        return self.shape

    # SETTERS
    def set_shape(self, new_shape: m_shape.Shape) -> None:
        self.shape = new_shape

    def is_line_full(self, line_number: int) -> bool:
        """
        :return: if the asked line is full (no empty boxes)
        """
        column_number = 0
        while column_number <= self.get_shape().get_width() and self.shape.is_occupied(column_number, line_number):
            column_number += 1
        return column_number == self.get_shape().get_width()

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
            self.shape.get_boxes()[line][:] = self.shape.get_boxes()[line - 1][:]
            line -= 1
        # We put None on the higher line
        for column in range(self.shape.get_width()):
            self.shape.get_boxes()[0][column] = None
