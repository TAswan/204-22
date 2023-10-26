from bauhaus import Encoding, proposition

from random import randint

E = Encoding()

class Hashable:
    def __hash__(self):
        return hash(str(self))

    def __eq__(self, __value: object) -> bool:
        return hash(self) == hash(__value)

    def __repr__(self):
        return str(self)

@proposition(E)
class Cell(Hashable):
    # Cell_x_y is occupied on the board
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Board cell [{self.x}, {self.y}] is occupied"

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

if __name__ == '__main__':
    board = Board()
    print(board)