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
import common.config as config_general

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
            config.GRID_HEIGHT,
            config.GRID_WIDTH,
            config.GRID_BEGIN_Y,
            config.GRID_BEGIN_X
        )

        self._window_next = curses.newwin(
            config.NEXT_HEIGHT,
            config.NEXT_WIDTH,
            config.NEXT_BEGIN_Y,
            config.NEXT_BEGIN_X
        )

        self._window_stored = curses.newwin(
            config.STORED_HEIGHT,
            config.STORED_WIDTH,
            config.STORED_BEGIN_Y,
            config.STORED_BEGIN_X
        )

        self._window_statistics = curses.newwin(
            config.STATISTICS_HEIGHT,
            config.STATISTICS_WIDTH,
            config.STATISTICS_BEGIN_Y,
            config.STATISTICS_BEGIN_X
        )

        self._window_keybinds = curses.newwin(
            config.KEYBINDS_HEIGHT,
            config.KEYBINDS_WIDTH,
            config.KEYBINDS_BEGIN_Y,
            config.KEYBINDS_BEGIN_X
        )

    def set_backgrounds(self) -> None:
        view.View.set_backgrounds(self)
        self._window_game.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_next.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_stored.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_statistics.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        self._window_keybinds.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))

        self.refresh_all()

    def refresh_all(self) -> None:
        view.View.refresh_all(self)
        self._window_game.refresh()
        self._window_next.refresh()
        self._window_stored.refresh()
        self._window_statistics.refresh()
        self._window_keybinds.refresh()

    def print_windows(self) -> None:
        self.print_grid()
        self.print_grid_border()

        self.print_next()
        self.print_next_border()

        self.print_stored()
        self.print_stored_border()

        self.print_statistics()
        self.print_statistics_border()

        self.print_keybinds()
        self.print_keybinds_border()

    def print_grid(self) -> None:
        """
        Show the game grid
        """
        grid = self._model.get_grid_with_active()

        for line in range(config_general.GRID_HEIGHT):
            for column in range(config_general.GRID_WIDTH):
                if grid[line][column] is not None:
                    # we put a bloc
                    self._window_game.addstr(
                        line + 1,
                        column * 2 + 1,  # *2 since tetrominos are 2 char wide
                        "██".encode(locale.getpreferredencoding()),
                        curses.color_pair(m_utils.get_color_pair(grid[line][column]).value)
                    )
                else:
                    # we put a space to hide a potential old bloc
                    self._window_game.addstr(
                        line + 1,
                        column * 2 + 1,  # *2 since tetrominos are 2 char wide
                        "  ",
                        curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                    )

        self._window_game.refresh()

    def print_grid_border(self) -> None:
        """
        Shows the border around the game grid
        """
        # first line
        self._window_game.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.GRID_WIDTH - 2):
            self._window_game.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_game.addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        # intermediate lines
        for line in range(1, config.GRID_HEIGHT - 1):
            self._window_game.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_game.addstr(
                line, config.GRID_WIDTH - 2,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_game.addstr(
            config.GRID_HEIGHT - 1, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.GRID_WIDTH - 2):
            self._window_game.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_game.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_game.refresh()

    def print_next(self) -> None:
        """
        Shows the next tetromino in the next window
        """
        next_tetromino, next_shape = self._model.get_next_tetromino_info()

        for line in range(4):
            for column in range(4):
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

    def print_next_border(self) -> None:
        """
        Shows the border around the next tetromino grid
        """
        # first line
        self._window_next.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.ceil((config.NEXT_WIDTH - 4 - 2) / 2)):  # -4 car Next, -1 car ╗
            self._window_next.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_next.addstr(
            "Next",  # only ASCII so no need en encode
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.floor((config.NEXT_WIDTH - 4 - 2) / 2)):  # -4 car Next, -1 car ╗
            self._window_next.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_next.addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        # intermediate lines
        for line in range(1, config.NEXT_HEIGHT - 2):
            self._window_next.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_next.addstr(
                line, config.NEXT_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_next.addstr(
            config.NEXT_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.NEXT_WIDTH - 1):
            self._window_next.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_next.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_next.refresh()

    def print_stored(self):
        """
        Show the stored tetromino window, with the stored tetromino if exists
        """
        stored_tetromino, stored_shape = self._model.get_stored_tetromino_info()
        if stored_tetromino is not None:
            for line in range(4):
                for column in range(4):
                    if stored_tetromino[line][column] is not None:
                        self._window_stored.addstr(
                            line + 1,
                            column * 2 + 1,
                            "██".encode(locale.getpreferredencoding()),
                            curses.color_pair(m_utils.get_color_pair(stored_tetromino.get_tetromino_type()).value)
                        )
                    else:
                        self._window_stored.addstr(
                            line + 1,
                            column * 2 + 1,
                            "  ",  # only ASCII so no need to encode
                            curses.A_BOLD | curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                        )

        self._window_stored.refresh()

    def print_stored_border(self) -> None:
        """
        Shows the border around the stored tetromino border
        """
        # first line
        self._window_stored.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.ceil((config.STORED_WIDTH - 6 - 2) / 2)):  # -6 car Stored, -2 car ╔ et ╗
            self._window_stored.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_stored.addstr(
            "Stored",
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.floor((config.STORED_WIDTH - 6 - 2) / 2)):  # -6 car Stored, -2 car ╔ et ╗
            self._window_stored.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_stored.addstr("╗", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))

        # intermediate lines
        for line in range(1, config.STORED_HEIGHT - 2):
            self._window_stored.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_stored.addstr(
                line, config.STORED_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_stored.addstr(
            config.STORED_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.STORED_WIDTH - 1):
            self._window_stored.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_stored.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_stored.refresh()

    def print_statistics(self) -> None:
        """
        Shows statistics on the statistic window
        """
        self._window_statistics.addstr(1, 2, "Level: " + str(1))
        self._window_statistics.addstr(2, 2, "Score: " + str(1))
        self._window_statistics.addstr(3, 2, "Lines: " + str(1))
        self._window_statistics.addstr(4, 2, "Time: " + str(1))

        self._window_statistics.refresh()

    def print_statistics_border(self) -> None:
        """
        Shows the border around the statistics window
        """
        # first line
        self._window_statistics.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.ceil((config.STATISTICS_WIDTH - 10 - 2) / 2)):  # -10 car Statistics, -2 car ╔ et ╗
            self._window_statistics.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_statistics.addstr("Statistics", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        for _ in range(math.floor((config.STATISTICS_WIDTH - 10 - 2) / 2)):  # -10 car Statistics, -2 car ╔ et ╗
            self._window_statistics.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_statistics.addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        # intermediate lines
        for line in range(1, config.STATISTICS_HEIGHT - 2):
            self._window_statistics.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_statistics.addstr(
                line, config.STATISTICS_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_statistics.addstr(
            config.STATISTICS_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.STATISTICS_WIDTH - 1):
            self._window_statistics.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_statistics.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_statistics.refresh()

    def print_keybinds(self) -> None:
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

    def print_keybinds_border(self) -> None:
        """
        Show the border around the keybinds
        """
        # first line
        self._window_keybinds.addstr(
            0, 0,
            "╔".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(math.ceil((config.KEYBINDS_WIDTH - 8 - 2) / 2)):  # -8 car Keybinds, -2 car ╔ et ╗
            self._window_keybinds.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_keybinds.addstr("Keybinds", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))
        for _ in range(math.floor((config.KEYBINDS_WIDTH - 8 - 2) / 2)):  # -8 car Keybinds, -2 car ╔ et ╗
            self._window_keybinds.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_keybinds.addstr(
            "╗".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        # intermediate lines
        for line in range(1, config.KEYBINDS_HEIGHT - 2):
            self._window_keybinds.addstr(
                line, 0,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
            self._window_keybinds.addstr(
                line, config.KEYBINDS_WIDTH - 1,
                "║".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )

        # last line
        self._window_keybinds.addstr(
            config.KEYBINDS_HEIGHT - 2, 0,
            "╚".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )
        for _ in range(1, config.KEYBINDS_WIDTH - 1):
            self._window_keybinds.addstr(
                "═".encode(locale.getpreferredencoding()),
                curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
            )
        self._window_keybinds.addstr(
            "╝".encode(locale.getpreferredencoding()),
            curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
        )

        self._window_keybinds.refresh()

    def treat_player_input(self, player_input: m_player_input.PlayerInput) -> None:
        # moves
        if player_input == m_player_input.PlayerInput.KEY_LEFT:
            self._model.process(
                m_message.Message(
                    m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO,
                    m_direction.Direction.LEFT
                )
            )
        elif player_input == m_player_input.PlayerInput.KEY_RIGHT:
            self._model.process(
                m_message.Message(
                    m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO,
                    m_direction.Direction.RIGHT
                )
            )
        elif player_input == m_player_input.PlayerInput.KEY_DOWN:
            self._model.process(
                m_message.Message(
                    m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO,
                    m_direction.Direction.DOWN
                )
            )
        # rotations
        elif player_input == m_player_input.PlayerInput.KEY_Q:
            self._model.process(
                m_message.Message(
                    m_message_subject.MessageSubject.ROTATE_ACTIVE_TETROMINO,
                    m_rotation.Rotation.LEFT
                )
            )
        elif player_input == m_player_input.PlayerInput.KEY_D:
            self._model.process(
                m_message.Message(
                    m_message_subject.MessageSubject.ROTATE_ACTIVE_TETROMINO,
                    m_rotation.Rotation.RIGHT
                )
            )
        # store
        elif player_input == m_player_input.PlayerInput.KEY_S:
            self._model.process(
                m_message.Message(
                    m_message_subject.MessageSubject.TOGGLE_STORED
                )
            )
        # controls
        elif player_input == m_player_input.PlayerInput.KEY_P:
            self._model.process(
                m_message.Message(
                    m_message_subject.MessageSubject.TOGGL_PAUSED,
                )
            )
        elif player_input == m_player_input.PlayerInput.KEY_ESC:
            pass  # TODO
