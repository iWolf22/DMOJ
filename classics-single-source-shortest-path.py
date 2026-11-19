# Problem: Single Source Shortest Path (sssp)
# Problem URL: https://dmoj.ca/problem/sssp
# Submission: 4236721 (https://dmoj.ca/submission/4236721)
# Language: Python (PY3)
# Submitted: 2022-01-23T00:35:58+00:00

# Single Source Shortest Path

from copy import copy
import math

nodes,edges = list(map(int,input().split()))

web = {i + 1:[[],[],math.inf] for i in range(nodes)}

for i in range(edges):
    node1, node2, cost = list(map(int,input().split()))
    web[node1][0].append(node2)
    web[node1][1].append(cost)
    web[node2][0].append(node1)
    web[node2][1].append(cost)

web[1][2] = 0

queue = [1]

while queue != []:
    for i in range(len(queue)):
        for j in range(len(web[queue[0]][0])):
            temp_location = queue[0]
            temp_destination = web[queue[0]][0][j]
            if web[temp_location][1][j] + web[temp_location][2] < web[temp_destination][2]:
                web[temp_destination][2] = web[temp_location][1][j] + web[temp_location][2]
                queue.append(temp_destination)
        del queue[0]

for i in range(len(web)):
    if (web[i + 1][2]) == math.inf:
        print(-1)
    else:
        print(web[i + 1][2])