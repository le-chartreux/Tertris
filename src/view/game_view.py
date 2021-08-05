"""
File that contains the declaration of the GameView class
"""

import curses
import locale  # to encode non-ASCII char

import math  # to compute the number of ═ to put on border

import view
import view.utils as m_utils
import view.color_pair as m_color_pair
import view.player_input as m_player_input

import common.message as m_message
import common.message.message_subject as m_message_subject
import common.direction as m_direction
import common.rotation as m_rotation

import view.config as config

import model as m_model


class GameView(view.View):
    def __init__(
            self,
            model: m_model.Model
    ) -> None:
        """
        Creates a GameView, heir of View, that adds:
        - a game window (_window_game)
        - a next tetromino window (_window_next)
        - a stored tetromino window (_window_stored)
        - a statistics window (_window_statistics)
        - a keymap window (_window_keymaps)
        """
        view.View.__init__(self, model)

        self._window_game = curses.newwin(
            config.GRID_WINDOW_HEIGHT,
            config.GRID_WINDOW_WIDTH,
            config.GRID_WINDOW_BEGIN_Y,
            config.GRID_WINDOW_BEGIN_X
        )

        self._window_next = curses.newwin(
            config.NEXT_WINDOW_HEIGHT,
            config.NEXT_WINDOW_WIDTH,
            config.NEXT_WINDOW_BEGIN_Y,
            config.NEXT_WINDOW_BEGIN_X
        )

        self._window_stored = curses.newwin(
            config.STORED_WINDOW_HEIGHT,
            config.STORED_WINDOW_WIDTH,
            config.STORED_WINDOW_BEGIN_Y,
            config.STORED_WINDOW_BEGIN_X
        )

        self._window_statistics = curses.newwin(
            config.STATISTICS_WINDOW_HEIGHT,
            config.STATISTICS_WINDOW_WIDTH,
            config.STATISTICS_WINDOW_BEGIN_Y,
            config.STATISTICS_WINDOW_BEGIN_X
        )

        self._window_keybinds = curses.newwin(
            config.KEYBINDS_WINDOW_HEIGHT,
            config.KEYBINDS_WINDOW_WIDTH,
            config.KEYBINDS_WINDOW_BEGIN_Y,
            config.KEYBINDS_WINDOW_BEGIN_X
        )

    def _set_backgrounds(self) -> None:
        view.View._set_backgrounds(self)
        self._window_game.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_next.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_stored.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_statistics.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_keybinds.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))

        self._refresh_all()

    def _print_static_windows(self) -> None:
        self._print_grid_border()
        self._print_next_border()
        self._print_stored_border()
        self._print_statistics_border()
        self._print_keybinds()
        self._print_keybinds_border()

    def _print_active_windows(self) -> None:
        self._print_grid()
        self._print_next()
        self._print_stored()
        self._print_statistics()

    def _print_grid(self) -> None:
        """
        Show the game grid
        """
        grid = self._model.get_grid_with_active()

        for (line_number_print, line_number_grid) in zip(
                range(config.GRID_HEIGHT_DISPLAYED),
                range(len(grid) - config.GRID_HEIGHT_DISPLAYED, len(grid))
        ):
            for (column_number_print, column_number_grid) in zip(
                    range(config.GRID_WIDTH_DISPLAYED),
                    range(len(grid[0]) - config.GRID_WIDTH_DISPLAYED, len(grid[0]))
            ):
                if grid[line_number_grid][column_number_grid] is not None:
                    # we put a bloc
                    self._window_game.addstr(
                        line_number_print + 1,
                        column_number_print * 2 + 1,  # *2 since tetrominos are 2 char wide
                        "██".encode(locale.getpreferredencoding()),
                        curses.color_pair(m_utils.get_color_pair(grid[line_number_grid][column_number_grid]).value)
                    )
                else:
                    # we put a space to hide a potential old bloc
                    self._window_game.addstr(
                        line_number_print + 1,
                        column_number_print * 2 + 1,  # *2 since tetrominos are 2 char wide
                        "  ",
                        curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                    )

        self._window_game.refresh()

    def _print_grid_border(self) -> None:
        """
        Shows the border around the game grid
        """
        # first line
        self._window_game.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.GRID_WINDOW_WIDTH - 2):
            self._window_game.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_game.addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        # intermediate lines
        for line in range(1, config.GRID_WINDOW_HEIGHT - 1):
            self._window_game.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_game.addstr(
                line, config.GRID_WINDOW_WIDTH - 2,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_game.addstr(
            config.GRID_WINDOW_HEIGHT - 1, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.GRID_WINDOW_WIDTH - 2):
            self._window_game.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_game.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_game.refresh()

    def _print_next(self) -> None:
        """
        Shows the next tetromino in the next window
        """
        # cleaning the board
        for line in range(4):
            for column in range(4):
                # we put a space to hide a potential old bloc
                self._window_next.addstr(
                    line + 1,
                    column * 2 + 1,
                    "  ".encode(locale.getpreferredencoding()),  # *2 since tetrominos are 2 char wide
                    curses.A_BOLD | curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                )

        next_tetromino, next_shape = self._model.get_next_tetromino_info()
        for line in range(len(next_shape)):
            for column in range(len(next_shape[0])):
                if next_shape[line][column] is not None:
                    # we put a bloc
                    self._window_next.addstr(
                        line + 1,
                        column * 2 + 1,  # *2 since tetrominos are 2 char wide
                        "██".encode(locale.getpreferredencoding()),
                        curses.color_pair(m_utils.get_color_pair(next_tetromino).value)
                    )
                else:
                    # we put a space to hide a potential old bloc
                    self._window_next.addstr(
                        line + 1,
                        column * 2 + 1,
                        "  ".encode(locale.getpreferredencoding()),  # *2 since tetrominos are 2 char wide
                        curses.A_BOLD | curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                    )

        self._window_next.refresh()

    def _print_next_border(self) -> None:
        """
        Shows the border around the next tetromino grid
        """
        # first line
        self._window_next.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.ceil((config.NEXT_WINDOW_WIDTH - 4 - 2) / 2)):  # -4 car Next, -1 car ╗
            self._window_next.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_next.addstr(
            "Next",  # only ASCII so no need en encode
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.floor((config.NEXT_WINDOW_WIDTH - 4 - 2) / 2)):  # -4 car Next, -1 car ╗
            self._window_next.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_next.addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        # intermediate lines
        for line in range(1, config.NEXT_WINDOW_HEIGHT - 2):
            self._window_next.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_next.addstr(
                line, config.NEXT_WINDOW_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_next.addstr(
            config.NEXT_WINDOW_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.NEXT_WINDOW_WIDTH - 1):
            self._window_next.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_next.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_next.refresh()

    def _print_stored(self):
        """
        Show the stored tetromino window, with the stored tetromino if exists
        """
        # cleaning the board
        for line in range(4):
            for column in range(4):
                # we put a space to hide a potential old bloc
                self._window_stored.addstr(
                    line + 1,
                    column * 2 + 1,
                    "  ",  # only ASCII so no need to encode
                    curses.A_BOLD | curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                )

        stored_tetromino, stored_shape = self._model.get_stored_tetromino_info()
        if stored_tetromino is not None:
            for line in range(len(stored_shape)):
                for column in range(len(stored_shape[0])):
                    if stored_shape[line][column] is not None:
                        self._window_stored.addstr(
                            line + 1,
                            column * 2 + 1,
                            "██".encode(locale.getpreferredencoding()),
                            curses.color_pair(m_utils.get_color_pair(stored_tetromino).value)
                        )

        self._window_stored.refresh()

    def _print_stored_border(self) -> None:
        """
        Shows the border around the stored tetromino border
        """
        # first line
        self._window_stored.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.ceil((config.STORED_WINDOW_WIDTH - 6 - 2) / 2)):  # -6 car Stored, -2 car ╔ et ╗
            self._window_stored.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_stored.addstr(
            "Stored",
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.floor((config.STORED_WINDOW_WIDTH - 6 - 2) / 2)):  # -6 car Stored, -2 car ╔ et ╗
            self._window_stored.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_stored.addstr("╗", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))

        # intermediate lines
        for line in range(1, config.STORED_WINDOW_HEIGHT - 2):
            self._window_stored.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_stored.addstr(
                line, config.STORED_WINDOW_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_stored.addstr(
            config.STORED_WINDOW_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.STORED_WINDOW_WIDTH - 1):
            self._window_stored.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_stored.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_stored.refresh()

    def _print_statistics(self) -> None:
        """
        Shows statistics on the statistic window
        """
        statistics = self._model.get_statistics()
        self._window_statistics.addstr(1, 2, "Level: " + str(statistics.get_level()))
        self._window_statistics.addstr(2, 2, "Score: " + str(statistics.get_score()))
        self._window_statistics.addstr(3, 2, "Lines: " + str(statistics.get_lines_completed()))
        self._window_statistics.addstr(4, 2, "Time: " + str(statistics.get_duration()))

        self._window_statistics.refresh()

    def _print_statistics_border(self) -> None:
        """
        Shows the border around the statistics window
        """
        # first line
        self._window_statistics.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.ceil((config.STATISTICS_WINDOW_WIDTH - 10 - 2) / 2)):  # -10 car Statistics, -2 car ╔ et ╗
            self._window_statistics.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_statistics.addstr("Statistics", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        for _ in range(math.floor((config.STATISTICS_WINDOW_WIDTH - 10 - 2) / 2)):  # -10 car Statistics, -2 car ╔ et ╗
            self._window_statistics.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_statistics.addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        # intermediate lines
        for line in range(1, config.STATISTICS_WINDOW_HEIGHT - 2):
            self._window_statistics.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_statistics.addstr(
                line, config.STATISTICS_WINDOW_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_statistics.addstr(
            config.STATISTICS_WINDOW_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.STATISTICS_WINDOW_WIDTH - 1):
            self._window_statistics.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_statistics.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_statistics.refresh()

    def _print_keybinds(self) -> None:
        """
        Shows keybinds
        """
        self._window_keybinds.addstr(1, 2, "Arrow-left: Left")
        self._window_keybinds.addstr(2, 2, "Arrow-right: Right")
        self._window_keybinds.addstr(3, 2, "Arrow-down: Down")

        self._window_keybinds.addstr(4, 2, "Q: Rotate left")
        self._window_keybinds.addstr(5, 2, "D: Rotate right")
        self._window_keybinds.addstr(6, 2, "S: Store actual")

        self._window_keybinds.addstr(7, 2, "P: Pause")
        self._window_keybinds.addstr(8, 2, "Esc: Quit")

        self._window_keybinds.refresh()

    def _print_keybinds_border(self) -> None:
        """
        Show the border around the keybinds
        """
        # first line
        self._window_keybinds.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.ceil((config.KEYBINDS_WINDOW_WIDTH - 8 - 2) / 2)):  # -8 car Keybinds, -2 car ╔ et ╗
            self._window_keybinds.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_keybinds.addstr("Keybinds", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        for _ in range(math.floor((config.KEYBINDS_WINDOW_WIDTH - 8 - 2) / 2)):  # -8 car Keybinds, -2 car ╔ et ╗
            self._window_keybinds.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_keybinds.addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        # intermediate lines
        for line in range(1, config.KEYBINDS_WINDOW_HEIGHT - 2):
            self._window_keybinds.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_keybinds.addstr(
                line, config.KEYBINDS_WINDOW_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_keybinds.addstr(
            config.KEYBINDS_WINDOW_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.KEYBINDS_WINDOW_WIDTH - 1):
            self._window_keybinds.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_keybinds.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_keybinds.refresh()

    def _treat_player_input(self, player_input: m_player_input.PlayerInput) -> None:
        super(GameView, self)._treat_player_input(player_input)

        # moves
        if player_input == m_player_input.PlayerInput.KEY_LEFT:
            self._send(
                m_message.Message(
                    m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO,
                    m_direction.Direction.LEFT
                )
            )
        elif player_input == m_player_input.PlayerInput.KEY_RIGHT:
            self._send(
                m_message.Message(
                    m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO,
                    m_direction.Direction.RIGHT
                )
            )
        elif player_input == m_player_input.PlayerInput.KEY_DOWN:
            self._send(
                m_message.Message(
                    m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO,
                    m_direction.Direction.DOWN
                )
            )
        # rotations
        elif player_input == m_player_input.PlayerInput.KEY_Q:
            self._send(
                m_message.Message(
                    m_message_subject.MessageSubject.ROTATE_ACTIVE_TETROMINO,
                    m_rotation.Rotation.LEFT
                )
            )
        elif player_input == m_player_input.PlayerInput.KEY_D:
            self._send(
                m_message.Message(
                    m_message_subject.MessageSubject.ROTATE_ACTIVE_TETROMINO,
                    m_rotation.Rotation.RIGHT
                )
            )
        # store
        elif player_input == m_player_input.PlayerInput.KEY_S:
            self._send(
                m_message.Message(
                    m_message_subject.MessageSubject.TOGGLE_STORED
                )
            )
        # controls
        elif player_input == m_player_input.PlayerInput.KEY_P:
            self._send(
                m_message.Message(
                    m_message_subject.MessageSubject.TOGGL_PAUSED
                )
            )
