# Problem: Fair Competition (faircompetition)
# Problem URL: https://dmoj.ca/problem/faircompetition
# Submission: 4655677 (https://dmoj.ca/submission/4655677)
# Language: Python (PY3)
# Submitted: 2022-06-26T19:32:12+00:00

# Fair Competition

from operator import invert


num_people, num_honour_roll = list(map(int, input().split()))

people_list = list(map(int, input().split()))

people_list = sorted(people_list, reverse=True)

#print(people_list)

last_jump = 0

for i in range(num_honour_roll - 1):
    if (people_list[i] != people_list[i + 1]):
        last_jump = i + 1

if num_people == num_honour_roll:
    last_jump = num_honour_roll
else:
    if people_list[num_honour_roll] != people_list[num_honour_roll - 1]:
        last_jump = num_honour_roll

print(last_jump)