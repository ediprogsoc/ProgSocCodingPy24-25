from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.whitesTurn = True
        self.history = []
        self.running = False

    def startGame(self):
        self.running = True
        while self.running:
            # select a piece
            # move the piece - valid
            # is won
            # add history
            self.whitesTurn = not self.whitesTurn


if __name__ == '__main__':
    g = Game()
    g.startGame()
