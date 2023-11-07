from bauhaus import Encoding, proposition, constraint

from random import randint

E = Encoding()

class Hashable:
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, __value: object) -> bool:
        return hash(self) == hash(__value)

    def __repr__(self):
        return str(self)

class Node():
    #  A node class for A* Pathfinding

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
        board = []
        for row in range(4, 20):
            for col in range(10):
                if randint(0, 1):
                    board.append(Cell(row, col))

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
class Anchor(Hashable):
    # Anchor coordinate (x,y) is occupied on the board
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Anchor is located at ({self.x}, {self.y})"
    
@proposition(E)
class Row_Cleared(Hashable):
    # Row row has been cleared
    def __init__(self, row):
        self.row = row

    def __repr__(self):
        return f"Row {self.row} has been cleared"

@constraint.at_most_k(E, k=20)
@proposition(E)
class Time(Hashable):
    # Time_m how many moves have been made by the tetromino (1-20)
    def __init__(self, move):
        self.move = move

    def __repr__(self):
        return f"Move {self.move}"

if __name__ == '__main__':
    board = Board()
    print(board)