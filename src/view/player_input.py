"""
File that contains the declaration of the PlayerInput class (enum)
"""

import enum
import curses  # for curses constants


class PlayerInput(enum.Enum):
    NOTHING = curses.ERR

    KEY_LEFT = curses.KEY_LEFT
    KEY_RIGHT = curses.KEY_RIGHT
    KEY_UP = curses.KEY_UP
    KEY_DOWN = curses.KEY_DOWN

    # characters can only be in lowercase for simplicity
    KEY_D = 100
    KEY_P = 112
    KEY_Q = 113
    KEY_S = 115

    KEY_ESC = 27

    # Entry key can change between terminals
    KEY_ENTER_1 = curses.KEY_ENTER
    KEY_ENTER_2 = 10
    KEY_ENTER_3 = 13

    KEY_UNUSED = -9999
