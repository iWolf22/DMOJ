# Problem: Another Contest 7 Problem 1 - Lonely Users (acc7p1)
# Problem URL: https://dmoj.ca/problem/acc7p1
# Submission: 3557676 (https://dmoj.ca/submission/3557676)
# Language: 
# Submitted: 2021-04-12T16:11:21+00:00

# Another Contest 7 Problem 1 - Lonely Users

num = int(input())

num_list = []

for i in range(num):
    num_list.append(int(input()))

for i in range(num):
    if num_list[i] == 2:
        print(num_list[i])
    else:
        print(num_list[i] - 1)