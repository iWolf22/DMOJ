# Problem: Mock CCC '18 Contest 3 J4/S2 - A Median Problem (nccc3j4s2)
# Problem URL: https://dmoj.ca/problem/nccc3j4s2
# Submission: 3672334 (https://dmoj.ca/submission/3672334)
# Language: Python (PY3)
# Submitted: 2021-06-12T02:11:09+00:00

# Mock CCC '18 Contest 3 J4/S2 - A Median Problem

num = int(input())

num_list = []

for i in range(num):
    num_list.append(list(map(int,input().split())))

new_list = []

for i in range(num):
    num_list[i] = sorted(num_list[i])

    if len(num_list[i]) % 2 == 1:
        new_list.append(num_list[i][int(len(num_list[i]) / 2)])
    else:
        new_list.append((num_list[i][int(len(num_list[i]) / 2) - 1] + num_list[i][int(len(num_list[i]) / 2)]) / 2)

num_list = sorted(new_list)

if len(num_list) % 2 == 1:
    print(num_list[int(len(num_list) / 2)])
else:
    print((num_list[int(len(num_list) / 2) - 1] + num_list[int(len(num_list) / 2)]) / 2)