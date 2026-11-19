# Problem: COCI '16 Contest 1 #1 Tarifa (coci16c1p1)
# Problem URL: https://dmoj.ca/problem/coci16c1p1
# Submission: 3672235 (https://dmoj.ca/submission/3672235)
# Language: Python (PY3)
# Submitted: 2021-06-12T01:17:54+00:00

# COCI '16 Contest 1 #1 Tarifa

num1 = int(input())
num2 = int(input())

num_list = []

for i in range(num2):
    num_list.append(int(input()))

counter = 0

for i in range(num2):
    counter += num1
    counter -= num_list[i]

counter += num1

print(counter)