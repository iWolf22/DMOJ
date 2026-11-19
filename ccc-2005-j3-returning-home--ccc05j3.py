# Problem: CCC '05 J3 - Returning Home (ccc05j3)
# Problem URL: https://dmoj.ca/problem/ccc05j3
# Submission: 3542177 (https://dmoj.ca/submission/3542177)
# Language: 
# Submitted: 2021-04-05T16:31:01+00:00

# CCC '05 J3 - Returning Home

direction_list = []
street_list = []

direction_list.append(input())
street_list.append(input())

while street_list[len(street_list) - 1] != "SCHOOL":
    direction_list.append(input())
    street_list.append(input())

for i in range(len(street_list) - 2,-1,-1):

    if direction_list[i + 1] == "L":
        print("Turn RIGHT onto " + street_list[i] + " street.")
    else:
        print("Turn LEFT onto " + street_list[i] + " street.")


if direction_list[0] == "L":
    print("Turn RIGHT into your HOME.")
else:
    print("Turn LEFT into your HOME.")