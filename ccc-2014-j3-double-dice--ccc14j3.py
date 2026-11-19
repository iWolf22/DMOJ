# Problem: CCC '14 J3 - Double Dice (ccc14j3)
# Problem URL: https://dmoj.ca/problem/ccc14j3
# Submission: 3225215 (https://dmoj.ca/submission/3225215)
# Language: 
# Submitted: 2020-12-20T18:29:02+00:00

#CCC '14 J3 - Double Dice

num1 = int(input())

num_list = []

a_score = 100
d_score = 100

for i in range(num1):
    num_list.append(input())

for i in range(len(num_list)):
    if int(num_list[i][0]) == int(num_list[i][2]):
        random = 1
    elif int(num_list[i][0]) > int(num_list[i][2]):
        d_score -= int(num_list[i][0])
    else:
        a_score -= int(num_list[i][2])

print(a_score)
print(d_score)