def isWon(board: list[list[int]]) -> bool:
    for i in range(3):
        # Check the columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != -1:
            return True
        # Check the rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != -1:
            return True

    # Check the diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != -1:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != -1:
        return True

    return False


def printBoard(board: list[list[int]]) -> None:
    print("|-----+-----+-----|")
    for row in board:
        for value in row:
            if value == 0:
                out = "O"
            elif value == 1:
                out = "X"
            else:
                out = " "
            print("|  " + out, end="  ")
        print("|\n|-----+-----+-----|")


board: list[list[int]] = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1]
]
currentPlayer: int = 0
while True:
    print("\nPlayer " + str(currentPlayer + 1) + "'s Turn")
    printBoard(board)
    col: int = int(input("Which Column? ")) - 1
    row: int = int(input("Which Row? ")) - 1
    if board[row][col] != -1:
        print("That space is occupied. Try Again.")
        continue
    board[row][col] = currentPlayer
    if isWon(board):
        print("Player", currentPlayer + 1, "has won!")
        printBoard(board)
        break
    currentPlayer = (currentPlayer + 1) % 2
