# Problem: CCC '18 J2 - Occupy parking (ccc18j2)
# Problem URL: https://dmoj.ca/problem/ccc18j2
# Submission: 3371351 (https://dmoj.ca/submission/3371351)
# Language: Python (PY3)
# Submitted: 2021-02-06T22:30:59+00:00

#CCC '18 J2 - Occupy parking

num1 = int(input())

cars1 = input()
cars2 = input()

counter = 0
for i in range(num1):
    if cars1[i] == cars2[i] == "C":
        counter += 1

print(counter)