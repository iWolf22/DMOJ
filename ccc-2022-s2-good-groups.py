# Problem: CCC '22 S2 - Good Groups (ccc22s2)
# Problem URL: https://dmoj.ca/problem/ccc22s2
# Submission: 4853149 (https://dmoj.ca/submission/4853149)
# Language: Python (PY3)
# Submitted: 2022-09-18T23:40:44+00:00

num_same = int(input())

same_list = []

for i in range(num_same):
    same_list.append(input().split())

num_dif = int(input())

dif_list = []

for i in range(num_dif):
    dif_list.append(input().split())

num_groups = int(input())

groups_dic = {}

for i in range(num_groups):
    group_input = list(input().split())
    for j in range(len(group_input)):
        groups_dic[group_input[j]] = i

counter = 0

for i in range(num_same):
    if groups_dic[same_list[i][0]] != groups_dic[same_list[i][1]]:
        counter += 1

for i in range(num_dif):
    if groups_dic[dif_list[i][0]] == groups_dic[dif_list[i][1]]:
        counter += 1

print(counter)