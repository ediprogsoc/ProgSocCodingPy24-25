
def checkWin(current_player, board):
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == current_player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        return True

    # Rows and Columns
    for i in range(3):
        # Column i
        if board[0][i] == board[1][i] == board[2][i] == current_player:
            return True
        # Row i
        if board[i][0] == board[i][1] == board[i][2] == current_player:
            return True
    # Not won
    return False


board = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1]
]
zero = " 0 "
ex = " X "
current_player = 0

while True:
    # Check win
    won = checkWin(current_player, board)
    if won:
        print("Player", current_player + 1, "has won!")
        break
    current_player = (current_player + 1) % 2

    # Show Board
    print("-------------")  # Dashes = space + bars
    for row in board:
        print(end="|")
        for value in row:
            if value == 1:
                out = ex
            elif value == 0:
                out = zero
            else:
                out = "   "
            print(out, end="|")
        print()
        print("-------------")
    # Input
    column = int(input("Enter a column. ")) - 1
    row = int(input("Enter a row. ")) - 1

    val = board[row][column]
    if val != -1:
        print("Space already taken.")
        continue

    board[row][column] = current_player
