"""
File that contains the declaration of the MessageSubject class (enumeration)
"""

import enum


class MessageSubject(enum.Enum):
    PAUSE = enum.auto()
    RUN = enum.auto()
    MOVE_ACTIVE_TETROMINO = enum.auto()
    ROTATE_ACTIVE_TETROMINO = enum.auto()
    TOGGLE_STORED = enum.auto()
