pieceIdentifier = {
    (0, 0): "Rook",
    (0, 1): "Knight",
    (0, 2): "Bishop",
    (0, 3): "Queen",
    (0, 4): "King",
    (0, 5): "Bishop",
    (0, 6): "Knight",
    (0, 7): "Rook",
    (7, 0): "Rook",
    (7, 1): "Knight",
    (7, 2): "Bishop",
    (7, 3): "King",
    (7, 4): "Queen",
    (7, 5): "Bishop",
    (7, 6): "Knight",
    (7, 7): "Rook"
}


class Piece:
    def __init__(self, rowNum, colNum):
        self.position = [rowNum, colNum]
        if rowNum in [1, 6]:
            self.pieceName = "Pawn"
        else:
            self.pieceName = pieceIdentifier[self.position]
        self.isWhitePiece = rowNum < 4

    def getMovement(self) -> list:
        movement = []
        # forward = 1 if self.isWhitePiece else -1
        forward = 2*self.isWhitePiece - 1
        match self.pieceName:
            case "Pawn":
                movement.append((0, 1*forward))
                if (self.position[0] == 1 and self.isWhitePiece) or (self.position[0] == 6 and not self.isWhitePiece):
                    movement.append((0, 2*forward))
            case "Rook":
                for i in range(-7, 8):
                    if i == 0:
                        continue
                    newRow = self.position[0] + i
                    newCol = self.position[1] + i
                    if self.isValidIndex(newRow):
                        movement.append((0, i))
                    if self.isValidIndex(newCol):
                        movement.append((i, 0))
            case "Knight":
                for dx in [-1, 1]:
                    for dy in [-2, 2]:
                        newRow1 = self.position[0] + dx
                        newCol1 = self.position[1] + dy
                        if self.isValidIndex(newRow1) and self.isValidIndex(newCol1):
                            movement.append((dx, dy))
                        newRow2 = self.position[0] + dy
                        newCol2 = self.position[1] + dx
                        if self.isValidIndex(newRow2) and self.isValidIndex(newCol2):
                            movement.append((dy, dx))
            case "Bishop":
                for i in range(-7, 8):
                    if i == 0:
                        continue
                    newRow = self.position[0] + i
                    newCol = self.position[1] + i
                    if self.isValidIndex(newRow) and self.isValidIndex(newCol):
                        movement.append((i, i))
            case "King":
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dy == 0 and dx == 0:
                            continue
                        movement.append((dx, dy))
            case "Queen":
                for i in range(-7, 8):
                    if i == 0:
                        continue
                    newRow = self.position[0] + i
                    newCol = self.position[1] + i
                    if self.isValidIndex(newRow):
                        movement.append((0, i))
                    if self.isValidIndex(newCol):
                        movement.append((i, 0))
                    if self.isValidIndex(newRow) and self.isValidIndex(newCol):
                        movement.append((i, i))
        return movement

    @staticmethod
    def isValidIndex(index):
        return 0 <= index <= 7


if __name__ == '__main__':
    print(ord('a'))
