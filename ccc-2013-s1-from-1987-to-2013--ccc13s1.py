# Problem: CCC '13 S1 - From 1987 to 2013 (ccc13s1)
# Problem URL: https://dmoj.ca/problem/ccc13s1
# Submission: 3223325 (https://dmoj.ca/submission/3223325)
# Language: 
# Submitted: 2020-12-20T01:13:11+00:00

#CCC '13 S1 - From 1987 to 2013

def find_next_num(num_string):
    for i in range(len(num_string)):
        for j in range(i + 1,len(num_string)):
            if num_string[i] == num_string[j]:
                return(True)
    return(False)

def next_num(num1):
    temp_bool = find_next_num(num1)
    if temp_bool == False:
        print(num1)
    else:
        next_num(str(int(num1) + 1))

num1 = int(input()) + 1
next_num(str(num1))