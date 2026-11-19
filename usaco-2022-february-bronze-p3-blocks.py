# Problem: USACO 2022 February Bronze P3 - Blocks (usaco22febb3)
# Problem URL: https://dmoj.ca/problem/usaco22febb3
# Submission: 4414989 (https://dmoj.ca/submission/4414989)
# Language: Python (PY3)
# Submitted: 2022-03-13T21:12:19+00:00

# USACO 2022 February Contest, Bronze
# Problem 3. Blocks

num = int(input())

dice_list = []
for i in range(4):
    dice_list.append(input().replace(""," ").split())

for i in range(num):
    temp_string = input().replace(""," ").split()
    if len(temp_string) == 1:
        temp_bool = False
        for j in range(4):
            if temp_string[0] in dice_list[j]:
                temp_bool = True
        if temp_bool == True:
            print("YES")
        else:
            print("NO")
    if len(temp_string) == 2:
        possible_list = [[],[]]
        for a in range(4):
            for b in range(2):
                if temp_string[b] in dice_list[a]:
                    possible_list[b].append(a + 1)

        temp_bool = False
        for a in range(len(possible_list[0])):
            for b in range(len(possible_list[1])):
                if possible_list[0][a] != possible_list[1][b]:
                    temp_bool = True
        
        if temp_bool == True:
            print("YES")
        else:
            print("NO")

    if len(temp_string) == 3:
        possible_list = [[],[],[]]

        for a in range(4):
            for b in range(3):
                if temp_string[b] in dice_list[a]:
                    possible_list[b].append(a + 1)
        
        temp_bool = False
        for a in range(len(possible_list[0])):
            for b in range(len(possible_list[1])):
                for c in range(len(possible_list[2])):
                    if possible_list[0][a] != possible_list[1][b] and possible_list[0][a] != possible_list[2][c] and possible_list[2][c] != possible_list[1][b]:
                        temp_bool = True

        if temp_bool == True:
            print("YES")
        else:
            print("NO")

    if len(temp_string) == 4:
        possible_list = [[],[],[],[]]

        for a in range(4):
            for b in range(4):
                if temp_string[b] in dice_list[a]:
                    possible_list[b].append(a + 1)

        temp_bool = False
        for a in range(len(possible_list[0])):
            for b in range(len(possible_list[1])):
                for c in range(len(possible_list[2])):
                    for d in range(len(possible_list[3])):
                        if possible_list[0][a] != possible_list[1][b] and possible_list[0][a] != possible_list[2][c] and possible_list[0][a] != possible_list[3][d] and possible_list[2][c] != possible_list[1][b] and possible_list[2][c] != possible_list[3][d] and possible_list[3][d] != possible_list[1][b]:
                            temp_bool = True

        if temp_bool == True:
            print("YES")
        else:
            print("NO")