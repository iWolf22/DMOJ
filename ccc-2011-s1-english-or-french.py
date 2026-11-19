# Problem: CCC '11 S1 - English or French? (ccc11s1)
# Problem URL: https://dmoj.ca/problem/ccc11s1
# Submission: 4189558 (https://dmoj.ca/submission/4189558)
# Language: Python (PY3)
# Submitted: 2022-01-08T17:27:55+00:00

# CCC '11 S1 - English or French

num = int(input())

t_counter = 0
s_counter = 0

for i in range(num):
    words = input()
    for j in range(len(words)):
        if words[j].upper() == "T":
            t_counter += 1
        if words[j].upper() == "S":
            s_counter += 1

if t_counter <= s_counter:
    print("French")
else:
    print("English")