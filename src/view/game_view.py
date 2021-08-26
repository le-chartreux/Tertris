"""
File that contains the declaration of the GameView class
"""

import curses
import _curses
import locale  # to encode non-ASCII char

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

    def set_background_colors(self) -> None:
        super(GameView, self).set_background_colors()
        self._window_game.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_statistics.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_next.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_stored.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_keybinds.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))

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

                    # in a try-catch because if the terminal is too small it will creates an error
                    # & curses raises an error when printing in the bottom-right corner
                    try:
                        # next comment because addstr is supposed to take str, but we use bytes to get a proper encoding
                        # noinspection PyTypeChecker
                        self._window_game.addstr(
                            line_number_print,
                            column_number_print * 2,  # *2 since tetrominos are 2 char wide
                            "██".encode(locale.getpreferredencoding()),
                            curses.color_pair(m_utils.get_color_pair(grid[line_number_grid][column_number_grid]).value)
                        )
                    except _curses.error:
                        pass
                else:
                    # we put a space to hide a potential old bloc

                    # in a try-catch because if the terminal is too small it will creates an error
                    # & curses raises an error when printing in the bottom-right corner
                    try:
                        self._window_game.addstr(
                            line_number_print,
                            column_number_print * 2,  # *2 since tetrominos are 2 char wide
                            "  ",
                            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                        )
                    except _curses.error:
                        pass

        self._window_game.refresh()

    def _print_next(self) -> None:
        """
        Shows the next tetromino in the next window
        """
        # cleaning the board
        for line in range(4):
            for column in range(4):
                # we put a space to hide a potential old bloc

                # in a try-catch because if the terminal is too small it will creates an error & curses raises an error
                # when printing in the bottom-right corner
                try:
                    # next comment because addstr is supposed to take str, but we use bytes to get a proper encoding
                    # noinspection PyTypeChecker
                    self._window_next.addstr(
                        line,
                        column * 2,
                        "  ".encode(locale.getpreferredencoding()),  # *2 since tetrominos are 2 char wide
                        curses.A_BOLD | curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                    )
                except _curses.error:
                    pass

        next_tetromino, next_shape = self._model.get_next_tetromino_info()
        for line in range(len(next_shape)):
            for column in range(len(next_shape[0])):
                if next_shape[line][column] is not None:
                    # we put a bloc

                    # in a try-catch because if the terminal is too small it will creates an error
                    # & curses raises an error when printing in the bottom-right corner
                    try:
                        # next comment because addstr is supposed to take str, but we use bytes to get a proper encoding
                        # noinspection PyTypeChecker
                        self._window_next.addstr(
                            line,
                            column * 2,  # *2 since tetrominos are 2 char wide
                            "██".encode(locale.getpreferredencoding()),
                            curses.color_pair(m_utils.get_color_pair(next_tetromino).value)
                        )
                    except _curses.error:
                        pass

        self._window_next.refresh()

    def _print_stored(self):
        """
        Show the stored tetromino window, with the stored tetromino if exists
        """
        # cleaning the board
        for line in range(4):
            for column in range(4):
                # we put a space to hide a potential old bloc

                # in a try-catch because if the terminal is too small it will creates an error & curses raises an error
                # when printing in the bottom-right corner
                try:
                    self._window_stored.addstr(
                        line,
                        column * 2,
                        "  ",  # only ASCII so no need to encode
                        curses.A_BOLD | curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                    )
                except _curses.error:
                    pass

        stored_tetromino, stored_shape = self._model.get_stored_tetromino_info()
        if stored_tetromino is not None:
            for line in range(len(stored_shape)):
                for column in range(len(stored_shape[0])):
                    if stored_shape[line][column] is not None:
                        # in a try-catch because if the terminal is too small it will creates an error
                        # & curses raises an error when printing in the bottom-right corner
                        try:
                            # next comment because addstr is supposed to take str, but we
                            # use bytes to get a proper encoding
                            # noinspection PyTypeChecker
                            self._window_stored.addstr(
                                line,
                                column * 2,
                                "██".encode(locale.getpreferredencoding()),
                                curses.color_pair(m_utils.get_color_pair(stored_tetromino).value)
                            )
                        except _curses.error:
                            pass

        self._window_stored.refresh()

    def _print_statistics(self) -> None:
        """
        Shows statistics on the statistic window
        """
        statistics = self._model.get_statistics()
        self._window_statistics.addstr(0, 1, "Level: " + str(statistics.get_level()))
        self._window_statistics.addstr(1, 1, "Score: " + str(statistics.get_score()))
        self._window_statistics.addstr(2, 1, "Lines: " + str(statistics.get_lines_completed()))
        self._window_statistics.addstr(3, 1, "Time:  " + str(statistics.get_duration()))

        self._window_statistics.refresh()

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
