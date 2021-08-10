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
    if tetromino_type == m_tetromino_type.TetrominoType.I_SHAPE:
        """
        [    ]
        [####]
        [    ]
        [    ]
        """
        shape = m_shape.Shape(4, 4)
        shape.set_boxes([
            [None, None, None, None],
            [tetromino_type, tetromino_type, tetromino_type, tetromino_type],
            [None, None, None, None],
            [None, None, None, None]
        ])
        return shape
    elif tetromino_type == m_tetromino_type.TetrominoType.O_SHAPE:
        """
        in guidelines it's:
        [ ## ]
        [ ## ]
        [    ]
        but this one is better with my code:
        [##]
        [##]
        """

        shape = m_shape.Shape(2, 2)
        shape.set_boxes([
            [tetromino_type, tetromino_type],
            [tetromino_type, tetromino_type]
        ])
        return shape
    elif tetromino_type == m_tetromino_type.TetrominoType.T_SHAPE:
        """
        [ # ] 
        [###] 
        [   ] 
        """
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [None, tetromino_type, None],
            [tetromino_type, tetromino_type, tetromino_type],
            [None, None, None],
        ])
        return shape
    elif tetromino_type == m_tetromino_type.TetrominoType.L_SHAPE:
        """
        [  #]
        [###]
        [   ]
        """
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [None, None, tetromino_type],
            [tetromino_type, tetromino_type, tetromino_type],
            [None, None, None],
        ])
        return shape
    elif tetromino_type == m_tetromino_type.TetrominoType.J_SHAPE:
        """
        [#  ]
        [###]
        [   ] 
        """
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [tetromino_type, None, None],
            [tetromino_type, tetromino_type, tetromino_type],
            [None, None, None],
        ])
        return shape
    elif tetromino_type == m_tetromino_type.TetrominoType.Z_SHAPE:
        """
        [## ]
        [ ##]
        [   ]
        """
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [tetromino_type, tetromino_type, None],
            [None, tetromino_type, tetromino_type],
            [None, None, None],
        ])
        return shape
    elif tetromino_type == m_tetromino_type.TetrominoType.S_SHAPE:
        """
        [ ## ]
        [##  ]
        [    ]
        """
        shape = m_shape.Shape(3, 3)
        shape.set_boxes([
            [None, tetromino_type, tetromino_type],
            [tetromino_type, tetromino_type, None],
            [None, None, None],
        ])
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
                % type(tetromino_type).name
            )


def random_tetromino() -> m_tetromino_type.TetrominoType:
    return random.choice([
        tetromino_type for tetromino_type in m_tetromino_type.TetrominoType.__iter__()
    ])
