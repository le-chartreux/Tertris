"""
File that contains the declaration of the Model class, the logic of the game
"""
import sys
import typing
import random
import time
import queue

import common.tetromino_type as m_tetromino_type
import common.message as m_message
import common.message.message_subject as m_message_subject
import common.rotation as m_rotation
import common.direction as m_direction
import common.statistics as m_statistics

import model.grid as m_grid
import model.active_tetromino as m_active_tetromino
import model.utils as m_utils
import model.config as m_config


class Model:
    def __init__(self, seed: typing.Optional[int] = None):
        """
        Creates a model, paused by default.

        :param seed: an optional seed for the randomization of the order of tetrominos
        """
        # setup of the random generation
        self._seed = seed if seed is not None else random.randrange(sys.maxsize)
        random.seed(self._seed)

        # setup of variables
        self._last_down = time.monotonic()
        self._never_down_this_tetromino = True
        self._player_already_store = False
        self._run_game = False
        self._exit_next_tick = False

        self._active_tetromino = m_active_tetromino.ActiveTetromino(m_utils.random_tetromino())
        self._active_tetromino.put_at_spawnpoint()
        self._stored_tetromino: typing.Optional[m_tetromino_type.TetrominoType] = None
        self._next_tetromino = m_utils.random_tetromino()

        self._grid = m_grid.Grid()

        self._inbox: queue.Queue[m_message.Message] = queue.Queue()

        self._statistics = m_statistics.Statistics()

    # GETTERS
    def get_statistics(self) -> m_statistics.Statistics:
        return self._statistics

    def get_grid_with_active(self) -> list[list[typing.Optional[m_tetromino_type.TetrominoType]]]:
        """
        :return: the shape of the actual grid
        """
        return self._grid.combine(
            self._active_tetromino,
            self._active_tetromino.get_x(),
            self._active_tetromino.get_y()
        ).get_boxes()

    def get_next_tetromino_info(
            self
    ) -> tuple[m_tetromino_type.TetrominoType, list[list[typing.Optional[m_tetromino_type.TetrominoType]]]]:
        return (
            self._next_tetromino,
            m_utils.get_tetromino_shape(self._next_tetromino).get_boxes()
        )

    def get_stored_tetromino_info(
            self
    ) -> tuple[
        typing.Optional[m_tetromino_type.TetrominoType],
        typing.Optional[list[list[typing.Optional[m_tetromino_type.TetrominoType]]]]
    ]:
        return (
            self._stored_tetromino,
            (
                m_utils.get_tetromino_shape(self._stored_tetromino).get_boxes()
                if self._stored_tetromino is not None
                else None
            )
        )

    def main_loop(self) -> None:
        """
        Enter on the main loop, where the model processes and treat _inbox when the fifo isn't empty
        """
        while not self._exit_next_tick:
            # check _inbox
            while not self._inbox.empty():
                self._process(self._inbox.get())

            if self._run_game:
                self._do_tick()

            time.sleep(0.01)

    def receive(self, message: m_message.Message) -> None:
        """
        Add a message to the _inbox queue

        :param message: message to add
        """
        self._inbox.put(message)

    def _process(self, message: m_message.Message) -> None:
        """
        Process a message

        :param message: the message to process
        """
        if message.get_subject() == m_message_subject.MessageSubject.TOGGL_PAUSED:
            self._run_game = not self._run_game
            if self._run_game:
                self._statistics.run_timer()
            else:
                self._statistics.pause_timer()
        elif (
                message.get_subject() == m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO
                and
                self._can_active_move(message.get_content())  # the direction is in content
        ):
            self._active_tetromino.move(message.get_content())
            if message.get_content() is m_direction.Direction.DOWN:
                self._never_down_this_tetromino = False
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
        elif message.get_subject() == m_message_subject.MessageSubject.QUIT:
            self._exit_next_tick = True

    def _do_tick(self) -> None:
        """
        Did everything that is needed when the game is running
        """
        if self._has_to_go_down():
            if self._can_active_move(m_direction.Direction.DOWN):
                self._active_tetromino.move(m_direction.Direction.DOWN)
                self._never_down_this_tetromino = False
                self._last_down = time.monotonic()
            elif self._is_game_lost():
                self._run_game = False
                self._statistics.pause_timer()
            else:
                # the tetromino is placed
                self._grid.add_tetromino(self._active_tetromino)
                self._to_next_tetromino()
                self._player_already_store = False
                self._never_down_this_tetromino = True

                # checks if some lines are completed
                number_of_completed_lines = 0
                for line in range(self._grid.get_height()):
                    if self._grid.is_line_full(line):
                        self._grid.drop_lines_upper(line)
                        number_of_completed_lines += 1

                if number_of_completed_lines != 0:
                    self._statistics.add_lines_completed(number_of_completed_lines)
                    self._statistics.add_points_for_lines(number_of_completed_lines)

    # QUESTIONS
    def _has_to_go_down(self) -> bool:
        """
        :return: if the active tetromino has to go down.
            True if more than  (0.8 - (level - 1)*0.007)**(level - 1) seconds happened since last down
            else False
        """
        level = self._statistics.get_level()
        return (time.monotonic() - self._last_down) > (0.8 - (level - 1) * 0.007) ** (level - 1)

    def _can_spawn(self, tetromino_type: m_tetromino_type.TetrominoType) -> bool:
        """
        :return: if the tetromino has the space to spawn
        """
        temp_tetromino = m_active_tetromino.ActiveTetromino(tetromino_type)
        remaining_down = m_config.SPAWN_LINE
        while remaining_down != 0 and self._can_active_move(m_direction.Direction.DOWN, temp_tetromino):
            temp_tetromino.move(m_direction.Direction.DOWN)
            remaining_down -= 1

        return remaining_down == 0

    def _can_active_rotate(self, rotation: m_rotation.Rotation) -> bool:
        """
        :param rotation: the rotation we want to know the feasibility
        :return: if it's possible for the active tetromino to do the rotation
        """
        active_tetromino_copied = self._active_tetromino.copy_shape()
        active_tetromino_copied.rotate(rotation)
        return self._grid.can_combine_perfectly(
            active_tetromino_copied,
            self._active_tetromino.get_x(),
            self._active_tetromino.get_y()
        )

    def _can_active_move(
            self,
            direction: m_direction.Direction,
            active_to_use: typing.Optional[m_active_tetromino.ActiveTetromino] = None
    ) -> bool:
        """
        :param direction: the direction we want to know the feasibility of the move
        :return: if it's possible for the active tetromino to move to that direction
        """
        if active_to_use is None:
            active_to_use = self._active_tetromino
        line = 0

        possible = True
        while line < active_to_use.get_height() and possible:
            column = 0
            while column < active_to_use.get_width() and possible:
                # possible if
                # - the bloc is empty
                # OR
                # - the bloc will not go outside of the grid border AND the destination of the bloc is empty

                bloc_empty = not active_to_use.is_occupied(x=column, y=line)

                will_not_go_outside = (
                        0 <= active_to_use.get_x() + column + direction.get_x_variation() < self._grid.get_width()
                        and
                        0 <= active_to_use.get_y() + line + direction.get_y_variation() < self._grid.get_height()
                )
                # we have to check that <will_not_go_outside>, else we query a bloc outside of the border
                futur_bloc_empty = False
                if will_not_go_outside:
                    futur_bloc_empty = not self._grid.is_occupied(
                        active_to_use.get_x() + direction.get_x_variation() + column,
                        active_to_use.get_y() + direction.get_y_variation() + line
                    )

                possible = (
                        bloc_empty
                        or
                        will_not_go_outside
                        and
                        futur_bloc_empty
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
            return self._can_spawn(self._stored_tetromino)

    def _is_game_lost(self) -> bool:
        """
        :return: if the game is lost (if the active tetromino has to go down, can't move and it never down)
        """
        return (
                self._has_to_go_down()
                and
                not self._can_active_move(m_direction.Direction.DOWN)
                and
                self._never_down_this_tetromino
        )

    # ACTIONS
    def _store_active(self) -> None:
        """
        Toggle the active Tetromino and the stored Tetromino
        """
        self._player_already_store = True

        stored_tetromino_temp = self._stored_tetromino
        self._stored_tetromino = self._active_tetromino.get_tetromino_type()

        if stored_tetromino_temp is None:
            # there is no stored, so we only store this one and use the next
            self._to_next_tetromino()
        else:
            self._active_tetromino = m_active_tetromino.ActiveTetromino(
                stored_tetromino_temp
            )
            self._active_tetromino.put_at_spawnpoint()

    def _to_next_tetromino(self) -> None:
        """
        Set the active tetromino to the next, and select the next
        """
        self._active_tetromino = m_active_tetromino.ActiveTetromino(self._next_tetromino)
        self._next_tetromino = m_utils.random_tetromino()
        self._active_tetromino.put_at_spawnpoint()
