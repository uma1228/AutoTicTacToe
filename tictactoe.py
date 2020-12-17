
board = [[None, None, None], [None, None, None], [None, None, None]]  # 0 is O and 1 is X


def playMove(play, row, col):  # takes in 0 or 1 based on the move
    global board
    if board[row][col] is None:  # making sure that the spot is not played yet
        board[row][col] = play


def printBoard():
    for i in range(len(board)):
        print(board[i])


playMove(0, 0, 0)
playMove(1,2,2)
playMove(0,2,2)
printBoard()