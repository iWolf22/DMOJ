# Problem: CCC '17 J3 - Exactly Electrical (ccc17j3)
# Problem URL: https://dmoj.ca/problem/ccc17j3
# Submission: 3320087 (https://dmoj.ca/submission/3320087)
# Language: Python (PY3)
# Submitted: 2021-01-24T16:51:20+00:00

#CCC '17 J3 - Exactly Electrical

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

num3 = int(input())

distanceX = num1[0] - num2[0]
distanceY = num1[1] - num2[1]

if distanceX < 0:
    distanceX = distanceX * -1
if distanceY < 0:
    distanceY = distanceY * -1

distance = distanceX + distanceY

if distance % 2 == num3 % 2 and distance <= num3:
    print("Y")
else:
    print("N")