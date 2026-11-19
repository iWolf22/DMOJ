# Problem: CCC '11 J5 - Unfriend (ccc11j5)
# Problem URL: https://dmoj.ca/problem/ccc11j5
# Submission: 4590414 (https://dmoj.ca/submission/4590414)
# Language: Python (PY3)
# Submitted: 2022-05-29T00:55:02+00:00

# CCC '11 J5 - Unfriend

import time


def recursive_combinations(index,people_list):

    global combinations_list

    if index <= 0:
        combinations_list.append(people_list.copy())
        return
    else:
        recursive_combinations(index - 1,people_list)
        people_list.append(index)
        recursive_combinations(index - 1,people_list)
        del people_list[-1]



num_people = int(input())

people_graph = {i + 1:[] for i in range(num_people)}

for i in range(num_people - 1):
    temp_input = int(input())

    people_graph[temp_input].append(1 + i)


combinations_list = []

recursive_combinations(num_people - 1,[])


counter = 0


for i in range(len(combinations_list)):

    queue = combinations_list[i].copy()
    visited = combinations_list[i].copy()
    terminate = False

    while queue != []:

        for j in range(len(people_graph[queue[0]])):
            if people_graph[queue[0]][j] not in combinations_list[i]:
                terminate = True
            else:
                if (people_graph[queue[0]][j] not in visited):
                    queue.append(people_graph[queue[0]][j])
        
        visited.append(queue[0])
        del queue[0]

        if terminate == True:
            break

    if terminate == False:
        counter += 1

print(counter)