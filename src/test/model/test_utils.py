import unittest
import enum

import common.tetromino_type as m_tetromino_type

import model.utils as m_utils
import model.shape as m_shape


class TestUtils(unittest.TestCase):

    def test_get_tetromino_shape(self):

        tetromino_type = m_tetromino_type.TetrominoType.I_SHAPE
        shape = m_shape.Shape(4, 4)
        shape.set_boxes([
            [None, None, None, None],
            [tetromino_type, tetromino_type, tetromino_type, tetromino_type],
            [None, None, None, None],
            [None, None, None, None]
        ])
        self.assertTrue(shape, m_utils.get_tetromino_shape(tetromino_type))

        tetromino_type = m_tetromino_type.TetrominoType.O_SHAPE
        shape = m_shape.Shape(2, 2)
        shape.set_boxes([
            [tetromino_type, tetromino_type],
            [tetromino_type, tetromino_type]
        ])
        self.assertTrue(shape, m_utils.get_tetromino_shape(tetromino_type))

        tetromino_type = m_tetromino_type.TetrominoType.T_SHAPE
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [None, tetromino_type, None],
            [tetromino_type, tetromino_type, tetromino_type],
            [None, None, None],
        ])
        self.assertTrue(shape, m_utils.get_tetromino_shape(tetromino_type))

        tetromino_type = m_tetromino_type.TetrominoType.L_SHAPE
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [None, None, tetromino_type],
            [tetromino_type, tetromino_type, tetromino_type],
            [None, None, None],
        ])
        self.assertTrue(shape, m_utils.get_tetromino_shape(tetromino_type))

        tetromino_type = m_tetromino_type.TetrominoType.J_SHAPE
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [tetromino_type, None, None],
            [tetromino_type, tetromino_type, tetromino_type],
            [None, None, None],
        ])
        self.assertTrue(shape, m_utils.get_tetromino_shape(tetromino_type))

        tetromino_type = m_tetromino_type.TetrominoType.Z_SHAPE
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [tetromino_type, tetromino_type, None],
            [None, tetromino_type, tetromino_type],
            [None, None, None],
        ])
        self.assertTrue(shape, m_utils.get_tetromino_shape(tetromino_type))

        tetromino_type = m_tetromino_type.TetrominoType.S_SHAPE
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [None, tetromino_type, tetromino_type],
            [tetromino_type, tetromino_type, None],
            [None, None, None],
        ])
        self.assertTrue(shape, m_utils.get_tetromino_shape(tetromino_type))

        m_tetromino_type.TetrominoType.FAKE_SHAPE = enum.auto()
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            m_utils.get_tetromino_shape(m_tetromino_type.TetrominoType.FAKE_SHAPE)
        with self.assertRaises(TypeError):
            # noinspection PyTypeChecker
            m_utils.get_tetromino_shape(32)

    def test_random_tetromino(self):
        for _ in range(20):
            self.assertIsInstance(m_utils.random_tetromino(), m_tetromino_type.TetrominoType)


if __name__ == '__main__':
    unittest.main()
