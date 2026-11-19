# Problem: CCC '01 S2 - Spirals (ccc01s2)
# Problem URL: https://dmoj.ca/problem/ccc01s2
# Submission: 3574926 (https://dmoj.ca/submission/3574926)
# Language: 
# Submitted: 2021-04-21T03:16:21+00:00

# CCC '01 S2 - Spirals

num1 = int(input())
num2 = int(input())

matrix = [[-1 for i in range(12)]for j in range(12)]

location = [6,6]
direction = "right"
distance = 1
counter = 0

for i in range(num1,num2 + 1):
    matrix[location[0]][location[1]] = i

    counter += 1

    if direction == "down":
        location[1] += 1
    elif direction == "up":
        location[1] -= 1
    elif direction == "left":
        location[0] -= 1
    else:
        location[0] += 1

    if counter == distance:
        counter = 0
        if direction == "down":
            direction = "left"
            distance += 1
        elif direction == "up":
            direction = "right"
            distance += 1
        elif direction == "left":
            direction = "up"
        else:
            direction = "down"

counter = 0
for i in range(len(matrix)):
    delete = True
    for j in range(len(matrix[i - counter])):
        if matrix[i - counter][j] != -1:
            delete = False
    if delete == True:
        del matrix[i - counter]
        counter += 1

counter = 0
for i in range(len(matrix[0])):
    delete = True
    for j in range(len(matrix)):

        if matrix[j][i - counter] != -1:
            delete = False
    if delete == True:
        for j in range(len(matrix)):
            del matrix[j][i - counter]
        counter += 1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == -1:
            matrix[i][j] = "  "

for i in range(len(matrix)):
    print(*matrix[i])