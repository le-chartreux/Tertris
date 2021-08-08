import unittest
import random

import model.shape as m_shape
import common.tetromino_type as m_tetromino_type


class TestShape(unittest.TestCase):

    @staticmethod
    def random_size_shape(
            min_height: int = 1,
            max_height: int = 50,
            min_width: int = 1,
            max_width: int = 50
    ):
        return m_shape.Shape(random.randint(min_height, max_height), random.randint(min_width, max_width))

    def test_can_combine_perfectly(self) -> None:
        # between two identical shapes full of empty boxes
        for _ in range(5):
            shape_1 = self.random_size_shape()
            shape_2 = m_shape.Shape(
                shape_1.get_height(),
                shape_1.get_width()
            )

            self.assertTrue(
                shape_1.can_combine_perfectly(
                    shape_2,
                    0,
                    0
                )
            )

        # between two shapes with empty boxes, but with a smaller one
        # and without overlay
        for _ in range(5):
            shape_1 = self.random_size_shape()

            shape_2 = self.random_size_shape(
                min_height=shape_1.get_height(),
                min_width=shape_1.get_width()
            )
            self.assertTrue(
                shape_2.can_combine_perfectly(
                    shape_1,
                    0,
                    0
                )
            )

            # between two shapes with empty boxes, but with a smaller one
            # and with overlay
            for _ in range(50):
                shape_1 = self.random_size_shape()

                shape_2 = self.random_size_shape(
                    min_height=shape_1.get_height() + 5,
                    max_height=shape_1.get_height() + 15,
                    min_width=shape_1.get_width() + 5,
                    max_width=shape_1.get_width() + 15
                )
                self.assertTrue(
                    shape_2.can_combine_perfectly(
                        shape_1,
                        random.randint(0, 4),
                        random.randint(0, 4)
                    )
                )

            # between a shape of empty boxes an one with some boxes
            for _ in range(50):
                shape_1 = m_shape.Shape(
                    random.randint(1, 50),
                    random.randint(1, 50)
                )

                shape_2 = self.random_size_shape(
                    min_height=shape_1.get_height() + 5,
                    max_height=shape_1.get_height() + 15,
                    min_width=shape_1.get_width() + 5,
                    max_width=shape_1.get_width() + 15
                )
                # filling the second shape
                for _ in range(10):
                    shape_2.set_box(
                        m_tetromino_type.TetrominoType.O_SHAPE,
                        random.randint(0, shape_2.get_width() - 1),
                        random.randint(0, shape_2.get_height() - 1)
                    )

                self.assertTrue(
                    shape_2.can_combine_perfectly(
                        shape_1,
                        random.randint(0, 5),
                        random.randint(0, 5)
                    )
                )

            # between 2 non-empty shapes
            for _ in range(500):  # maybe overkill haha
                overlay_x, overlay_y = random.randint(0, 5), random.randint(0, 5)

                shape_1 = self.random_size_shape()

                shape_2 = self.random_size_shape(
                    min_height=shape_1.get_height() + 5,
                    max_height=shape_1.get_height() + 15,
                    min_width=shape_1.get_width() + 5,
                    max_width=shape_1.get_width() + 15
                )

                # filling the shapes
                positions_to_put_list = []

                for shape_to_fill in shape_1, shape_2:
                    positions_to_put_list.append([
                        (
                            random.randint(0, shape_to_fill.get_width() - 1),
                            random.randint(0, shape_to_fill.get_height() - 1)
                        ) for _ in range(random.randint(5, 6))
                    ])
                    for position_to_put in positions_to_put_list[len(positions_to_put_list) - 1]:
                        shape_to_fill.set_box(
                            m_tetromino_type.TetrominoType.O_SHAPE,
                            position_to_put[0],
                            position_to_put[1]
                        )

                intersects = True
                for position_to_put_1 in positions_to_put_list[0]:
                    if (
                            (position_to_put_1[0] + overlay_x, position_to_put_1[1] + overlay_y)
                            in positions_to_put_list[1]
                    ):
                        intersects = False

                self.assertEqual(
                    shape_2.can_combine_perfectly(
                        shape_1,
                        overlay_x,
                        overlay_y
                    ),
                    intersects
                )


if __name__ == '__main__':
    unittest.main()