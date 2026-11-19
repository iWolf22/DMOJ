# Problem: CCC '08 S3 - Maze (ccc08s3)
# Problem URL: https://dmoj.ca/problem/ccc08s3
# Submission: 3998344 (https://dmoj.ca/submission/3998344)
# Language: 
# Submitted: 2021-11-01T00:30:48+00:00

#CCC '08 S3 - Maze

num1 = int(input())

for i in range(num1):
    y = int(input())
    x = int(input())
    char_list = []
    char_list.append(["*" for o in range(x + 2)])
    for j in range(y):
        char_list.append(list(input().replace(""," ").split()))
        char_list[j + 1].insert(0,"*")
        char_list[j + 1].append("*")

    char_list.append(["*" for o in range(x + 2)])

    queue = [[1,1]]
    found = False

    counter = 0

    while queue != []:
        if found == True:
            break
        del_counter = 0
        counter += 1
        for j in range(len(queue)):
            if queue[j - del_counter][0] == y and queue[j - del_counter][1] == x and char_list[queue[j - del_counter][0]][queue[j - del_counter][1]] != "*":
                found = True
            elif char_list[queue[j - del_counter][0]][queue[j - del_counter][1]] == "*":
                del queue[j - del_counter]
                del_counter += 1
            elif char_list[queue[j - del_counter][0]][queue[j - del_counter][1]] == "+":
                char_list[queue[j - del_counter][0]][queue[j - del_counter][1]] = "*"
                queue.append([queue[j - del_counter][0] + 1,queue[j - del_counter][1]])
                queue.append([queue[j - del_counter][0] - 1,queue[j - del_counter][1]])
                queue.append([queue[j - del_counter][0],queue[j - del_counter][1] + 1])
                queue.append([queue[j - del_counter][0],queue[j - del_counter][1] - 1])
                del queue[j - del_counter]
                del_counter += 1
            elif char_list[queue[j - del_counter][0]][queue[j - del_counter][1]] == "-":
                char_list[queue[j - del_counter][0]][queue[j - del_counter][1]] = "*"
                queue.append([queue[j - del_counter][0],queue[j - del_counter][1] + 1])
                queue.append([queue[j - del_counter][0],queue[j - del_counter][1] - 1])
                del queue[j - del_counter]
                del_counter += 1
            else:
                char_list[queue[j - del_counter][0]][queue[j - del_counter][1]] = "*"
                queue.append([queue[j - del_counter][0] + 1,queue[j - del_counter][1]])
                queue.append([queue[j - del_counter][0] - 1,queue[j - del_counter][1]])
                del queue[j - del_counter]
                del_counter += 1

        #for l in range(len(char_list)):
            #print(char_list[l])
        #print(" ")
    
    if found == True:
        print(counter)
    else:
        print(-1)