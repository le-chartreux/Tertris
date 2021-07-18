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
        self.set_boxes(m_utils.get_tetromino_shape(tetromino_type).get_boxes())
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
        new_shape = m_shape.Shape(4, 4)

        if rotation == m_rotation.Rotation.RIGHT:
            for y in range(4):
                for x in range(4):
                    new_shape.set_box(
                        self.get_box(x, y),
                        3 - y,
                        x
                    )
        elif rotation == m_rotation.Rotation.LEFT:
            for y in range(4):
                for x in range(4):
                    new_shape.set_box(
                        self.get_box(x, y),
                        y,
                        3 - x
                    )
        elif rotation == m_rotation.Rotation.REVERSE:
            for y in range(4):
                for x in range(4):
                    new_shape.set_box(
                        self.get_box(x, y),
                        3 - x,
                        3 - y
                    )
        else:
            if isinstance(rotation, m_rotation.Rotation):
                raise ValueError(
                    "Error: invalid rotation given: name = %s; value = %s" % (rotation.name, rotation.value)
                )
            else:
                raise ValueError(
                    "Error: invalid rotation given: type must be Rotation but a %s is given" % type(rotation)
                )

        self.set_boxes(new_shape.get_boxes())
