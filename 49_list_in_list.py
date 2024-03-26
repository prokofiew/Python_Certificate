board = []

for i in range(8):
    row = ["x" for i in range(8)]
    board.append(row)

for i in board:
    print(i)

print()
print("========== OTHER WAY ===========")
# OTHER WAY

board2 = [["y" for i in range(8)] for j in range(8)]

for i in board2:
    print(i)
