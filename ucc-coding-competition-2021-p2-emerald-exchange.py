# Problem: UCC Coding Competition '21 P2 - Emerald Exchange (ucc21p2)
# Problem URL: https://dmoj.ca/problem/ucc21p2
# Submission: 4582636 (https://dmoj.ca/submission/4582636)
# Language: Python (PY3)
# Submitted: 2022-05-26T01:29:34+00:00

# UCC Coding Competition '21 P2 - Emerald Exchange

num = int(input())

num_list = list(map(int,input().split()))

max_weight = 0
counter_weight = 0

for i in range(num):
    if (num_list[i] % 2 == 1):
        counter_weight = 0
    else:
        counter_weight += num_list[i]

    max_weight = max(max_weight,counter_weight)

print(max_weight)