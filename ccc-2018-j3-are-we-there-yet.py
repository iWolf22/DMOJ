# Problem: CCC '18 J3 - Are we there yet? (ccc18j3)
# Problem URL: https://dmoj.ca/problem/ccc18j3
# Submission: 3371692 (https://dmoj.ca/submission/3371692)
# Language: Python (PY3)
# Submitted: 2021-02-06T23:35:03+00:00

num_list = []
num_list = list(map(int,input().split()))
num_list.insert(0,0)

array = [[0 for i in range(5)] for i in range(5)]

for i in range(5):
    for j in range(5):
        num = 0
        if i == j:
            array[i][j] = num
        elif i < j:
            for k in range(i + 1,j + 1,1):
                num += num_list[k]
            array[i][j] = num
        else:
            for k in range(j + 1,i + 1,1):
                num += num_list[k]
            array[i][j] = num

for i in range(5):
    print(*array[i])