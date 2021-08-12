"""
File that contains various utils for the model
"""
import random

import common.tetromino_type as m_tetromino_type
import model.shape as m_shape


def get_tetromino_shape(tetromino_type: m_tetromino_type.TetrominoType) -> m_shape.Shape:
    """
    :param tetromino_type: type of the tetromino we want the shape
    :return: the initial shape of the tetromino type given
    """
    # I use 4 letter names so it's the same size as None so the shape is clear
    i_te = m_tetromino_type.TetrominoType.I_SHAPE
    o_te = m_tetromino_type.TetrominoType.O_SHAPE
    s_te = m_tetromino_type.TetrominoType.S_SHAPE
    z_te = m_tetromino_type.TetrominoType.Z_SHAPE
    j_te = m_tetromino_type.TetrominoType.J_SHAPE
    l_te = m_tetromino_type.TetrominoType.L_SHAPE
    t_te = m_tetromino_type.TetrominoType.T_SHAPE

    bodies = {
        i_te: [
            [None, None, None, None],
            [i_te, i_te, i_te, i_te],
            [None, None, None, None],
            [None, None, None, None]
        ],
        o_te: [
            [o_te, o_te],
            [o_te, o_te]
        ],
        t_te: [
            [None, t_te, None],
            [t_te, t_te, t_te],
            [None, None, None]
        ],
        l_te: [
            [None, None, l_te],
            [l_te, l_te, l_te],
            [None, None, None],
        ],
        j_te: [
            [j_te, None, None],
            [j_te, j_te, j_te],
            [None, None, None],
        ],
        z_te: [
            [z_te, z_te, None],
            [None, z_te, z_te],
            [None, None, None],
        ],
        s_te: [
            [None, s_te, s_te],
            [s_te, s_te, None],
            [None, None, None]
        ]
    }
    if tetromino_type in bodies.keys():
        shape = m_shape.Shape(1, 1)  # since we set the boxes after we don't care about the width and height
        shape.set_boxes(bodies[tetromino_type])
        return shape
    else:
        if isinstance(tetromino_type, m_tetromino_type.TetrominoType):
            raise ValueError(
                "Error: impossible to create the tetromino shape for the given tetromino: invalid tetromino type (%s)"
                % tetromino_type.name
            )
        else:
            raise TypeError(
                "Error: impossible to create the tetromino shape for the given tetromino: "
                "type must be TetrominoType but a %s is given."
                % type(tetromino_type)
            )


def random_tetromino() -> m_tetromino_type.TetrominoType:
    return random.choice([
        tetromino_type for tetromino_type in m_tetromino_type.TetrominoType.__iter__()
    ])
