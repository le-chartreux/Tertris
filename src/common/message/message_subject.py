"""
File that contains the declaration of the MessageSubject class (enumeration)
"""

import enum


class MessageSubject(enum.Enum):
    TOGGL_PAUSED = enum.auto()
    MOVE_ACTIVE_TETROMINO = enum.auto()
    ROTATE_ACTIVE_TETROMINO = enum.auto()
    TOGGLE_STORED = enum.auto()
    QUIT = enum.auto()
