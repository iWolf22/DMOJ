# Problem: An Animal Contest 5 P1 - Bamboo Cookies (aac5p1)
# Problem URL: https://dmoj.ca/problem/aac5p1
# Submission: 4300671 (https://dmoj.ca/submission/4300671)
# Language: Python (PY3)
# Submitted: 2022-02-06T22:20:36+00:00

# An Animal Contest 5 P1 - Bamboo Cookies

num = int(input())

num_list = list(map(int,input().split()))

odd = 0
even = 0

for i in range(num):
    if num_list[i] % 2 == 0:
        odd += 1
    else:
        even += 1

print(int(odd / 2) + int(even / 2))