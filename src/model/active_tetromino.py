"""
File that contains the declaration of the ActiveTetromino class
"""
import common.direction as m_direction
import common.rotation as m_rotation
import common.tetromino_type as m_tetromino_type

import model.shape as m_shape
import model.utils as m_utils


class ActiveTetromino(m_shape.Shape):
    def __init__(self, tetromino_type: m_tetromino_type.TetrominoType):
        super(ActiveTetromino, self).__init__(4, 4)
        self._x = 0
        self._y = 0
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

    def rotate(self, rotation: m_rotation.Rotation) -> None:
        """
        Move the tetromino by one box according to the asked rotation

        :param rotation: the rotation the tetromino has to move to
        """
        # TODO
        pass
