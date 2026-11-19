# Problem: CCCHK '15 J3 - Queens can't attack me! (hkccc15j3)
# Problem URL: https://dmoj.ca/problem/hkccc15j3
# Submission: 3557809 (https://dmoj.ca/submission/3557809)
# Language: Python (PY3)
# Submitted: 2021-04-12T17:22:10+00:00

# CCCHK '15 J3 - Queens can't attack me!

def queen(queen_list,queen):
    for i in range(len(queen_list)):
        for j in range(len(queen_list[i])):
            if queen_list[i][j] == "0":
                if queen[0] == i + 1 or queen[1] == j + 1 or queen[0] - (i + 1) == queen[1] - (j + 1) or (queen[0] - (i + 1)) * -1 == queen[1] - (j + 1):
                    queen_list[i][j] = "1"

    return(queen_list)

board,num_queens = list(map(int,input().split()))

board = [["0" for i in range(board)] for i in range(board)]

queen_list = []

for i in range(num_queens):
    queen_list.append(list(map(int,input().split())))

for i in range(num_queens):
    board[queen_list[i][0] - 1][queen_list[i][1] - 1] = "Q"

for i in range(len(queen_list)):
    board = queen(board,queen_list[i])

counter = 0
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == "0":
            counter += 1

print(counter)