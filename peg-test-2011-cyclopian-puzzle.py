# Problem: PEG Test '11 - Cyclopian Puzzle (fur5)
# Problem URL: https://dmoj.ca/problem/fur5
# Submission: 3912707 (https://dmoj.ca/submission/3912707)
# Language: Python (PY3)
# Submitted: 2021-09-25T17:15:00+00:00

#Cyclopian Puzzle

def recursion(num,A,B,C):
    if num == 1:
        print(A + B)
        return
    recursion(num - 1,A,C,B)
    print(A + B)
    recursion(num - 1,C,B,A)

num = int(input())

recursion(num,"A","C","B")