# Problem: COCI '06 Contest 3 #1 Patuljci (coci06c3p1)
# Problem URL: https://dmoj.ca/problem/coci06c3p1
# Submission: 3571784 (https://dmoj.ca/submission/3571784)
# Language: Python (PY3)
# Submitted: 2021-04-19T22:20:51+00:00

# COCI '06 Contest 3 #1 Patuljci

num_list = []

for i in range(9):
    num_list.append(int(input()))

total = sum(num_list)

stop = False

for i in range(9):
    for j in range(9):
        if i != j and total - (num_list[i] + num_list[j]) == 100:
            if i > j:
                del num_list[i]
                del num_list[j]
            else:
                del num_list[j]
                del num_list[i]
            stop = True
            break
    if stop == True:
        break

num_list = sorted(num_list)

for i in range(len(num_list)):
    print(num_list[i])