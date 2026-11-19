# Problem: Educational DP Contest AtCoder D - Knapsack 1 (dpd)
# Problem URL: https://dmoj.ca/problem/dpd
# Submission: 7297526 (https://dmoj.ca/submission/7297526)
# Language: PYPY3 (PYPY3)
# Submitted: 2025-09-06T18:11:42+00:00

n, W = map(int, input().split())

dp = [0] * (W + 1)

for i in range(n):
    w, v = map(int, input().split())

    for j in range(W, -1, -1):
        if w <= j:
            dp[j] = max(v + dp[j - w], dp[j])

print(dp[W])