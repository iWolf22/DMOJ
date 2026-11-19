# Problem: CCC '20 J3 - Art (ccc20j3)
# Problem URL: https://dmoj.ca/problem/ccc20j3
# Submission: 3432889 (https://dmoj.ca/submission/3432889)
# Language: Python (PY3)
# Submitted: 2021-02-18T15:27:01+00:00

# CCC '20 J3 - Art

num1 = int(input())

num_list = []

for i in range(num1):
    num_list.append(input())

for i in range(num1):
    num_list[i] = num_list[i].replace(","," ").split(" ")

for i in range(num1):
    num_list[i][0] = int(num_list[i][0])
    num_list[i][1] = int(num_list[i][1])

smallest = [1000,1000]
largest = [0,0]

for i in range(num1):
    if smallest[0] > num_list[i][0]:
        smallest[0] = num_list[i][0]
    if smallest[1] > num_list[i][1]:
        smallest[1] = num_list[i][1]
    if largest[0] < num_list[i][0]:
        largest[0] = num_list[i][0]
    if largest[1] < num_list[i][1]:
        largest[1] = num_list[i][1]

print(str(smallest[0] - 1) + "," + str(smallest[1] - 1))
print(str(largest[0] + 1) + "," + str(largest[1] + 1))