# Problem: ECOO '21 P3 - Quintessential Questions (ecoo21p3)
# Problem URL: https://dmoj.ca/problem/ecoo21p3
# Submission: 3605222 (https://dmoj.ca/submission/3605222)
# Language: Python (PY3)
# Submitted: 2021-05-04T02:18:41+00:00

# Quintessential Questions

import sys
input = sys.stdin.readline

num_question,num_professors,num_emails = list(map(int,input().split()))

total_score = [-1 for i in range(num_question)]
prof_num = [-1 for i in range(num_question)]

for i in range(num_emails):
    prof,question_num,score = list(map(int,input().split()))
    if total_score[question_num - 1] < score:
        total_score[question_num - 1] = score
        prof_num[question_num - 1] = prof

print(*prof_num)