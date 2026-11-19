# Problem: CCC '19 S1 - Flipper (ccc19s1)
# Problem URL: https://dmoj.ca/problem/ccc19s1
# Submission: 3440307 (https://dmoj.ca/submission/3440307)
# Language: Python (PY3)
# Submitted: 2021-02-21T18:07:07+00:00

# CCC '19 S1 - Flipper

def Flipper(direction,array):
    new_array = [[0,0],[0,0]]
    if direction == "H":
        new_array[0][0] = array[1][0]
        new_array[0][1] = array[1][1]
        new_array[1][0] = array[0][0]
        new_array[1][1] = array[0][1]
        return(new_array)
    else:
        new_array[0][0] = array[0][1]
        new_array[0][1] = array[0][0]
        new_array[1][1] = array[1][0]
        new_array[1][0] = array[1][1]
        return(new_array)

instructions = input().replace(""," ").split()

array = [[1,2],[3,4]]

for i in range(len(instructions)):
    array = Flipper(instructions[i],array)

print(*array[0])
print(*array[1])