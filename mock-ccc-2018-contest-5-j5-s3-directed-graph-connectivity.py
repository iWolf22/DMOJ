# Problem: Mock CCC '18 Contest 5 J5/S3 - Directed Graph Connectivity (nccc5j5s3)
# Problem URL: https://dmoj.ca/problem/nccc5j5s3
# Submission: 4050611 (https://dmoj.ca/submission/4050611)
# Language: Python (PY3)
# Submitted: 2021-11-21T04:06:16+00:00

# Mock CCC '18 Contest 5 J5/S3 - Directed Graph Connectivity

goal_node, M_edges = list(map(int,input().split()))

temp_list = []
for i in range(M_edges):
    temp_list.append(list(map(int, input().split())))

for j in range(M_edges):

    node_list = []
    node_dic = {}

    for i in range(M_edges):
        if i != j:
            temp_num1,temp_num2 = temp_list[i][0],temp_list[i][1]

            if temp_num1 not in node_list:
                node_list.append(temp_num1)
                node_dic[temp_num1] = [temp_num2]
            else:
                node_dic[temp_num1].append(temp_num2)

    #print(node_dic)

    queue = [1]
    visted = []
    found = False

    while queue != []:
        for i in range(len(queue)):
            if queue[0] == goal_node:
                found = True
                queue = []
                break
            elif queue[0] not in node_list:
                visted.append(queue[0])
                del queue[0]
            else:
                for l in range(len(node_dic[queue[0]])):
                    if node_dic[queue[0]][l] not in visted:
                        queue.append(node_dic[queue[0]][l])

                visted.append(queue[0])
                del queue[0]

    if found == True:
        print("YES")
    else:
        print("NO")