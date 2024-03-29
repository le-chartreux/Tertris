"""
File that contains configurations used by the view
"""

# dimensions of the displayed part of the grid, in boxes
# it's the last 20 lines that will be displayed, not the 20 first (20 since GRID_HEIGHT_DISPLAYED = 20)
GRID_WIDTH_DISPLAYED = 10
GRID_HEIGHT_DISPLAYED = 20

# due to curses limitations, we can't print char on the lower-left corner of a window, so

GRID_WINDOW_BEGIN_X = 2
GRID_WINDOW_BEGIN_Y = 2
GRID_WINDOW_WIDTH = GRID_WIDTH_DISPLAYED * 2  # width*2 (*2 since tetrominos are 2 bloc width)
GRID_WINDOW_HEIGHT = GRID_HEIGHT_DISPLAYED

NEXT_WINDOW_BEGIN_X = 27
NEXT_WINDOW_BEGIN_Y = 1
NEXT_WINDOW_WIDTH = 4 * 2
NEXT_WINDOW_HEIGHT = 4

STORED_WINDOW_BEGIN_X = 39
STORED_WINDOW_BEGIN_Y = 1
STORED_WINDOW_WIDTH = 4 * 2  # width*2 (*2 since tetrominos are 2 bloc width)
STORED_WINDOW_HEIGHT = 4

STATISTICS_WINDOW_BEGIN_X = 27
STATISTICS_WINDOW_BEGIN_Y = 8
STATISTICS_WINDOW_WIDTH = 20
STATISTICS_WINDOW_HEIGHT = 4
