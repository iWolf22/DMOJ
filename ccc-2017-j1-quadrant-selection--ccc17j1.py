# Problem: CCC '17 J1 - Quadrant Selection (ccc17j1)
# Problem URL: https://dmoj.ca/problem/ccc17j1
# Submission: 3319925 (https://dmoj.ca/submission/3319925)
# Language: 
# Submitted: 2021-01-24T16:24:09+00:00

#CCC '17 J1 - Quadrant Selection

num1 = int(input())
num2 = int(input())

if num1 > 0 and num2 > 0:
    print("1")
elif num1 > 0 and num2 < 2:
    print("4")
elif num1 < 0 and num2 > 0:
    print("2")
else:
    print("3")