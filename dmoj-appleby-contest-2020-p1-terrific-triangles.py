# Problem: Appleby Contest '20 P1 - Terrific Triangles (ac20p1)
# Problem URL: https://dmoj.ca/problem/ac20p1
# Submission: 3591817 (https://dmoj.ca/submission/3591817)
# Language: Python (PY3)
# Submitted: 2021-04-27T02:47:53+00:00

import math

num = int(input())

num_list = []

for i in range(num):
    num_list.append(list(map(int,input().split())))

for i in range(num):
    num_list[i] = sorted(num_list[i])
    
    if (num_list[i][0] ** 2) + (num_list[i][1] ** 2) == num_list[i][2] ** 2:
        print("R")
    elif (num_list[i][0] ** 2) + (num_list[i][1] ** 2) > num_list[i][2] ** 2:
        print("A")
    else:
        print("O")