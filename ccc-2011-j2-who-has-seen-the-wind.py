# Problem: CCC '11 J2 - Who Has Seen The Wind (ccc11j2)
# Problem URL: https://dmoj.ca/problem/ccc11j2
# Submission: 3339671 (https://dmoj.ca/submission/3339671)
# Language: Python (PY3)
# Submitted: 2021-01-30T18:41:41+00:00

# CCC '11 J2 - Who Has Seen The Wind

h = int(input())
m = int(input())

counter = 0
A = -6 * (counter ** 4) + h * (counter ** 3) + 2 * (counter ** 2) + counter
while A >= 0:
    counter += 1
    A = -6 * (counter ** 4) + h * (counter ** 3) + 2 * (counter ** 2) + counter


if counter <= m:
    print("The balloon first touches ground at hour:")
    print(counter)
else:
    print("The balloon does not touch ground in the given time.")