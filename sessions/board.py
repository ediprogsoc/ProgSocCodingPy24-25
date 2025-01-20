from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.makeBoard()
        self.selected: Piece | None = None

    def __str__(self):
        return str(self.board)

    def makeBoard(self):
        # self.board[rowNum][colNum]
        for rowNum in range(8):
            self.board.append([None]*8)
            # [None, None, None, ..., None]
            for colNum in range(8):
                if rowNum in [0, 1, 6, 7]:
                    self.board[rowNum][colNum] = Piece(rowNum, colNum)

    def selectPiece(self, position):
        pass

    def movePiece(self, position):
        pass

    @staticmethod
    def chessToIndex(notation):
        # E.g. a1
        letter, number = notation.split("")
        col = ord(letter.lower())-97
        row = int(number)
        return row, col


if __name__ == '__main__':
    b = Board()
    print(b)
