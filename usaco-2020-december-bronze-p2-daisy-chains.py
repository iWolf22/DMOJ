# Problem: USACO 2020 December Bronze P2- Daisy Chains (usaco20decb2)
# Problem URL: https://dmoj.ca/problem/usaco20decb2
# Submission: 3294340 (https://dmoj.ca/submission/3294340)
# Language: Python (PY3)
# Submitted: 2021-01-16T15:50:28+00:00

counter = 0
ran = int(input())
num_list1 = input().split()
num_list = []

for i in range(len(num_list1)):
    num_list.append(int(num_list1[i]))

for i in range(len(num_list)):
    for j in range(len(num_list) - i):
        num_counter = 0
        for y in range(i + 1):
            num_counter += num_list[y + j]
        
        temp_bool = False
        for y in range(i + 1):
            if num_counter / (i + 1) == num_list[y + j] and temp_bool == False:
                counter += 1
                temp_bool = True

print(counter)