# Problem: USACO 2021 January Bronze P1 - Uddered but not Herd (usaco21janb1)
# Problem URL: https://dmoj.ca/problem/usaco21janb1
# Submission: 3367421 (https://dmoj.ca/submission/3367421)
# Language: Python (PY3)
# Submitted: 2021-02-06T01:48:52+00:00

#USACO 2021 January Bronze P1 - Uddered but not Herd

alphabet = input().lower()

word = input().lower()

letter = 0
stop = False
counter = 0
while stop == False:
    counter += 1
    for i in range(len(alphabet)):
        if alphabet[i] == word[letter]:
            letter += 1
            if letter >= len(word):
                stop = True
                break
    if letter >= len(word):
        stop = True

print(counter)