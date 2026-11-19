# Problem: CCC '12 S5 - Mouse Journey (ccc12s5)
# Problem URL: https://dmoj.ca/problem/ccc12s5
# Submission: 4577229 (https://dmoj.ca/submission/4577229)
# Language: 
# Submitted: 2022-05-23T18:52:52+00:00

# CCC '12 S5 - Mouse Journey

area_size = list(map(int,input().split()))

matrix = [[0 for i in range(area_size[1] + 1)] for j in range(area_size[0] + 1)]

matrix[0][1] = 1

num_cats = int(input())

for i in range(num_cats):
    temp_cat = list(map(int,input().split()))
    matrix[temp_cat[0]][temp_cat[1]] = -1

for i in range(1,len(matrix)):
    for j in range(1,len(matrix[i])):


        if matrix[i][j] != -1:

            if matrix[i][j - 1] != -1 and matrix[i - 1][j] != -1:
                matrix[i][j] = matrix[i][j] + matrix[i][j - 1] + matrix[i - 1][j]

            elif matrix[i][j - 1] == -1 and matrix[i - 1][j] != -1:
                matrix[i][j] = matrix[i][j] + matrix[i - 1][j]

            elif matrix[i][j - 1] != -1 and matrix[i - 1][j] == -1:
                matrix[i][j] = matrix[i][j] + matrix[i][j - 1]

            else:
                matrix[i][j] = 0

# for a in range(len(matrix)):
#     print(*matrix[a])

print(matrix[-1][-1])