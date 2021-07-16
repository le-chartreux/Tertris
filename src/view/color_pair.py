"""
File that defines ColorPair, enum to identify colors
"""
import enum


class ColorPair(enum.Enum):
    I_COLOR = 1
    O_COLOR = 2
    T_COLOR = 3
    L_COLOR = 4
    J_COLOR = 5
    Z_COLOR = 6
    S_COLOR = 7

    BLACK_N_WHITE = 8
    RED_N_BLUE = 9
    BLACK_N_BLUE = 10
    BLACK_N_BLACK = 11
    RED_N_WHITE = 12
