# Problem: CCC '18 J1 - Telemarketer or not? (ccc18j1)
# Problem URL: https://dmoj.ca/problem/ccc18j1
# Submission: 3371306 (https://dmoj.ca/submission/3371306)
# Language: Python (PY3)
# Submitted: 2021-02-06T22:26:03+00:00

# CCC '18 J1 - Telemarketer or not?

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if (num1 == 8 or num1 == 9) and (num4 == 8 or num4 == 9) and num2 == num3:
    print("ignore")
else:
    print("answer")