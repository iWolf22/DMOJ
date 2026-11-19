# Problem: USACO 2020 December Bronze P1 - Do You Know Your ABCs? (usaco20decb1)
# Problem URL: https://dmoj.ca/problem/usaco20decb1
# Submission: 3294339 (https://dmoj.ca/submission/3294339)
# Language: Python (PY3)
# Submitted: 2021-01-16T15:50:09+00:00

num_list1 = input().split()
num_list = []

for i in range(len(num_list1)):
    num_list.append(int(num_list1[i]))


num_list = sorted(num_list)


if num_list[0] == num_list[1] == num_list[2]:#All equal
    print(num_list[0],num_list[1],num_list[2])
elif num_list[0] == num_list[1] and num_list[2] == num_list[0] + num_list[1]:#First 2 the same
    print(num_list[0],num_list[1],num_list[3])
elif num_list[0] == num_list[1] and num_list[2] != num_list[0] + num_list[1]:#First 2 the same
    print(num_list[0],num_list[1],num_list[2])
elif num_list[1] == num_list[2]:#Last Two Are The Same
    print(num_list[0],num_list[1],num_list[2])
elif num_list[0] + num_list[1] == num_list[2]:#All Not The Same
    print(num_list[0],num_list[1],num_list[3])
else:#All Not The Same
    print(num_list[0],num_list[1],num_list[2])