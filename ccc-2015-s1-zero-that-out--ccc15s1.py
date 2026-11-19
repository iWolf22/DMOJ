# Problem: CCC '15 S1 - Zero That Out (ccc15s1)
# Problem URL: https://dmoj.ca/problem/ccc15s1
# Submission: 3329575 (https://dmoj.ca/submission/3329575)
# Language: 
# Submitted: 2021-01-27T03:05:36+00:00

#CCC '15 S1 - Zero That Out

num1 = int(input())

list_num = []

for i in range(num1):
    list_num.append(int(input()))
    if list_num[len(list_num) - 1] == 0:
        del list_num[len(list_num) - 1]
        if len(list_num) != 0:
            del list_num[len(list_num) - 1]

print(sum(list_num))