# Problem: COCI '14 Contest 2 #2 Utrka (coci14c2p2)
# Problem URL: https://dmoj.ca/problem/coci14c2p2
# Submission: 3956905 (https://dmoj.ca/submission/3956905)
# Language: Python (PY3)
# Submitted: 2021-10-15T02:21:41+00:00

# COCI '14 Contest 2 #2 Utrka

num_names = int(input())

names_list = []
names_list2 = []


for i in range(num_names):
    names_list.append(input())

for i in range(num_names - 1):
    names_list2.append(input())

names_list = sorted(names_list)
names_list2 = sorted(names_list2)


temp = False

for i in range(num_names - 1):
    if names_list2[i] != names_list[i]:
        temp = True
        print(names_list[i])
        break

if temp == False:
    print(names_list[len(names_list) - 1])