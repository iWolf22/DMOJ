# Problem: CCC '19 J2 - Time to Decompress (ccc19j2)
# Problem URL: https://dmoj.ca/problem/ccc19j2
# Submission: 3440118 (https://dmoj.ca/submission/3440118)
# Language: Python (PY3)
# Submitted: 2021-02-21T17:10:15+00:00

#CCC '19 J2 - Time to Decompress

num1 = int(input())

list1 = []

for i in range(num1):
    list1.append(input().split())

for i in range(num1):
    print(int(list1[i][0]) * list1[i][1])