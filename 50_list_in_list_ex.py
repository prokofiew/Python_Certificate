board = [["-" for i in range(8)] for j in range(8)]

board[0][0] = "R"
board[0][7] = "R"
board[7][0] = "R"
board[7][7] = "R"
board[4][2] = "K"
board[3][4] = "P"

for i in board:
    print(i)
