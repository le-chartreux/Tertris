"""
File that contains the declaration of the Shape class
"""
import typing

import common.rotation as m_rotation
import common.tetromino_type as m_tetromino_type


class Shape:
    def __init__(self, height: int, width: int):
        """
        Creates a Shape object, a list of list rectangle filled with None

        :param height: the height of the rectangle (number of list of list)
        :param width: the width of the rectangle (size of list of list)
        """
        self._boxes: list[list[typing.Optional[m_tetromino_type.TetrominoType]]] = [
            [
                None for _ in range(width)
            ] for _ in range(height)
        ]

    # GETTERS
    def get_height(self) -> int:
        """
        :return: the height of the rectangle (number of list of list)
        """
        return len(self._boxes)

    def get_width(self) -> int:
        """
        :return: the width of the rectangle (size of list in list)
        """
        if len(self._boxes) == 0:
            return 0
        else:
            return len(self._boxes[0])

    def get_box(self, x: int, y: int) -> typing.Optional[m_tetromino_type.TetrominoType]:
        """
        :param x: horizontal position of the box we want
        :param y: vertical position of the box we want
        :return: the box at (x, y)
        """
        return self._boxes[y][x]

    def get_boxes(self) -> list[list[typing.Optional[m_tetromino_type.TetrominoType]]]:
        return self._boxes

    # SETTERS
    def set_box(self, box_value: typing.Optional[m_tetromino_type.TetrominoType], x: int, y: int) -> None:
        """
        :param box_value: new value of the box at (x, y)
        :param x: horizontal position of the box we want to set
        :param y: vertical position of the box we want to set
        """
        self._boxes[y][x] = box_value

    def set_boxes(self, boxes: list[list[typing.Optional[m_tetromino_type.TetrominoType]]]) -> None:
        self._boxes = boxes

    def is_occupied(self, x: int, y: int) -> bool:
        """
        :param x: horizontal position of the box we want to know if occupied
        :param y: vertical position of the box we want to know if occupied
        :return: if the box at (x, y) is occupied
        """
        return self.get_box(x, y) is not None

    def can_combine_perfectly(self, other_shape: "Shape", x_overlay: int, y_overlay: int) -> bool:
        """
        Checks if a logical "xor" can be made on the two shapes.
        If at least one box is occupied on the two shapes, will return False. Else will return True

        :param other_shape: other shape to combine. Have to be smaller that this one, including the overlay
        :param x_overlay: horizontal overlay
        :param y_overlay: vertical overlay
        :return: the combination of this shape and the given shape
        """
        # checking that the overlay doesn't put some other_shape's occupied boxes outside of self borders
        for y in range(other_shape.get_height()):
            for x in range(other_shape.get_width()):
                if (
                    other_shape.is_occupied(x, y)
                    and
                    (
                        x + x_overlay >= self.get_width()
                        or
                        x + x_overlay < 0
                        or
                        y + y_overlay >= self.get_height()
                        or
                        y + y_overlay < 0
                    )
                ):
                    return False

        # checking that the combination won't put two occupied box at the same place
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                if (
                    self.is_occupied(x, y)
                    and
                    (
                        0 <= x - x_overlay < other_shape.get_width()
                        and
                        0 <= y - y_overlay < other_shape.get_height()
                        and
                        other_shape.is_occupied(x - x_overlay, y - y_overlay)
                    )
                ):
                    return False

        return True

    def combine(self, other_shape: "Shape", x_overlay: int, y_overlay: int) -> "Shape":
        """
        Does a logical "or" on the two shapes, and returns the result. If a box is occupied on the two shapes, the one
        of self is kept.

        :param other_shape: other shape to combine. Has to be smaller that this one or the same size
        :param x_overlay: horizontal overlay
        :param y_overlay: vertical overlay
        :return: the combination of this shape and the given shape
        """
        combination = Shape(self.get_height(), self.get_width())

        # adding other_shape on the combination
        for y in range(other_shape.get_height()):
            for x in range(other_shape.get_width()):
                if other_shape.is_occupied(x, y):
                    combination.set_box(other_shape.get_box(x, y), x + x_overlay, y + y_overlay)

        # adding self on the combination (and replacing other_shape elements if needed)
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                if self.is_occupied(x, y):
                    combination.set_box(self.get_box(x, y), x, y)

        return combination

    def copy_shape(self) -> "Shape":
        """
        :return: a copy of self. Modifying it doesn't modify self
        """
        new_shape = Shape(self.get_height(), self.get_width())
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                new_shape.set_box(
                    self.get_box(x, y),
                    x,
                    y
                )

        return new_shape

    def rotate(self, rotation: m_rotation.Rotation) -> None:
        """
        Rotate the shape according to the asked rotation

        :param rotation: the rotation the shape has to move to
        """
        new_shape = Shape(self.get_height(), self.get_width())

        if rotation == m_rotation.Rotation.RIGHT:
            for y in range(self.get_height()):
                for x in range(self.get_width()):
                    new_shape.set_box(
                        self.get_box(x, y),
                        self.get_height() -1 - y,
                        x
                    )
        elif rotation == m_rotation.Rotation.LEFT:
            for y in range(self.get_height()):
                for x in range(self.get_width()):
                    new_shape.set_box(
                        self.get_box(x, y),
                        y,
                        self.get_width() -1 - x
                    )
        elif rotation == m_rotation.Rotation.REVERSE:
            for y in range(self.get_height()):
                for x in range(self.get_width()):
                    new_shape.set_box(
                        self.get_box(x, y),
                        self.get_width() - 1 - x,
                        self.get_height() - 1 - y
                    )
        else:
            if isinstance(rotation, m_rotation.Rotation):
                raise ValueError(
                    "Error: invalid rotation given: name = %s; value = %s" % (rotation.name, rotation.value)
                )
            else:
                raise ValueError(
                    "Error: invalid rotation given: type must be Rotation but a %s is given" % type(rotation)
                )

        self.set_boxes(new_shape.get_boxes())

    def is_equal(self, other_shape: "Shape") -> bool:
        """
        :param other_shape: the other shape we want to compare to this one
        :return: if the two shapes are equals
        """
        if self.get_width() != other_shape.get_width() or self.get_height() != other_shape.get_height():
            return False

        x = 0
        equals = True
        while x < other_shape.get_width() and equals:
            y = 0
            while y < other_shape.get_height() and equals:
                if (
                    self.get_box(x, y) != other_shape.get_box(x, y)
                ):
                    equals = False
                y += 1
            x += 1

        return equals
