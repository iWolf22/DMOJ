# Problem: DWITE '08 R2 #2 - My favourite digit (dwite08c2p2)
# Problem URL: https://dmoj.ca/problem/dwite08c2p2
# Submission: 3491120 (https://dmoj.ca/submission/3491120)
# Language: Python (PY3)
# Submitted: 2021-03-16T00:21:25+00:00

# DWITE '08 R2 #2 - My favourite digit

num_list = [0 for i in range(5)]

word_list = []

for i in range(len(num_list)):
    word_list.append(input())

for i in range(len(word_list)):
    for j in range(len(word_list[i])):
        if num_list[i] < int(word_list[i][j]):
            num_list[i] = int(word_list[i][j])

for i in range(len(num_list)):
    print(num_list[i])