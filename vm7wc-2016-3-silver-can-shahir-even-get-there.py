# Problem: VM7WC '16 #3 Silver - Can Shahir even get there?! (vmss7wc16c3p2)
# Problem URL: https://dmoj.ca/problem/vmss7wc16c3p2
# Submission: 3978684 (https://dmoj.ca/submission/3978684)
# Language: Python (PY3)
# Submitted: 2021-10-24T17:12:16+00:00

# VM7WC '16 #3 Silver - Can Shahir even get there

num_houses,num_roads,date_house,my_house = list(map(int,input().split()))

house_dic = {i + 1: [] for i in range(num_houses)}

for i in range(num_roads):
    temp1,temp2 = list(map(int,input().split()))
    house_dic[temp1].append(temp2)
    house_dic[temp2].append(temp1)

queue = [my_house]

visited = []

found = False

while queue != []:
    del_count = 0
    #print(queue)
    for i in range(len(queue)):
        visited.append(queue[i - del_count])
        if queue[i - del_count] == date_house:
            found = True
        temp_list = house_dic[queue[i - del_count]]
        del queue[i - del_count]
        del_count += 1
        for j in range(len(temp_list)):
            if temp_list[j] not in visited:
                queue.append(temp_list[j])

if found == True:
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")