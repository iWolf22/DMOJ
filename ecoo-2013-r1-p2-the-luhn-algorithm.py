# Problem: ECOO '13 R1 P2 - The Luhn Algorithm (ecoo13r1p2)
# Problem URL: https://dmoj.ca/problem/ecoo13r1p2
# Submission: 3520820 (https://dmoj.ca/submission/3520820)
# Language: Python (PY3)
# Submitted: 2021-03-31T03:21:06+00:00

num_list = []

for i in range(5):
    num_list.append(input().split())

for i in range(5):
    num = ""
    for j in range(5):
        counter = 0
        if len(num_list[i][j]) % 2 == 0:
            for l in range(len(num_list[i][j])):
                if l % 2 == 1:
                    temp_num = int(num_list[i][j][l]) * 2
                    temp_str = str(temp_num)
                    for k in range(len(temp_str)):
                        counter += int(temp_str[k])
                else:
                    counter += int(num_list[i][j][l])
        else:
            for l in range(len(num_list[i][j])):
                if l % 2 == 0:
                    temp_num = int(num_list[i][j][l]) * 2
                    temp_str = str(temp_num)
                    for k in range(len(temp_str)):
                        counter += int(temp_str[k])
                else:
                    counter += int(num_list[i][j][l])
        for l in range(10):
            if (l + counter) % 10 == 0:
                num = num + str(l)
                break

    print(num)