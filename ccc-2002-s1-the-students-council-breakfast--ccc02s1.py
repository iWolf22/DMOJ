# Problem: CCC '02 S1 - The Students' Council Breakfast (ccc02s1)
# Problem URL: https://dmoj.ca/problem/ccc02s1
# Submission: 4568564 (https://dmoj.ca/submission/4568564)
# Language: 
# Submitted: 2022-05-19T01:12:08+00:00

# CCC '02 S1 - The Students' Council Breakfast

import math

pink = int(input())
green = int(input())
red = int(input())
orange = int(input())

goal = int(input())

total_combinations = 0
min_tickets = math.inf

for a in range(goal + 1):
    for b in range(goal + 1):
        for c in range(goal + 1):
            for d in range(goal + 1):
                if pink * a + green * b + red * c + orange * d == goal:
                    print("# of PINK is " + str(a) + " # of GREEN is " + str(b) + " # of RED is " + str(c) + " # of ORANGE is " + str(d))
                    total_combinations += 1
                    min_tickets = min(min_tickets, a + b + c + d)

print("Total combinations is " + str(total_combinations) + ".")
print("Minimum number of tickets to print is " + str(min_tickets) + ".")