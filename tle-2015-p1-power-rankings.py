# Problem: TLE '15 P1 - Power Rankings (tle15p1)
# Problem URL: https://dmoj.ca/problem/tle15p1
# Submission: 3433403 (https://dmoj.ca/submission/3433403)
# Language: Python (PY3)
# Submitted: 2021-02-18T20:33:10+00:00

# TLE '15 P1 - Power Rankings

num_list = list(map(int,input().split()))

name_list = []
for i in range(num_list[0]):
    name_list.append(input())

number_list = []
for i in range(num_list[1]):
    number_list.append(list(map(int,input().split())))

final_list = [[0,name_list[i]] for i in range(num_list[0])]

for i in range(num_list[0]):
    for j in range(num_list[1]):
        final_list[i][0] += number_list[j][i]

final_list = sorted(final_list,reverse = True)

for i in range(len(final_list)):
    print(str(i + 3) + ". " + final_list[i][1])