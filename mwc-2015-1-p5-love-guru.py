# Problem: MWC '15 #1 P5: Love Guru (mwc15c1p5)
# Problem URL: https://dmoj.ca/problem/mwc15c1p5
# Submission: 3902515 (https://dmoj.ca/submission/3902515)
# Language: PYPY3 (PYPY3)
# Submitted: 2021-09-19T23:49:45+00:00

# MWC '15 #1 P5: Love Guru

import math

word1 = input().lower()
word2 = input().lower()

char_dic = {chr(i + 97):i + 1 for i in range(26)}

#print(char_dic)

counter1 = 0
counter2 = 0

for i in range(len(word1)):
    counter1 += pow(char_dic[word1[i]], (i + 1), 10)

for i in range(len(word2)):
    counter2 += pow(char_dic[word2[i]], (i + 1), 10)

final1 = counter1 % 10
final2 = counter2 % 10
if final1 == 0:
    final1 = 10
if final2 == 0:
    final2 = 10

print(final1 + final2)