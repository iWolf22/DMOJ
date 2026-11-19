# Problem: DWITE '09 R5 #2 - Round to Second Prime (dwite09c5p2)
# Problem URL: https://dmoj.ca/problem/dwite09c5p2
# Submission: 3355013 (https://dmoj.ca/submission/3355013)
# Language: Python (PY3)
# Submitted: 2021-02-02T17:01:48+00:00

#DWITE '09 R5 #2 - Round to Second Prime

num_list = []
for i in range(5):
    num_list.append(int(input()))


amount = 100

prime_list = [i for i in range(0,amount)]
new_prime_list = [i for i in range(0,amount)]

for i in range(1,amount):
    j = 0
    for number in prime_list:
        if j > i:
            if prime_list[j] % new_prime_list[i] == 0:
                del prime_list[j]
        j += 1 

prime_list[1] = 2
del prime_list[0]

for j in range(len(num_list)):
    temp1 = []
    temp2 = []
    for i in range(len(prime_list)):
        if num_list[j] < prime_list[i]:
            temp1.append(prime_list[i])
        if num_list[j] > prime_list[i]:
            temp2.append(prime_list[i])
    size = len(temp2)
    if temp1[1] - num_list[j] <= num_list[j] - temp2[size - 2]:
        print(temp1[1])
    else:
        print(temp2[size - 2])