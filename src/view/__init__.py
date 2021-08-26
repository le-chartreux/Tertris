"""
File that contains the declaration of the View class, the user interface of the game
"""

import curses
import _curses
import abc
import time
import locale  # to encode non-ASCII char

import model as m_model

import common.message as m_message
import common.message.message_subject as m_message_subject

import view.utils as m_utils
import view.player_input as m_player_input
import view.color_pair as m_color_pair


class View(abc.ABC):
    def __init__(
            self,
            model: m_model.Model
    ):
        """
        Creates a View object, that contains a window of all the terminal (_window_all).
        After its creation, the View object has to be .setup() then .main_loop() to be print.
        WARNINGS:
            - to close the software without letting Python close an instance of View can broke the user terminal !
            - View instances have to be singletons
        """
        self._model = model
        self._window_all = curses.initscr()
        self._run = False
        self._exit_next_tick = False

    def __del__(self):
        """
        Destroy the View instance in a proper way
        """
        self._window_all.keypad(False)  # disable special keys compatibility
        self._window_all.clear()
        m_utils.revert_curses()

    def setup(self, background_file_path: str) -> None:
        """
        Setup everything that is needed for the view before printing

        :param background_file_path: path to the background file
        """
        m_utils.setup_curses()
        # setup _window_all for text entries
        self._window_all.nodelay(True)  # don't wait user entry when getch()
        self._window_all.keypad(True)  # allow compatibility of special keys (arrow-up for example)
        # Gestion des couleurs
        m_utils.set_colorscheme()

        self.set_background_colors()
        self._load_background(background_file_path)

    def main_loop(self) -> None:
        """
        Enters in the main loop, that prints the view and reacts to player inputs
        """
        self._run = True

        while not self._exit_next_tick:
            if self._run:
                self._print_active_windows()
                older_untreated_player_input = self._get_player_input()
                while older_untreated_player_input is not m_player_input.PlayerInput.NOTHING:
                    self._treat_player_input(older_untreated_player_input)
                    older_untreated_player_input = self._get_player_input()
            else:
                time.sleep(0.3)

    def _send(self, message: m_message.Message) -> None:
        """
        :param message: the message to send to the model
        """
        self._model.receive(message)

    def set_background_colors(self) -> None:
        """
        Set all backgrounds to their color
        """
        self._window_all.bkgd(" ", curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))

    def _load_background(self, file_path: str) -> None:
        """
        :param file_path: file path of the background
        """
        with open(file_path, "r") as background_file:
            line_number = 0
            line = background_file.readline()
            while line:
                # in a try-catch because if the terminal is too small it will creates an error
                try:
                    # next comment because addstr is supposed to take str, but we use bytes to get a proper encoding
                    # noinspection PyTypeChecker
                    self._window_all.addstr(
                        line_number,
                        0,
                        line.encode(locale.getpreferredencoding()),
                        curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value)
                    )
                except _curses.error:
                    pass
                line = background_file.readline()
                line_number += 1
        self._window_all.refresh()

    def _refresh_all(self) -> None:
        """
        Refresh all the windows.
        """
        self._window_all.refresh()

    @abc.abstractmethod
    def _print_active_windows(self) -> None:
        """
        Shows active windows. This windows can change, so they will been refresh on the main loop
        """
        pass

    def _clear(self) -> None:
        """
        Clear the windows
        """
        self._window_all.clear()

    def _get_player_input(self) -> m_player_input.PlayerInput:
        """
        :return: the first key that the user presses of the buffer
        """
        try:
            return m_player_input.PlayerInput(self._window_all.getch())
        except ValueError:
            return m_player_input.PlayerInput.KEY_UNUSED

    def _treat_player_input(self, player_input_to_treat: m_player_input.PlayerInput) -> None:
        """
        Treat a player input
        """
        # closing the app
        if player_input_to_treat is m_player_input.PlayerInput.KEY_ESC:
            self._send(
                m_message.Message(
                    m_message_subject.MessageSubject.QUIT
                )
            )
            self._exit_next_tick = True
