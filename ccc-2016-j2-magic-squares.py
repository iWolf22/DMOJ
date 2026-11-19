# Problem: CCC '16 J2 - Magic Squares (ccc16j2)
# Problem URL: https://dmoj.ca/problem/ccc16j2
# Submission: 3228348 (https://dmoj.ca/submission/3228348)
# Language: Python (PY3)
# Submitted: 2020-12-21T17:26:51+00:00

def find_magic(total_list,base_num):
    for i in range(len(total_list)):
        if sum(total_list[i]) != base_num:
            return False
    for i in range(len(total_list)):
        if total_list[0][i] + total_list[1][i] + total_list[2][i] + total_list[3][i] != base_num:
            return False
    return True

num1 = input().split()
num2 = input().split()
num3 = input().split()
num4 = input().split()

int_num1 = []
int_num2 = []
int_num3 = []
int_num4 = []

for i in range(4):
    int_num1.append(int(num1[i]))
    int_num2.append(int(num2[i]))
    int_num3.append(int(num3[i]))
    int_num4.append(int(num4[i]))

total_list = []
total_list.append(int_num1)
total_list.append(int_num2)
total_list.append(int_num3)
total_list.append(int_num4)

base_num = sum(int_num1)

temp = find_magic(total_list,base_num)

if temp == True:
    print("magic")
else:
    print("not magic")