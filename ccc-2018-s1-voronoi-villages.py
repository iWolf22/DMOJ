# Problem: CCC '18 S1 - Voronoi Villages (ccc18s1)
# Problem URL: https://dmoj.ca/problem/ccc18s1
# Submission: 3372232 (https://dmoj.ca/submission/3372232)
# Language: Python (PY3)
# Submitted: 2021-02-07T01:23:24+00:00

import sys
input = sys.stdin.readline

num1 = int(input())

num_list = []

for i in range(num1):
    num_list.append(int(input()))

num_list.sort()

smallest = 10000000000000000
for i in range(1,num1 - 1):
    if smallest > ((num_list[i + 1] - num_list[i]) / 2) + ((num_list[i] - num_list[i - 1]) / 2):
        smallest = ((num_list[i + 1] - num_list[i]) / 2) + ((num_list[i] - num_list[i - 1]) / 2)

print(float(smallest))