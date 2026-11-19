# Problem: CCC '16 J1 - Tournament Selection (ccc16j1)
# Problem URL: https://dmoj.ca/problem/ccc16j1
# Submission: 3228316 (https://dmoj.ca/submission/3228316)
# Language: 
# Submitted: 2020-12-21T17:11:47+00:00

#CCC '16 J1 - Tournament Selection

num_list = []

for i in range(6):
    num_list.append(input())

counter = 0
for i in range(len(num_list)):
    if num_list[i] == "W":
        counter += 1

if counter == 0:
    print("-1")
elif counter == 2 or counter == 1:
    print("3")
elif counter == 3 or counter == 4:
    print("2")
else:
    print("1")