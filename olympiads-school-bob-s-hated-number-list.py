# Problem: Bob's Hated Number List (oly21practice54)
# Problem URL: https://dmoj.ca/problem/oly21practice54
# Submission: 3687211 (https://dmoj.ca/submission/3687211)
# Language: Python (PY3)
# Submitted: 2021-06-19T22:11:44+00:00

# Bob's Hated Number List

target,length_list = list(map(int,input().split()))

num_list = list(map(int,input().split()))

counter1 = 0
counter2 = target

while True:

    if counter1 % 2 == 1:
        counter2 -= counter1
    else:
        counter2 += counter1
    counter1 += 1

    if counter2 not in num_list:
        print(counter2)
        break