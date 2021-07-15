"""
File that contains the declaration of the Model class, the logic of the game
"""

import typing
import random
import time

import common.tetromino_type as m_tetromino_type
import common.message as m_message
import common.message.message_subject as m_message_subject
import common.rotation as m_rotation
import common.direction as m_direction

import model.grid as m_grid
import model.active_tetromino as m_active_tetromino
import model.utils as m_utils


class Model:
    def __init__(self, seed: int):
        """
        Creates a model, paused by default.

        :param seed: an optional seed for the randomization of the order of tetrominos
        """
        # setup of the random generation
        self._seed = seed
        random.seed(self._seed)

        # setup of variables
        self._last_down = 0.0
        self._never_down_this_tetromino = True
        self._player_already_store = False
        self._run = False

        self._active_tetromino = m_active_tetromino.ActiveTetromino(m_utils.random_tetromino())
        self._stored_tetromino: typing.Optional[m_tetromino_type.TetrominoType] = None
        self._next_tetromino = m_utils.random_tetromino()

        self._grid = m_grid.Grid()

    def get_grid(self) -> list[list[typing.Optional[m_tetromino_type.TetrominoType]]]:
        """
        :return: the shape of the actual grid
        """
        return self._grid.get_boxes()

    def process(self, message: m_message.Message) -> None:
        """
        Asks to the model to process the message

        :param message: the message to process
        """
        if message.get_subject() == m_message_subject.MessageSubject.RUN:
            self._run = True
            while self._run:
                self._do_tick()
        elif message.get_subject() == m_message_subject.MessageSubject.PAUSE:
            self._run = False
        elif (
            message.get_subject() == m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO
            and
            self._can_active_move(message.get_content())  # the direction is in content
        ):
            self._active_tetromino.move(message.get_content())
        elif (
            message.get_subject() == m_message_subject.MessageSubject.ROTATE_ACTIVE_TETROMINO
            and
            self._can_active_rotate(message.get_content())
        ):
            self._active_tetromino.rotate(message.get_content())
        elif (
            message.get_subject() == m_message_subject.MessageSubject.TOGGLE_STORED
            and
            self._can_store_active()
        ):
            self._store_active()

    def _do_tick(self) -> None:
        """
        Did everything that is needed when the game is running
        """
        print("tick")
        if self._has_to_go_down():
            self._last_down = time.monotonic()
            if self._can_active_move(m_direction.Direction.DOWN):
                self._active_tetromino.move(m_direction.Direction.DOWN)
                self._never_down_this_tetromino = False
            elif self._is_game_lost():
                self._run = False
                print("game lost")
            else:
                # the tetromino is placed
                self._grid.add_tetromino(self._active_tetromino)
                self._active_tetromino = m_active_tetromino.ActiveTetromino(self._next_tetromino)
                self._next_tetromino = m_utils.random_tetromino()
                self._player_already_store = False

                # checks if some lines are completed
                number_of_completed_lines = 0
                for line in range(self._grid.get_height()):
                    if self._grid.is_line_full(line):
                        self._grid.drop_lines_upper(line)
                        number_of_completed_lines += 1

                # TODO l'ajouter aux statistiques

    # QUESTIONS
    def _has_to_go_down(self) -> bool:
        """
        :return: if the active tetromino has to go down.
            True if more than  (0.8 - (level - 1)*0.007)**(level - 1) seconds happened since last down
            else False
        """
        level = 1  # TODO faire le système de niveaux
        return (time.monotonic() - self._last_down) > (0.8 - (level - 1) * 0.007) ** (level - 1)

    def _can_active_rotate(self, rotation: m_rotation.Rotation) -> bool:
        """
        :param rotation: the rotation we want to know the feasibility
        :return: if it's possible for the active tetromino to do the rotation
        """
        # TODO
        return True

    def _can_active_move(self, direction: m_direction.Direction) -> bool:
        """
        :param direction: the direction we want to know the feasibility of the move
        :return: if it's possible for the active tetromino to move to that direction
        """
        line = 0

        possible = True
        while line < self._active_tetromino.get_height() and possible:
            column = 0
            while column < self._active_tetromino.get_width() and possible:
                possible = (
                    not self._active_tetromino.is_occupied(x=column, y=line)  # There is no bloc
                    or  # or
                    (  # The bloc will go outside of the grid border
                        0 <= (
                            self._active_tetromino.get_x() + column + direction.get_x_variation()
                        ) < self._grid.get_width()
                        and
                        0 <= (
                                self._active_tetromino.get_y() + line + direction.get_y_variation()
                        ) < self._grid.get_height()
                    )
                    and not (  # ... and the futur bloc is empty
                        self._grid.is_occupied(
                            self._active_tetromino.get_x() + direction.get_x_variation() + column,
                            self._active_tetromino.get_y() + direction.get_y_variation() + line
                        )
                    )
                )
                column += 1
            line += 1

        return possible

    def _can_store_active(self) -> bool:
        """
        :return: if the player can store the active tetromino, so:
            - not self._player_already_store
            and
            - the stored tetromino has the space to spawn
        """
        if self._player_already_store:
            # that's impossible: the player already store a tetromino without ending a fall
            return False
        elif self._stored_tetromino is None:
            # if there is no stored tetromino, that's all since spawning issues can't happened
            return True
        else:
            # TODO check if possible
            return True

    def _is_game_lost(self) -> bool:
        """
        :return: if the game is lost (if the active tetromino can't move and it never down)
        """
        return not self._can_active_move(m_direction.Direction.DOWN) and self._never_down_this_tetromino

    # ACTIONS
    def _store_active(self) -> None:
        """
        Toggle the active Tetromino and the stored Tetromino
        """
        stored_tetromino = self._stored_tetromino
        self._stored_tetromino = self._active_tetromino.get_tetromino_type()
        self._active_tetromino = m_active_tetromino.ActiveTetromino(
            stored_tetromino
        )