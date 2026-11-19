# Problem: CCC '04 J2 - Terms of Office (ccc04j2)
# Problem URL: https://dmoj.ca/problem/ccc04j2
# Submission: 2612843 (https://dmoj.ca/submission/2612843)
# Language: Python (PY3)
# Submitted: 2020-08-05T16:46:00+00:00

num1 = int(input())
num2 = int(input())

print("All positions change in year " + str(num1))

while num1 + 60 <= num2:
    num1 += 60
    print("All positions change in year " + str(num1))