# Problem: Bob's Apple Shopping (oly20practice78)
# Problem URL: https://dmoj.ca/problem/oly20practice78
# Submission: 4415101 (https://dmoj.ca/submission/4415101)
# Language: PYPY3 (PYPY3)
# Submitted: 2022-03-13T21:50:16+00:00

# Bob's Apple Shopping

import math

num_stores, num_apples = list(map(int,input().split()))

apple_stores = []

max_value = 0

for i in range(num_stores):
    apple_stores.append(list(map(int,input().split())))
    max_value = max(apple_stores[i][0],max_value)

apple_list = [math.inf for i in range(num_apples + max_value + 1)]

apple_list[0] = 0

for i in range(len(apple_list)):
    for j in range(len(apple_stores)):
        new_index = i + apple_stores[j][0]
        if new_index <= len(apple_list) - 1:
            #print(apple_list[i] + apple_stores[j][1])
            if apple_list[new_index] > apple_list[i] + apple_stores[j][1]:
                apple_list[new_index] = apple_list[i] + apple_stores[j][1]

print(min(apple_list[num_apples::]))