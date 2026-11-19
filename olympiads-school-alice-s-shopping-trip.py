# Problem: Alice's Shopping Trip (oly20practice24)
# Problem URL: https://dmoj.ca/problem/oly20practice24
# Submission: 4753147 (https://dmoj.ca/submission/4753147)
# Language: Python (PY3)
# Submitted: 2022-08-06T23:41:16+00:00

num_time, num_nodes = list(map(int,input().split()))

nodes_list = []

for i in range(num_nodes):
    nodes_list.append(int(input()))

nodes_list.sort(key = lambda x: abs(x))

current_loc = 0

counter = 0

for i in range(num_nodes):
    if num_time > abs(nodes_list[i] - current_loc):
        num_time -= abs(nodes_list[i] - current_loc)
        current_loc = nodes_list[i]
        counter += 1
    else:
        break

print(counter)