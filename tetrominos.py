'''
Tetromino's are consist of multiple blocks, so we need to create said
blocks every time we create a Tetromino (e.g. when it moves). These
tuples provide the values from which the block coordinates extend out
from the anchor point--(0, 0) is the anchor coordinate since the
anchor coordinate plus 0 gives the anchor coordinate.
'''
TETROMINOS = {
    "line": [
        [(0, 0), (1, 0), (2, 0), (-1, 0)],      # Original position
        [(0, 0), (0, -1), (0, 1), (0, 2)],      # 90 degrees rotation
        [(0, 0), (1, 0), (2, 0), (-1, 0)],      # 180 degrees rotation
        [(0, 0), (0, -1), (0, 1), (0, 2)]       # 270 degrees rotation
    ],
    "square": [
        [(0, 0), (1, 0), (0, -1), (1, -1)],     # Original position
        [(0, 0), (1, 0), (0, -1), (1, -1)],     # 90 degrees rotation
        [(0, 0), (1, 0), (0, -1), (1, -1)],     # 180 degrees rotation
        [(0, 0), (1, 0), (0, -1), (1, -1)]      # 270 degrees rotation
    ],
    "J": [
        [(0, 0), (1, 0), (-1, 0), (1, 1)],      # Original position
        [(0, 0), (0, 1), (0, -1), (-1, 1)],     # 90 degrees rotation
        [(0, 0), (1, 0), (-1, 0), (-1, -1)],    # 180 degrees rotation
        [(0, 0), (0, 1), (0, -1), (1, -1)]      # 270 degrees rotation
    ],
    "L": [
        [(0, 0), (1, 0), (-1, 0), (-1, 1)],     # Original position
        [(0, 0), (0, 1), (-1, -1), (0, -1)],    # 90 degrees rotation
        [(0, 0), (1, 0), (-1, 0), (1, -1)],     # 180 degrees rotation
        [(0, 0), (0, 1), (0, -1), (1, 1)]       # 270 degrees rotation
    ],
    "S": [
        [(0, 0), (1, 0), (0, 1), (-1, 1)],      # Original position
        [(0, 0), (0, 1), (-1, 0), (-1, -1)],    # 90 degrees rotation
        [(0, 0), (1, 0), (0, 1), (-1, 1)],      # 180 degrees rotation
        [(0, 0), (0, 1), (-1, 0), (-1, -1)],    # 270 degrees rotation
    ],
    "T": [
        [(0, 0), (1, 0), (-1, 0), (0, 1)],      # Original position
        [(0, 0), (0, 1), (0, -1), (-1, 0)],     # 90 degrees rotation
        [(0, 0), (1, 0), (-1, 0), (0, -1)],     # 180 degrees rotation
        [(0, 0), (0, 1), (0, -1), (1, 0)]       # 270 degrees rotation
    ],
    "Z": [
        [(0, 0), (-1, 0), (0, 1), (1, 1)],      # Original position
        [(0, 0), (0, -1), (-1, 0), (-1, 1)],    # 90 degrees rotation
        [(0, 0), (-1, 0), (0, 1), (1, 1)],      # 180 degrees rotation
        [(0, 0), (0, -1), (-1, 0), (-1, 1)]     # 270 degrees rotation
    ]
}
