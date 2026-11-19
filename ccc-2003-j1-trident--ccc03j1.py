# Problem: CCC '03 J1 - Trident (ccc03j1)
# Problem URL: https://dmoj.ca/problem/ccc03j1
# Submission: 2158477 (https://dmoj.ca/submission/2158477)
# Language: Python (PY3)
# Submitted: 2020-06-18T19:40:10+00:00

t = int(input())
s = int(input())
h = int(input())
for i in range(t):
    print("*" + " " * s + "*" + " " * s + "*")
print("*" + "*" * s + "*" + "*" * s + "*")
for i in range(h):
    print(" " * (s + 1) + "*")