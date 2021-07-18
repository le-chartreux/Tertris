"""
File that contains the declaration of the View class, the user interface of the game
"""

import curses
import abc

import model as m_model

import common.message as m_message

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

    def __del__(self):
        """
        Destroy the View instance in a proper way
        """
        self._window_all.keypad(False)  # disable special keys compatibility
        self._window_all.clear()
        m_utils.revert_curses()

    def setup(self) -> None:
        """
        Setup everything that is needed for the view before printing
        """
        m_utils.setup_curses()
        # setup _window_all for text entries
        self._window_all.nodelay(True)  # don't wait user entry when getch()
        self._window_all.keypad(True)  # allow compatibility of special keys (arrow-up for example)
        # Gestion des couleurs
        m_utils.set_colorscheme()
        self._set_backgrounds()

    def main_loop(self) -> None:
        """
        Enters in the main loop, that prints the view and reacts to player inputs
        """
        self._run = True
        self._print_static_windows()

        while self._run:
            self._print_active_windows()
            player_input = self._get_player_input()
            while player_input is not player_input.NOTHING:
                self._treat_player_input(player_input)
                player_input = self._get_player_input()

    def _send(self, message: m_message.Message) -> None:
        """
        :param message: the message to send to the model
        """
        self._model.receive(message)

    def _set_backgrounds(self) -> None:
        """
        Set every background on the write color. set_colorscheme() has to be already call
        """
        self._window_all.bkgd(' ', curses.color_pair(m_color_pair.ColorPair.BLACK_N_WHITE.value))

        self._refresh_all()

    def _refresh_all(self) -> None:
        """
        Refresh every window. All the windows have to exist.
        """
        self._window_all.refresh()

    @abc.abstractmethod
    def _print_static_windows(self) -> None:
        """
        Print static windows. This windows will never change, so they will never been refresh on the main loop
        """
        pass

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

    @abc.abstractmethod
    def _treat_player_input(self, player_input: m_player_input.PlayerInput) -> None:
        """
        Treat a player input
        """
        pass
