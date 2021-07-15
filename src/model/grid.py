"""
File that contains the declaration of the Shape class
"""

import typing
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
