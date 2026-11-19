# Problem: CCC '11 J3 - Sumac Sequences (ccc11j3)
# Problem URL: https://dmoj.ca/problem/ccc11j3
# Submission: 3341151 (https://dmoj.ca/submission/3341151)
# Language: Python (PY3)
# Submitted: 2021-01-30T23:33:01+00:00

#CCC '11 J3 - Sumac Sequences

num2 = int(input())
num1 = int(input())

bool1 = True
counter = 1

while bool1 == True:
    counter += 1
    if num1 > num2:
        bool1 = False
    num3 = num2 - num1
    num2 = num1
    num1 = num3


print(counter)