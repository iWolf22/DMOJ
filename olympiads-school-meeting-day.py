# Problem: Meeting Day (oly22practice25)
# Problem URL: https://dmoj.ca/problem/oly22practice25
# Submission: 4478709 (https://dmoj.ca/submission/4478709)
# Language: Python (PY3)
# Submitted: 2022-04-04T00:17:38+00:00

# Meeting Day

import math

num_cities, num_roads, meeting_location = list(map(int,input().split()))

cities_dic = {i + 1:[] for i in range(num_cities)}

for i in range(num_roads):
    city1, city2, cost = list(map(int,input().split()))
    cities_dic[city1].append([city2,cost])

cost_list = [math.inf for i in range(num_cities)]

cost_list[meeting_location - 1] = 0

queue_list = [meeting_location]

while (queue_list != []):
    current_value = cost_list[queue_list[0] - 1]

    for i in range(len(cities_dic[queue_list[0]])):
        target_location = cities_dic[queue_list[0]][i][0]
        target_cost = cities_dic[queue_list[0]][i][1]
        target_value = cost_list[target_location - 1]
        
        if current_value + target_cost < target_value:
            queue_list.append(target_location)
            cost_list[target_location - 1] = target_cost + current_value

    del queue_list[0]

saved_cost = cost_list.copy()


fliped_dic = {i + 1:[] for i in range(num_cities)}

for i in range(len(cities_dic)):
    for j in range(len(cities_dic[i + 1])):
        fliped_dic[cities_dic[i + 1][j][0]].append([i + 1,cities_dic[i + 1][j][1]])

# -------------------------------------------------------------------------------------

cities_dic = fliped_dic

cost_list = [math.inf for i in range(num_cities)]

cost_list[meeting_location - 1] = 0

queue_list = [meeting_location]

while (queue_list != []):
    current_value = cost_list[queue_list[0] - 1]

    for i in range(len(cities_dic[queue_list[0]])):
        target_location = cities_dic[queue_list[0]][i][0]
        target_cost = cities_dic[queue_list[0]][i][1]
        target_value = cost_list[target_location - 1]
        
        if current_value + target_cost < target_value:
            queue_list.append(target_location)
            cost_list[target_location - 1] = target_cost + current_value

    del queue_list[0]

#print(cost_list)
#print(saved_cost)

final_list = []

for i in range(len(cost_list)):
    final_list.append(cost_list[i] + saved_cost[i])

print(max(final_list))