# Problem: CCC '14 J2 - Vote Count (ccc14j2)
# Problem URL: https://dmoj.ca/problem/ccc14j2
# Submission: 3225152 (https://dmoj.ca/submission/3225152)
# Language: Python (PY3)
# Submitted: 2020-12-20T18:15:51+00:00

#CCC '14 J2 - Vote Count

num1 = int(input())
votes = input()

a_counter = 0
b_counter = 0

for i in range(len(votes)):
    if votes[i] == "A":
        a_counter += 1
    else:
        b_counter += 1

if a_counter == b_counter:
    print("Tie")
elif a_counter < b_counter:
    print("B")
else:
    print("A")