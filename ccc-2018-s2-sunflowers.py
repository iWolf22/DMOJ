# Problem: CCC '18 S2 - Sunflowers (ccc18s2)
# Problem URL: https://dmoj.ca/problem/ccc18s2
# Submission: 3372820 (https://dmoj.ca/submission/3372820)
# Language: Python (PY3)
# Submitted: 2021-02-07T03:22:18+00:00

#CCC '18 S2 - Sunflowers

import sys
input = sys.stdin.readline

num1 = int(input())

fill_list = []
for i in range(num1):
    fill_list.append(list(map(int,input().split())))

temp_list = [fill_list[0][0],fill_list[0][num1 - 1],fill_list[num1 - 1][num1 - 1],fill_list[num1 - 1][0]]
for i in range(4):
    if temp_list[i] == min(temp_list):
        save = i

if save == 0:
    one = 1
elif save == 3:
    fill_list = list(zip(*fill_list[::-1]))

elif save == 2:
    fill_list = list(zip(*fill_list[::-1]))
    fill_list = list(zip(*fill_list[::-1]))

else:
    fill_list = list(zip(*fill_list[::-1]))
    fill_list = list(zip(*fill_list[::-1]))
    fill_list = list(zip(*fill_list[::-1]))

for i in range(num1):
    print(*fill_list[i])