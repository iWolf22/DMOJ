# Problem: SAC '22 Code Challenge 3 P1 - Hair Hazards (sac22cc3p1)
# Problem URL: https://dmoj.ca/problem/sac22cc3p1
# Submission: 4433822 (https://dmoj.ca/submission/4433822)
# Language: Python (PY3)
# Submitted: 2022-03-20T17:55:04+00:00

# SAC '22 Code Challenge 3 P1 - Hair Hazards

start_num = int(input())

minus_num = int(input())

num_cuts = int(input())

for i in range(num_cuts):
    start_num -= minus_num
    print(start_num)