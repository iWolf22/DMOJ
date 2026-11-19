# Problem: Mock CCC '19 Contest 1 J1 - Pusheen's Report Card (nccc6j1)
# Problem URL: https://dmoj.ca/problem/nccc6j1
# Submission: 2132020 (https://dmoj.ca/submission/2132020)
# Language: Python (PY3)
# Submitted: 2020-06-06T17:36:18+00:00

CS452 = int(input())
PHIL145 = int(input())
if CS452 < PHIL145:
    print("PHIL145")
elif CS452 > PHIL145:
    print("CS452")
else:
    b = 0