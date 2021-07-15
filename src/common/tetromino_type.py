"""
File that contains the declaration of the TetrominoType class (enumeration)
"""

import enum


class TetrominoType(enum.Enum):
    I_SHAPE = enum.auto()
    O_SHAPE = enum.auto()
    T_SHAPE = enum.auto()
    L_SHAPE = enum.auto()
    J_SHAPE = enum.auto()
    Z_SHAPE = enum.auto()
    S_SHAPE = enum.auto()
