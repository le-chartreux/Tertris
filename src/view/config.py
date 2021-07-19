"""
File that contains configurations used by the view
"""

import common.config as config_general


GRID_BEGIN_X = 1
GRID_BEGIN_Y = 1
GRID_WIDTH = config_general.GRID_WIDTH * 2 + 2 + 1  # width*2 + border + space to print everything
#                                                    (*2 since tetrominos are 2 bloc width)
GRID_HEIGHT = config_general.GRID_HEIGHT + 2  # height + borders

NEXT_BEGIN_X = GRID_BEGIN_X + GRID_WIDTH + 2
NEXT_BEGIN_Y = 1
NEXT_WIDTH = 4 * 2 + 2  # width*2 + border (*2 since tetrominos are 2 bloc width)
NEXT_HEIGHT = 2 + 4 + 1  # height + borders + space to print everything

STORED_BEGIN_X = NEXT_BEGIN_X + NEXT_WIDTH + 2
STORED_BEGIN_Y = 1
STORED_WIDTH = 4 * 2 + 2  # width*2 + border (*2 since tetrominos are 2 bloc width)
STORED_HEIGHT = 2 + 4 + 1  # height + borders + space to print everything

STATISTICS_BEGIN_X = GRID_BEGIN_X + GRID_WIDTH + 2
STATISTICS_BEGIN_Y = NEXT_BEGIN_Y + NEXT_HEIGHT
STATISTICS_WIDTH = 18 + 2 + 2  # statistics + border
STATISTICS_HEIGHT = 4 + 2 + 1  # height + borders + space to print everything

KEYBINDS_BEGIN_X = GRID_BEGIN_X + GRID_WIDTH + 2
KEYBINDS_BEGIN_Y = STATISTICS_BEGIN_Y + STATISTICS_HEIGHT
KEYBINDS_WIDTH = 18 + 2 + 2  # keymaps + borders
KEYBINDS_HEIGHT = 8 + 2 + 1  # Keymaps + borders + space to print everything
