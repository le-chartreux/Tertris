import unittest
import sys
import random

import common.tetromino_type as m_tetromino_type
import common.message as m_message
import common.message.message_subject as m_message_subject
import common.rotation as m_rotation
import common.direction as m_direction

import model as m_model
import model.grid as m_grid
import model.active_tetromino as m_active_tetromino

import test.model.utils as m_test_utils


class TestDirection(unittest.TestCase):
    def setUp(self) -> None:
        self.model = m_model.Model()

    def tearDown(self) -> None:
        self.model = m_model.Model()

    def test__init__(self) -> None:
        # checking that the seed works fine
        seed = random.randrange(sys.maxsize)

        model_1 = m_model.Model(seed)
        model_2 = m_model.Model(seed)

        self.assertEqual(model_1._active_tetromino.get_tetromino_type(), model_2._active_tetromino.get_tetromino_type())

    def test_receive(self) -> None:
        # firstly it is empty
        self.assertTrue(self.model._inbox.empty())

        # after that we add a message
        self.model.receive(m_message.Message(m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO))

        # so there is something in the inbox
        self.assertFalse(self.model._inbox.empty())

    def test_process(self) -> None:
        # for a "TOGGL_PAUSED"
        for _ in range(5):
            game_running_before = self.model._run_game
            timer_running_before = self.model._statistics._timer_paused_since is None

            self.model._process(m_message.Message(m_message_subject.MessageSubject.TOGGL_PAUSED))

            self.assertNotEqual(
                game_running_before,
                self.model._run_game
            )
            self.assertNotEqual(
                timer_running_before,
                self.model._statistics._timer_paused_since is None
            )

        # for a "MOVE_ACTIVE_TETROMINO"
        for _ in range(50):
            # multiple time because since it's random we don't want it to pass thanks to luck
            for tetromino_type in m_tetromino_type.TetrominoType.__iter__():
                self.model._active_tetromino = m_active_tetromino.ActiveTetromino(tetromino_type)

                # resetting the grid so we don't overload it with tons of tetromino, because else
                # we will quickly have a grid where it's impossible to move in any direction, so the test will
                # not be smart
                self.model._grid = m_grid.Grid()

                # filling the grid with some tetrominos, so there is a possibility that the active can't moves
                m_test_utils.fill_grid_with_tetrominos(self.model._grid, random.randint(0, 10))

                # testing the directions
                for direction in m_direction.Direction.__iter__():
                    self.model._active_tetromino.put_at_spawnpoint()

                    x_before_move = self.model._active_tetromino.get_x()
                    y_before_move = self.model._active_tetromino.get_y()

                    can_move = self.model._can_active_move(direction)

                    self.model._process(
                        m_message.Message(
                            m_message_subject.MessageSubject.MOVE_ACTIVE_TETROMINO,
                            direction
                        )
                    )

                    self.assertEqual(
                        x_before_move + direction.get_x_variation() == self.model._active_tetromino.get_x(),
                        can_move or direction.get_x_variation() == 0
                    )

                    self.assertEqual(
                        y_before_move + direction.get_y_variation() == self.model._active_tetromino.get_y(),
                        can_move or direction.get_y_variation() == 0
                    )

        # for a "ROTATE_ACTIVE_TETROMINO"
        for _ in range(50):
            # multiple time because since it's random we don't want it to pass thanks to luck
            for tetromino_type in m_tetromino_type.TetrominoType.__iter__():
                self.model._active_tetromino = m_active_tetromino.ActiveTetromino(tetromino_type)

                # resetting the grid so we don't overload it with tons of tetromino, because else
                # we will quickly have a grid where it's impossible to move in any direction, so the test will
                # not be smart
                self.model._grid = m_grid.Grid()

                # filling the grid with some tetrominos, so there is a possibility that the active can't moves
                m_test_utils.fill_grid_with_tetrominos(self.model._grid, random.randint(0, 10))

                # testing the directions
                for rotation in m_rotation.Rotation.__iter__():
                    self.model._active_tetromino.put_at_spawnpoint()

                    can_rotate = self.model._can_active_rotate(rotation)
                    boxes_before_rotation = self.model._active_tetromino.copy_shape()

                    self.model._process(
                        m_message.Message(
                            m_message_subject.MessageSubject.ROTATE_ACTIVE_TETROMINO,
                            rotation
                        )
                    )

                    self.assertEqual(
                        boxes_before_rotation.is_equal(self.model._active_tetromino),  # true if no rotation or O shape
                        (
                                not can_rotate
                                or
                                (
                                        self.model._active_tetromino.get_tetromino_type()
                                        is
                                        m_tetromino_type.TetrominoType.O_SHAPE
                                )
                        )  # because the O shape doesn't changes it's shape when it rotates :)
                    )

        # for a "TOGGLE_STORED"
        # resetting the grid so we are sure that the stored tetromino has the space to spawn
        self.model._grid = m_grid.Grid()

        # test when there is no stored tetromino
        self.model._stored_tetromino = None
        # since there is no stored, it should set the stored to the active then the active to the next
        active_type_before_toggle = self.model._active_tetromino.get_tetromino_type()
        next_type_before_toggle = self.model._next_tetromino

        self.model._process(m_message.Message(m_message_subject.MessageSubject.TOGGLE_STORED))

        self.assertIsNotNone(self.model._stored_tetromino)
        self.assertIs(self.model._stored_tetromino, active_type_before_toggle)
        self.assertIs(self.model._active_tetromino.get_tetromino_type(), next_type_before_toggle)

        # test when there is a stored tetromino & we can't store
        self.model._can_store_active = lambda: False
        for _ in range(5):
            active_type_before_toggle = self.model._active_tetromino.get_tetromino_type()
            stored_type_before_toggle = self.model._stored_tetromino

            self.model._process(m_message.Message(m_message_subject.MessageSubject.TOGGLE_STORED))

            self.assertIs(
                active_type_before_toggle,
                self.model._active_tetromino.get_tetromino_type()
            )
            self.assertIs(
                stored_type_before_toggle,
                self.model._stored_tetromino
            )

        # test when there is a stored tetromino & we can store
        self.model._can_store_active = lambda: True
        for _ in range(5):
            active_type_before_toggle = self.model._active_tetromino.get_tetromino_type()
            stored_type_before_toggle = self.model._stored_tetromino

            self.model._process(m_message.Message(m_message_subject.MessageSubject.TOGGLE_STORED))

            self.assertIs(
                active_type_before_toggle,
                self.model._stored_tetromino
            )
            self.assertIs(
                stored_type_before_toggle,
                self.model._active_tetromino.get_tetromino_type()
            )

        # for a "QUIT"
        self.model._exit_next_tick = False
        self.model._process(m_message.Message(m_message_subject.MessageSubject.QUIT))
        self.assertTrue(self.model._exit_next_tick)

    def test_do_tick(self) -> None:
        # TODO
        pass

    def test_has_to_go_down(self) -> None:
        # TODO
        pass

    def test_can_spawn(self) -> None:
        # TODO
        pass

    def test_can_active_rotate(self) -> None:
        # TODO
        pass

    def test_can_active_move(self) -> None:
        # TODO
        pass

    def test_can_store_active(self) -> None:
        # TODO
        pass

    def test_is_game_lost(self) -> None:
        # TODO
        pass

    def test_store_active(self) -> None:
        # TODO
        pass

    def test_to_next_tetromino(self) -> None:
        # TODO
        pass


if __name__ == '__main__':
    unittest.main()
