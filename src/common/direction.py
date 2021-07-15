"""
File that contains the declaration of the Direction class (enumeration)
"""

import enum


class Direction(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()

    def get_x_variation(self) -> int:
        """
        :return: how the horizontal position of the object will change by going to this direction
        """
        if self == Direction.LEFT:
            return -1
        elif self == Direction.RIGHT:
            return 1
        else:
            return 0

    def get_y_variation(self) -> int:
        """
        :return: how the vertical position of the object will change by going to this direction
        """
        if self == Direction.UP:
            return -1
        elif self == Direction.DOWN:
            return 1
        else:
            return 0
