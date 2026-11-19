# Problem: CCC '20 S1 - Surmising a Sprinter's Speed (ccc20s1)
# Problem URL: https://dmoj.ca/problem/ccc20s1
# Submission: 4753120 (https://dmoj.ca/submission/4753120)
# Language: Python (PY3)
# Submitted: 2022-08-06T23:36:50+00:00

# CCC '20 S1 - Surmising a Sprinter's Speed

import math

num_nodes = int(input())

time_loc = []

for i in range(num_nodes):
    time_loc.append(list(map(int,input().split())))

time_loc.sort(key = lambda time_loc: time_loc[0])

fastest = 0

for i in range(num_nodes - 1):
    if fastest < abs(time_loc[i][1] - time_loc[i + 1][1]) / abs(time_loc[i][0] - time_loc[i + 1][0]):
        fastest = abs(time_loc[i][1] - time_loc[i + 1][1]) / abs(time_loc[i][0] - time_loc[i + 1][0])

print(fastest)