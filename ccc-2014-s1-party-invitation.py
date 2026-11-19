# Problem: CCC '14 S1 - Party Invitation (ccc14s1)
# Problem URL: https://dmoj.ca/problem/ccc14s1
# Submission: 3225469 (https://dmoj.ca/submission/3225469)
# Language: Python (PY3)
# Submitted: 2020-12-20T19:08:49+00:00

#CCC '14 S1 - Party Invitation

def random_del(del_num,num1_list):
    del_list = []
    counter_var = 1
    for i in range(len(num1_list)):
        if del_num == counter_var:
            del_list.append(i)
            counter_var = 1
        else:
            counter_var += 1
        

    for i in range(len(del_list)):
        del num1_list[del_list[i] - i]
    
    return (num1_list)

num1 = int(input())
num1_list = [i + 1 for i in range(num1)]

num2 = int(input())
input_list = []
for i in range(num2):
    input_list.append(int(input()))

for i in range(len(input_list)):
    num1_list = random_del(input_list[i],num1_list)

for i in range(len(num1_list)):
    print(num1_list[i])