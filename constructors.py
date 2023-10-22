from random import randint

class Board:
    def __init__(self):
        self.board = [[False for _ in range(10)] for _ in range(4)] + [[True if randint(0, 1) else False for _ in range(10)] for _ in range(16)]

    def __repr__(self):
        strOut = ''
        for row in self.board:
            for col in row:
                strOut += str(col) + '\t'
            strOut += '\n'
        return strOut
    
if __name__ == '__main__':
    board = Board()
    print(board)