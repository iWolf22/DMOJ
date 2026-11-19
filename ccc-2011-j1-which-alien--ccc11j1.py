# Problem: CCC '11 J1 - Which Alien? (ccc11j1)
# Problem URL: https://dmoj.ca/problem/ccc11j1
# Submission: 3339609 (https://dmoj.ca/submission/3339609)
# Language: 
# Submitted: 2021-01-30T18:26:59+00:00

#CCC '11 J1 - Which Alien?

antenna = int(input())
eyes = int(input())

list1 = [False, False, False]

if antenna >= 3 and eyes <= 4:
    list1[0] = True
if antenna <= 6 and eyes >= 2:
    list1[1] = True
if antenna <= 2 and eyes <= 3:
    list1[2] = True

if list1[0] == True:
    print("TroyMartian")
if list1[1] == True:
    print("VladSaturnian")
if list1[2] == True:
    print("GraemeMercurian")