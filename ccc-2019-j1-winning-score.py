# Problem: CCC '19 J1 - Winning Score (ccc19j1)
# Problem URL: https://dmoj.ca/problem/ccc19j1
# Submission: 3440062 (https://dmoj.ca/submission/3440062)
# Language: Python (PY3)
# Submitted: 2021-02-21T16:48:54+00:00

# CCC '19 J1 - Winning Score

num_list = []

for i in range(6):
    num_list.append(int(input()))

if num_list[0] * 3 + num_list[1] * 2 + num_list[2] == num_list[3] * 3 + num_list[4] * 2 + num_list[5]:
    print("T")
elif num_list[0] * 3 + num_list[1] * 2 + num_list[2] < num_list[3] * 3 + num_list[4] * 2 + num_list[5]:
    print("B")
else:
    print("A")