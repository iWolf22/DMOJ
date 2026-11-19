# Problem: CCC '00 S4 - Golf (ccc00s4)
# Problem URL: https://dmoj.ca/problem/ccc00s4
# Submission: 4366065 (https://dmoj.ca/submission/4366065)
# Language: Python (PY3)
# Submitted: 2022-02-21T04:11:45+00:00

# CCC '00 S4 - Golf

import math

distance = int(input())

num_clubs = int(input())

clubs_list = []

for i in range(num_clubs):
    clubs_list.append(int(input()))

location_list = [math.inf for i in range(distance + 1)]

location_list[0] = 0

for i in range(distance):
    for j in range(num_clubs):
        new_location = i + clubs_list[j]
        new_swings = location_list[i] + 1
        if new_location <= distance and new_swings < location_list[new_location]:
            location_list[new_location] = location_list[i] + 1

        #print(location_list)

if location_list[-1] == math.inf:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in", location_list[-1], "strokes.")