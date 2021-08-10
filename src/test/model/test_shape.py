import unittest
import random

import common.tetromino_type as m_tetromino_type
import common.rotation as m_rotation

import model.shape as m_shape


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
            for _ in range(100):
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
                        ) for _ in range(random.randint(1, 100))
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

    def test_combine(self) -> None:
        # same sizes, only empty boxes, no overlay
        for _ in range(10):
            shape_1 = self.random_size_shape()
            shape_2 = m_shape.Shape(shape_1.get_height(), shape_1.get_width())
            self.assertTrue(
                shape_1.is_equal(shape_1.combine(shape_2, 0, 0))
            )

        # different sizes, only empty boxes, with overlay
        for _ in range(10):
            shape_1 = self.random_size_shape()
            shape_2 = self.random_size_shape(
                min_height=shape_1.get_height() + 5,
                max_height=shape_1.get_height() + 15,
                min_width=shape_1.get_width() + 5,
                max_width=shape_1.get_width() + 15
            )
            self.assertTrue(
                shape_2.is_equal(
                    shape_2.combine(shape_1, random.randint(0, 5), random.randint(0, 5))
                )
            )

        # different sizes, one empty and one with boxes
        for _ in range(10):
            shape_1 = self.random_size_shape()
            shape_2 = self.random_size_shape(
                min_height=shape_1.get_height() + 5,
                max_height=shape_1.get_height() + 15,
                min_width=shape_1.get_width() + 5,
                max_width=shape_1.get_width() + 15
            )
            for _ in range(10):
                shape_2.set_box(
                    m_tetromino_type.TetrominoType.O_SHAPE,
                    random.randint(
                        0,
                        shape_2.get_width() - 1
                    ),
                    random.randint(
                        0,
                        shape_2.get_height() - 1
                    )
                )

            self.assertTrue(
                shape_2.is_equal(shape_2.combine(shape_1, random.randint(0, 5), random.randint(0, 5)))
            )

        # different sizes, both with non-empty boxes and with an overlay
        overlay_x, overlay_y = random.randint(0, 5), random.randint(0, 5)
        for _ in range(100):
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
                    ) for _ in range(random.randint(1, 100))
                ])
                for position_to_put in positions_to_put_list[len(positions_to_put_list) - 1]:
                    shape_to_fill.set_box(
                        m_tetromino_type.TetrominoType.O_SHAPE,
                        position_to_put[0],
                        position_to_put[1]
                    )

            combination = shape_2.combine(shape_1, overlay_x, overlay_y)
            is_good = True
            x = 0
            while x < combination.get_width() and is_good:
                y = 0
                while (
                        y < combination.get_height()
                        and
                        is_good
                ):
                    if not (
                            combination.is_occupied(x, y)
                            and
                            (
                                (
                                        x + overlay_x < shape_1.get_width()
                                        and
                                        y + overlay_y < shape_1.get_height()
                                        and
                                        shape_1.is_occupied(x + overlay_x, y + overlay_y)
                                )
                                or
                                shape_2.is_occupied(x, y)
                            )
                            or
                            not combination.is_occupied(x, y)
                    ):
                        is_good = False
                    y += 1
                x += 1

    def test_copy_shape(self) -> None:
        # asserting an empty shape is copied as an empty shape
        shape = self.random_size_shape()
        copy_shape = shape.copy_shape()
        # asserting the copy and the original are similar
        self.assertTrue(shape.is_equal(copy_shape))

        # asserting an shape with some boxes is correctly copied
        shape = self.random_size_shape()
        copy_shape = shape.copy_shape()
        for _ in range(5):
            copy_shape.set_box(
                m_tetromino_type.TetrominoType.O_SHAPE,
                random.randint(0, shape.get_width() - 1),
                random.randint(0, shape.get_height() - 1)
            )
        copy_shape = shape.copy_shape()
        # asserting the copy and the original are similar
        self.assertTrue(shape.is_equal(copy_shape))

        # changing the copy and asserting it doesn't change the original
        shape = self.random_size_shape()
        copy_shape = shape.copy_shape()
        place_to_put_x = random.randint(0, shape.get_width() - 1)
        place_to_put_y = random.randint(0, shape.get_height() - 1)
        copy_shape.set_box(m_tetromino_type.TetrominoType.O_SHAPE, place_to_put_x, place_to_put_y)
        self.assertFalse(shape.is_occupied(place_to_put_x, place_to_put_y))

    def test_rotate(self) -> None:
        # testing each rotation for each tetromino, in clockwise then anticlockwise

        def test_one_shape(
                initial: m_shape.Shape,
                right_rotation: m_shape.Shape,
                reverse_rotation: m_shape.Shape,
                left_rotation: m_shape.Shape
        ):
            # testing all rotations
            test_shape = initial.copy_shape()
            # clockwise
            order_to_check = [right_rotation, reverse_rotation, left_rotation, initial]
            for to_check in order_to_check:
                test_shape.rotate(m_rotation.Rotation.RIGHT)
                self.assertTrue(test_shape.is_equal(to_check))

            # anticlockwise
            order_to_check = [left_rotation, reverse_rotation, right_rotation, initial]
            for to_check in order_to_check:
                test_shape.rotate(m_rotation.Rotation.LEFT)
                self.assertTrue(test_shape.is_equal(to_check))

        # for the <I> tetromino
        tetromino_type = m_tetromino_type.TetrominoType.I_SHAPE
        shape_initial = m_shape.Shape(4, 4)
        shape_right_rotation = m_shape.Shape(4, 4)
        shape_reverse_rotation = m_shape.Shape(4, 4)
        shape_left_rotation = m_shape.Shape(4, 4)

        shape_initial.set_boxes([
            [None, None, None, None],
            [tetromino_type, tetromino_type, tetromino_type, tetromino_type],
            [None, None, None, None],
            [None, None, None, None]
        ])
        shape_right_rotation.set_boxes([
            [None, None, tetromino_type, None],
            [None, None, tetromino_type, None],
            [None, None, tetromino_type, None],
            [None, None, tetromino_type, None]
        ])
        shape_reverse_rotation.set_boxes([
            [None, None, None, None],
            [None, None, None, None],
            [tetromino_type, tetromino_type, tetromino_type, tetromino_type],
            [None, None, None, None]
        ])
        shape_left_rotation.set_boxes([
            [None, tetromino_type, None, None],
            [None, tetromino_type, None, None],
            [None, tetromino_type, None, None],
            [None, tetromino_type, None, None]
        ])

        test_one_shape(
            shape_initial,
            shape_right_rotation,
            shape_reverse_rotation,
            shape_left_rotation
        )

        # for the <O> tetromino
        tetromino_type = m_tetromino_type.TetrominoType.O_SHAPE
        shape_initial = m_shape.Shape(3, 4)
        shape_right_rotation = m_shape.Shape(4, 3)
        shape_reverse_rotation = m_shape.Shape(3, 4)
        shape_left_rotation = m_shape.Shape(4, 3)

        shape_initial.set_boxes([
            [None, tetromino_type, tetromino_type, None],
            [None, tetromino_type, tetromino_type, None],
            [None, None, None, None],
        ])
        shape_right_rotation.set_boxes([
            [None, None, None],
            [None, tetromino_type, tetromino_type],
            [None, tetromino_type, tetromino_type],
            [None, None, None]
        ])
        shape_reverse_rotation.set_boxes([
            [None, None, None, None],
            [None, tetromino_type, tetromino_type, None],
            [None, tetromino_type, tetromino_type, None],
        ])
        shape_left_rotation.set_boxes([
            [None, None, None],
            [tetromino_type, tetromino_type, None],
            [tetromino_type, tetromino_type, None],
            [None, None, None]
        ])

        test_one_shape(
            shape_initial,
            shape_right_rotation,
            shape_reverse_rotation,
            shape_left_rotation
        )


if __name__ == '__main__':
    unittest.main()
