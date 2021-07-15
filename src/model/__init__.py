"""
File that contains the declaration of the Model class, the logic of the game
"""

import typing

import common.tetromino_type as m_tetromino_type
import common.message as m_message
import common.message.message_subject as m_message_subject
import common.rotation as m_rotation
import common.direction as m_direction

import model.grid as m_grid


class Model:
    def __init__(self, seed: int):
        """
        Creates a model, paused by default.

        :param seed: an optional seed for the randomization of the order of tetrominos
        """
        self._seed: int = seed
        self._last_down: float = 0.0
        self._player_already_store: bool = False
        self._run: bool = False
        self._stored_tetromino: typing.Optional[m_tetromino_type.TetrominoType]

        self._grid = m_grid.Grid()

    def get_grid(self) -> list[list[typing.Optional[m_tetromino_type.TetrominoType]]]:
        """
        :return: the shape of the actual grid
        """
        return self._grid.get_shape().get_boxes()

    def process(self, message: m_message.Message) -> None:
        """
        Asks to the model to process the message

        :param message: the message to process
        """
        if message.get_subject() == m_message_subject.MessageSubject.RUN:
            self._run = True
            while self._run:

        elif message.get_subject() == m_message_subject.MessageSubject.PAUSE:
            self._run = False

    def _do_tick(self) -> None:
        """
        Did everything that is needed when the game is running
        """


    def _can_active_rotate(self, rotation: m_rotation.Rotation) -> bool:
        """
        :param rotation: the rotation we want to know the feasibility
        :return: if it's possible for the active tetromino to do the rotation
        """
        # TODO
        pass

    def _can_active_move(self, direction: m_direction.Direction) -> bool:
        """
        :param direction: the direction we want to know the feasibility of the move
        :return: if it's possible for the active tetromino to move to that direction
        """
        # TODO
        pass
