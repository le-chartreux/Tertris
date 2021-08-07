import unittest
import random

import model.shape as m_shape


class TestShape(unittest.TestCase):

    def setUp(self) -> None:
        self._shape = m_shape.Shape(
            random.randint(1, 50),
            random.randint(1, 50)
        )

    def tearDown(self) -> None:
        self._shape = m_shape.Shape(
            random.randint(1, 50),
            random.randint(1, 50)
        )

    def test_can_combine_perfectly(self) -> None:
        # between two identical shapes full of empty boxes
        other_shape = m_shape.Shape(
            self._shape.get_height(),
            self._shape.get_width()
        )
        self.assertTrue(
            self._shape.can_combine_perfectly(
                other_shape,
                0,
                0
            )
        )

        # TODO continuer



if __name__ == '__main__':
    unittest.main()
