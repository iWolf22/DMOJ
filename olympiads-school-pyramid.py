# Problem: Pyramid (oly22practice57)
# Problem URL: https://dmoj.ca/problem/oly22practice57
# Submission: 4626320 (https://dmoj.ca/submission/4626320)
# Language: PYPY3 (PYPY3)
# Submitted: 2022-06-13T00:19:26+00:00

# Pyramid

num_elements = int(input())

elements = list(map(int, input().split()))

left_list = [[0,-1]]

for i in range(len(elements)):
    if elements[i] == left_list[-1][0] + 1:
        left_list.append([left_list[-1][0] + 1, i])

right_list = [[0,1]]

for i in range(len(elements) - 1, 0, -1):
    if elements[i] == right_list[-1][0] + 1:
        right_list.append([right_list[-1][0] + 1, i])


max_val = 0

for i in range(min(len(left_list) , len(right_list))):
    if left_list[i][1] < right_list[i][1]:
        max_val = i

print(max_val)