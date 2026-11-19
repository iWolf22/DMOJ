# Problem: CCC '17 J2 - Shifty Sum (ccc17j2)
# Problem URL: https://dmoj.ca/problem/ccc17j2
# Submission: 3319975 (https://dmoj.ca/submission/3319975)
# Language: Python (PY3)
# Submitted: 2021-01-24T16:30:55+00:00

#CCC '17 J2 - Shifty Sum

num1 = int(input())
num2 = int(input())

total = 0
for i in range(num2 + 1):
    total += num1 * (10 ** i)

print(total)