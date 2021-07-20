"""
File that contains configurations used by the view
"""

# dimensions of the displayed part of the grid, in boxes
# it's the last 20 lines that will be displayed, not the 20 first (20 since GRID_HEIGHT_DISPLAYED = 20)
GRID_WIDTH_DISPLAYED = 10
GRID_HEIGHT_DISPLAYED = 20

GRID_WINDOW_BEGIN_X = 1
GRID_WINDOW_BEGIN_Y = 1
GRID_WINDOW_WIDTH = GRID_WIDTH_DISPLAYED * 2 + 2 + 1  # width*2 + border + space to print everything
#                                                    (*2 since tetrominos are 2 bloc width)
GRID_WINDOW_HEIGHT = GRID_HEIGHT_DISPLAYED + 2  # height + borders

NEXT_WINDOW_BEGIN_X = GRID_WINDOW_BEGIN_X + GRID_WINDOW_WIDTH + 2
NEXT_WINDOW_BEGIN_Y = 1
NEXT_WINDOW_WIDTH = 4 * 2 + 2  # width*2 + border (*2 since tetrominos are 2 bloc width)
NEXT_WINDOW_HEIGHT = 2 + 4 + 1  # height + borders + space to print everything

STORED_WINDOW_BEGIN_X = NEXT_WINDOW_BEGIN_X + NEXT_WINDOW_WIDTH + 2
STORED_WINDOW_BEGIN_Y = 1
STORED_WINDOW_WIDTH = 4 * 2 + 2  # width*2 + border (*2 since tetrominos are 2 bloc width)
STORED_WINDOW_HEIGHT = 2 + 4 + 1  # height + borders + space to print everything

STATISTICS_WINDOW_BEGIN_X = GRID_WINDOW_BEGIN_X + GRID_WINDOW_WIDTH + 2
STATISTICS_WINDOW_BEGIN_Y = NEXT_WINDOW_BEGIN_Y + NEXT_WINDOW_HEIGHT
STATISTICS_WINDOW_WIDTH = 18 + 2 + 2  # statistics + border
STATISTICS_WINDOW_HEIGHT = 4 + 2 + 1  # height + borders + space to print everything

KEYBINDS_WINDOW_BEGIN_X = GRID_WINDOW_BEGIN_X + GRID_WINDOW_WIDTH + 2
KEYBINDS_WINDOW_BEGIN_Y = STATISTICS_WINDOW_BEGIN_Y + STATISTICS_WINDOW_HEIGHT
KEYBINDS_WINDOW_WIDTH = 18 + 2 + 2  # keymaps + borders
KEYBINDS_WINDOW_HEIGHT = 8 + 2 + 1  # Keymaps + borders + space to print everything
