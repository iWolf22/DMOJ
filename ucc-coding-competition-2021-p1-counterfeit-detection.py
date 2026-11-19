# Problem: UCC Coding Competition '21 P1 - Counterfeit Detection (ucc21p1)
# Problem URL: https://dmoj.ca/problem/ucc21p1
# Submission: 3644947 (https://dmoj.ca/submission/3644947)
# Language: Python (PY3)
# Submitted: 2021-05-26T01:40:13+00:00

# UCC Coding Competition '21 P1 - Counterfeit Detection

string = input()

counter = 0

last = False
for i in range(len(string)):
    if last == "2" and string[i] != "5":
        counter += 1
    last = string[i]

if string[len(string) - 1] == "2":
    counter += 1

print(counter)