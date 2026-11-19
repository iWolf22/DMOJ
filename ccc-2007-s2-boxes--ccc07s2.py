# Problem: CCC '07 S2 - Boxes (ccc07s2)
# Problem URL: https://dmoj.ca/problem/ccc07s2
# Submission: 3534667 (https://dmoj.ca/submission/3534667)
# Language: 
# Submitted: 2021-04-03T02:06:45+00:00

# CCC '07 S2 - Boxes

num1 = int(input())

box_list = []

for i in range(num1):
    box_list.append(sorted(list(map(int,input().split()))))
    box_list[i].append(box_list[i][0] * box_list[i][1] * box_list[i][2])

box_list = sorted(box_list,key=lambda l:l[3],reverse=False)

num2 = int(input())

item_list = []

for i in range(num2):
    item_list.append(sorted(list(map(int,input().split()))))
    item_list[i].append(item_list[i][0] * item_list[i][1] * item_list[i][2])


for j in range(len(item_list)):
    break_point = False
    for i in range(len(box_list)):
        if box_list[i][0] >= item_list[j][0] and box_list[i][1] >= item_list[j][1] and box_list[i][2] >= item_list[j][2] and box_list[i][3] >= item_list[j][3]:
            print(box_list[i][3])
            break_point = True
            break
    if break_point == False:
        print("Item does not fit.")