# Problem: ECOO '21 P2 - DNA Derren (ecoo21p2)
# Problem URL: https://dmoj.ca/problem/ecoo21p2
# Submission: 3605220 (https://dmoj.ca/submission/3605220)
# Language: Python (PY3)
# Submitted: 2021-05-04T02:18:07+00:00

DNA = input()

DNA_list = DNA[0]

pre = DNA[0]


for i in range(1,len(DNA)):

    if (pre == "A" and DNA[i] != "A") or (pre != "A" and DNA[i] == "A"):
        DNA_list = str(DNA_list) + str(DNA[i])
    else:
        DNA_list = str(DNA_list) + " " + str(DNA[i])
    pre = DNA[i]

print(DNA_list)