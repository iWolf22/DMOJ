# Problem: CCC '12 J3 - Icon Scaling (ccc12j3)
# Problem URL: https://dmoj.ca/problem/ccc12j3
# Submission: 4576655 (https://dmoj.ca/submission/4576655)
# Language: 
# Submitted: 2022-05-23T14:41:27+00:00

# CCC '12 J3 - Icon Scaling

num = int(input())

char_list = [["*","x","*"],[" ","x","x"],["*"," ","*"]]

new_list = [[0 for i in range(num * 3)] for j in range(num * 3)]

for a in range(3):
    for b in range(3):
        for c in range(num):
            for d in range(num):
                new_list[a * num + c][b * num + d] = char_list[a][b]

for i in range(num * 3):
    new_string = ""
    for j in range(num * 3):
        new_string = new_string + new_list[i][j]
    print(new_string)