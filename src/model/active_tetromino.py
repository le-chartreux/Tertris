"""
File that contains the declaration of the ActiveTetromino class
"""
import common.direction as m_direction
import common.tetromino_type as m_tetromino_type

import model.shape as m_shape
import model.utils as m_utils

import model.config as m_config


class ActiveTetromino(m_shape.Shape):
    def __init__(self, tetromino_type: m_tetromino_type.TetrominoType):
        shape = m_utils.get_tetromino_shape(tetromino_type)
        super(ActiveTetromino, self).__init__(shape.get_height(), shape.get_width())
        self.set_boxes(shape.get_boxes())
        self._x = self.get_spawn_location_y(tetromino_type)
        self._y = 19
        self._type = tetromino_type

    # GETTER
    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_tetromino_type(self) -> m_tetromino_type.TetrominoType:
        return self._type

    # OTHER METHODS
    def move(self, direction: m_direction.Direction) -> None:
        """
        Move the tetromino by one box according to the asked direction

        :param direction: the direction the tetromino has to move to
        """
        self._x += direction.get_x_variation()
        self._y += direction.get_y_variation()

    @staticmethod
    def get_spawn_location_y(tetromino_type: m_tetromino_type.TetrominoType) -> int:
        """
        :param tetromino_type:
        :return:
        """
        if tetromino_type in (m_tetromino_type.TetrominoType.I_SHAPE, m_tetromino_type.TetrominoType.O_SHAPE):
            # the I and O spawn in the middle columns
            return (m_config.GRID_WIDTH // 2) - (4 // 2)
        else:
            # the rest spawn in the left-middle columns
            return (m_config.GRID_WIDTH // 2) - (4 // 2) - 1
