# Problem: CCC '04 J3 - Smile with Similes (ccc04j3)
# Problem URL: https://dmoj.ca/problem/ccc04j3
# Submission: 2612868 (https://dmoj.ca/submission/2612868)
# Language: Python (PY3)
# Submitted: 2020-08-05T16:55:00+00:00

num1 = int(input())
num2 = int(input())
adj = []
noun = []
for i in range(num1):
    adj.append(input())
for i in range(num2):
    noun.append(input())
for j in range(len(adj)):
    for i in range(len(noun)):
        print(adj[j] , "as" , noun[i])