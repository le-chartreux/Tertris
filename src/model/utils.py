"""
File that contains various utils for the model
"""
import common.tetromino_type as p_tetromino_type
import model.shape as p_shape


def get_tetromino_shape(tetromino_type: p_tetromino_type.TetrominoType) -> p_shape.Shape:
    shape = p_shape.Shape(4, 4)
    # (x, y) tuple
    positions: tuple[
        tuple[int, int],
        tuple[int, int],
        tuple[int, int],
        tuple[int, int]
    ]
    if tetromino_type == p_tetromino_type.TetrominoType.I:
        """
         0123
        [    ] 0
        [####] 1
        [    ] 2
        [    ] 3
        """
        positions = (
            (0, 1),
            (1, 1),
            (2, 1),
            (3, 1)
        )
    elif tetromino_type == p_tetromino_type.TetrominoType.O:
        """
         0123
        [    ] 0
        [ ## ] 1
        [ ## ] 2
        [    ] 3
        """
        positions = (
            (1, 1),
            (2, 1),
            (1, 2),
            (2, 2)
        )
    elif tetromino_type == p_tetromino_type.TetrominoType.T:
        """
         0123
        [    ] 0
        [ #  ] 1
        [ ## ] 2
        [ #  ] 3
        """
        positions = (
            (1, 1),
            (1, 2),
            (2, 2),
            (3, 1)
        )
    elif tetromino_type == p_tetromino_type.TetrominoType.L:
        """
         0123
        [    ] 0
        [ ###] 1
        [ #  ] 2
        [    ] 3
        """
        positions = (
            (1, 1),
            (2, 1),
            (3, 1),
            (1, 2)
        )
    elif tetromino_type == p_tetromino_type.TetrominoType.J:
        """
         0123
        [    ] 0
        [ ###] 1
        [   #] 2
        [    ] 3
        """
        positions = (
            (1, 1),
            (2, 1),
            (3, 1),
            (1, 3)
        )
    elif tetromino_type == p_tetromino_type.TetrominoType.Z:
        """
         0123
        [    ] 0
        [ ## ] 1
        [  ##] 2
        [    ] 3
        """
        positions = (
            (1, 1),
            (2, 1),
            (2, 2),
            (3, 2)
        )
    elif tetromino_type == p_tetromino_type.TetrominoType.S:
        """
         0123
        [    ] 0
        [ ## ] 1
        [##  ] 2
        [    ] 3
        """
        positions = (
            (1, 1),
            (2, 1),
            (0, 2),
            (1, 2)
        )
    else:
        if isinstance(tetromino_type, p_tetromino_type.TetrominoType):
            raise ValueError(
                "Error: impossible to create the tetromino shape for the given tetromino: invalid tetromino type (%s)"
                % tetromino_type.name
            )
        else:
            raise TypeError(
                "Error: impossible to create the tetromino shape for the given tetromino: "
                "type must be TetrominoType but a %s is given."
                % type(tetromino_type).name
            )

    for position in positions:
        shape.set_box(tetromino_type, position[0], position[1])
