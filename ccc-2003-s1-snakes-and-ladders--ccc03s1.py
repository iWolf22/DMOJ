# Problem: CCC '03 S1 - Snakes and Ladders (ccc03s1)
# Problem URL: https://dmoj.ca/problem/ccc03s1
# Submission: 3653004 (https://dmoj.ca/submission/3653004)
# Language: Python (PY3)
# Submitted: 2021-05-30T15:49:10+00:00

# CCC '03 S1 - Snakes and Ladders

location = 1

while True:
    temp = int(input())
    if temp == 0:
        print("You Quit!")
        break
    location += temp
    if location == 100:
        print("You are now on square 100")
        print("You Win!")
        break
    elif location > 100:
        location -= temp
    elif location == 99:
        location = 77
    elif location == 54:
        location = 19
    elif location == 90:
        location = 48
    elif location == 9:
        location = 34
    elif location == 40:
        location = 64
    elif location == 67:
        location = 86
    else:
        error = 0
    print("You are now on square" , location)