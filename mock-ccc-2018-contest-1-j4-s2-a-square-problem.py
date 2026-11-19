# Problem: Mock CCC '18 Contest 1 J4/S2 - A Square Problem (nccc1j4s2)
# Problem URL: https://dmoj.ca/problem/nccc1j4s2
# Submission: 3648122 (https://dmoj.ca/submission/3648122)
# Language: Python (PY3)
# Submitted: 2021-05-28T01:18:50+00:00

# Mock CCC '18 Contest 1 J4/S2 - A Square Problem

def latin(num_list):
    for i in range(len(num_list)):
        for j in range(len(num_list[i])):
            for l in range(j + 1,len(num_list[i])):
                if num_list[i][j] == num_list[i][l]:
                    return False
            for l in range(i + 1,len(num_list[i])):
                if num_list[l][j] == num_list[i][j]:
                    return False
    return True

def reduced(num_list):
    temp = [i for i in range(10)] + [chr(i) for i in range(65,91)]
    for i in range(len(num_list)):
        if str(temp[i]) != num_list[0][i]:
            return False
    return True

num = int(input())

num_list = []

for i in range(num):
    num_list.append(input())
    num_list[len(num_list) - 1] = num_list[len(num_list) - 1].replace(""," ")
    num_list[len(num_list) - 1] = num_list[len(num_list) - 1].split()

temp1 = latin(num_list)

temp2 = reduced(num_list)

if temp1 == True and temp2 == True:
    print("Reduced")
elif temp1 == True:
    print("Latin")
else:
    print("No")