"""
File that contains the declaration of the ActiveTetromino class
"""
import model.shape as m_shape
import common.direction as m_direction
import common.rotation as m_rotation


class ActiveTetromino:
    def __init__(self, shape: m_shape.Shape):
        self._x = 0
        self._y = 0
        self._shape = shape

    # GETTER
    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_shape(self) -> m_shape.Shape:
        return self._shape

    # OTHER METHODS
    def move(self, direction: m_direction.Direction) -> None:
        if direction == m_direction.Direction.DOWN:
            self._y += 1
        elif direction == m_direction.Direction.UP:
            self._y -= 1
        elif direction == m_direction.Direction.LEFT:
            self._x -= 1
        elif direction == m_direction.Direction.RIGHT:
            self._x += 1
        else:
            if isinstance(direction, m_direction.Direction):
                raise ValueError(
                    "Error: impossible to move the active tetromino: invalid direction (%s)" % direction.name
                )
            else:
                raise TypeError(
                    "Error: impossible to move the active tetromino: direction must be a Direction but a %s is given"
                    % type(direction).name
                )

    def rotate(self, rotation: m_rotation.Rotation) -> None:
        # TODO
        pass
