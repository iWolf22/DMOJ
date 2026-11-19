# Problem: Longest Sequence (oly22practice27)
# Problem URL: https://dmoj.ca/problem/oly22practice27
# Submission: 4478455 (https://dmoj.ca/submission/4478455)
# Language: Python (PY3)
# Submitted: 2022-04-03T23:16:16+00:00

# Longest Sequence

left, right = list(map(int,input().split()))

counter = 0
while True:
    if left > right:
        break
    else:
        counter += 1
        left = left * 2

print(counter)