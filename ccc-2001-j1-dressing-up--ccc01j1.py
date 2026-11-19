# Problem: CCC '01 J1 - Dressing Up (ccc01j1)
# Problem URL: https://dmoj.ca/problem/ccc01j1
# Submission: 3208077 (https://dmoj.ca/submission/3208077)
# Language: Python (PY3)
# Submitted: 2020-12-16T00:48:00+00:00

# CCC '01 J1 - Dressing Up

def create_tie(num):
    for i in range(int((num - 1) / 2)):
        print(("*" + "*" * (2 * i)) + (" " * (2 * num - (i * 4 + 2))) + ("*" + "*" * (2 * i)))

    for i in range(int((num - 1) / 2),-1,-1):
        print(("*" + "*" * (2 * i)) + (" " * (2 * num - (i * 4 + 2))) + ("*" + "*" * (2 * i)))

num = int(input())

create_tie(num)