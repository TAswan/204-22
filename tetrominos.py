# (0, 0) is the anchor coordinate
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
        [(0, 0), (1, 0), (-1, 0), (-1, 1)] ,    # Original position
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
