# Problem: ECOO '21 P1 - Many Messages (ecoo21p1)
# Problem URL: https://dmoj.ca/problem/ecoo21p1
# Submission: 3605218 (https://dmoj.ca/submission/3605218)
# Language: Python (PY3)
# Submitted: 2021-05-04T02:17:43+00:00

# Many Messages

num1 = int(input())
num2 = int(input())
num3 = int(input())

temp = True

for i in range(3):
    num1 += num2
    if num1 >= num3:
        print(num1)
        temp = False
        break

if temp == True:
    print("Who knows...")