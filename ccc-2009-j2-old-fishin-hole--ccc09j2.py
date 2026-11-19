# Problem: CCC '09 J2 - Old Fishin' Hole (ccc09j2)
# Problem URL: https://dmoj.ca/problem/ccc09j2
# Submission: 4448284 (https://dmoj.ca/submission/4448284)
# Language: Python (PY3)
# Submitted: 2022-03-26T02:38:19+00:00

# CCC '09 J2 - Old Fishin' Hole

trout_cost = int(input())
pike_cost = int(input())
pickerel_cost = int(input())
max_cost = int(input())

counter = 0

for a in range(max_cost + 1):
    for b in range(max_cost + 1):
        for c in range(max_cost + 1):
            if max_cost >= (a * trout_cost) + (b * pike_cost) + (c * pickerel_cost):
                if (a == 0 and b == 0 and c == 0):
                    pass
                else:
                    print(a , "Brown Trout," , b , "Northern Pike," , c , "Yellow Pickerel")
                    counter += 1

print("Number of ways to catch fish:" , counter)