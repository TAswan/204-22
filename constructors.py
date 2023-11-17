from bauhaus import Encoding, proposition, constraint

from random import randint

from tetrominos import TETROMINOS

E = Encoding()

class Hashable:
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, __value: object) -> bool:
        return hash(self) == hash(__value)

    def __repr__(self):
        return str(self)

class Node():
    # A node class for A* Pathfinding

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):               #<-- added a hash method
        return hash(self.position)

@proposition(E)
class Tetromino:
    # Tetromino of shape and rotation at anchor at time 
    def init(self, anchor, shape, rotation, time):
        a = Block(anchor[0], anchor[1], time)
        piece_coordinates = []
        for coordinates in TETROMINOS[shape][rotation]:
            piece_coordinates.append(Block(anchor[0] + coordinates[0], anchor[1] + coordinates[1], time))
        self.anchor = a
        self.tetromino = piece_coordinates

    # def init(self, anchor, piece_coordinates, rotation_states):
    #     self.anchor = anchor
    #     self.piece_coordinates = piece_coordinates
    #     self.rotation_states = rotation_states
    #     self.current_rotation = 0
        
    # def rotate(self):
    #     self.current_rotation = (self.current_rotation + 1) % len(self.rotation_states)
    #     self.piece_coordinates = self.rotation_states[self.current_rotation]

    def display(self):
        print("Anchor Coordinate:", self.anchor)
        print("Piece Coordinates:")
        for coord in self.piece_coordinates:
            print("  ", coord)
        # print("Current Rotation State:", self.current_rotation)

@proposition(E)
class Cell(Hashable):
    # Cell_x_y is occupied on the board
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Board cell ({self.x}, {self.y}) is occupied"

class Board:
    # List of Cell propositions which denoted which cells of the board are occupied
    def __init__(self):
        board = [[None for _ in range(10)] for _ in range(20)]
        for row in range(4, 20):
            for col in range(10):
                if randint(0, 1):
                    board[col][row] = (Cell(row, col))

        self.board = board

    def __repr__(self):
        board = [["⬛️" for _ in range(10)] for _ in range(20)]
        for cell in self.board:
            board[cell.x][cell.y] = "🟦"

        strOut = ''
        for row in board:
            strOut += ' '.join(row) + "\n"

        return strOut

@proposition(E)
class Block(Hashable):
    # Block of a Tetromino coordinate (x,y) is occupied on the board at time t
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    def __repr__(self):
        return f"Block of a Tetromino is located at ({self.x}, {self.y}) at time t"
    
@proposition(E)
class Row_Cleared(Hashable):
    # Row row has been cleared
    def __init__(self, row):
        self.row = row

    def __repr__(self):
        return f"Row {self.row} has been cleared"
