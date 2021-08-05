import unittest
import common.direction as m_direction


class TestDirection(unittest.TestCase):

    def test_get_x_variation(self):
        self.assertEqual(m_direction.Direction.LEFT.get_x_variation(), -1, "Should be -1")
        self.assertEqual(m_direction.Direction.RIGHT.get_x_variation(), 1, "Should be 1")
        self.assertEqual(m_direction.Direction.UP.get_x_variation(), 0, "Should be 0")
        self.assertEqual(m_direction.Direction.DOWN.get_x_variation(), 0, "Should be 0")

    def test_get_y_variation(self):
        self.assertEqual(m_direction.Direction.LEFT.get_y_variation(), 0, "Should be 0")
        self.assertEqual(m_direction.Direction.RIGHT.get_y_variation(), 0, "Should be 0")
        self.assertEqual(m_direction.Direction.UP.get_y_variation(), -1, "Should be -1")
        self.assertEqual(m_direction.Direction.DOWN.get_y_variation(), 1, "Should be 1")


if __name__ == '__main__':
    unittest.main()
