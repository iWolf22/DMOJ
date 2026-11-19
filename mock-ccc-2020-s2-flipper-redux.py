# Problem: Mock CCC '20 S2 - Flipper Redux (mccc1s2)
# Problem URL: https://dmoj.ca/problem/mccc1s2
# Submission: 3472376 (https://dmoj.ca/submission/3472376)
# Language: Python (PY3)
# Submitted: 2021-03-07T17:21:05+00:00

# Mock CCC '20 S2 - Flipper Redux

def row_fillper(light_array,row):
    new_array = light_array
    for i in range(len(light_array)):
        if light_array[row][i] == 0:
            new_array[row][i] = 1
        else:
            new_array[row][i] = 0

    return new_array

def col_fillper(light_array,col):
    new_array = light_array
    for i in range(len(light_array)):
        if light_array[i][col] == 0:
            new_array[i][col] = 1
        else:
            new_array[i][col] = 0

    return new_array



num = int(input())

light_array = []
instruction_list = []

for i in range(num):
    light_array.append(list(map(int,input().split())))

for i in range(len(light_array)):
    if light_array[0][i] == 1:
        instruction_list.append("C " + str(i + 1))
        light_array = col_fillper(light_array,i)

for i in range(len(light_array)):
    if light_array[i][0] == 1:
        instruction_list.append("R " + str(i + 1))
        light_array = row_fillper(light_array,i)

temp = False
for i in range(len(light_array)):
    for j in range(len(light_array)):
        if light_array[i][j] == 1:
            temp = True

if temp == False:
    print(len(instruction_list))
    for i in range(len(instruction_list) - 1,-1,-1):
        print(instruction_list[i])
else:
    print(-1)