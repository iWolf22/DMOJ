# Problem: Mock CCC '18 Contest 2 J1 - An Arithmetic Problem (nccc2j1)
# Problem URL: https://dmoj.ca/problem/nccc2j1
# Submission: 2129277 (https://dmoj.ca/submission/2129277)
# Language: Python (PY3)
# Submitted: 2020-06-04T02:54:27+00:00

num = input("").split()
a = int(num[0])
b = int(num[2])
c = int(num[4])
if a + b == c:
    print("True")
else:
    print("False")