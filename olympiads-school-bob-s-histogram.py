# Problem: Bob's Histogram (oly21practice78)
# Problem URL: https://dmoj.ca/problem/oly21practice78
# Submission: 4048711 (https://dmoj.ca/submission/4048711)
# Language: Python (PY3)
# Submitted: 2021-11-20T17:38:31+00:00

# Bob's Histogram

num = int(input())

num_list = list(map(int,input().split()))

avg1 = int(sum(num_list) / len(num_list))
avg2 = int(sum(num_list) / len(num_list)) + 1

counter1 = 0
counter2 = 0

for i in range(len(num_list)):
    counter1 += (num_list[i] - avg1) ** 2

for i in range(len(num_list)):
    counter2 += (num_list[i] - avg2) ** 2


if counter1 >= counter2:
    print(counter2)
else:
    print(counter1)