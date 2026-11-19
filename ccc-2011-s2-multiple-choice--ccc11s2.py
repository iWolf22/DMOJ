# Problem: CCC '11 S2 - Multiple Choice (ccc11s2)
# Problem URL: https://dmoj.ca/problem/ccc11s2
# Submission: 4191092 (https://dmoj.ca/submission/4191092)
# Language: 
# Submitted: 2022-01-09T03:37:33+00:00

# CCC '11 S2 - Multiple Choice

num = int(input())

letter_list = []

for i in range(num):
    letter_list.append(input())

counter = 0

for i in range(num):
    if input() == letter_list[i]:
        counter += 1

print(counter)