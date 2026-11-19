# Problem: CCC '11 J4 - Boring Business (ccc11j4)
# Problem URL: https://dmoj.ca/problem/ccc11j4
# Submission: 4592402 (https://dmoj.ca/submission/4592402)
# Language: 
# Submitted: 2022-05-29T20:39:49+00:00

# CCC '11 J4 - Boring Business

commands = []
list_cords = [
    [0,0],
    [0,-1],
    [0,-2],
    [0,-3],
    [1,-3],
    [2,-3],
    [3,-3],
    [3,-4],
    [3,-5],
    [4,-5],
    [5,-5],
    [5,-4],
    [5,-3],
    [6,-3],
    [7,-3],
    [7,-4],
    [7,-5],
    [7,-6],
    [7,-7],
    [6,-7],
    [5,-7],
    [4,-7],
    [3,-7],
    [2,-7],
    [1,-7],
    [0,-7],
    [-1,-7],
    [-1,-6],
    [-1,-5]
]

location = [-1,-5]

i = 0

while True:
    temp_list = input().split()
    if temp_list[0] == "q":
        break
    temp_list[1] = int(temp_list[1])
    commands.append(temp_list)

    stop = False

    for j in range(commands[i][1]):

        if commands[i][0] == "d":
            location[1] -= 1
        elif commands[i][0] == "l":
            location[0] -= 1
        elif commands[i][0] == "r":
            location[0] += 1
        else:
            location[1] += 1

        for l in range(len(list_cords)):
            if list_cords[l][0] == location[0] and list_cords[l][1] == location[1]:
                stop = True
        
        list_cords.append([location[0],location[1]])

    if stop == False:
        print(str(location[0]) + " " + str(location[1]) + " safe")
    else:
        print(str(location[0]) + " " + str(location[1]) + " DANGER")
        break

    i += 1