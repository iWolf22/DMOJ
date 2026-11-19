# Problem: Sorting (a4b1)
# Problem URL: https://dmoj.ca/problem/a4b1
# Submission: 3556091 (https://dmoj.ca/submission/3556091)
# Language: Python (PY3)
# Submitted: 2021-04-11T22:10:26+00:00

num = int(input())

num_list = []

for i in range(num):
    num_list.append(int(input()))

num_list = sorted(num_list)


for i in range(num):
    print(num_list[i])