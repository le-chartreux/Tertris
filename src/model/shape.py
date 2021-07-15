"""
File that contains the declaration of the Shape class
"""
import typing
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
    def get_boxes(self) -> list[list[typing.Optional[m_tetromino_type.TetrominoType]]]:
        return self._boxes

    def get_box(self, x: int, y: int) -> typing.Optional[m_tetromino_type.TetrominoType]:
        """
        :param x: horizontal position of the box we want
        :param y: vertical position of the box we want
        :return: the box at (x, y)
        """
        return self._boxes[y][x]

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

    def combine(self, other_shape: "Shape", x_overlay: int, y_overlay: int) -> "Shape":
        """
        Does a logical "or" on the two shapes, and returns the result. If a box is occupied on the two shapes, the one
        of self is kept.

        :param other_shape: other shape to combine. Have to be smaller that this one
        :param x_overlay: horizontal overlay. Positive. Have to be small enough so <other_shape> is smaller than self
        :param y_overlay: vertical overlay. Positive. Have to be small enough so <other_shape> is smaller than self
        :return: the combination of this shape and the given shape
        """
        combination = Shape(self.get_width(), self.get_height())
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                if self.is_occupied(x, y):
                    combination.set_box(self.get_box(x, y), x, y)
                elif (
                        y + y_overlay < other_shape.get_height()
                        and x + x_overlay < other_shape.get_width()
                        and other_shape.is_occupied(x, y)
                ):
                    combination.set_box(other_shape.get_box(x, y), x, y)
                # else we let it at None

        return combination

    def get_height(self) -> int:
        """
        :return: the height of the rectangle (number of list of list)
        """
        return len(self._boxes)

    def get_width(self) -> int:
        """
        :return: the width of the rectangle (size of list of list)
        """
        if len(self._boxes) == 0:
            return 0
        else:
            return len(self._boxes[0])
