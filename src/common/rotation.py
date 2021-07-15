"""
File that contains the declaration of the Rotation class (enumeration)
"""

import enum


class Rotation(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    REVERSE = enum.auto()
