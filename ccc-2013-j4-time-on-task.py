# Problem: CCC '13 J4 - Time on task (ccc13j4)
# Problem URL: https://dmoj.ca/problem/ccc13j4
# Submission: 3223191 (https://dmoj.ca/submission/3223191)
# Language: Python (PY3)
# Submitted: 2020-12-20T00:45:37+00:00

#CCC '13 J4 - Time on task

time_chores = int(input())
num_chores = int(input())
list_chores = []

for i in range(num_chores):
    list_chores.append(int(input()))

list_chores = sorted(list_chores)

chores_counter = 0

for i in range(len(list_chores)):
    if list_chores[i] > time_chores:
        break
    else:
        chores_counter += 1
        time_chores -= list_chores[i]

print(chores_counter)