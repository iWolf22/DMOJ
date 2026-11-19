# Problem: CCC '03 J2 - Picture Perfect (ccc03j2)
# Problem URL: https://dmoj.ca/problem/ccc03j2
# Submission: 3642185 (https://dmoj.ca/submission/3642185)
# Language: 
# Submitted: 2021-05-24T16:46:17+00:00

import math

num_list = []

temp = int(input())
while True:
    if temp == 0:
        break
    else:
        num_list.append(temp)
        temp = int(input())

final_list = []

for i in range(len(num_list)):
    if math.sqrt(num_list[i]) % 1 == 0:
        final_list.append([math.sqrt(num_list[i]),math.sqrt(num_list[i])])
    else:
        for j in range(math.ceil(math.sqrt(num_list[i])),0,-1):
            if (num_list[i] / j) % 1 == 0:
                final_list.append([j,num_list[i] / j])
                break

for i in range(len(final_list)):
    print("Minimum perimeter is " + str(int(final_list[i][0] * 2 + final_list[i][1] * 2)) + " with dimensions " + str(int(final_list[i][0])) + " x " + str(int(final_list[i][1])))