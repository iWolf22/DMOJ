# Problem: Bob's Reverse Number (oly21practice23)
# Problem URL: https://dmoj.ca/problem/oly21practice23
# Submission: 3506018 (https://dmoj.ca/submission/3506018)
# Language: Python (PY3)
# Submitted: 2021-03-22T20:22:25+00:00

num = input().split()

num1 = ""
num2 = ""

for i in range(len(num[0]) - 1,-1,-1):
    num1 = num1 + num[0][i]

for i in range(len(num[1]) - 1,-1,-1):
    num2 = num2 + num[1][i]

num1 = int(num1)
num2 = int(num2)

if num1 < num2:
    print(num1)
else:
    print(num2)