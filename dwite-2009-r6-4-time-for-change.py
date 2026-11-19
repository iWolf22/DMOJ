# Problem: DWITE '09 R6 #4 - Time for Change (dwite09c6p4)
# Problem URL: https://dmoj.ca/problem/dwite09c6p4
# Submission: 4476892 (https://dmoj.ca/submission/4476892)
# Language: Python (PY3)
# Submitted: 2022-04-03T17:25:27+00:00

# DWITE '08 R3 #4 - Time for change

import math

for i in range(5):
    total_cost = int(input())

    num_coins = int(input())
    coins_list = []

    for j in range(num_coins):
        coins_list.append(int(input()))

    coins_list = sorted(coins_list, reverse = True)
    
    dp_list = [math.inf for i in range(total_cost + 1)]
    dp_list[0] = 0

    for a in range(len(dp_list)):
        for b in range(len(coins_list)):
            if a + coins_list[b] < len(dp_list) and dp_list[a] + 1 < dp_list[a + coins_list[b]]:
                dp_list[a + coins_list[b]] = dp_list[a] + 1
    print(dp_list[-1])
    #print(dp_list)