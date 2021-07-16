"""
File that contains various utils for the views
"""

import curses
import locale

import common.tetromino_type as m_tetromino_type
import view.color_pair as m_color_pair


def setup_curses() -> None:
    """
    Setup curses to we can correctly use it
    """
    locale.setlocale(locale.LC_ALL, "")
    curses.curs_set(0)  # don't show cursor
    curses.noecho()  # don't show what is writen by the user
    curses.cbreak()  # don't wait that the user presses Enter to read what they write


def revert_curses() -> None:
    """
    Reset curses to it's original settings, then quit
    """
    curses.curs_set(1)
    curses.nocbreak()
    curses.echo()
    curses.endwin()


def set_colorscheme() -> None:
    """
    Setup the color system
    """
    curses.start_color()

    curses.init_pair(m_color_pair.ColorPair.I_COLOR.value, curses.COLOR_CYAN, curses.COLOR_WHITE)
    curses.init_pair(m_color_pair.ColorPair.O_COLOR.value, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(m_color_pair.ColorPair.T_COLOR.value, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
    curses.init_pair(m_color_pair.ColorPair.L_COLOR.value, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(m_color_pair.ColorPair.J_COLOR.value, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(m_color_pair.ColorPair.Z_COLOR.value, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(m_color_pair.ColorPair.S_COLOR.value, curses.COLOR_GREEN, curses.COLOR_WHITE)

    curses.init_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(m_color_pair.ColorPair.RED_N_BLUE.value, curses.COLOR_RED, curses.COLOR_BLUE)
    curses.init_pair(m_color_pair.ColorPair.BLACK_N_BLUE.value, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(m_color_pair.ColorPair.BLACK_N_BLACK.value, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(m_color_pair.ColorPair.RED_N_WHITE.value, curses.COLOR_RED, curses.COLOR_WHITE)


def get_color_pair(tetromino_type: m_tetromino_type.TetrominoType) -> m_color_pair.ColorPair:
    """
    :param tetromino_type: type of the tetromino that we want to know the color
    :return: the color pair linked to this tetromino type
    """
    if tetromino_type == m_tetromino_type.TetrominoType.I_SHAPE:
        return m_color_pair.ColorPair.I_COLOR
    elif tetromino_type == m_tetromino_type.TetrominoType.O_SHAPE:
        return m_color_pair.ColorPair.O_COLOR
    elif tetromino_type == m_tetromino_type.TetrominoType.T_SHAPE:
        return m_color_pair.ColorPair.T_COLOR
    elif tetromino_type == m_tetromino_type.TetrominoType.L_SHAPE:
        return m_color_pair.ColorPair.L_COLOR
    elif tetromino_type == m_tetromino_type.TetrominoType.J_SHAPE:
        return m_color_pair.ColorPair.J_COLOR
    elif tetromino_type == m_tetromino_type.TetrominoType.Z_SHAPE:
        return m_color_pair.ColorPair.Z_COLOR
    elif tetromino_type == m_tetromino_type.TetrominoType.S_SHAPE:
        return m_color_pair.ColorPair.S_COLOR
