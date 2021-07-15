"""
File that contains the declaration of the Direction class (enumeration)
"""

import enum


class Direction(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()
