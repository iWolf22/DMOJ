# Problem: CCC '05 S2 - Mouse Move (ccc05s2)
# Problem URL: https://dmoj.ca/problem/ccc05s2
# Submission: 3542277 (https://dmoj.ca/submission/3542277)
# Language: Python (PY3)
# Submitted: 2021-04-05T17:12:23+00:00

# CCC '05 S2 - Mouse Move

dimensions = list(map(int,input().split()))

directions_list = []

while True:
    num = list(map(int,input().split()))
    if num[0] == 0 and num[1] == 0:
        break
    else:
        directions_list.append(num)

location = [0,0]

for i in range(len(directions_list)):
    location[0] += directions_list[i][0]
    location[1] += directions_list[i][1]
    if location[0] < 0:
        location[0] = 0
    if location[1] < 0:
        location[1] = 0
    if location[0] > dimensions[0]:
        location[0] = dimensions[0]
    if location[1] > dimensions[1]:
        location[1] = dimensions[1]
    print(*location)