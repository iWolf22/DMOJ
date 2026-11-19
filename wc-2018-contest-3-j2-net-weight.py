# Problem: WC '18 Contest 3 J2 - Net Weight (wc18c3j2)
# Problem URL: https://dmoj.ca/problem/wc18c3j2
# Submission: 4265632 (https://dmoj.ca/submission/4265632)
# Language: Python (PY3)
# Submitted: 2022-01-30T01:51:16+00:00

# WC '18 Contest 3 J2 - Net Weight

num = int(input())

num_list = []

for i in range(num):
    num_list.append(int(input()))

num_list = sorted(num_list,reverse = True)

#print(num_list)

num1 = -1
num2 = -1

for i in range(len(num_list)):
    if num_list[i] <= 100:
        if num1 == -1:
            num1 = num_list[i]
        else:
            num2 = num_list[i]
            break

if num1 == -1:
    num1 = 0
if num2 == -1:
    num2 = 0

print(num1 + num2)